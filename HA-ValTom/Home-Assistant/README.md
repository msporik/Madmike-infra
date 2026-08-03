# Home Assistant – HA ValTom

## Role a rozsah

Instance je připravovaná pro Tomáše Valentu. Prvním praktickým cílem je zobrazit výrobu a provoz GoodWe FVE v jednoduchém dashboardu. Později může Home Assistant řídit bojler podle energetické situace.

Jde o čistou samostatnou instalaci. Není kopií domácího HA MadMike ani jiné lokality a nepřebírají se do ní jejich zařízení, entity, automatizace nebo síťové předpoklady.

## Poslední doložený stav k 2026-08-03

- Cílovým hardwarem zůstává Home Assistant Green s Home Assistant OS.
- HA Green je vypnutý a uložený u správce v šuplíku. U Tomáše dosud nebyl nainstalovaný ani propojený s místními zařízeními.
- Raspberry Pi 5 byl pouze zvažovanou alternativou. Náhrada se má řešit až tehdy, pokud se při kontrolovaném testu zopakuje problém se startem a diagnostika potvrdí potřebu jiného hardwaru.
- Aktuální verze Home Assistant Core, OS a Supervisor nejsou na vypnutém zařízení ověřené.
- Integrace GoodWe, produkční FVE dashboard ani řízení bojleru se neposunuly a nejsou realizované.

### Přehled vrstev

| Vrstva | Zamýšlená role | Doložený stav |
|---|---|---|
| Home Assistant Green | Cílový aplikační hardware | Připravený, vypnutý, dosud nenasazený u Tomáše |
| Home Assistant OS | Core, Supervisor a správa aplikací | Čistá instalace z května 2026; současný stav neověřený |
| Lokální síť | Přístup k HA a GoodWe | Cílová IP, rezervace a topologie nejsou známé |
| Cloudflare Tunnel | Vzdálený HTTPS přístup k HA | Historicky funkční; při vypnutém Green je konektor offline |
| GoodWe | Lokálně čtená energetická data | Nerealizováno |
| Dashboard | Přehled výroby, spotřeby, odběru a přetoku | Nerealizováno |
| Řízení bojleru | Budoucí řízení až podle ověřených dat a zapojení | Nerealizováno |
| Zálohy | Obnova konfigurace a provozu | Existuje jen starší přípravný backup; produkční režim chybí |
| Monitoring | Dostupnost HA a upozornění na problém | Zapojení po nasazení teprve čeká |

### Příprava, image a zálohy

- V květnu 2026 proběhla čistá instalace Home Assistant OS.
- Z přípravy existuje jeden tehdejší master image / full backup čistého základu. Novější image nevznikl.
- Tento přípravný podklad není pravidelným produkčním zálohováním.
- Praktický restore této instance není doložený.
- Po aktualizaci a před fyzickým přesunem musí vzniknout nový aktuální full backup. Pravidelné produkční zálohování a restore test se mají nastavit až v návaznosti na skutečné nasazení.

### Historická inventura připravené instalace

V květnu 2026 byly v připravené instalaci potvrzené HACS, Advanced SSH & Web Terminal, Matter, Matter Server, Google Cast, Thread, Radio Browser, Google Translate TTS a Cloudflared. Protože je zařízení vypnuté, nejde o živě ověřený seznam současných aktivních komponent ani o potvrzení, že jsou všechny potřebné.

Cloudflare Tunnel na `https://valtom.mikehub.cz` před vypnutím Green fungoval spolehlivě. Dne 2026-08-03 vracel veřejný endpoint chybu Cloudflare `1033`, což je při vypnutém zařízení očekávaný stav, nikoli doložená závada tunelu.

## Handover: první kontrola

1. Ověřit fyzické umístění a napájení Green. Pokud je stále vypnutý, nevyhodnocovat nedostupný veřejný endpoint jako samostatnou poruchu.
2. Přečíst [nasazení a vzdálený přístup](Nasazeni-a-pristup.md) a nepřeskakovat kontrolovaný test startu.
3. Bez zobrazení tajných hodnot ověřit, že jsou dostupné správcovské přístupy, Cloudflare podklady a starší backup.
4. Po spuštění zaznamenat verze Core, OS, Supervisoru a skutečně aktivní aplikace a integrace.
5. Před změnami vytvořit použitelný backup; potom měnit vždy jednu srozumitelnou vrstvu a ověřit lokální i vzdálený přístup.
6. GoodWe nejprve zprovoznit pouze pro čtení a validovat data podle [GoodWe a energetika](GoodWe-a-energie.md).
7. Po nasazení nastavit produkční zálohy, monitoring a odpovědnost za místní zásah.

## Bezpečná změna a aktualizace

1. Zapsat výchozí stav: verze, dostupnost, relevantní varování a účel změny.
2. Ověřit, že existuje stažitelný full backup a návratová cesta. Backup ani tajné hodnoty neukládat do GitHubu.
3. Udržet lokální přístup; změnu Cloudflare neprovádět jako jediný současně dostupný způsob správy.
4. Aktualizovat jednu vrstvu nebo předem vymezený celek. Neprovádět současně přesun do jiné sítě, zásadní upgrade a integraci GoodWe.
5. Po změně ověřit start, lokální UI, logy, Cloudflare, potřebné integrace a vytvoření nového backupu.
6. Při opakovaném problému se startem, ztrátě lokálního přístupu nebo chybě migrace zastavit další změny, zachovat důkazy a použít připravenou návratovou cestu.

Podporované postupy aktualizace, backupu a obnovy se řídí [oficiální dokumentací Home Assistant OS](https://www.home-assistant.io/common-tasks/os/). Konkrétní produkční strategii a retenci určuje centrální dokumentace záloh tohoto repozitáře.

## Odpovědnosti k potvrzení při nasazení

**Vyžaduje ověření v živém systému.**

- vlastník správcovského účtu, stav MFA a použitelný recovery postup;
- kdo může provést místní kontrolu napájení a kabeláže;
- kdo reaguje na nedostupnost, starý backup nebo chybu integrace;
- kde je uložený poslední použitelný backup a kdo smí provést obnovu;
- jaký běžný uživatelský přístup má mít Tomáš a zda potřebuje administrátorské oprávnění.

## Autoritativní další kroky

| Oblast | Autoritativní dokument |
|---|---|
| Kontrolovaný test Green, fyzické nasazení, aktualizace a ověření přístupu | [Nasazení a vzdálený přístup](Nasazeni-a-pristup.md) |
| GoodWe, energetická data, dashboard a budoucí bojler | [GoodWe a energetika](GoodWe-a-energie.md) |
| Pravidelné produkční zálohy a praktický restore | [Společná strategie záloh Home Assistantu](../../MadMike/Zalohy/Home-Assistant.md) |

Úkoly se udržují pouze v uvedených autoritativních dokumentech a zde se neduplikují.

## Související dokumentace

- [Centrální DNS, NPM a HTTPS](../../MadMike/Servery/DNS-NPM-HTTPS.md)
- [Společný monitoring](../../MadMike/Monitoring/README.md)
- [Společné zásady přístupů](../../MadMike/Pristupy/README.md)
