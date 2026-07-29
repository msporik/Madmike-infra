# Hardware

## Naposledy doložené zařízení

| Role | Zařízení | Stav / poznámka |
|---|---|---|
| hlavní PtP spoj | MikroTik Sextant / LHG | přesné přiřazení obou konců ověřit |
| starší Sextant | RB711G-5HnD / Sextant G | RouterOS `6.49.19`, 32 MB RAM; stabilní, nepřevádět bez důvodu na ROS 7 |
| místní core | historicky RB450G nebo starší hEX S | současné aktivní zařízení a konfiguraci ověřit |
| lokální distribuce | různé switche a SOHO routery | úplná inventura chybí; další DHCP a NAT jsou možné |

## Schválené cílové role

| Role | Řešení | Stav / podmínka |
|---|---|---|
| místní router | hEX S (2025) | schválený jediný core; lokální DHCP a firewall |
| přijímací PtP rádio | stávající vhodné rádio | pouze bridge/CPE; přesný model ověřit |
| vnitřní distribuce | spravované L2 prvky podle skutečné potřeby | Včelín a další mezilehlé body bez DHCP a NAT |
| soukromá Wi-Fi | samostatná AP | počet a modely určit podle pokrytí a dostupného HW |
| hostovská Wi-Fi | samostatné SSID na vhodných AP | oddělit od privátní sítě a správy |
| sloup a mobilhome | zatím neurčeno | rozhodnout až po ověření optiky, trasy, napájení a potřebné kapacity |

RB5009 ani CRS326 už nejsou otevřenou podmínkou cílového návrhu. Použijí se jen tehdy, pokud se později objeví nová konkrétní potřeba, která odůvodní změnu schválené jednoduché architektury.

Detailní kusová evidence, skladové počty, sériová čísla a dostupnost konkrétních rezerv zůstávají v Airtable. Tento dokument eviduje pouze zařízení a role podstatné pro topologii Rybníků.

## Otevřené kontroly

- [ ] Udělat úplný seznam aktivních routerů, switchů, AP a jejich napájení.
- [ ] Ověřit dostupnost hEX S (2025) a vhodných AP v kusové HW evidenci před přípravou zásahu.
- [ ] Ověřit dostupné SFP moduly, typ optiky, PoE zdroje a přepěťové ochrany.
- [ ] Před návrhem sloupu ověřit přesné schopnosti konkrétního mANTBoxu nebo jiného rádia.
