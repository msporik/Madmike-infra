# PBS a disaster recovery

> Poslední doložený provozní stav: **2026-07-28**.  
> Rozsah DR a sporné body byly potvrzeny **2026-07-29**. Údaje bez novější živé kontroly nejsou vydávány za aktuální stav.

## Účel a hranice

Offsite PBS slouží k obnově hlavních systémů MadMike při ztrátě domácího PVE Ryzen. PVE Dell u Richarda poskytuje oddělený Proxmox Backup Server a podle dostupných prostředků také prostor pro dočasnou DR obnovu.

Současný rozsah výslovně neřeší ztrátu celé Dell/offsite lokality. Druhá nezávislá kopie celého PBS datastore proto nyní není požadavkem.

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
  - `tank-nas`: 2× 8 TB, samostatná NAS/archivní rezerva.

`tank-pbs` tedy **není** pool ze všech čtyř disků. Dlouhodobě je schválený přechod na jeden čtyřdiskový pool, ale jeho přesná topologie zatím rozhodnutá není. Realizace a migrace patří do projektu [Servery](../Servery/README.md).

Datová cesta PBS:

```text
tank-pbs na PVE Dell
→ virtuální disk VM200
→ ext4 uvnitř PBS
→ /mnt/datastore
→ datastore backup
```

Po výměně disků blokoval start PBS starý neexistující disk a mount `/mnt/backup`. Neplatná konfigurace byla odstraněna, nový datastore byl vytvořen na `/mnt/datastore` a automatický mount byl opraven pomocí UUID ve `fstab`. Připojení datastore bylo prakticky ověřeno restartem VM200.

Podrobnosti fyzických hostů jsou v projektu [Servery](../Servery/README.md). Síťové propojení je v [WireGuardu](../Servery/WireGuard.md).

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

ZFS scrub má zůstat přibližně měsíční. Jeho skutečné plánování, poslední výsledek a notifikace se musí ověřit zvlášť.

## Mapa chráněných objektů

| Systém | Poslední doložená ochrana | Praktická obnova | Poznámka |
|---|---|---|---|
| VM401 Nextcloud | PBS job 2026-07-28 `OK` | Ano | Testovací restore na Dell jako VM402 a pozdější produkční restore na nově instalovaný PVE Ryzen |
| VM501 Windows/PREMIER | PBS job 2026-07-28 `OK` | Ano | Restore z PBS zpět na Ryzen ověřen; Dell VM501 vznikla importem, nikoli PBS restore |
| VM510 Monitoring | PBS job 2026-07-28 `OK` | Ne | Před restore testem je nutné ověřit persistentní Docker data a mounty |
| CT100 Zabbix | Historický PBS backup 2026-07-28 | Ne | Zdrojový CT byl následně odstraněn; staré backup groups se nemažou bez ověření původu |
| Home Assistant | Není přímým objektem tohoto PBS jobu | Viz [Home Assistant](Home-Assistant.md) | Schválený řetězec vede přes Nextcloud a jeho PBS zálohu |
| MikroTik konfigurace | Není přímým objektem tohoto PBS jobu | Ne | Stav exportů a cílový řetězec jsou v [MikroTik](MikroTik.md) |

## Ověřené obnovy a správná klasifikace

### Nextcloud

- Ryzen / VM401 → Dell / VM402: úspěšná testovací obnova z PBS;
- po spuštění fungovaly Apache, MariaDB, Nextcloud i přístup k datům;
- VM401 byla později úspěšně obnovena z PBS na nově nainstalovaný PVE Ryzen;
- produkční `cloud.madmike.cz` a uživatelská data po obnově fungovaly.

Dell / VM401 je starší migrační test Nextcloudu, nikoli PBS DR obnova.

Podrobný provozní přehled je v projektu [Nextcloud](../Nextcloud/README.md).

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

## Stručný DR runbook pro ztrátu PVE Ryzen

1. Potvrdit rozsah incidentu a pokud možno zachovat původní disky beze změny.
2. Ověřit dostupnost PVE Dell, VM200, datastore `backup`, posledních použitelných snapshotů a WireGuard spojení.
3. Zvolit cíl obnovy:
   - preferovaně opravený nebo náhradní PVE Ryzen;
   - dočasně PVE Dell, pokud má dostatek prostředků a jsou předem vyřešeny kolize VMID a sítí.
4. Obnovit systémy podle provozní priority. VM401 poskytuje Nextcloud a budoucí HA backupy, VM501 účetní prostředí a VM510 monitoring.
5. U každé VM ověřit start, síť, storage, aplikační data a přístup uživatelů.
6. Teprve po přejímce přesměrovat produkční provoz a zabránit souběžnému spuštění staré i obnovené kopie.
7. Po stabilizaci spustit nový backup, zkontrolovat jeho výsledek a zaznamenat průběh obnovy.

## Interpretace kapacity

PVE storage `tank-pbs` může kvůli thick `refreservation` virtuálního disku VM200 vypadat téměř plné. Při poslední kontrole PVE ukazovalo přibližně 97 %, zatímco skutečný PBS datastore byl využitý zhruba ze 3 %.

Pro reálnou kapacitu záloh je autoritativní PBS datastore `backup`, nikoli procento PVE storage.

## Otevřené kontroly

- [ ] Ověřit živý výběr objektů backup jobu a odstranit případnou neexistující položku CT100.
- [ ] Ověřit poslední úspěšné běhy Backup, Verify, Prune a Garbage Collection.
- [ ] Ověřit aktuální obsazení datastore `backup`.
- [ ] Ověřit plánování a poslední běh scrubů na `tank-pbs` a `tank-nas`.
- [ ] Ověřit SMART a teploty čtyř SAS disků a systémového SSD proti živému stavu.
- [ ] Ověřit persistentní Docker data a mounty VM510 a provést testovací restore.
- [ ] Prakticky ověřit start PVE Dell, VM200 a datastore po úplném výpadku napájení.
- [ ] Otestovat nativní notifikace neúspěšného Backup, Verify, Prune a Garbage Collection jobu.
- [ ] Stanovit rozumnou četnost opakovaných testů obnovy.
- [ ] Určit původ nejasných/orphaned backup groups a účel Dell / VM400.
- [ ] Zdokumentovat bezpečné umístění recovery materiálů hostitelů bez zveřejnění tajných údajů.
- [ ] Rozhodnout o klientském šifrování PBS a při jeho použití bezpečně uložit recovery klíč.
