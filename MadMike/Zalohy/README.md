# Zálohy

Zálohování, obnovitelnost a disaster recovery důležitých systémů MadMike.

## Účel a hranice

Záloha má hodnotu až tehdy, když je známý její rozsah, pravidelně se kontroluje a byla prakticky ověřena obnova. Dokumentace proto důsledně odděluje:

- vytvoření zálohy;
- kontrolu integrity;
- praktickou obnovu;
- aplikační přejímku obnoveného systému;
- úplný DR scénář včetně hostitelů, sítí, přístupů a obnovovacích materiálů.

Projekt vlastní zálohovací řetězce, retenci, údržbu, důkazy obnovitelnosti a DR postupy. Hardware, ZFS topologie, provoz konkrétních aplikací, monitoring a přístupy zůstávají v jejich autoritativních projektech a zde se pouze odkazují.

## Rozsah současného DR

Současné offsite DR řešení chrání především proti ztrátě domácího PVE Ryzen. Ztráta celé Dell/offsite lokality je vědomě mimo rozsah. Druhá nezávislá kopie celého PBS datastore proto nyní není požadavkem.

## Oblasti projektu

- [PBS a disaster recovery](PBS-DR.md) – offsite Proxmox Backup Server, backup joby, retence, údržba, ověřené obnovy a DR postup pro ztrátu PVE Ryzen.
- [Home Assistant](Home-Assistant.md) – stav jednotlivých HA instalací a schválený řetězec Home Assistant Cloud / Nextcloud / PBS.
- [MikroTik](MikroTik.md) – exporty a binární zálohy konfigurací, druhá kopie a budoucí test obnovy.

## Rychlá orientace při incidentu

1. Nejdřív určit, zda selhal produkční systém, zálohovací cesta, nebo jen monitoring.
2. Zachovat původní disky, backup groups, task logy a neznámé objekty beze změny.
3. Ověřit poslední použitelnou zálohu a všechny závislosti obnovy dříve, než se začne cokoli přepisovat nebo mazat.
4. Použít runbook příslušné oblasti a provozní přejímku dokončit v autoritativním projektu aplikace.
5. Zabránit souběžnému spuštění původní a obnovené produkční kopie se stejnou identitou, IP adresou nebo daty.
6. Po stabilizaci vytvořit nový backup, zkontrolovat jeho výsledek a zaznamenat průběh zásahu.

## Provozní zásady

- Kritické systémy mají mít kopii mimo produkční host.
- Úspěšné vytvoření zálohy samo o sobě nepotvrzuje obnovitelnost.
- Obnovy se testují odděleně od produkce, pokud nejde o řízenou produkční obnovu.
- Migrace nebo import se neoznačují jako test obnovy z PBS.
- Historické, migrační a DR kopie se nemažou bez určení jejich původu a role.
- Selhání Backup, Verify, Prune, Garbage Collection nebo ZFS scrubu má vyvolat upozornění vyžadující pozornost.
- Během incidentu se nespouští Prune, Garbage Collection ani jiné úlohy odstraňující data, dokud není známý rozsah problému a návratová cesta.
- Hesla, tokeny, privátní klíče, app hesla a recovery klíče do repozitáře nepatří. Dokumentace může uvést pouze jejich bezpečné umístění.

## Handover minimum

Před samostatnou správou záloh musí být známé:

- které systémy jsou chráněné, kam se zálohují a jaká je jejich poslední doložená retence;
- jak otevřít PVE Ryzen, PVE Dell, PBS, Pulse a související autoritativní dokumentaci;
- jak odlišit PVE storage `tank-pbs` od skutečného využití PBS datastore `backup`;
- jak ověřit poslední Backup, Verify, Prune, Garbage Collection, ZFS scrub a SMART bez změny konfigurace;
- které obnovy byly skutečně provedené a které jsou pouze plánem;
- kde jsou bezpečně uložené přístupové a obnovovací materiály bez zveřejnění jejich obsahu;
- kdo rozhoduje o spuštění DR a kdo může provést místní zásah v offsite lokalitě.

Konkrétní odpovědnost za místní zásah u Richarda a bezpečné umístění recovery materiálů: **Vyžaduje ověření v živém systému.**

Konkrétní otevřené úkoly jsou vedené pouze v příslušných detailních dokumentech, aby se neduplikovaly v `TODO.md`.
