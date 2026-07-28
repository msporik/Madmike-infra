# Síť – Rybníky „Amerika“

## Doložený stav z podkladů k 2026-07-14

Síť je funkční, ale vznikala postupně a není dosud kompletně zinventarizovaná.

- konektivita přichází od HOME přes 5GHz PtP spoj dlouhý přibližně 500–600 m;
- na jednom konci spoje je starší MikroTik Sextant, druhý konec byl v podkladech označován jako LHG; přesné modely a role obou konců je nutné potvrdit;
- starší Sextant běžel stabilně na RouterOS `6.49.19` a má 32 MB RAM;
- za přijímacím bodem pokračuje místní síť do Obýváku a Včelína;
- Včelín fyzicky rozděluje ethernet do Hospody a Dílny;
- Hospoda a Dílna mají místní Wi-Fi;
- z Hospody pokračuje nebo je plánována trasa ke sloupu a následně k mobilhome;
- v síti historicky vzniklo několik samostatně NATovaných větví se SOHO/TP-Link routery.

Není potvrzený jeden aktuální seznam routerů, switchů, AP, adres, portů ani kabelových tras.

## Platná architektonická rozhodnutí

- PtP rádio má být transportní bridge/CPE, ne hlavní router lokality.
- Za rádiem má být samostatný core router.
- Rybníky mají mít lokální DHCP.
- NAT má být pouze na místním core směrem k HOME.
- Včelín má být L2 distribuční bod bez dalšího DHCP a NAT.
- Wi-Fi mají zajišťovat samostatná AP.
- VLAN a CAPsMAN se nasadí jen s konkrétním provozním přínosem.
- Stabilní Sextant se nemá bez důvodu převádět na RouterOS 7.

## Témata projektu

- [Topologie](Topologie.md) – známá fyzická kostra, historická adresace a nejasná místa.
- [Hardware](Hardware.md) – doložené zařízení a kandidáti pro cílovou síť.
- [Plán rekonstrukce](Plan-rekonstrukce.md) – etapizace, rozhodovací body a rizika.
- Společný adresní plán je v [MadMike / Síť / Adresní plán](../../MadMike/Sit/Adresni-plan.md).
- Centrální správa MikroTiků je v [MadMike / Monitoring / Mikr](../../MadMike/Monitoring/Mikr.md).

## Bezprostřední další krok

Nejdřív provést fyzickou a konfigurační inventuru na místě. Teprve podle ní rozhodnout, zda bude pragmatickým core hEX S, nebo cílovým core RB5009.
