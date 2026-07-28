# Interní DNS, NPM a HTTPS

## Účel

Jednotný interní přístup k administračním a monitorovacím službám přes zapamatovatelné názvy a důvěryhodné HTTPS. Klient nepoužívá přímo IP adresu a port služby.

Tyto administrační a monitorovací služby nejsou veřejně publikované. Z domácí LAN jsou dostupné přímo, zvenku po připojení přes WireGuard.

## Princip

1. Klient se zeptá interního DNS na RB5009.
2. Wildcard záznam pošle požadavek pro `*.mikehub.cz` na Nginx Proxy Manager.
3. NPM na VM510 podle hostname vybere cílovou službu.
4. Klient komunikuje s NPM přes HTTPS; NPM pokračuje na interní upstream.

## Interní DNS

- DNS pro domácí síť poskytuje RB5009 na `192.168.89.1`.
- Statický wildcard `*.mikehub.cz` směřuje na NPM `192.168.89.35`.
- `valtom.mikehub.cz` je výjimka a zůstává směrovaný veřejným DNS mimo interní NPM.
- Funkce wildcardu byla prakticky ověřena mimo jiné na `pveryzen.mikehub.cz`.

AdGuard není autoritativním místem pro tyto interní překlady. Slouží odděleně k filtrování reklam.

## Nginx Proxy Manager

NPM běží na Ryzen / VM510 Monitoring, IP `192.168.89.35`.

| Veřejný název v interní síti | Upstream z NPM | Role |
|---|---|---|
| `pveryzen.mikehub.cz` | `https://192.168.89.32:8006` | Produkční PVE Ryzen |
| `kuma.mikehub.cz` | `http://uptime-kuma:3001` | Uptime Kuma |
| `mikr.mikehub.cz` | `http://mikr-manager:3000` | Mikr Manager; hostitelský port je `3002` |
| `npm.mikehub.cz` | `http://nginx-proxy-manager:81` | Správa NPM |
| `pulse.mikehub.cz` | `http://pulse:7655` | Pulse |
| `pvedell.mikehub.cz` | `https://192.168.100.11:8006` | PVE Dell přes WireGuard |
| `pbs.mikehub.cz` | `https://192.168.100.12:8007` | PBS ve VM200 přes WireGuard |

Porty upstreamů jsou interní; uživatel přistupuje přes standardní HTTPS na NPM.

## Docker sítě na VM510

- sdílená síť pro proxy komunikaci: `npm_default`;
- NPM: `npm_default`;
- Mikr: vlastní `mikr_default` a současně `npm_default`;
- Pulse: vlastní `pulse_default` a současně `npm_default`;
- Uptime Kuma: připojená také k `npm_default`.

Použití názvů kontejnerů jako upstreamu vyžaduje, aby NPM a cílový kontejner sdílely `npm_default`.

## HTTPS certifikát

- certifikát vydává Let's Encrypt přes DNS challenge v NPM;
- DNS provider je Cloudflare;
- certifikát pokrývá `mikehub.cz` a `*.mikehub.cz`;
- klíč certifikátu je ECDSA 256;
- DNS propagation time je nastavený na 30 sekund;
- oprávnění Cloudflare tokenu je omezené na úpravu DNS v zóně `mikehub.cz`;
- token ani jeho hodnota se do repozitáře neukládají;
- na proxy hostech jsou zapnuté Force SSL a HTTP/2;
- HSTS a HSTS Subdomains zůstávají vypnuté.

## Otevřené kontroly

1. Ověřit, že připojení Uptime Kuma k `npm_default` přežije případné odstranění a znovuvytvoření kontejneru.
2. Ověřit, že notebookový WireGuard používá DNS `192.168.89.1`, aby interní názvy fungovaly i mimo domov.
3. Při každém přidání služby zapsat současně DNS chování, NPM upstream a způsob přístupu.
