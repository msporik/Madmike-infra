# Zálohy

Zálohování a obnova důležitých systémů MadMike.

## Cíl

Záloha má hodnotu až tehdy, když je známý její rozsah, pravidelně se kontroluje a byla prakticky ověřena obnova. Dokumentace proto odděluje:

- aktuálně používané zálohování;
- úspěšně provedené testy obnovy;
- schválený cílový stav;
- neověřené nastavení a otevřené úkoly.

## Rozsah současného DR

Současné offsite DR řešení chrání především proti ztrátě domácího PVE Ryzen. Ztráta celé Dell/offsite lokality je vědomě mimo rozsah. Druhá nezávislá kopie celého PBS datastore proto nyní není požadavkem.

## Oblasti projektu

- [PBS a disaster recovery](PBS-DR.md) – offsite Proxmox Backup Server, chráněné VM, ověřené obnovy a DR postup pro ztrátu PVE Ryzen.
- [Home Assistant](Home-Assistant.md) – stav jednotlivých HA instalací a schválený řetězec Home Assistant Cloud / Nextcloud / PBS.
- [MikroTik](MikroTik.md) – exporty a binární zálohy konfigurací, druhá kopie a budoucí test obnovy.

## Provozní zásady

- Kritické systémy mají mít kopii mimo produkční host.
- Úspěšné vytvoření zálohy samo o sobě nepotvrzuje obnovitelnost.
- Obnovy se testují odděleně od produkce, pokud nejde o řízenou produkční obnovu.
- Migrace nebo import se neoznačují jako test obnovy z PBS.
- Historické, migrační a DR kopie se nemažou bez určení jejich původu a role.
- Selhání Backup, Verify, Prune, Garbage Collection nebo ZFS scrubu má vyvolat upozornění vyžadující pozornost.
- Hesla, tokeny, privátní klíče, app hesla a recovery klíče do repozitáře nepatří. Dokumentace může uvést pouze jejich bezpečné umístění.

Konkrétní otevřené úkoly jsou vedené pouze v příslušných detailních dokumentech, aby se neduplikovaly v `TODO.md`.
