# PREMIER

Produkční účetní systém PREMIER provozovaný ve Windows VM501 na hlavním serveru PVE Ryzen.

> Poslední doložený technický stav: **2026-07-28**.  
> Uživatelé, pracovní postup, AI/OCR, vzdálený přístup a odpovědnosti byly potvrzeny **2026-07-29**. Údaje bez novější živé kontroly nejsou vydávány za aktuální měření.

## Účel a hranice

Tento projekt je autoritativní pro:

- účel PREMIERu, jeho uživatele a účetní pracovní postup;
- aplikační provoz, AI/OCR, správu licence bez tajných hodnot a aplikační zálohy;
- praktické požadavky na vzdálený přístup k PREMIERu;
- aplikační kontrolu po aktualizaci, restartu nebo obnově.

Konfigurace hostitele a VM501 patří do projektu [Servery](../Servery/PVE-Ryzen.md). PBS joby, retence a důkazy obnovy patří do projektu [Zálohy](../Zalohy/PBS-DR.md). Společná bezpečnostní pravidla a výběr cílového přístupového modelu patří do projektu [Přístupy](../Pristupy/README.md). NAT a firewall jsou síťová konfigurace a patří do projektu [Síť](../Sit/MikroTik.md).

Do repozitáře nepatří účetní data, názvy účetních jednotek, doklady, přihlašovací údaje, licenční klíče ani jiné tajné nebo osobní údaje.

## Vlastnictví a uživatelé

- Správce infrastruktury odpovídá za VM501, Windows, PREMIER, aktualizace a licenční podklady.
- PREMIER používají pouze správce infrastruktury a externí účetní.
- Správce zadává přijaté faktury; účetní je následně účtuje.
- Změna, odstávka nebo obnova se musí koordinovat s oběma uživateli a nesmí bez funkční náhrady zablokovat práci účetní.
- Kontaktní údaje, hesla a licenční materiály se uchovávají mimo GitHub. Jejich bezpečné umístění dosud není v dokumentaci potvrzené.

## Pracovní postup a integrace

1. Správce připraví a zadá přijaté faktury.
2. PREMIER AI/OCR se používá k automatickému čtení dokladů.
3. Účetní doklady zkontroluje a zaúčtuje.
4. Účetní se nyní připojuje vzdáleně z internetu.

Nextcloud není součástí doloženého účetního pracovního postupu. PREMIER API ani automatický import faktur nejsou doložené jako nasazené. Automatizace importu se nebude zavádět před ustálením jednoduchého toku dokumentů a jednoznačných stavů nezpracované, připravené, zadané a chybějící.

## Doložený stav

| Oblast | Doložený stav | Datum důkazu | Autoritativní detail |
|---|---|---|---|
| Produkční umístění | PVE Ryzen / VM501 | 2026-07-28 | [PVE Ryzen](../Servery/PVE-Ryzen.md) |
| Konfigurace VM | 4 vCPU, 8 GB RAM, `q35`, 60GB disk na `tank-ssd`, IP `192.168.89.34`, funkční QEMU Guest Agent | 2026-07-28 | [PVE Ryzen](../Servery/PVE-Ryzen.md); datovaný stav, nikoli živé měření při tomto zpracování |
| Aplikace | PREMIER je nainstalovaný a používaný; AI/OCR se reálně používá | 2026-07-29 | uživatelské potvrzení |
| Uživatelé a role | správce zadává přijaté faktury, účetní je účtuje; jiní uživatelé nejsou | 2026-07-29 | uživatelské potvrzení |
| Vzdálený přístup | veřejné RDP přes MikroTik účetní funguje; omezení na české IP není nasazené | 2026-07-29 | [Přístup a provoz](Pristup-a-provoz.md) |
| Obnova | VM501 byla obnovena z PBS zpět na Ryzen; byly ověřeny Windows, RDP, PREMIER a dostupnost účetních dat | doloženo k 2026-07-28 | [PBS a disaster recovery](../Zalohy/PBS-DR.md) |
| Záloha celé VM | po obnově proběhl další úspěšný inkrementální PBS backup | 2026-07-28 | [PBS a disaster recovery](../Zalohy/PBS-DR.md) |
| Aplikační záloha | vlastní záloha PREMIERu mimo PBS neexistuje | 2026-07-29 | uživatelské potvrzení |
| Aktualizace a licence | Windows a PREMIER má aktualizovat správce; licenci drží správce | 2026-07-29 | uživatelské potvrzení |

Parametry VM jsou pouze datovaný souhrn potřebný pro vazbu aplikace na infrastrukturu. Po živé kontrole se jejich autoritativní znění aktualizuje v projektu Servery, nikoli duplicitně zde.

## Závislosti

Pro použitelný provoz PREMIERu jsou nutné:

- funkční PVE Ryzen a VM501;
- Windows, síťová konektivita a QEMU Guest Agent;
- funkční RDP cesta pro účetní;
- aplikace PREMIER, dostupná data, platná licence a funkční AI/OCR;
- použitelná PBS záloha celé VM;
- po budoucím zavedení také podporovaná aplikační záloha PREMIERu.

Výpadek jedné vrstvy se nesmí zaměnit za chybu jiné vrstvy. Dostupné RDP ještě nepotvrzuje funkčnost PREMIERu, úspěšný PBS backup nepotvrzuje možnost obnovit jednu účetní jednotku a spuštění PREMIERu po obnově samo nepotvrzuje dlouhodobě použitelný přístup účetní.

## Obnova a ochrana dat

- Dell / VM501 vznikla historicky importem staršího diskového obrazu, nikoli obnovou z PBS.
- Windows, RDP, PREMIER a účetní data byly na Dellu funkční; tím byla ověřena použitelnost importu, ne PBS restore.
- VM501 byla později úspěšně obnovena z PBS zpět na PVE Ryzen.
- Po návratu na Ryzen proběhl další úspěšný inkrementální PBS backup.
- PBS chrání celou VM, ale nenahrazuje rychlou obnovu jedné účetní jednotky nebo opravu logické chyby uvnitř aplikace.
- Vlastní aplikační záloha PREMIERu dosud neexistuje a zůstává významnou provozní mezerou.

Při obnově se zachovává doložená konfigurace VM501. Změna řadiče disku, síťového adaptéru nebo jiná modernizace virtuálního hardwaru se nespojuje s havarijní obnovou; jde o samostatnou plánovanou změnu s vlastním backupem, testem a návratovou cestou.

## Informace vyžadující ověření

**Vyžaduje ověření v živém systému.**

- přesná verze a edice Windows, aktivace, stav aktualizací a podpory;
- přesná verze a edice PREMIERu a licenční stav bez zobrazení klíče;
- obecné umístění aplikačních dat, instalačních médií a licenčních podkladů;
- přesná živá konfigurace VM501 a veřejné RDP cesty;
- zařízení a místa přístupu účetní a její požadavky na tisk, schránku a přenos souborů;
- podporovaný postup vlastní aplikační zálohy a obnovy jedné účetní jednotky;
- požadované RPO, RTO a přijatelná doba odstávky účetního systému.

Praktický provozní, aktualizační, diagnostický a obnovovací postup včetně jediného seznamu otevřených úkolů je v [Přístupu a provozu](Pristup-a-provoz.md).
