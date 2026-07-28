# WireGuard

## Účel

WireGuard zajišťuje přístup mezi domácí sítí, vzdálenými lokalitami a serverovou sítí u Richarda. Pro administrační služby na Dellu a PBS je součástí serverové přístupové infrastruktury.

Tento dokument neeviduje privátní klíče, preshared keys ani jiné tajné hodnoty.

## Potvrzené aktivní tunely

| Propojení | Stav | Známý účel a směrování |
|---|---|---|
| HOME ↔ PBS / Richard | funguje | Přístup mezi HOME a serverovou sítí `192.168.100.0/24` |
| HOME ↔ Honza | funguje | Přístup mezi lokalitami; přesné živé WG adresy a vzdálený LAN rozsah ověřit |
| HOME ↔ RD Švecovi | funguje | Dříve označováno také jako `SEF`; přesné živé WG adresy a vzdálený LAN rozsah ověřit |
| notebook ↔ HOME | funguje | Přístup k `192.168.89.0/24` a `192.168.100.0/24` |

## Notebookový WireGuard

- WG síť: `10.89.1.0/24`;
- adresa rozhraní na RB5009: `10.89.1.1/24`;
- naslouchací port: `51821`;
- povolený přístup: domácí síť `192.168.89.0/24` a serverová síť `192.168.100.0/24`;
- pro interní názvy `*.mikehub.cz` má klient používat DNS `192.168.89.1`.

Připojení bylo prakticky ověřené i ze zahraničí. Přesná klientská WG adresa se doplní až podle živé konfigurace.

## Serverová síť u Richarda

Přes tunel HOME ↔ PBS / Richard jsou z HOME dostupné zejména:

- PVE Dell: `192.168.100.11`;
- PBS ve VM200: `192.168.100.12`.

NPM na `192.168.89.35` používá tuto trasu pro upstreamy `pvedell.mikehub.cz` a `pbs.mikehub.cz`.

## Návrh adresace tunelů

Předběžný návrh společné site-to-site WG sítě `10.200.0.0/24` je vedený v [adresním plánu](../Sit/Adresni-plan.md). Jde o návrh, nikoli o potvrzení současných živých WG adres všech peerů.

## Starý IPsec

IPsec byl v minulosti zkoušený k Honzovi a k RD Švecovi. Měl by být odstraněný, ale stav není živě ověřený. Starý rozsah `192.168.30.0/24` zatím neumíme spolehlivě přiřadit ke konkrétní lokalitě nebo konfiguraci.

## Otevřené kontroly

1. Vypsat na RB5009 všechny aktivní WG peery, jejich WG adresy, `allowed-address` a routy.
2. Ověřit, zda kromě čtyř známých propojení neexistuje další aktivní WireGuard tunel.
3. Ověřit přesné vzdálené LAN rozsahy Honzy a RD Švecových.
4. Ověřit a případně odstranit zbytky starého IPsec na HOME, u Honzy a u RD Švecových.
5. Při kontrole starého IPsec určit původ rozsahu `192.168.30.0/24`.
6. Ověřit DNS `192.168.89.1` v notebookovém WireGuard profilu.
