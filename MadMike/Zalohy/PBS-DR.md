# PBS a disaster recovery

> Poslední doložený provozní stav: **2026-07-28**.  
> Rozsah DR a sporné body byly potvrzeny **2026-07-29**. Údaje bez novější živé kontroly nejsou vydávány za aktuální stav.

## Účel a hranice

Offsite PBS slouží k obnově hlavních systémů MadMike při ztrátě domácího PVE Ryzen. PVE Dell u Richarda poskytuje oddělený Proxmox Backup Server a podle dostupných prostředků také prostor pro dočasnou DR obnovu.

Současný rozsah výslovně neřeší ztrátu celé Dell/offsite lokality. Druhá nezávislá kopie celého PBS datastore proto nyní není požadavkem.

Hardware hostitelů, ZFS topologie a provoz VM jsou autoritativně v projektu [Servery](../Servery/README.md). Tento dokument vlastní backup joby, retenci, údržbu PBS, důkazy obnovitelnosti a DR postupy.

## Aktuální architektura

### Produkční strana

- host: PVE Ryzen;
- hlavní chráněné systémy: Nextcloud VM401, Windows/PREMIER VM501 a Monitoring VM510;
- vzdálené PBS storage v PVE: `pbs-backup`;
- propojení: WireGuard.

### Offsite strana

- host: Dell PowerEdge R430 / PVE Dell;
- PBS: Dell / VM200, 4 vCPU, 8 GB RAM, 64 GB systémový disk;
- datastore: `backup`, přibližně 6,8 TB;
- datový disk PBS je připojený uvnitř VM na `/mnt/datastore`;
- 4× 8TB SAS Seagate Exos jsou rozdělené do dvou samostatných ZFS mirrorů:
  - `tank-pbs`: 2× 8 TB, backing storage pro PBS;
  - `tank-nas`: 2× 8 TB, samostatná rezerva.

`tank-pbs` tedy **není** pool ze všech čtyř disků. Dlouhodobě je schválený přechod na jeden čtyřdiskový pool, ale jeho přesná topologie zatím rozhodnutá není. Realizace a migrace patří do projektu [Servery](../Servery/PVE-Dell.md#schválený-dlouhodobý-směr-storage).

Datová cesta PBS:

```text
tank-pbs na PVE Dell
→ virtuální disk VM200
→ ext4 uvnitř PBS
→ /mnt/datastore
→ datastore backup
```

Po výměně disků blokoval start PBS starý neexistující disk a mount `/mnt/backup`. Neplatná konfigurace byla odstraněna, nový datastore byl vytvořen na `/mnt/datastore` a automatický mount byl opraven pomocí UUID ve `fstab`. Připojení datastore bylo prakticky ověřeno restartem VM200.

Síťové propojení a adresy jsou v [WireGuardu](../Servery/WireGuard.md). Tajné hodnoty PBS připojení se do tohoto dokumentu nezapisují.

## Poslední doložená konfigurace zálohování

Stav níže byl naposledy doložen 2026-07-28:

```text
Cíl: pbs-backup
Režim: Snapshot
Komprese: ZSTD
Čas: denně 02:00
Objekty: CT100, VM401, VM501, VM510
```

Retence:

```text
Keep Daily:   14
Keep Weekly:   8
Keep Monthly: 12
```

Údržba PBS:

- Verify: denně ve 04:00;
- `ignore-verified`: zapnuto;
- opakované ověření již ověřených dat po 30 dnech;
- Prune: denně;
- Garbage Collection: denně.

Starší checkpoint z 2026-07-13 uváděl Verify pouze v neděli ve 04:00. Novější kontrola z 2026-07-28 potvrzuje denní rozvrh a je pro tento zápis rozhodující.

Poslední kontrolované backupy i Garbage Collection skončily `OK`. CT100 byl následně při úklidu monitoringu odstraněn, takže současný výběr objektů v jobu je potřeba živě zkontrolovat a případnou neexistující položku odstranit.

ZFS scrub má zůstat přibližně měsíční. Jeho skutečné plánování, poslední výsledek a notifikace: **Vyžaduje ověření v živém systému.**

## Mapa chráněných objektů

| Systém | Poslední doložená ochrana | Praktická obnova | Poznámka |
|---|---|---|---|
| VM401 Nextcloud | PBS job 2026-07-28 `OK` | Ano | Testovací restore na Dell jako VM402 a pozdější produkční restore na nově instalovaný PVE Ryzen |
| VM501 Windows/PREMIER | PBS job 2026-07-28 `OK` | Ano | Restore z PBS zpět na Ryzen ověřen; Dell VM501 vznikla importem, nikoli PBS restore |
| VM510 Monitoring | PBS job 2026-07-28 `OK` | Ne | Před restore testem je nutné ověřit všechna persistentní data a mounty |
| CT100 Zabbix | Historický PBS backup 2026-07-28 | Ne | Zdrojový CT byl následně odstraněn; staré backup groups se nemažou bez ověření původu |
| Home Assistant | Není přímým objektem tohoto PBS jobu | Viz [Home Assistant](Home-Assistant.md) | Schválený řetězec vede přes Nextcloud a jeho PBS zálohu |
| MikroTik konfigurace | Není přímým objektem tohoto PBS jobu | Ne | Stav exportů a cílový řetězec jsou v [MikroTik](MikroTik.md) |

## Běžná provozní kontrola

Kontrola se provádí bez změny konfigurace a bez ručního spouštění údržby:

1. Ověřit dostupnost PVE Ryzen, PVE Dell a PBS přes jejich běžné interní adresy nebo WireGuard.
2. Na PVE Ryzen ověřit, že storage `pbs-backup` není ve stavu chyby.
3. Na PVE Dell ověřit `tank-pbs`, stav VM200 a datovou cestu podle [PVE Dell / Bezpečná základní kontrola](../Servery/PVE-Dell.md#bezpečná-základní-kontrola).
4. Uvnitř VM200 ověřit, že `/mnt/datastore` je skutečně připojený a že PBS datastore `backup` není omylem prázdný adresář na systémovém disku.
5. V PBS zkontrolovat stav a skutečné obsazení datastore, poslední snapshoty chráněných objektů a historii kritických úloh.
6. Samostatně zkontrolovat poslední Backup, Verify, Prune a Garbage Collection včetně času, výsledku a případného chybového logu.
7. V Pulse porovnat dostupnost, stav ZFS a disků, kapacitu, stáří záloh a `Verified`; Pulse je přehled, nikoli jediný důkaz úspěchu úlohy.
8. Při odchylce zachovat task log a čas události a pokračovat podle diagnostiky. Neprovádět preventivní mazání snapshotů nebo backup groups.

Očekávaný zdravý stav:

- WireGuard a `pbs-backup` jsou dostupné;
- `tank-pbs`, VM200, `/mnt/datastore` a datastore `backup` tvoří souvislou datovou cestu;
- poslední očekávané snapshoty existují a nejsou neobvykle staré;
- Backup, Verify, Prune a Garbage Collection nemají nevyřešenou chybu;
- ZFS nemá nové read/write/checksum chyby a nejsou hlášené kritické SMART problémy;
- kapacita datastore má bezpečnou rezervu.

Požadovaná hranice stáří backupu a minimální kapacitní rezerva: **Vyžaduje ověření v živém systému.**

## Ověřené obnovy a správná klasifikace

### Nextcloud

- Ryzen / VM401 → Dell / VM402: úspěšná testovací obnova z PBS;
- po spuštění fungovaly Apache, MariaDB, Nextcloud i přístup k datům;
- VM401 byla později úspěšně obnovena z PBS na nově nainstalovaný PVE Ryzen;
- produkční `cloud.madmike.cz` a uživatelská data po obnově fungovaly.

Dell / VM401 je starší migrační test Nextcloudu, nikoli PBS DR obnova. Podrobný provozní přehled je v projektu [Nextcloud](../Nextcloud/README.md).

### Windows a PREMIER

- Dell / VM501 vznikla importem, nikoli obnovou z PBS;
- Windows, RDP, PREMIER a účetní data byly na Dellu funkční, ale tento krok se nepočítá jako PBS restore;
- VM501 byla následně úspěšně obnovena z PBS zpět na PVE Ryzen;
- po návratu proběhl další úspěšný inkrementální PBS backup.

Podrobný provozní přehled je v projektu [PREMIER](../Premier/README.md).

### Offsite provoz

- Dell byl fyzicky přesunut k Richardovi.
- WireGuard a routing mezi lokalitami byly ověřeny.
- Oba ZFS pooly byly po přesunu `ONLINE`.
- Scrub po přesunu proběhl bez chyb.
- SMART kontrola čtyř SAS disků neukázala kriticky vadný disk.
- Automatické připojení PBS datastore přežilo restart VM200.

Restart samotné VM200 není totéž jako úplný výpadek napájení a start celého Dellu. Celý power-loss scénář zůstává k praktickému ověření.

## Příprava každé obnovy

Před spuštěním restore:

1. určit důvod obnovy, požadovaný bod v čase a cílové prostředí;
2. potvrdit, že vybraný snapshot patří správnému zdrojovému hostu a objektu;
3. ověřit výsledek posledního Verify nebo přesně zaznamenat, že ověření chybí;
4. zkontrolovat cílovou kapacitu, storage mapování, VMID, IP adresu, DNS a závislosti;
5. rozhodnout, zda půjde o izolovaný test, produkční obnovu, nebo dočasný DR provoz;
6. zabránit souběžnému spuštění dvou produkčních kopií;
7. připravit návratovou cestu a přejímací kritéria aplikace.

Testovací restore se nejdřív spouští bez produkčního síťového připojení nebo s bezpečně změněnou identitou. Snapshot se nepovažuje za použitelný jen proto, že restore úloha skončila `OK`.

## Runbook obnovy jednotlivých VM

### VM401 Nextcloud

1. Obnovit správný snapshot na zvolené storage; u testu použít nekolidující VMID a izolovanou síť.
2. Ověřit přítomnost systémového i datového disku a správné připojení datového prostoru.
3. Spustit VM a ověřit boot, filesystémy, čas, síť a QEMU Guest Agent.
4. Podle [Nextcloud / Provoz a úložiště](../Nextcloud/Provoz-a-uloziste.md) ověřit webový server, databázi, datový adresář a konzistenci aplikace.
5. Ověřit přihlášení, několik skutečných souborů a případně veřejné HTTPS až po rozhodnutí, že jde o autoritativní produkční kopii.
6. Původní produkci ponechat vypnutou nebo izolovanou po celou dobu přejímky.

### VM501 Windows a PREMIER

1. Obnovit snapshot na nekolidující VMID nebo na původní VMID pouze po bezpečném odstavení původní VM501.
2. Ověřit systémový disk, boot Windows, síť, čas a QEMU Guest Agent.
3. Podle [PREMIER / Přístup a provoz](../Premier/Pristup-a-provoz.md) ověřit RDP, spuštění PREMIERu a dostupnost účetních dat bez neřízeného zápisu.
4. Pokud jde o DR provoz, určit jedinou autoritativní kopii a způsob dočasného přístupu účetní.
5. Po přejímce ověřit vlastní aplikační zálohu PREMIERu samostatně; PBS obnova celé VM ji nenahrazuje.

### VM510 Monitoring

1. Před restore ověřit, že vybraný snapshot obsahuje očekávané Docker volumes a bind mounty.
2. Po obnově zkontrolovat filesystém, síť, čas, Docker a adresáře `/opt/npm`, `/opt/pulse` a `/opt/mikr`.
3. Postupovat podle [VM510 / Pořadí obnovy](../Servery/VM510-Docker.md#pořadí-obnovy-vm510): NPM jako první, potom Pulse a Mikr, následně Uptime Kuma.
4. Ověřit proxy hosty a certifikáty, zdroje Pulse, zařízení Mikru, monitory Kumy a historická data.
5. Pokud chybí persistence, zastavit další inicializaci a vybrat jiný snapshot nebo řízenou aplikační obnovu.

## Dokončení a záznam obnovy

Obnova je dokončená až po aplikační přejímce:

1. zaznamenat zdrojový snapshot, cílový host, storage, VMID, začátek a konec;
2. uvést, zda šlo o test, produkční restore nebo DR provoz;
3. zapsat ověřené funkce, ruční kroky, problémy a výsledek;
4. potvrdit, která kopie je nyní autoritativní a že druhá nemůže nechtěně naběhnout;
5. po stabilizaci vytvořit nový backup a ověřit jeho výsledek;
6. aktualizovat tento dokument a aplikační projekt bez tajných hodnot.

## Stručný DR runbook pro ztrátu PVE Ryzen

1. Potvrdit rozsah incidentu a pokud možno zachovat původní disky beze změny.
2. Ověřit dostupnost PVE Dell, VM200, datastore `backup`, posledních použitelných snapshotů a WireGuard spojení.
3. Zvolit cíl obnovy:
   - preferovaně opravený nebo náhradní PVE Ryzen;
   - dočasně PVE Dell, pokud má dostatek prostředků a jsou předem vyřešeny kolize VMID, storage a sítí.
4. Obnovit systémy podle provozní priority. VM401 poskytuje Nextcloud a budoucí HA backupy, VM501 účetní prostředí a VM510 infrastrukturu a monitoring.
5. U každé VM provést příslušný runbook a aplikační přejímku.
6. Teprve po přejímce přesměrovat produkční provoz a zabránit souběžnému spuštění staré i obnovené kopie.
7. Po stabilizaci spustit nový backup, zkontrolovat jeho výsledek a zaznamenat průběh obnovy.

Požadované pořadí služeb, RPO a RTO nejsou jako společné rozhodnutí doložené: **Vyžaduje ověření v živém systému.**

## Výpadek zálohovací cesty bez výpadku produkce

Pokud produkční VM běží, ale `pbs-backup`, PVE Dell nebo PBS nejsou dostupné:

1. označit VM401, VM501 a VM510 jako dočasně bez potvrzené offsite ochrany;
2. omezit zbytné rizikové změny a aktualizace, dokud se ochrana neobnoví;
3. oddělit problém WireGuardu, PVE Dell, VM200, mountu `/mnt/datastore`, PBS služby a autentizace;
4. zachovat chybové logy a tajné údaje nerekonfigurovat naslepo;
5. nevytvářet nový prázdný datastore se stejným názvem a neformátovat neověřené zařízení;
6. po opravě ověřit datovou cestu a spustit řízený backup pouze tehdy, když nebude kolidovat s jinou úlohou;
7. potvrdit vznik nového použitelného snapshotu a následný Verify.

## Backup groups, VMID a nejasné objekty

Poslední doložený stav používá kořenový PBS namespace. Stejná VMID použitá na Ryzenu a Dellu mohou spolu s historickými importy a migracemi vytvářet nejasné nebo orphaned backup groups.

Před smazáním jakékoli skupiny se musí určit:

1. zdrojový host a původ objektu;
2. zda šlo o backup, restore, import nebo migraci;
3. datum a použitelnost posledního snapshotu;
4. zda skupina ještě plní DR nebo historickou roli.

Dell / VM400 má zatím neověřený účel a nesmí být bez dalšího důkazu označena jako nepotřebná.

## Recovery materiály hostitelů

Obnova VM z PBS neřeší sama o sobě obnovu PVE nebo PBS hostitele. Mimo selhaný Ryzen musí být bezpečně dostupné alespoň:

- údaje potřebné pro přístup k Dell/PBS a WireGuard propojení;
- identifikace PBS datastore, fingerprintu a používaného účtu nebo tokenu;
- popis storage layoutu a síťových závislostí;
- instalační postup PVE a informace potřebné k opětovnému připojení PBS;
- případný klientský recovery klíč, pokud bude klientské šifrování zapnuto.

Do GitHubu se zapisuje pouze bezpečné umístění těchto materiálů, nikdy jejich tajný obsah.

Klientské šifrování PBS je k 2026-07-29 **nerozhodnuté**. Dokumentace proto netvrdí, že je zapnuté ani že je definitivně vypnuté.

## Interpretace kapacity

PVE storage `tank-pbs` může kvůli thick `refreservation` virtuálního disku VM200 vypadat téměř plné. Při poslední kontrole PVE ukazovalo přibližně 97 %, zatímco skutečný PBS datastore byl využitý zhruba ze 3 %.

Pro reálnou kapacitu záloh je autoritativní PBS datastore `backup`, nikoli procento PVE storage. Neobvyklý rozdíl se nejdřív vysvětlí datovou cestou a rezervací; není důvodem k okamžitému mazání záloh.

## Diagnostika

| Projev | První kontrola | Bezpečný další krok |
|---|---|---|
| Backup z Ryzenu selhal | task log, `pbs-backup`, WireGuard, kapacita a dostupnost datastore | zachovat log; neodstraňovat staré snapshoty, dokud není potvrzen nový použitelný backup |
| PBS GUI funguje, datastore chybí | `/mnt/datastore`, zařízení, filesystem a VM200 | nespouštět údržbu a nevytvářet prázdný datastore; pokračovat v PVE Dell runbooku |
| Datastore je téměř plný | skutečné PBS využití, růst a retence | odlišit PBS kapacitu od PVE `refreservation`; mazání nespouštět jako první krok |
| Verify hlásí chybu | dotčený snapshot/chunk, task log, ZFS a SMART | zachovat data i logy; neprovádět Prune/GC před určením rozsahu a obnovitelnosti |
| Prune nebo GC selhaly | task log, kapacita, mount a současně běžící úlohy | neopakovat úlohu naslepo; nejdřív odstranit příčinu a ověřit datastore |
| Pulse hlásí orphaned backup | VMID, zdrojový host, import/migrace/restore | nic nemazat; určit původ skupiny podle tohoto dokumentu |
| Restore skončil `OK`, aplikace nefunguje | storage mapování, síť, mounty a aplikační logy | pokračovat v autoritativním aplikačním runbooku; restore úlohu nepovažovat za dokončenou obnovu |
| Dell není dostupný z HOME | WireGuard, internet lokality a iDRAC | oddělit síťový problém od výpadku hostitele; viz PVE Dell a WireGuard |

## Handover a odpovědnosti

- Rozhodnutí o spuštění produkčního DR, výběru snapshotu a přepnutí autoritativní kopie musí provést správce infrastruktury.
- Místní zásah v offsite lokalitě se koordinuje s osobou, která má fyzický přístup k Dellu; konkrétní jméno a dostupnost: **Vyžaduje ověření v živém systému.**
- Aplikační přejímku provádí osoba, která zná běžnou funkci systému; u PREMIERu musí být ověřen i pracovní přístup účetní.
- O každé produkční obnově se zapisuje výsledek do tohoto dokumentu a do autoritativního projektu aplikace.
- Tajné přístupy a recovery materiály se spravují podle projektu [Přístupy](../Pristupy/README.md), nikoli v tomto souboru.

## Otevřené kontroly

- [ ] Ověřit živý výběr objektů backup jobu a odstranit případnou neexistující položku CT100.
- [ ] Ověřit poslední úspěšné běhy Backup, Verify, Prune a Garbage Collection.
- [ ] Ověřit aktuální obsazení datastore `backup`.
- [ ] Ověřit plánování a poslední běh scrubů na `tank-pbs` a `tank-nas`.
- [ ] Ověřit SMART a teploty čtyř SAS disků a systémového SSD proti živému stavu.
- [ ] Ověřit persistentní Docker data a mounty VM510 a provést testovací restore.
- [ ] Prakticky ověřit start PVE Dell, VM200 a datastore po úplném výpadku napájení.
- [ ] Stanovit rozumnou četnost opakovaných testů obnovy.
- [ ] Stanovit společné RPO, RTO, pořadí obnovy a hranici stáří záloh vyžadující zásah.
- [ ] Určit původ nejasných/orphaned backup groups a samostatně ověřit účel Dell / VM400 jako odlišného objektu.
- [ ] Zdokumentovat bezpečné umístění recovery materiálů hostitelů bez zveřejnění tajných údajů.
- [ ] Rozhodnout o klientském šifrování PBS a při jeho použití bezpečně uložit recovery klíč.
- [ ] Určit odpovědnost a dostupnost místního zásahu u Richarda.

Testy nativních notifikací Backup, Verify, Prune a Garbage Collection jsou vedené v [Monitoring / Pulse](../Monitoring/Pulse.md).
