# WireGuard

> Poslední prakticky doložené propojení serverových a domácích sítí je funkční. Úplná živá inventura peerů, `allowed-address` a rout zatím nebyla provedena.

## Účel

WireGuard zajišťuje přístup mezi domácí sítí, vzdálenými lokalitami a serverovou sítí u Richarda. HOME RB5009 funguje jako centrální WireGuard hub.

Tento dokument neeviduje veřejné adresy endpointů, privátní klíče, preshared keys ani jiné tajné hodnoty. Neupravené exporty RouterOS nebo klientské konfigurace se do GitHubu ani chatu nevkládají.

## Dopad na serverovou infrastrukturu

Na WireGuardu závisí:

- připojení PVE Ryzen k offsite PBS jako storage `pbs-backup`;
- přístup z HOME k PVE Dell `192.168.100.11` a PBS `192.168.100.12`;
- upstreamy NPM `pvedell.mikehub.cz` a `pbs.mikehub.cz`;
- vzdálený správcovský přístup notebooku k domácí a offsite síti;
- interní DNS notebooku přes `192.168.89.1`.

Výpadek WireGuardu neznamená automaticky výpadek lokálních produkčních VM na Ryzenu. Znamená však ztrátu vzdáleného PBS, offsite správy a části interních HTTPS upstreamů.

## Potvrzené aktivní tunely

| Propojení | Stav | Známý účel a směrování |
|---|---|---|
| HOME ↔ PBS / Richard | funguje | přístup mezi HOME a serverovou sítí `192.168.100.0/24` |
| HOME ↔ Honza | funguje | HOME `10.200.0.1`, Honza `10.200.0.3`; vzdálená LAN `192.168.10.0/24` |
| HOME ↔ RD Švecovi | funguje | ve starších podkladech také `SEF` nebo `ŠÉF`; LAN `192.168.22.0/24`, živou WG adresu ověřit |
| notebook ↔ HOME | funguje | přístup k `192.168.89.0/24` a `192.168.100.0/24` |

Příslušnost LAN `192.168.22.0/24` k lokalitě RD Švecovi je potvrzená. Historická WG adresa `10.200.0.10` vyžaduje živé ověření.

## Notebookový WireGuard

- WG síť: `10.89.1.0/24`;
- adresa rozhraní na RB5009: `10.89.1.1/24`;
- naslouchací port: `51821`;
- povolený přístup: `192.168.89.0/24` a `192.168.100.0/24`;
- DNS klienta: `192.168.89.1`.

Připojení včetně interních názvů `*.mikehub.cz` bylo prakticky ověřené ze zahraničí. Přesná klientská WG adresa se doplní podle živé konfigurace.

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

## Bezpečná inventura na RB5009

Příkazy níže jsou čtecí, ale výstup může obsahovat endpointy, veřejné klíče a interní topologii. Před sdílením se sanitizuje.

```routeros
/interface wireguard print detail
/interface wireguard peers print detail
/ip address print where interface~"wg"
/ip route print where gateway~"wg"
/ip firewall filter print where in-interface~"wg" or out-interface~"wg"
/ip firewall nat print
/ip ipsec policy print
```

U každého peeru se zaznamená pouze:

- jednoznačný název a lokalita;
- WG adresa a vzdálená LAN;
- `allowed-address` bez překryvu;
- potřebné routy a firewallová role;
- datum posledního úspěšného testu;
- vlastník vzdáleného zařízení a způsob místního zásahu.

Endpointy a klíče se do dokumentace nekopírují.

## Ověřené poznatky z nasazení

### Handshake neověřuje LAN routing

Funkční peer, handshake a ping WG adres ještě neznamenají, že funguje klient↔LAN nebo LAN↔LAN. Nejčastější příčiny byly:

- chybějící statická route;
- firewall;
- překryv `allowed-address`;
- stará aktivní IPsec policy, která provoz zachytila před WireGuardem.

### Statické routy

MikroTik při ověřeném nasazení nevytvořil potřebné LAN routy automaticky. Routy byly doplněny ručně na HOME i vzdálených routerech. Ruční routy jsou preferované, protože jsou čitelné a předvídatelné.

### Starý IPsec

Při migraci HOME ↔ Honza aktivní IPsec policy přebíraly klientský provoz před WireGuardem. Typický symptom:

- router↔router funguje;
- klient↔LAN nefunguje;
- routy vypadají správně;
- sniffer na WG rozhraní při klientském pingu nic nevidí.

Funkční oprava byla deaktivovat odpovídající IPsec policy na obou stranách, vyčistit conntrack a znovu ověřit klient↔LAN. Poslední doložený stav pro HOME ↔ Honza je **IPsec deaktivovaný, ale ještě ne odstraněný**.

## Běžná provozní kontrola

Pro každý důležitý tunel se ověřují odděleně:

1. aktuální handshake a přenos dat;
2. WG adresa ↔ WG adresa;
3. router ↔ vzdálená LAN;
4. skutečný klient v jedné LAN ↔ druhá LAN;
5. konkrétní služba, například PVE Dell nebo PBS;
6. u notebooku také interní DNS bez explicitně zadaného DNS serveru.

Serverová kontrola HOME ↔ Richard je úplná až tehdy, když:

- z HOME odpovídá `192.168.100.11` a `192.168.100.12`;
- PVE Ryzen vidí storage `pbs-backup`;
- NPM otevře `pvedell.mikehub.cz` a `pbs.mikehub.cz`;
- test neprokáže jen handshake, ale i skutečnou aplikační cestu.

## Diagnostika

```routeros
/ip route print where dst-address=REMOTE_LAN/24
/ip ipsec policy print
/tool sniffer quick interface=WG_INTERFACE
```

| Projev | Pravděpodobná oblast | První krok |
|---|---|---|
| Není handshake | endpoint, internet, port, klíče nebo peer | ověřit obě strany a poslední změnu; klíče neregenerovat jako první pokus |
| Handshake je, WG adresy se nepingnou | `allowed-address` nebo firewall | porovnat peer konfiguraci a input/forward pravidla |
| WG adresy fungují, vzdálená LAN ne | statická route, forward firewall nebo IPsec | ověřit routy na obou stranách a staré policy |
| Router↔LAN funguje, klient↔LAN ne | return route, firewall, NAT nebo IPsec | sniffer na WG a test z konkrétního klienta |
| PVE Dell funguje přes IP, hostname ne | DNS/NPM, nikoliv WG | pokračovat v [DNS, NPM a HTTPS](DNS-NPM-HTTPS.md) |
| PVE Dell funguje, PBS ne | VM200 nebo PBS služba | pokračovat v [PVE Dell](PVE-Dell.md) a projektu Zálohy |
| Notebook se připojí, interní názvy nefungují | klientský DNS | ověřit `DNS = 192.168.89.1` a firewall DNS na RB5009 |
| Po změně IPsec provoz stále nejde | starý conntrack | po potvrzené změně policy vyčistit relevantní conntrack a znovu testovat |

Pokud sniffer při klientském pingu nic nevidí, paket je zachycen před vstupem do WireGuardu nebo jej zastavuje firewall či policy routing.

## Změna peeru nebo přidání lokality

1. Ověřit skutečný LAN subnet nové lokality a vyloučit kolizi.
2. Zvolit jedinečnou WG adresu podle adresního plánu.
3. Zaznamenat současnou funkční konfiguraci a připravit rollback.
4. Vyměnit pouze veřejné klíče; privátní klíče se nikam nekopírují.
5. Na vzdáleném peeru povolit WG adresu HOME a pouze potřebné domácí sítě.
6. Na HOME peeru povolit jedinečnou WG adresu lokality a její vzdálenou LAN.
7. Přidat ruční routy na obou stranách a zkontrolovat firewall i starý IPsec.
8. Ověřit všech pět vrstev provozní kontroly.
9. Teprve po úspěchu odstranit překonanou konfiguraci; funkční starý tunel se nemaže před přejímkou nového.

`allowed-address` jednotlivých peerů se nesmí překrývat. `0.0.0.0/0` se nepoužívá na více site-to-site peerech.

Obecný dlouhodobý princip adresace je v [adresním plánu](../Sit/Adresni-plan.md). Provozní přidělení WG adres, peerů, `allowed-address` a rout zůstává v tomto dokumentu a za skutečné se považuje až po živém potvrzení.

## Obnova přístupu

1. Určit, zda selhal internet, jeden peer, HOME hub nebo pouze klientský profil.
2. Použít místní správu routeru nebo jinou již existující důvěryhodnou cestu; nevytvářet veřejnou správu jako nouzový workaround.
3. Obnovit poslední známou funkční konfiguraci konkrétního peeru, rout a firewallu.
4. Pokud jsou ztracené klíče, vytvořit nový peer řízeně na obou stranách a starý zneplatnit až po přejímce.
5. Po obnově ověřit skutečné služby a zapsat datum a rozsah testu bez tajných hodnot.

## Otevřené kontroly

**Vyžaduje ověření v živém systému.**

- [ ] Vypsat na RB5009 všechny aktivní WG peery, jejich WG adresy, `allowed-address` a routy.
- [ ] Ověřit, zda kromě čtyř známých propojení neexistuje další aktivní WireGuard tunel.
- [ ] Ověřit přesnou WG adresu klienta notebooku a peeru HOME ↔ Richard.
- [ ] Ověřit, zda historická WG adresa `10.200.0.10` stále patří aktivnímu peeru RD Švecovi.
- [ ] Ověřit a případně odstranit zbytky starého IPsec na HOME, u Honzy a u RD Švecových až po potvrzení, že na nich nic nezávisí.
- [ ] Při kontrole starého IPsec určit původ rozsahu `192.168.30.0/24`.
