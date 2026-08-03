# Home Assistant – HA ValTom

## Role

Instance je připravovaná pro Tomáše Valentu. Prvním praktickým cílem je zobrazit výrobu a provoz GoodWe FVE v jednoduchém dashboardu. Později může Home Assistant řídit bojler podle energetické situace.

## Poslední doložený stav k 2026-08-03

- Cílovým hardwarem zůstává Home Assistant Green s Home Assistant OS.
- HA Green je vypnutý a uložený u správce v šuplíku. U Tomáše dosud nebyl nainstalovaný ani propojený s místními zařízeními.
- Raspberry Pi 5 byl pouze zvažovanou alternativou. Náhrada se má řešit až tehdy, pokud se při kontrolovaném testu zopakuje problém se startem a diagnostika potvrdí potřebu jiného hardwaru.
- Aktuální verze Home Assistant Core, OS a Supervisor nejsou na vypnutém zařízení ověřené.
- Integrace GoodWe, produkční FVE dashboard ani řízení bojleru se neposunuly a nejsou realizované.

### Příprava, image a zálohy

- V květnu 2026 proběhla čistá instalace Home Assistant OS.
- Z přípravy existuje jeden tehdejší master image / full backup čistého základu. Novější image nevznikl.
- Tento přípravný podklad není pravidelným produkčním zálohováním.
- Praktický restore této instance není doložený.
- Po aktualizaci a před fyzickým přesunem musí vzniknout nový aktuální full backup. Pravidelné produkční zálohování a restore test se mají nastavit až v návaznosti na skutečné nasazení.

### Historická inventura připravené instalace

V květnu 2026 byly v připravené instalaci potvrzené HACS, Advanced SSH & Web Terminal, Matter, Matter Server, Google Cast, Thread, Radio Browser, Google Translate TTS a Cloudflared. Protože je zařízení vypnuté, nejde o živě ověřený seznam současných aktivních komponent.

Cloudflare Tunnel na `https://valtom.mikehub.cz` před vypnutím Green fungoval spolehlivě. Dne 2026-08-03 vracel veřejný endpoint chybu Cloudflare `1033`, což je při vypnutém zařízení očekávaný stav, nikoli doložená závada tunelu.

## Autoritativní další kroky

| Oblast | Autoritativní dokument |
|---|---|
| Kontrolovaný test Green, fyzické nasazení a ověření přístupu | [Nasazení a vzdálený přístup](Nasazeni-a-pristup.md) |
| GoodWe, energetická data, dashboard a budoucí bojler | [GoodWe a energetika](GoodWe-a-energie.md) |
| Pravidelné produkční zálohy a praktický restore | [Společná strategie záloh Home Assistantu](../../MadMike/Zalohy/Home-Assistant.md) |

Úkoly se udržují pouze v uvedených autoritativních dokumentech a zde se neduplikují.

## Související dokumentace

- [Centrální DNS, NPM a HTTPS](../../MadMike/Servery/DNS-NPM-HTTPS.md)
- [Společný monitoring](../../MadMike/Monitoring/README.md)
- [Společné zásady přístupů](../../MadMike/Pristupy/README.md)
