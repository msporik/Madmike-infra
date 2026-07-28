# Zálohy

Zálohování a obnova důležitých systémů MadMike.

## Cíl

Záloha má hodnotu až tehdy, když je známý její rozsah, pravidelně se kontroluje a byla prakticky ověřena obnova. Dokumentace proto odděluje:

- aktuálně používané zálohování;
- úspěšně provedené testy obnovy;
- plánované zálohy;
- neověřené nastavení a otevřené úkoly.

## Oblasti projektu

- [PBS a disaster recovery](PBS-DR.md) – offsite Proxmox Backup Server, chráněné VM a testy obnovy.
- [Home Assistant](Home-Assistant.md) – plán zálohování domácího HA a dalších HA instalací.
- [MikroTik](MikroTik.md) – exporty konfigurací a jejich budoucí ověření obnovy.

## Provozní zásady

- Kritické systémy mají mít zálohu mimo produkční host.
- Úspěšné vytvoření zálohy samo o sobě nepotvrzuje obnovitelnost.
- Obnovy se testují odděleně od produkce.
- Historické, migrační a DR kopie se nemažou bez určení jejich původu a role.
- Selhání záloh, Verify, Prune nebo Garbage Collection má vyvolat upozornění vyžadující pozornost.
- Hesla, tokeny, privátní klíče a recovery kódy do repozitáře nepatří.

## Hlavní otevřené úkoly

1. Ověřit živé PBS joby, jejich rozsah, rozvrhy a retenci.
2. Ověřit nastavení Verify, Prune a Garbage Collection.
3. Prakticky otestovat nativní notifikace PVE a PBS.
4. Stanovit rozumnou četnost opakovaných testů obnovy.
5. Rozlišit užitečné DR kopie od objektů, o jejichž původu zatím není jasno.
