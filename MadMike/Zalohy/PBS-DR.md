# PBS a disaster recovery

> Poslední doložený provozní stav: **2026-08-12**.  
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

Stav byl živě read-only ověřen 2026-08-12:

```text
Cíl: pbs-backup
Režim: Snapshot
Čas: denně 02:00
Objekty: VM401, VM501, VM510
```

CT100 byl dříve součástí backup jobu, ale po odstranění kontejneru již v živé konfiguraci jobu není. Na PVE Ryzen při kontrole existovaly právě VM401, VM501 a VM510, takže žádná aktuální VM nebyla z jobu vynechána.

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

Starší checkpoint z 2026-07-13 uváděl Verify pouze v neděli ve 04:00. Novější kontrola z 2026-07-28 a živé ověření 2026-08-12 potvrzují denní rozvrh.

Živá read-only kontrola 2026-08-12 potvrdila:

- jeden aktivní backup job na PVE Ryzen pro VM401, VM501 a VM510;
- automatické backup tasky ve sledovaném výpisu od 2026-07-29 do 2026-08-12 skončily všechny `OK`;
- fyzickou existenci aktuálních snapshotů VM401, VM501 a VM510 na datastore;
- poslední kontrolované Verify běhy 2026-08-09 až 2026-08-12 skončily `OK`;
- poslední kontrolované Prune a Garbage Collection skončily `OK`;
- datastore `backup` je skutečně připojený jako `/dev/sdb`, ext4, na `/mnt/datastore`;
- kapacitu datastore přibližně 6,8 TB, využito přibližně 287 GB, volno přibližně 6,2 TB, tedy asi 5 % obsazení.

ZFS scrub má zůstat přibližně měsíční. Jeho skutečné plánování, poslední výsledek a notifikace: **Vyžaduje ověření v živém systému.**

## Mapa chráněných objektů

| Systém | Poslední doložená ochrana | Praktická obnova | Poznámka |
|---|---|---|---|
| VM401 Nextcloud | PBS job 2026-08-12 `OK` | Ano | Testovací restore na Dell jako VM402 a pozdější produkční restore na nově instalovaný PVE Ryzen |
| VM501 Windows/PREMIER | PBS job 2026-08-12 `OK` | Ano | Restore z PBS zpět na Ryzen ověřen; Dell VM501 vznikla importem, nikoli PBS restore |
| VM510 Monitoring | PBS job 2026-08-12 `OK` | Ne | Před restore testem je nutné ověřit všechna persistentní data a mounty |
| CT100 Zabbix | Historický PBS backup | Ne | Zdrojový CT byl odstraněn a již není v aktuálním backup jobu; staré backup groups se nemažou bez ověření původu |
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

### VM510 Monitoring

Praktický restore VM510 zatím nebyl proveden. Při kontrole 2026-08-12 byl pouze ověřen aktuální backup job, fyzická existence snapshotů a úspěšné Verify. Praktický restore zůstává samostatným budoucím DR úkolem.

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
5. Pokud chybí persistence, zastavit další inicializaci a vybrat jiný snapshot nebo řízený postup.

## Otevřené úkoly

- [x] Ověřit živý výběr objektů backup jobu a odstranit případnou neexistující položku CT100. — 2026-08-12 ověřeno; CT100 již v jobu není, job obsahuje VM401, VM501 a VM510.
- [x] Ověřit poslední úspěšné běhy Backup, Verify, Prune a Garbage Collection. — 2026-08-12 ověřeno, poslední kontrolované běhy `OK`.
- [ ] Ověřit plánování ZFS scrubů, poslední výsledek a způsob notifikace.
- [ ] Stanovit požadovanou maximální stáří posledního použitelného backupu a minimální bezpečnou rezervu datastore.
- [ ] Prakticky otestovat restore VM510 Monitoring v izolovaném prostředí.
- [ ] Prakticky otestovat plný power-loss / cold-start scénář PVE Dell + VM200 + datastore.
