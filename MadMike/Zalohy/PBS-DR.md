# PBS a disaster recovery

## Účel

Offsite zálohy a prakticky ověřitelná obnova hlavních systémů MadMike. Produkce běží převážně na PVE Ryzen; PVE Dell u Richarda poskytuje oddělený PBS a prostor pro DR obnovy.

## Aktuální architektura

### Produkční strana

- host: PVE Ryzen;
- hlavní chráněné systémy: Nextcloud VM401, Windows/PREMIER VM501 a Monitoring VM510;
- vzdálené PBS storage v PVE: `pbs-backup`;
- propojení: WireGuard.

### Offsite strana

- host: Dell PowerEdge R430 / PVE Dell;
- PBS: Dell / VM200, 4 vCPU, 8 GB RAM, 64GB systémový disk;
- datastore: `backup`, přibližně 6,8 TB;
- datový disk PBS je připojený uvnitř VM na `/mnt/datastore`;
- 4× 8TB SAS Seagate Exos jsou rozdělené do dvou samostatných ZFS mirrorů:
  - `tank-pbs`: 2× 8 TB, backing storage pro PBS;
  - `tank-nas`: 2× 8 TB, samostatná NAS/archivní rezerva.

`tank-pbs` tedy **není** pool ze všech čtyř disků.

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

## Poslední ověřená konfigurace zálohování

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

Starší checkpoint z 2026-07-13 ještě uváděl Verify pouze v neděli ve 04:00; novější kontrola z 2026-07-28 potvrzuje denní rozvrh a je pro dokumentaci rozhodující.

Poslední kontrolované backupy i Garbage Collection skončily `OK`. CT100 byl následně při úklidu monitoringu odstraněn, takže současný výběr objektů v jobu je potřeba živě zkontrolovat a případnou neexistující položku odstranit.

ZFS scrub má zůstat přibližně měsíční. Jeho skutečné plánování a notifikace se musí ověřit zvlášť.

## Ověřené testy obnovy

### Nextcloud

- produkční zdroj: Ryzen / VM401;
- testovací obnova: Dell / VM402;
- obnova z PBS byla úspěšná;
- po spuštění fungovaly Apache, MariaDB, Nextcloud i přístup k datům;
- z PBS byla následně úspěšně obnovena také produkční VM401 na nově nainstalovaný PVE Ryzen;
- produkční `cloud.madmike.cz` a uživatelská data po obnově fungovaly.

Podrobný provozní přehled je v projektu [Nextcloud](../Nextcloud/README.md).

### Windows a PREMIER

- produkční zdroj: Ryzen / VM501;
- testovací obnova: Dell / VM501;
- Windows, RDP, PREMIER i účetní data byly po obnově funkční;
- VM501 byla později úspěšně obnovena z PBS zpět na PVE Ryzen;
- po migraci proběhl další úspěšný inkrementální PBS backup.

Podrobný provozní přehled je v projektu [PREMIER](../Premier/README.md).

Dell / VM401 je starší migrační test Nextcloudu, nikoli PBS DR obnova. Dell / VM400 má zatím neověřený účel.

## Ověřený offsite provoz

- Dell byl fyzicky přesunut k Richardovi.
- WireGuard a routing mezi lokalitami byly ověřeny.
- Oba ZFS pooly byly po přesunu `ONLINE`.
- Scrub po přesunu proběhl bez chyb.
- SMART kontrola čtyř SAS disků neukázala kriticky vadný disk.
- Automatické připojení PBS datastore přežilo restart VM200.

Restart samotné VM200 není totéž jako úplný výpadek napájení a start celého Dellu. Celý power-loss scénář zůstává k praktickému ověření.

## Interpretace kapacity

PVE storage `tank-pbs` může kvůli thick `refreservation` virtuálního disku VM200 vypadat téměř plné. Při poslední kontrole PVE ukazovalo přibližně 97 %, zatímco skutečný PBS datastore byl využitý zhruba ze 3 %.

Pro reálnou kapacitu záloh je autoritativní PBS datastore `backup`, nikoli procento PVE storage.

## Otevřené kontroly

- [ ] Ověřit živý výběr objektů backup jobu a odstranit případnou neexistující položku CT100.
- [ ] Ověřit poslední úspěšné běhy Backup, Verify, Prune a Garbage Collection.
- [ ] Ověřit aktuální obsazení datastore `backup`.
- [ ] Ověřit plánování a poslední běh scrubů na `tank-pbs` a `tank-nas`.
- [ ] Ověřit SMART a teploty čtyř SAS disků a systémového SSD proti živému stavu.
- [ ] Prakticky ověřit start PVE Dell, VM200 a datastore po úplném výpadku napájení.
- [ ] Otestovat nativní notifikace neúspěšného Backup, Verify, Prune a Garbage Collection jobu.
- [ ] Stanovit rozumnou četnost opakovaných testů obnovy.
- [ ] Rozhodnout a zdokumentovat roli `tank-nas`.
- [ ] Doplnit stručný DR runbook pro ztrátu PVE Ryzen.
- [ ] Rozhodnout o klientském šifrování PBS záloh a bezpečném uložení klíče.
