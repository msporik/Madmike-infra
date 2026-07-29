# Rybníky – Amerika

Samostatná kapitola dokumentace lokality Rybníky „Amerika“. Zachycuje místní síť, její známou fyzickou kostru a plán postupné konsolidace.

Protože v této kapitole řešíme jediný ucelený celek, jsou dokumenty sítě vedené přímo zde bez podadresáře `Sit`.

## Naposledy doložený fyzický stav

Síť je funkční, ale vznikala postupně a není dosud kompletně fyzicky ani konfiguračně zinventarizovaná.

- konektivita přichází od HOME přes 5GHz PtP spoj dlouhý přibližně 500–600 m;
- přesné modely a role obou konců spoje je nutné potvrdit;
- starší Sextant běžel stabilně na RouterOS `6.49.19` a má 32 MB RAM;
- za přijímacím bodem pokračuje místní síť do Obýváku a Včelína;
- Včelín fyzicky rozděluje ethernet do Hospody a Dílny;
- Hospoda a Dílna mají místní Wi-Fi;
- z Hospody pokračuje nebo je plánována trasa ke sloupu a následně k mobilhome;
- historicky mohlo vzniknout několik samostatně NATovaných větví se SOHO/TP-Link routery.

Není potvrzený jeden aktuální seznam routerů, switchů, AP, adres, portů ani kabelových tras.

## Schválený cílový stav

Rozhodnutí z brainstormingu z 2026-07-22 nahrazuje starší otevřené varianty:

- přijímací PtP rádio bude pouze transportní bridge/CPE;
- jediným místním routerem bude **hEX S (2025)**;
- hEX S zajistí lokální DHCP a firewall;
- propojení s HOME bude řešené přímým směrováním přes existující PtP, bez WireGuardu;
- místní Wi-Fi se rozdělí na soukromou a hostovskou;
- hostovská síť bude oddělená od soukromé sítě i správy;
- Včelín a další mezilehlé body budou pouze L2 distribuce bez dalšího DHCP a NAT;
- Wi-Fi budou zajišťovat samostatná AP;
- VLAN a CAPsMAN se doplní jen tehdy, pokud přinesou konkrétní provozní užitek;
- stabilní starší rádio se nebude bez důvodu měnit ani převádět na RouterOS 7.

Toto je schválená cílová architektura, nikoli tvrzení, že už byla nasazená. Skutečný výchozí stav a migrační detaily se ověří na místě.

## Dokumenty

- [Topologie](Topologie.md) – známá fyzická kostra, cílová logická topologie a nejasná místa.
- [Hardware](Hardware.md) – doložené zařízení a schválené role cílové sítě.
- [Plán rekonstrukce](Plan-rekonstrukce.md) – bezpečná etapizace přechodu na schválený stav.
- Společný adresní plán je v [MadMike / Síť / Adresní plán](../MadMike/Sit/Adresni-plan.md).
- Centrální monitoring MikroTiků je v [MadMike / Monitoring / Mikr](../MadMike/Monitoring/Mikr.md).
- Detailní kusová a skladová evidence hardwaru zůstává v Airtable.

## Hranice kapitoly

- Kapitola popisuje zařízení, trasy a rozhodnutí specifické pro lokalitu Rybníky „Amerika“.
- Společné síťové principy, adresní plán, monitoring a zálohy zůstávají ve svých autoritativních dokumentech v kapitole MadMike.
- Přesné aktivní zařízení a adresy je nutné ověřit na místě; starší projektové podklady nejsou živým exportem konfigurace.
- Samostatný podadresář projektu vznikne až tehdy, když v kapitole přibude další skutečně oddělená a dlouhodobě udržovaná oblast.

## Bezprostřední další krok

- [ ] Na místě provést fyzickou a konfigurační inventuru a podle ní připravit konkrétní portovou mapu, adresaci a návratový postup pro nasazení hEX S (2025).
