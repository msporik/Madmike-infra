# Rybníky – Amerika

> Poslední doložený stav a schválená rozhodnutí: **2026-07-29**. Nejde o potvrzení současného živého stavu.

Samostatná kapitola dokumentace lokality Rybníky „Amerika“. Zachycuje místní síť, její známou fyzickou kostru, cílovou architekturu a bezpečný plán postupné konsolidace.

Protože v této kapitole řešíme jediný ucelený celek, jsou dokumenty sítě vedené přímo zde bez podadresáře `Sit`.

## Účel a rozsah

Lokalita je funkční, ale vznikala postupně a není dosud kompletně fyzicky ani konfiguračně zinventarizovaná. Cílem je vytvořit přehlednou, servisovatelnou a převážně MikroTik síť bez neřízených routerových a NAT ostrovů.

Kapitola zahrnuje:

- sektorový rádiový přívod od HOME a přijímací bod Rybníků;
- místní core, větve Obývák, Včelín, Hospoda a Dílna;
- místní privátní a hostovskou Wi-Fi;
- plánované pokračování ke sloupu a mobilhome;
- místní role zařízení, topologii, přejímací testy a plán rekonstrukce.

Společný adresní plán, obecné postupy MikroTik, monitoring a zálohy zůstávají v autoritativních dokumentech kapitoly MadMike.

## Naposledy doložený fyzický stav

- konektivita přichází od HOME přes sektorový 5GHz rádiový přívod dlouhý přibližně 500–600 m; nejde o vyhrazené PtP;
- na straně HOME byla původní jednotka `AP HOME` nahrazena kvalitnějším sektorem, jehož přesný typ je nutné ověřit;
- sektor obsluhuje také nejméně jedno další připojení, proto se jeho konfigurace nesmí měnit bez posouzení dopadu na ostatní klienty;
- přijímací jednotka na straně Rybníků zůstala beze změny;
- naposledy doložená stabilní kapacita spoje byla přibližně 100 Mb/s při internetové přípojce HOME 1 Gb/s; aktuální rádiové parametry a propustnost nejsou změřené;
- starší Sextant byl doložený s RouterOS `6.49.19` a 32 MB RAM, ale jeho dnešní přesnou roli je nutné potvrdit;
- za přijímacím bodem pokračuje místní síť do Obýváku a Včelína;
- Včelín fyzicky rozděluje ethernet do Hospody a Dílny;
- Hospoda a Dílna mají místní Wi-Fi;
- sloup a mobilhome jsou plánované části; stav případné trasy a optiky ke sloupu se musí ověřit;
- historicky mohlo vzniknout několik samostatně NATovaných větví se SOHO/TP-Link routery.

Není potvrzený jeden aktuální seznam routerů, switchů, AP, adres, portů ani kabelových tras.

> **Vyžaduje ověření v živém systému.**

## Schválený cílový stav

Rozhodnutí z brainstormingu z 2026-07-22 a jejich upřesnění z 2026-07-29 nahrazují starší otevřené varianty:

- přijímací rádio bude pouze transportní bridge/CPE;
- jediným místním routerem bude **hEX S (2025)**;
- hEX S zajistí lokální DHCP, směrování a firewall;
- propojení s HOME bude řešené přímým směrováním přes existující sektorový rádiový přívod, bez lokálního NATu a bez WireGuardu;
- správa Rybníků z HOME bude povolená;
- provoz z privátní sítě Rybníků do HOME bude ve výchozím stavu zakázaný a případné výjimky budou jednotlivě uvedené v allowlistu;
- hostovská síť bude přísně oddělená od privátní sítě, HOME i managementu a hosté budou izolovaní také mezi sebou;
- počáteční omezení hostů bude 15 Mb/s na klienta a 70–80 Mb/s celkem; jde o nastavitelné výchozí hodnoty, ne o garantované limity;
- privátní i hostovské SSID budou dostupné na všech vhodných AP; údaje hostovské sítě musí být měnitelné centrálně a mohou být předávané QR kódem;
- AP budou připojená kabelem, rozmístěná podle změřeného pokrytí a nastavená s koordinovanými kanály a přiměřeným výkonem; bezdrátové repeatery ani mesh nenahradí kabelovou infrastrukturu;
- Včelín a další mezilehlé body budou pouze L2 distribuce bez dalšího DHCP a NAT;
- VLAN a CAPsMAN se použijí jen tam, kde přinesou konkrétní provozní nebo bezpečnostní užitek;
- stabilní přijímací rádio se nebude bez důvodu měnit ani převádět na RouterOS 7;
- Mikr bude evidovat MikroTiky lokality a aktivně sledovat hEX S, rádiový přívod a klíčovou distribuci; cílem je souhrnný alarm lokality místo laviny navazujících alarmů.

Toto je schválená cílová architektura, nikoli tvrzení, že už byla nasazená. Skutečný výchozí stav a migrační detaily se ověří na místě.

## Rychlá orientace pro převzetí

Před prvním zásahem musí správce:

1. projít [známou a cílovou topologii](Topologie.md);
2. rozlišit doložený současný stav od schváleného budoucího stavu;
3. provést pouze čtecí inventuru a porovnat ji s dokumentací;
4. určit skutečný router, DHCP, NAT, statické adresy, port-forwardy a kritické klienty;
5. ověřit místní přístup, použitelné zálohy konfigurací a fyzický rollback;
6. postupovat podle [plánu rekonstrukce](Plan-rekonstrukce.md) vždy jen po jedné ověřitelné etapě.

Dokud není známá topologie, přístupová cesta a návratový postup, neprovádí se změna rádia, core, adresace, DHCP, firewallu ani větví.

## Dokumenty

- [Topologie](Topologie.md) – známá fyzická kostra, cílová logická topologie, provozní kontrola a diagnostika.
- [Hardware](Hardware.md) – doložené zařízení, skladoví kandidáti, cílové role a bezpečná výměna.
- [Plán rekonstrukce](Plan-rekonstrukce.md) – bezpečná etapizace, přejímací testy a návratové postupy.
- Společný adresní plán je v [MadMike / Síť / Adresní plán](../MadMike/Sit/Adresni-plan.md).
- Obecné postupy správy a aktualizace jsou v [MadMike / Síť / MikroTik](../MadMike/Sit/MikroTik.md).
- Centrální monitoring MikroTiků je v [MadMike / Monitoring / Mikr](../MadMike/Monitoring/Mikr.md).
- Zálohy konfigurací a obnova jsou v [MadMike / Zálohy / MikroTik](../MadMike/Zalohy/MikroTik.md).
- Detailní kusová a skladová evidence hardwaru zůstává v Airtable.

## Hranice kapitoly

- Kapitola popisuje zařízení, trasy a rozhodnutí specifické pro lokalitu Rybníky „Amerika“.
- Společné síťové principy, adresní plán, monitoring a zálohy zůstávají ve svých autoritativních dokumentech v kapitole MadMike.
- Přesné aktivní zařízení a adresy je nutné ověřit na místě; starší projektové podklady nejsou živým exportem konfigurace.
- Samostatný podadresář projektu vznikne až tehdy, když v kapitole přibude další skutečně oddělená a dlouhodobě udržovaná oblast.

## Bezprostřední další krok

Nejdřív provést fyzickou a konfigurační inventuru. Jednotlivé otevřené kontroly jsou vedené v dokumentech [Topologie](Topologie.md), [Hardware](Hardware.md) a [Plán rekonstrukce](Plan-rekonstrukce.md), aby se neduplikovaly.
