# PREMIER

Produkční účetní systém PREMIER provozovaný ve Windows VM na hlavním serveru PVE Ryzen.

## Hranice projektu

Tento projekt je autoritativní pro:

- účel a provoz aplikace PREMIER;
- požadavky na vzdálený přístup;
- provozní kontroly a navazující úkoly kolem VM501.

Konfigurace hostitele a virtuálního stroje je popsána v [PVE Ryzen](../Servery/PVE-Ryzen.md). Zálohy a ověřená obnova patří do projektu [Zálohy](../Zalohy/PBS-DR.md).

Do repozitáře nepatří účetní data, přihlašovací údaje, licenční klíče ani jiné tajné hodnoty.

## Ověřený stav

- produkční systém běží jako **Ryzen / VM501**;
- platforma je Windows;
- VM má 4 vCPU, 8 GB RAM, typ stroje `q35` a 60GB disk na `tank-ssd`;
- známá interní IP VM je `192.168.89.34`;
- PREMIER je nainstalovaný a používaný;
- vzdálený přístup přes RDP funguje;
- obnova VM z PBS byla prakticky ověřena včetně spuštění Windows, RDP, PREMIERu a dostupnosti účetních dat.

Podrobnosti přístupu a běžného provozu jsou v [Přístupu a provozu](Pristup-a-provoz.md).

## Otevřené kontroly

1. Porovnat konfiguraci VM501 s aktuálním živým stavem.
2. Ověřit verzi a edici Windows, aktivaci, aktualizace a stav podpory.
3. Ověřit verzi PREMIERu, licenční stav bez ukládání klíče a umístění aplikačních dat.
4. Zjistit, zda PREMIER vytváří vlastní aplikační zálohy a kam.
5. Dokončit bezpečnější vzdálený přístup.
6. Doplnit krátký provozní a DR runbook.
