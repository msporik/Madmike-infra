# Interní DNS, NPM a HTTPS

## Účel

Jednotný interní přístup k administračním a monitorovacím službám přes zapamatovatelné názvy a důvěryhodné HTTPS. Klient nepoužívá přímo IP adresu a port služby.

Tyto služby nejsou veřejně publikované. Z domácí LAN jsou dostupné přímo, zvenku po připojení přes WireGuard.

## Výsledná architektura

1. Klient se zeptá interního DNS na RB5009.
2. Wildcard záznam pošle požadavek pro `*.mikehub.cz` na Nginx Proxy Manager.
3. NPM na Ryzen / VM510 podle hostname vybere cílovou službu.
4. Klient komunikuje s NPM přes HTTPS; NPM pokračuje na interní HTTP nebo HTTPS upstream.

NPM se ke vzdálenému PVE Dell a PBS dostává přes WireGuard do sítě `192.168.100.0/24`.

## Interní DNS

- DNS pro domácí síť poskytuje RB5009 na `192.168.89.1`.
- DNS služba má pro interní klienty zapnuté `allow-remote-requests`.
- Statický wildcard `*.mikehub.cz` směřuje na NPM `192.168.89.35`.
- `valtom.mikehub.cz` je výjimka a zůstává směrovaný veřejným DNS mimo interní NPM. Podrobnosti jsou v [HA ValTom / Home Assistant / Nasazení a přístup](../../HA-ValTom/Home-Assistant/Nasazeni-a-pristup.md).
- AdGuard není autoritativním místem pro tyto interní překlady. Slouží odděleně k filtrování reklam.

Notebookový WireGuard profil používá:

```ini
DNS = 192.168.89.1
```

Pro síť notebookového tunelu `10.89.1.0/24` jsou na RB5009 povolené pouze DNS dotazy na port 53/TCP a 53/UDP. Závěrečný input drop dál blokuje DNS dotazy z internetu.

Nastavení bylo prakticky ověřené přes WireGuard z Itálie: bez ručně zadaného DNS serveru se interní názvy překládaly na NPM a `valtom.mikehub.cz` zůstal veřejnou výjimkou.

## Nginx Proxy Manager

NPM běží na Ryzen / VM510 Monitoring, IP `192.168.89.35`.

| Název | Upstream z NPM | Role |
|---|---|---|
| `pveryzen.mikehub.cz` | `https://192.168.89.32:8006` | Produkční PVE Ryzen |
| `kuma.mikehub.cz` | `http://192.168.89.35:3001` | Uptime Kuma přes publikovaný port hostitele |
| `mikr.mikehub.cz` | `http://mikr-manager:3000` | Mikr Manager; hostitelský port je `3002` |
| `npm.mikehub.cz` | `http://nginx-proxy-manager:81` | Správa NPM |
| `pulse.mikehub.cz` | `http://pulse:7655` | Pulse |
| `pvedell.mikehub.cz` | `https://192.168.100.11:8006` | PVE Dell přes WireGuard |
| `pbs.mikehub.cz` | `https://192.168.100.12:8007` | PBS ve VM200 přes WireGuard |

Na proxy hostech se používá:

- společný wildcard certifikát;
- Force SSL;
- HTTP/2;
- Block Common Exploits;
- WebSocket Support podle potřeby aplikace;
- vypnuté Cache Assets;
- zatím vypnuté HSTS a HSTS Subdomains.

Schéma upstreamu odpovídá skutečné službě: Proxmox VE a PBS používají interní HTTPS, lokální Docker aplikace HTTP.

## Propojení NPM s Docker službami

Existují dva ověřené modely:

1. **Publikovaný port hostitele.** NPM míří na IP VM a publikovaný port. Takto je zapojená Uptime Kuma přes `192.168.89.35:3001`.
2. **Jméno kontejneru.** NPM a aplikace sdílejí externí Docker síť `npm_default`. Tuto síť musí mít aplikace trvale deklarovanou v Compose.

### Pulse

Compose soubor:

```text
/opt/pulse/docker-compose.yml
```

Pulse má deklarované vlastní `pulse_default` i externí `npm_default`. Ověřený výsledný stav:

```text
/pulse → npm_default pulse_default
```

### Mikr Manager

Compose soubor:

```text
/opt/mikr/docker-compose.yml
```

Mikr má deklarované vlastní `mikr_default` i externí `npm_default`. Ověřený výsledný stav:

```text
/mikr-manager → mikr_default npm_default
```

### Uptime Kuma

Kuma nebyla nasazena přes Compose. Kvůli NPM proto nebyla převáděna do nového způsobu nasazení; NPM používá její publikovaný port na VM. Případné ruční připojení Kumy k `npm_default` není pro funkci proxy potřebné a při `recreate` může bez následků zmizet.

## HTTPS certifikát

- certifikát vydává Let's Encrypt přes DNS challenge v NPM;
- DNS provider je Cloudflare;
- certifikát pokrývá `mikehub.cz` a `*.mikehub.cz`;
- klíč certifikátu je ECDSA 256;
- DNS propagation time je 30 sekund;
- oprávnění Cloudflare tokenu je omezené na úpravu DNS v zóně `mikehub.cz`;
- token ani jeho hodnota se do repozitáře neukládají.

Wildcard pokrývá jednopatrové názvy typu `pveryzen.mikehub.cz`. Nepokrývá víceúrovňové jméno typu `pve.home.mikehub.cz`, proto se používají ploché názvy.

Cloudflare slouží pro DNS challenge certifikátu a veřejnou výjimku `valtom.mikehub.cz`; interní služby přes něj nejsou publikované.

## Prakticky ověřené chování

- všechny uvedené interní názvy se otevřely přes HTTPS bez varování certifikátu;
- přihlášení do PVE Ryzen funguje;
- konzole VM a Shell přes PVE fungují, takže je ověřená i cesta WebSocketů;
- Kuma funguje přes `192.168.89.35:3001`;
- Mikr a Pulse fungují přes jména kontejnerů a přežijí `recreate`, protože `npm_default` je v Compose;
- NPM dosáhne do vzdálené sítě `192.168.100.0/24`;
- `pvedell.mikehub.cz` i `pbs.mikehub.cz` byly přes WireGuard otevřené.

## Přidání další služby

1. Zvolit plochý název `sluzba.mikehub.cz`.
2. Ověřit skutečnou interní adresu, port a schéma HTTP/HTTPS.
3. U Docker služby na VM510 zvolit jeden z ověřených modelů:
   - IP VM a publikovaný port;
   - jméno kontejneru a trvale deklarovaná síť `npm_default`.
4. V NPM přidat Proxy Host.
5. Vybrat existující wildcard certifikát.
6. Zapnout Force SSL a podle aplikace WebSocket Support.
7. Ověřit přihlášení a hlavní funkce přes LAN nebo WireGuard.

Díky internímu wildcard DNS se standardně nic dalšího nepřidává na RB5009, v Cloudflare ani u WEDOS.

## Důležitá poučení

- Proxmox přes obyčejné HTTP po přihlášení končil chybou `401: No ticket`; plnohodnotný přístup vyžaduje HTTPS.
- `nslookup jmeno 192.168.89.1` ověří odpověď RB5009, ale ne to, že klient tento DNS server skutečně používá. Rozhodující je test bez explicitně uvedeného serveru.
- Ruční `docker network connect npm_default KONTEJNER` je vhodný jen pro test. Při novém vytvoření kontejneru se ztratí; přesně tak vznikl výpadek Pulse a `502 Bad Gateway`.
- První pokus o Kumu přes hostitelský port skončil `502`, pozdější konečné nastavení `192.168.89.35:3001` bylo z NPM znovu ověřené jako funkční. Z prvního selhání nelze odvozovat obecné pravidlo.
- `docker compose config` může načíst `.env` a vypsat skutečné tajné hodnoty. Neupravený výstup se nekopíruje do chatu ani dokumentace.

## Otevřené kontroly

- [ ] Ověřit, že Cloudflare API token je uložený v Bitwardenu a případný nezašifrovaný TXT soubor byl odstraněn.
- [ ] Po budoucím `recreate` Pulse nebo Mikr ověřit pouze při potížích, že se načetla deklarovaná síť `npm_default`.
- [ ] HSTS případně zapnout až po delším stabilním provozu a samostatném rozhodnutí.
