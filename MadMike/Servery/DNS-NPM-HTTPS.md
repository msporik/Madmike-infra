# Interní DNS, NPM a HTTPS

> Architektura byla prakticky ověřena z LAN i přes WireGuard **2026-07-28**. Veřejná výjimka MikroTik MCP byla doplněna a prakticky ověřena **2026-09-04**.

## Účel

Jednotný interní přístup k administračním a monitorovacím službám přes zapamatovatelné názvy a důvěryhodné HTTPS. Klient nepoužívá přímo IP adresu a port služby.

Níže uvedené administrační a monitorovací služby obsluhované NPM nejsou veřejně publikované. Z domácí LAN jsou dostupné přímo, zvenku po připojení přes WireGuard. Přímá interní IP a port zůstávají nouzovou cestou pro diagnostiku. Vědomé veřejné výjimky přes Cloudflare nebo jinou publikační cestu jsou uvedené samostatně.

## Výsledná architektura

1. Klient se zeptá interního DNS na RB5009.
2. Wildcard záznam pošle požadavek pro `*.mikehub.cz` na Nginx Proxy Manager.
3. NPM na Ryzen / VM510 podle hostname vybere cílovou službu.
4. Klient komunikuje s NPM přes HTTPS; NPM pokračuje na interní HTTP nebo HTTPS upstream.

NPM se ke vzdálenému PVE Dell a PBS dostává přes WireGuard do sítě `192.168.100.0/24`.

```text
klient
→ DNS na RB5009
→ *.mikehub.cz = 192.168.89.35
→ NPM na VM510
→ lokální služba nebo WireGuard do offsite sítě
```

## Vlastnictví jednotlivých vrstev

| Vrstva | Autoritativní místo |
|---|---|
| Interní wildcard a DNS přístup klientů | tento dokument; zařízení RB5009 v projektu [Síť](../Sit/README.md) |
| WireGuard do offsite sítě | [WireGuard.md](WireGuard.md) |
| Docker nasazení NPM a persistence | [VM510-Docker.md](VM510-Docker.md) |
| Proxy hosty a wildcard certifikát | tento dokument |
| Veřejný MikroTik MCP endpoint | [MikroTik-MCP.md](MikroTik-MCP.md) |
| Chování cílové aplikace | projekt dané aplikace |
| Tajné údaje Cloudflare a přístupy | projekt [Přístupy](../Pristupy/README.md) a bezpečné úložiště mimo GitHub |

## Interní DNS

- DNS pro domácí síť poskytuje RB5009 na `192.168.89.1`.
- DNS služba má pro interní klienty zapnuté `allow-remote-requests`.
- Statický wildcard `*.mikehub.cz` směřuje na NPM `192.168.89.35`.
- `valtom.mikehub.cz` je veřejná výjimka mimo interní NPM. Podrobnosti jsou v [HA ValTom / Nasazení a přístup](../../HA-ValTom/Home-Assistant/Nasazeni-a-pristup.md).
- `domov.mikehub.cz` a `mcp.mikehub.cz` jsou veřejné výjimky vedené přes Cloudflare Tunnel `homeassistant-domov`, nikoli přes NPM. Podrobnosti jsou v [domácím Home Assistantu](../Home-Assistant/README.md).
- `mikrotik-mcp.mikehub.cz` je veřejná výjimka vedená přes samostatný Cloudflare Tunnel `mikrotik-mcp` s konektorem přímo na VM511. Veřejná cesta nevede přes NPM. Podrobnosti jsou v [MikroTik-MCP.md](MikroTik-MCP.md).
- Interní wildcard `*.mikehub.cz → 192.168.89.35` veřejné názvy v domácí LAN přebíjí, pokud pro ně není vytvořená explicitní interní výjimka. Lokální test stejného hostname proto nemusí testovat veřejný Cloudflare Tunnel.
- AdGuard není autoritativním místem interních překladů; slouží odděleně k filtrování reklam.

Notebookový WireGuard profil používá:

```ini
DNS = 192.168.89.1
```

Pro notebookovou WG síť `10.89.1.0/24` jsou na RB5009 povolené pouze DNS dotazy na port 53/TCP a 53/UDP. Závěrečný input drop dál blokuje DNS dotazy z internetu.

## Nginx Proxy Manager

NPM běží na [Ryzen / VM510](VM510-Docker.md), IP `192.168.89.35`.

| Název | Upstream z NPM | Role |
|---|---|---|
| `pveryzen.mikehub.cz` | `https://192.168.89.32:8006` | Produkční PVE Ryzen |
| `kuma.mikehub.cz` | `http://192.168.89.35:3001` | Uptime Kuma přes publikovaný port hostitele |
| `mikr.mikehub.cz` | `http://mikr-manager:3000` | Mikr Manager; hostitelský port je `3002` |
| `npm.mikehub.cz` | `http://nginx-proxy-manager:81` | Správa NPM |
| `pulse.mikehub.cz` | `http://pulse:7655` | Pulse |
| `pvedell.mikehub.cz` | `https://192.168.100.11:8006` | PVE Dell přes WireGuard |
| `pbs.mikehub.cz` | `https://192.168.100.12:8007` | PBS ve VM200 přes WireGuard |
| `mikrotik-mcp.mikehub.cz` | `http://192.168.89.36:8000` | Interní HTTPS cesta k MikroTik MCP; veřejný AI provoz jde mimo NPM přes Cloudflare Tunnel |

Na proxy hostech se používá:

- společný wildcard certifikát;
- Force SSL;
- HTTP/2;
- Block Common Exploits;
- WebSocket Support podle potřeby aplikace;
- vypnuté Cache Assets;
- zatím vypnuté HSTS a HSTS Subdomains.

HSTS zůstává vědomě odložené rozhodnutí, nikoliv nedokončený provozní úkol.

## Vazba na Docker

NPM používá dva ověřené modely:

1. **IP VM a publikovaný port** – Uptime Kuma přes `192.168.89.35:3001`.
2. **Jméno kontejneru ve sdílené síti `npm_default`** – Pulse a Mikr Manager.

Compose cesty, kontejnery, porty a trvalé deklarace sítí jsou v [VM510-Docker.md](VM510-Docker.md). Ruční `docker network connect` je diagnostický nebo dočasný krok, ne náhrada Compose deklarace.

## HTTPS certifikát

- vydává Let's Encrypt přes DNS challenge v NPM;
- DNS provider je Cloudflare;
- pokrývá `mikehub.cz` a `*.mikehub.cz`;
- klíč je ECDSA 256;
- DNS propagation time je 30 sekund;
- Cloudflare token má být omezený na úpravu DNS v zóně `mikehub.cz`;
- token ani jeho hodnota se do repozitáře neukládají.

Wildcard pokrývá jednopatrové názvy typu `pveryzen.mikehub.cz`, nikoliv víceúrovňové jméno typu `pve.home.mikehub.cz`. Proto se používají ploché názvy.

Cloudflare slouží pro DNS challenge a pro vědomé veřejné výjimky. Aktuálně jsou doložené tyto cesty:

| Veřejný název | Účel | Cesta |
|---|---|---|
| `valtom.mikehub.cz` | vzdálený přístup k HA ValTom | Cloudflare Tunnel přímo k Home Assistantu ValTom |
| `domov.mikehub.cz` | vzdálený přístup k domácímu Home Assistantu | Cloudflare Tunnel přímo k Home Assistantu |
| `mcp.mikehub.cz` | read-only Home Assistant MCP přístup pro AI klienty | Cloudflare Tunnel k aplikaci Home Assistant MCP Server |
| `mikrotik-mcp.mikehub.cz` | read-only MikroTik MCP přístup pro AI klienty | samostatný Cloudflare Tunnel `mikrotik-mcp` → `cloudflared` na VM511 → `http://localhost:8000` |

Tyto veřejné cesty nevedou přes domácí NPM. U MikroTik MCP je interní NPM proxy host pouze paralelní interní HTTPS cesta; veřejný ChatGPT/Claude provoz jej nepoužívá.

## Běžná kontrola

### Z klienta

```powershell
nslookup pveryzen.mikehub.cz
nslookup valtom.mikehub.cz
```

Kontroluje se:

- použitý DNS server je `192.168.89.1` nebo zamýšlená interní cesta;
- interní jméno se překládá na `192.168.89.35`;
- veřejná výjimka se z externího DNS nepřekládá na interní NPM;
- HTTPS certifikát odpovídá jménu a není expirovaný;
- funguje přihlášení a hlavní funkce, u PVE také konzole/Shell přes WebSocket.

Příkaz s explicitním DNS serverem ověří odpověď RB5009, ale neprokáže, že klient tento server skutečně používá. Rozhodující je i test bez explicitně uvedeného serveru.

U veřejných výjimek je nutné rozlišit interní a externí test. Pokud interní wildcard přebíjí veřejný hostname, lokální `curl` může skončit na NPM a neověřuje Cloudflare Tunnel.

### Na VM510

```bash
sudo docker ps --filter name=nginx-proxy-manager
cd /opt/npm
sudo docker compose config --quiet
sudo docker compose ps
sudo docker compose logs --tail=100
```

Neupravený `docker compose config` se nesdílí, protože může obsahovat tajné hodnoty.

## Diagnostické větvení

Při poruše interních NPM služeb se testují vrstvy v tomto pořadí:

1. DNS překlad jména;
2. dostupnost NPM na `192.168.89.35`;
3. stav proxy hostu a certifikátu;
4. dostupnost upstreamu přímo z VM510;
5. skutečná funkce cílové aplikace.

| Projev | Pravděpodobná vrstva | První kontrola |
|---|---|---|
| Jméno se nepřeloží | klientské DNS nebo RB5009 | použitý DNS server, wildcard a WG profil |
| Interní jméno ukazuje jinam než na `.35` | veřejná/cacheovaná DNS odpověď | DNS klienta, cache a výjimky |
| Všechny interní názvy selžou | VM510, NPM nebo wildcard | dostupnost `.35`, NPM kontejner a RB5009 |
| Jeden název vrací `502` | upstream nebo Docker síť | přímý cíl, schéma, port a členství v `npm_default` |
| Lokální služby fungují, Dell/PBS ne | WireGuard/offsite síť | trasa do `192.168.100.0/24`, PVE Dell a VM200 |
| Přímý upstream funguje, proxy ne | NPM proxy host | hostname, Forward Scheme, Forward Host/Port a WebSocket |
| Přihlášení PVE končí `401: No ticket` | nesprávné HTTP/HTTPS | používat HTTPS na klientské straně i správné HTTPS schéma upstreamu |
| Certifikát je nedůvěryhodný nebo expirovaný | NPM/Let's Encrypt/Cloudflare | přiřazený certifikát, poslední obnova a DNS challenge |
| PVE stránka funguje, konzole ne | WebSocket | WebSocket Support a aplikační log NPM |
| Veřejný MCP funguje lokálně přes stejný hostname, ale ne z AI klienta | split DNS / veřejný tunnel | ověřit Cloudflare Tunnel a testovat z externí cesty, ne přes interní wildcard |

## Restart a obnova NPM

Při běžné poruše:

```bash
cd /opt/npm
sudo docker compose restart
sudo docker compose ps
sudo docker compose logs --tail=100
```

Pokud restart nepomůže, nejprve zachovat logy a ověřit persistence. NPM se nepřeinstaluje ani neinicializuje nad prázdnou databází, dokud nejsou potvrzené jeho volumes a záloha.

Po obnově VM510 nebo NPM se ověří:

1. proxy hosty a jejich upstreamy;
2. wildcard certifikát a jeho přiřazení;
3. dostupnost lokálních služeb;
4. dostupnost PVE Dell a PBS přes WireGuard;
5. WebSocket u PVE;
6. nouzový přímý přístup zůstal zachovaný.

## Plánovaná změna nebo aktualizace

1. Ověřit poslední použitelný backup VM510 a persistentní data NPM.
2. Zaznamenat běžící image/verzi, proxy hosty a platnost certifikátu bez exportu tajných hodnot.
3. Měnit jednu vrstvu: DNS, NPM, certifikát nebo upstream; nespojovat je bez důvodu do jednoho zásahu.
4. Připravit návratovou cestu a zachovat přímé IP/port přístupy.
5. Po změně projít běžnou kontrolu všech interních názvů a relevantních veřejných výjimek.
6. Obnovu certifikátu netestovat mazáním fungujícího certifikátu. Použít podporovanou funkci NPM a ověřit výsledek v logu a prohlížeči.

## Přidání další služby

Pro běžnou interní službu:

1. Zvolit plochý název `sluzba.mikehub.cz`.
2. Ověřit skutečnou interní adresu, port a schéma HTTP/HTTPS.
3. U Docker služby použít jeden z modelů v [VM510-Docker.md](VM510-Docker.md).
4. V NPM přidat Proxy Host.
5. Vybrat existující wildcard certifikát.
6. Zapnout Force SSL a podle aplikace WebSocket Support.
7. Ověřit přihlášení a hlavní funkci přes LAN nebo WireGuard.

Díky internímu wildcard DNS se standardně nic dalšího nepřidává na RB5009, v Cloudflare ani u WEDOS.

Pokud služba musí být dostupná z internetu bez WireGuardu, nejde o běžný NPM případ. Musí být výslovně navržena jako veřejná výjimka a zdokumentována v autoritativním dokumentu dané služby.

## Důležitá poučení

- Proxmox přes obyčejné HTTP po přihlášení končil chybou `401: No ticket`; plnohodnotný přístup vyžaduje HTTPS.
- Ruční `docker network connect` je vhodný jen pro test. Trvalé síťové vazby patří do Compose.
- `docker compose config` může načíst `.env` a vypsat skutečné tajné hodnoty.
- `ENCRYPTION_KEY` Mikru se nesmí měnit naslepo; může být nutný pro čtení uložených přístupových údajů.
- Jedna fungující odpověď portu nepotvrzuje přihlášení, WebSocket ani aplikační funkci.
- Interní NPM endpoint a veřejný Cloudflare Tunnel jsou dvě různé cesty. Úspěšný test přes interní wildcard neprokazuje veřejnou dostupnost.
- Před návrhem nové publikační cesty je nutné nejprve dohledat stávající architekturu v tomto dokumentu; nevytvářet paralelní ingress jen podle momentálního dojmu.

## Otevřené kontroly

**Vyžaduje ověření v živém systému.**

- [ ] Ověřit současnou verzi NPM, stav všech proxy hostů a datum poslední úspěšné obnovy wildcard certifikátu.
- [ ] Ověřit, že Cloudflare API token je uložený v Bitwardenu a případný nezašifrovaný TXT soubor byl odstraněn.

Persistentní data a praktická obnova NPM jsou evidované pouze v [VM510-Docker.md](VM510-Docker.md).