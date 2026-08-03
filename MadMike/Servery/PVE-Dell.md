# PVE Dell

> Poslední doložený technický stav: **2026-07-28**. Při tomto zpracování nebyl host znovu porovnán s živým systémem.

## Role

Offsite DR host u Richarda. Provozuje Proxmox Backup Server ve VM200 a poskytuje oddělené prostředí pro testovací obnovy a dočasný DR provoz.

- hostname: `pbs-madmike`;
- interní IP PVE hostu: `192.168.100.11`;
- běžný HTTPS přístup: `https://pvedell.mikehub.cz`;
- přístup z HOME: přes WireGuard;
- vzdálená hardwarová správa: iDRAC8.

Dell není běžný produkční host ani trvalý NAS. Volný výkon nebo místo nejsou důvodem přesouvat na něj služby z Ryzenu bez konkrétního DR nebo migračního účelu.

## Ověřený hardware

- server: Dell PowerEdge R430;
- procesory: 2× Intel Xeon E5-2630L v4;
- paměť: 64 GB ECC RAM;
- řadič: HBA330 v IT režimu;
- systémový disk: 400 GB SATA SSD;
- datové disky: 4× 8 TB SAS Seagate Exos 7E8;
- síť: 1 Gbit;
- dva napájecí zdroje na oddělených napájecích větvích.

Existence dvou zdrojů nepotvrzuje chování hostitele, VM200 a datastore po úplném výpadku. Praktický power-cycle test patří do DR ověření v projektu [Zálohy](../Zalohy/PBS-DR.md).

## Současné ZFS storage

Ověřený současný stav tvoří dva samostatné mirrory:

```text
tank-pbs → mirror ze 2× 8 TB SAS
tank-nas → mirror ze 2× 8 TB SAS
```

Mountpointy na PVE hostu:

```text
/mnt/tank-pbs
/mnt/tank-nas
```

PVE storage záznamy:

```text
pbs-datastore → /mnt/tank-pbs
nas-storage   → /mnt/tank-nas
```

Po výměně disků a fyzickém přesunu byly oba pooly `ONLINE`; scrub proběhl bez chyb a SMART kontrola neukázala kriticky vadný disk. Jde o datovaný stav, nikoliv současné měření.

## Schválený dlouhodobý směr storage

Dlouhodobým cílem je jeden společný pool ze všech čtyř 8TB SAS disků. Přesná topologie budoucího poolu zatím není schválená; starší návrh RAIDZ2 je kandidát, nikoliv konečné rozhodnutí.

Migrace se provede nenásilně a až podle samostatného bezpečného plánu. Ten musí předem určit:

- cílovou topologii, datasety a PVE storage;
- dočasné umístění dat během přestavby;
- ověřenou zálohu a prakticky použitelnou obnovu;
- pořadí kroků, odstávku a návratový postup;
- způsob opětovného připojení datastore k VM200.

Do realizace zůstávají dva současné mirrory autoritativním provozním stavem.

## Dell / VM200 – Proxmox Backup Server

- 4 vCPU;
- 8 GB RAM;
- 64 GB systémový disk;
- interní IP: `192.168.100.12`;
- běžný HTTPS přístup: `https://pbs.mikehub.cz`;
- PBS datastore `backup`, přibližně 6,8 TB;
- datový disk je uvnitř VM připojený na `/mnt/datastore`.

Datová cesta:

```text
tank-pbs
→ virtuální disk VM200
→ ext4
→ /mnt/datastore
→ datastore backup
```

Po změně storage byl odstraněn starý neexistující disk i mount `/mnt/backup`. Automatický mount nového datastore je vedený pomocí UUID ve `fstab` a byl ověřen restartem VM200.

Autoritativní dokumentace zálohování, údržby datastore, SMART, scrubů a testů obnovy je v [PBS a disaster recovery](../Zalohy/PBS-DR.md).

## Virtuální stroje

| VM | Poslední doložený stav | Ověřená role |
|---|---|---|
| Dell / VM200 | běží | Proxmox Backup Server |
| Dell / VM400 | vypnutá | účel neznámý; nutno ověřit |
| Dell / VM401 | vypnutá | migrační test při přesunu Nextcloudu z bare metal instalace na PVE Ryzen |
| Dell / VM402 | vypnutá | úspěšná testovací obnova produkčního Nextcloudu z PBS |
| Dell / VM501 | vypnutá | funkční import Windows/PREMIER; nešlo o PBS restore |

VM400, VM401, VM402 a VM501 jsou ponechané, dokud nebude jejich další osud jednotlivě rozhodnutý. Před odstraněním kterékoliv z nich je nutné ověřit obsah, původ, backup groups a potřebnost.

## Ověřené DR výsledky

- Obnova Nextcloudu do Dell / VM402 byla úspěšná; fungovaly Apache, MariaDB, Nextcloud i přístup k datům.
- Dell / VM501 vznikla importem starého diskového obrazu; Windows, RDP a PREMIER byly funkční, ale tento krok není PBS restore.
- VM501 byla později úspěšně obnovena z PBS zpět na PVE Ryzen.
- Dell / VM401 je starší migrační test, nikoliv DR obnova.
- WireGuard a routing mezi domácí a offsite lokalitou byly prakticky ověřené.

Podrobnosti a další ověřovací úkoly jsou v projektu [Zálohy](../Zalohy/README.md).

## Bezpečná základní kontrola

Na PVE Dell:

```bash
pveversion -v
hostnamectl
ip -brief address
qm list
pct list
pvesm status
zpool status -x
zfs list -o name,used,avail,mountpoint
df -hT
systemctl --failed
journalctl -p err -b --no-pager
```

Kontrola vazby VM200:

```bash
qm status 200
qm config 200
```

Uvnitř VM200 se podle projektu Zálohy ověří zejména:

```bash
findmnt /mnt/datastore
df -hT /mnt/datastore
systemctl --failed
```

Očekávaný zdravý stav:

- `tank-pbs` a `tank-nas` jsou `ONLINE` bez nových chyb;
- PVE storage jsou dostupné;
- běží VM200, ostatní doložené testovací VM jsou vypnuté;
- `/mnt/datastore` je skutečně připojený a PBS vidí datastore `backup`;
- host je dostupný přes WireGuard a iDRAC;
- poslední kritické PBS úlohy nemají chybu.

## Korektní restart

### VM200

1. Ověřit, že neprobíhá backup, Verify, Prune, Garbage Collection ani restore.
2. Zaznamenat stav datastore a posledních úloh.
3. VM200 vypnout nebo restartovat standardním způsobem.
4. Po startu ověřit `/mnt/datastore`, PBS datastore `backup`, webové rozhraní a úlohy.

### Celý PVE Dell

1. Koordinovat odstávku PBS s domácím PVE Ryzen a zastavit plánované úlohy pouze řízeně.
2. Ověřit oba ZFS pooly a stav VM200.
3. Korektně vypnout VM200 a potom hostitele.
4. Po startu nejprve ověřit iDRAC, PVE, síť, storage a ZFS.
5. Spustit VM200 a ověřit skutečný mount `/mnt/datastore` dříve, než se systém označí za obnovený.
6. Ověřit spojení z Ryzenu na storage `pbs-backup` a funkci PBS GUI.

Plný power-loss test se provádí jako plánovaný DR test s možností místního zásahu, nikoliv náhodným odpojením napájení.

## Plánovaná aktualizace PVE Dell

1. Ověřit podporovanou verzi, správné repozitáře, stav ZFS a systémového disku.
2. Zkontrolovat, že neběží žádná PBS úloha a že existuje návratová cesta k hostiteli i VM200.
3. Zaznamenat výchozí verzi a čekající balíčky:

```bash
apt update
apt list --upgradable
```

4. Aktualizaci PVE hostitele a PBS ve VM200 nespojovat bez konkrétního důvodu do jednoho neoddělitelného zásahu.
5. Po aktualizaci hostitele provést základní kontrolu; po aktualizaci PBS ověřit datastore, poslední snapshoty a naplánované úlohy.
6. Přechod hlavní verze provést pouze podle samostatného oficiálního postupu.

Oficiální provozní reference: [Proxmox VE – Host System Administration](https://pve.proxmox.com/pve-docs/chapter-sysadmin.html).

## Diagnostika

| Projev | První kontrola | Bezpečný další krok |
|---|---|---|
| Dell není dostupný z HOME | WireGuard, veřejná strana lokality, iDRAC | oddělit síťový problém od výpadku hostitele |
| PVE běží, VM200 ne | `qm status 200`, Tasks a `qm config 200` | před startem ověřit storage a předchozí ukončení |
| VM200 běží, datastore chybí | `findmnt`, `fstab`, zařízení a filesystem | PBS úlohy nespouštět; nevytvářet nový prázdný datastore |
| `tank-pbs` nebo `tank-nas` není `ONLINE` | `zpool status -v`, SMART a fyzický disk | zachovat stav, neodpojovat více disků a nejprve určit návratovou cestu |
| PVE storage vypadá téměř plná | porovnat thick `refreservation` s využitím PBS datastore | pro reálnou kapacitu záloh použít PBS pohled, ne samotné procento PVE storage |
| PBS GUI funguje, backup z Ryzenu ne | WireGuard, storage `pbs-backup`, účet/token a Tasks | tajné údaje nerekonfigurovat naslepo; zachovat chybový log |
| Testovací VM má kolizi IP/VMID | stav produkční kopie na Ryzenu | testovací VM izolovat; nikdy nespouštět dvě produkční kopie |

## DR guardrails

- VM401, VM402 a VM501 na Dellu se nespouštějí jen pro kontrolu bez posouzení kolize s produkcí.
- Restore, import a migrace jsou rozdílné události a v dokumentaci se tak označují.
- Při dočasném DR provozu se určí jedna autoritativní kopie a původní produkce se vypne nebo izoluje.
- Návrat z DR se provádí řízeně, se záznamem posledních změn a novým backupem.
- Samotný dostupný PBS dashboard neprokazuje obnovitelnost; rozhodující je použitelný snapshot a praktická přejímka aplikace.

## Otevřené kontroly

**Vyžaduje ověření v živém systému.**

- [ ] Zjistit původ a účel Dell / VM400.
- [ ] Ověřit aktuální verzi a konfiguraci PVE Dell, VM200, storage a sítě proti živému systému.
- [ ] Připravit a schválit bezpečný migrační plán z dnešních dvou mirrorů na jeden pool ze čtyř 8TB disků, včetně cílové topologie, zálohy, obnovy a rollbacku.

Pravidelné kontroly SMART, scrubů, PBS úloh a power-loss test jsou evidované pouze v [PBS a disaster recovery](../Zalohy/PBS-DR.md).
