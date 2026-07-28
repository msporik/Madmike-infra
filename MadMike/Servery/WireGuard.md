# WireGuard

## Účel

WireGuard zajišťuje přístup mezi domácí sítí, vzdálenými lokalitami a serverovou sítí u Richarda. Pro administrační služby na Dellu a PBS je součástí serverové přístupové infrastruktury.

Tento dokument neeviduje privátní klíče, preshared keys ani jiné tajné hodnoty.

## Potvrzené aktivní tunely

| Propojení | Stav | Známý účel a směrování |
|---|---|---|
| HOME ↔ PBS / Richard | funguje | Přístup mezi HOME a serverovou sítí `192.168.100.0/24` |
| HOME ↔ Honza | funguje | HOME `10.200.0.1`, Honza `10.200.0.3`; vzdálená LAN `192.168.10.0/24` |
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

## Lokalita Honza

- místní LAN: `192.168.10.0/24`;
- místní router a brána: `192.168.10.1`;
- WG adresa HOME: `10.200.0.1`;
- WG adresa Honza: `10.200.0.3`;
- propojení i vzdálený WinBox byly prakticky ověřené.

Podrobnosti místní sítě jsou v [Honza / Síť](../../Honza/Sit/README.md).

## Návrh adresace tunelů

Předběžný návrh společné site-to-site WG sítě `10.200.0.0/24` je vedený v [adresním plánu](../Sit/Adresni-plan.md). Adresy HOME a Honza jsou potvrzené; ostatní adresy zůstávají návrhem, dokud je nepotvrdí živá konfigurace.

## Starý IPsec

IPsec byl v minulosti zkoušený k Honzovi a k RD Švecovi. Měl by být odstraněný, ale stav není živě ověřený. Starý rozsah `192.168.30.0/24` zatím neumíme spolehlivě přiřadit ke konkrétní lokalitě nebo konfiguraci.

## Otevřené kontroly

1. Vypsat na RB5009 všechny aktivní WG peery, jejich WG adresy, `allowed-address` a routy.
2. Ověřit, zda kromě čtyř známých propojení neexistuje další aktivní WireGuard tunel.
3. Ověřit přesný vzdálený LAN rozsah a živé WG adresy RD Švecových.
4. Ověřit a případně odstranit zbytky starého IPsec na HOME, u Honzy a u RD Švecových.
5. Při kontrole starého IPsec určit původ rozsahu `192.168.30.0/24`.
6. Ověřit DNS `192.168.89.1` v notebookovém WireGuard profilu.
