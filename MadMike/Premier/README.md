# PREMIER

Produkční účetní systém PREMIER provozovaný ve Windows VM501 na hlavním serveru PVE Ryzen.

> Poslední doložený technický stav: **2026-07-28**.  
> Uživatelé, workflow, AI/OCR, vzdálený přístup a odpovědnosti byly potvrzeny **2026-07-29**. Údaje bez novější živé kontroly nejsou vydávány za aktuální měření.

## Účel a hranice

Tento projekt je autoritativní pro:

- účel PREMIERu, jeho uživatele a účetní workflow;
- aplikační provoz, AI/OCR, správu licence bez tajných hodnot a aplikační zálohy;
- praktické požadavky na vzdálený přístup k PREMIERu;
- aplikační kontrolu po aktualizaci, restartu nebo obnově.

Konfigurace hostitele a VM501 patří do projektu [Servery](../Servery/PVE-Ryzen.md). PBS joby, retence a důkazy obnovy patří do projektu [Zálohy](../Zalohy/PBS-DR.md). Společná bezpečnostní pravidla a výběr cílového přístupového modelu patří do projektu [Přístupy](../Pristupy/README.md). NAT a firewall jsou síťová konfigurace a patří do projektu [Síť](../Sit/MikroTik.md).

Do repozitáře nepatří účetní data, názvy účetních jednotek, přihlašovací údaje, licenční klíče ani jiné tajné hodnoty.

## Uživatelé a workflow

- PREMIER používá pouze správce infrastruktury a externí účetní.
- Správce zadává přijaté faktury.
- PREMIER AI/OCR se používá k automatickému čtení dokladů.
- Účetní následně doklady účtuje.
- Účetní se nyní připojuje vzdáleně z internetu.
- Nextcloud není součástí doloženého pracovního postupu účetní.
- Zařízení, místa přístupu a požadavky účetní na tisk, schránku a přenos souborů zatím nejsou zjištěné.

Změna přístupu musí zachovat jednoduchý pracovní postup a nesmí bez funkční náhrady zablokovat práci účetní.

## Doložený stav

| Oblast | Doložený stav | Datum důkazu | Zdroj |
|---|---|---|---|
| Produkční umístění | PVE Ryzen / VM501 | 2026-07-28 | [PVE Ryzen](../Servery/PVE-Ryzen.md) a uživatelské potvrzení |
| Konfigurace VM | 4 vCPU, 8 GB RAM, `q35`, 60GB disk na `tank-ssd`, IP `192.168.89.34`, funkční QEMU Guest Agent | 2026-07-28 | poslední dokumentovaný stav; nikoli živé měření při tomto auditu |
| Aplikace | PREMIER je nainstalovaný a používaný; AI/OCR se reálně používá | 2026-07-29 | uživatelské potvrzení |
| Uživatelé a role | správce zadává přijaté faktury, účetní je účtuje; jiní uživatelé nejsou | 2026-07-29 | uživatelské potvrzení |
| Vzdálený přístup | veřejné RDP přes MikroTik účetní funguje; omezení na české IP není nasazené | 2026-07-29 | uživatelské potvrzení |
| Obnova | VM501 byla obnovena z PBS zpět na Ryzen; byly ověřeny Windows, RDP, PREMIER a účetní data | doloženo k 2026-07-28 | [PBS a disaster recovery](../Zalohy/PBS-DR.md) |
| Záloha celé VM | po obnově proběhl další úspěšný inkrementální PBS backup | 2026-07-28 | [PBS a disaster recovery](../Zalohy/PBS-DR.md) |
| Aplikační záloha | vlastní záloha PREMIERu mimo PBS neexistuje | 2026-07-29 | uživatelské potvrzení |
| Odpovědnost | Windows a PREMIER má aktualizovat správce; licenci drží správce | 2026-07-29 | uživatelské potvrzení |

Parametry VM jsou pouze datovaný souhrn. Po živé kontrole se jejich autoritativní znění aktualizuje v projektu Servery, nikoli duplicitně zde.

## Historie obnovy a záloh

- Dell / VM501 vznikla importem staršího diskového obrazu, nikoli obnovou z PBS.
- Funkčnost Windows, RDP, PREMIERu a účetních dat na Dellu proto dokládá použitelnost importu, ale nepočítá se jako PBS restore.
- VM501 byla později úspěšně obnovena z PBS zpět na PVE Ryzen.
- Po návratu na Ryzen proběhl další úspěšný inkrementální PBS backup.

PBS chrání celou VM, ale nenahrazuje jednoduchou obnovu jedné účetní jednotky. Absence vlastní aplikační zálohy PREMIERu je skutečná provozní mezera.

## Správa a integrace

- Za aktualizace Windows i PREMIERu odpovídá správce infrastruktury.
- Licenci drží správce; klíč ani jiné tajné licenční údaje se do repozitáře nezapisují.
- Přesná verze a edice Windows, aktivace, stav podpory a aktualizací nejsou živě ověřené.
- Přesná verze PREMIERu, obecné umístění aplikačních dat a instalačních médií nejsou ověřené.
- PREMIER AI/OCR je používaná součást současného workflow.
- PREMIER API není doložené jako nasazené.
- Další automatizace nad rámec používaného AI/OCR není v současném provozu zdokumentovaná.

Přístupový, aktualizační, zálohovací a DR postup včetně jediného seznamu otevřených úkolů je v [Přístupu a provozu](Pristup-a-provoz.md).
