# WireGuard

## Účel

WireGuard zajišťuje přístup mezi domácí sítí, vzdálenými lokalitami a serverovou sítí u Richarda. HOME RB5009 funguje jako centrální WireGuard hub.

Tento dokument neeviduje veřejné adresy endpointů, privátní klíče, preshared keys ani jiné tajné hodnoty.

## Potvrzené aktivní tunely

| Propojení | Stav | Známý účel a směrování |
|---|---|---|
| HOME ↔ PBS / Richard | funguje | Přístup mezi HOME a serverovou sítí `192.168.100.0/24` |
| HOME ↔ Honza | funguje | HOME `10.200.0.1`, Honza `10.200.0.3`; vzdálená LAN `192.168.10.0/24` |
| HOME ↔ RD Švecovi | funguje | Ve starších podkladech také `SEF` nebo `ŠÉF`; LAN `192.168.22.0/24`, živou WG adresu ověřit |
| notebook ↔ HOME | funguje | Přístup k `192.168.89.0/24` a `192.168.100.0/24` |

Příslušnost LAN `192.168.22.0/24` k lokalitě ŠÉF / RD Švecovi je potvrzená. Starší checkpoint zároveň uvádí WG adresu `10.200.0.10`; ta zůstává historickou stopou do ověření v živé konfiguraci.

## Notebookový WireGuard

- WG síť: `10.89.1.0/24`;
- adresa rozhraní na RB5009: `10.89.1.1/24`;
- naslouchací port: `51821`;
- povolený přístup: domácí síť `192.168.89.0/24` a serverová síť `192.168.100.0/24`;
- DNS klienta: `192.168.89.1`.

Připojení včetně interních názvů `*.mikehub.cz` bylo prakticky ověřené ze zahraničí. Přesná klientská WG adresa se doplní až podle živé konfigurace.

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
- handshake, router↔router, klient↔LAN, LAN↔LAN a vzdálený WinBox byly prakticky ověřené.

Podrobnosti místní sítě jsou v [Honza / Síť](../../Honza/Sit/README.md).

## Ověřené poznatky z nasazení

### Handshake neověřuje LAN routing

Funkční peer, handshake a ping WG adres ještě neznamenají, že funguje klient↔LAN nebo LAN↔LAN. Nejčastější příčiny při nasazování byly:

- chybějící statická route;
- stará aktivní IPsec policy, která provoz zachytila dřív, než vstoupil do WireGuardu.

### Statické routy

MikroTik při ověřeném nasazení nevytvořil potřebné LAN routy automaticky. Routy byly doplněny ručně na HOME i na vzdálených routerech.

Ruční routy jsou preferované, protože jsou čitelné, předvídatelné a snáze se diagnostikují.

### Starý IPsec

Při migraci HOME ↔ Honza aktivní IPsec policy přebíraly klientský provoz před WireGuardem. Typický symptom:

- router↔router funguje;
- klient↔LAN nefunguje;
- routy vypadají správně;
- sniffer na WG rozhraní při klientském pingu nic nevidí.

Funkční oprava byla:

1. deaktivovat odpovídající IPsec policy na obou stranách;
2. vyčistit conntrack;
3. znovu ověřit klient↔LAN.

Poslední doložený stav pro HOME ↔ Honza je **IPsec deaktivovaný, ale ještě ne odstraněný**. Zbytky měly zůstat několik dní disabled, přežít běžný provoz a reboot obou routerů a teprve potom se odstranit.

## Zásady pro další lokalitu

1. Ověřit skutečný LAN subnet nové lokality a vyloučit kolizi.
2. Vytvořit WG interface a přidělit jedinečnou WG adresu.
3. Vyměnit pouze veřejné klíče; privátní klíče se nikam nekopírují.
4. Na vzdáleném peeru povolit WG adresu HOME a domácí LAN.
5. Na HOME peeru povolit jedinečnou WG adresu lokality a její vzdálenou LAN.
6. Přidat ruční routy na obou stranách.
7. Ověřit firewall a zbytky starého IPsec.

`allowed-address` jednotlivých peerů se nesmí překrývat. Zejména se nepoužívá `0.0.0.0/0` na více site-to-site peerech.

Obecný dlouhodobý princip adresace je v [adresním plánu](../Sit/Adresni-plan.md). Provozní přidělení WG adres, peerů, `allowed-address` a rout zůstává pouze v tomto dokumentu a za skutečné se považuje až po potvrzení v živé konfiguraci.

## Testovací a diagnostický postup

Po zprovoznění se ověřují tři různé vrstvy:

1. WG adresa ↔ WG adresa;
2. router ↔ vzdálená LAN;
3. skutečný klient v jedné LAN ↔ druhá LAN.

Pokud třetí test selže:

```routeros
/ip route print where dst-address=REMOTE_LAN/24
/ip ipsec policy print
/tool sniffer quick interface=WG_INTERFACE
```

Pokud sniffer při klientském pingu nic nevidí, paket je zachycený před vstupem do WireGuardu nebo jej zastavuje firewall/policy routing. Po změně starého IPsec je vhodné vyčistit conntrack.

## Otevřené kontroly

- [ ] Vypsat na RB5009 všechny aktivní WG peery, jejich WG adresy, `allowed-address` a routy.
- [ ] Ověřit, zda kromě čtyř známých propojení neexistuje další aktivní WireGuard tunel.
- [ ] Ověřit, zda historická WG adresa `10.200.0.10` stále patří aktivnímu peeru RD Švecovi.
- [ ] Ověřit a případně odstranit zbytky starého IPsec na HOME, u Honzy a u RD Švecových.
- [ ] Při kontrole starého IPsec určit původ rozsahu `192.168.30.0/24`.
