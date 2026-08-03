# Hardware

## Naposledy doložené zařízení

| Role | Zařízení | Stav / poznámka |
|---|---|---|
| vysílací strana přívodu | kvalitnější 5GHz sektor `AP HOME` | aktivní náhrada původní jednotky; sektorový/PtMP provoz, přesný model a konfiguraci ověřit |
| přijímací strana přívodu | stávající přijímací jednotka | zůstala beze změny; přesný model a režim ověřit |
| historicky doložený Sextant | RB711G-5HnD / Sextant G | RouterOS `6.49.19`, 32 MB RAM; dnešní roli potvrdit a stabilní kus nepřevádět bez důvodu na ROS 7 |
| místní core | historicky RB450G nebo starší hEX S | současné aktivní zařízení a konfiguraci ověřit |
| lokální distribuce | různé switche a SOHO routery | úplná inventura chybí; další DHCP a NAT jsou možné |

## Schválené cílové role

| Role | Řešení | Stav / podmínka |
|---|---|---|
| místní router | hEX S (2025) | schválený jediný core; lokální DHCP, směrování a firewall |
| přijímací rádio | stávající vhodné rádio | pouze bridge/CPE; přesný model ověřit |
| vnitřní distribuce | spravované L2 prvky podle skutečné potřeby | Včelín a další mezilehlé body bez DHCP a NAT |
| soukromá Wi-Fi | samostatná AP | počet a modely určit podle pokrytí a dostupného HW |
| hostovská Wi-Fi | samostatné SSID na vhodných AP | oddělit od privátní sítě, HOME i správy; zajistit izolaci klientů |
| sloup a mobilhome | zatím neurčeno | rozhodnout až po ověření optiky, trasy, napájení a potřebné kapacity |

RB5009 ani CRS326 nejsou podmínkou cílového návrhu. Použijí se jen tehdy, pokud se později objeví konkrétní potřeba, která odůvodní změnu schválené jednoduché architektury.

## Výběr konkrétních kusů

Aktuální dostupnost, stav a rezervace konkrétních zařízení se vždy ověřují v Airtable, které je jedinou autoritou proměnlivé kusové evidence. Tento dokument eviduje pouze schválené cílové role a podmínky výběru.

## Požadavky před výběrem kusů

- znát skutečný počet metalických a optických portů v každém bodě;
- ověřit PoE standard, napětí, příkon a rezervu zdrojů;
- ověřit typ vlákna, konektory a kompatibilní SFP moduly;
- u venkovních metalických tras vyřešit přepěťovou ochranu a uzemnění;
- u sloupu a mobilhome ověřit napájení, krytí, teploty a servisní přístup;
- nevybírat AP pouze podle dostupnosti ve skladu, ale také podle pokrytí, pásma a způsobu oddělení hostů.

## Otevřené kontroly

- [ ] Udělat úplný seznam aktivních routerů, switchů, AP a jejich napájení.
- [ ] V Airtable určit a rezervovat konkrétní hEX S (2025) a vhodná AP až podle inventury.
- [ ] Ověřit přesné modely a stav skladových AP uvažovaných pro nasazení.
- [ ] Ověřit dostupné SFP moduly, typ optiky, PoE zdroje, přepěťové ochrany a uzemnění.
- [ ] Před návrhem sloupu ověřit přesné schopnosti konkrétního mANTBoxu nebo jiného rádia.
