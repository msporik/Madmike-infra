# PVE Dell

## Role

Offsite DR host u Richarda. Provozuje Proxmox Backup Server ve VM200 a poskytuje oddělené prostředí pro testovací obnovy.

- hostname: `pbs-madmike`;
- interní IP PVE hostu: `192.168.100.11`;
- přístup z HOME: přes WireGuard.

## Ověřený hardware

- server: Dell PowerEdge R430;
- procesory: 2× Intel Xeon E5-2630L v4;
- paměť: 64 GB ECC RAM;
- řadič: HBA330 v IT režimu;
- systémový disk: 400 GB SATA SSD;
- datové disky: 4× 8 TB SAS Seagate Exos 7E8;
- vzdálená správa: iDRAC8;
- síť: 1 Gbit;
- dva napájecí zdroje na oddělených napájecích větvích.

Samotná existence dvou zdrojů nepotvrzuje chování celého serveru, VM200 a datastore po úplném výpadku. Praktický power-cycle test patří do DR ověření v projektu [Zálohy](../Zalohy/PBS-DR.md).

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

Po výměně disků byly oba pooly `ONLINE` a SMART kontrola neukázala kriticky vadný disk. Po fyzickém přesunu serveru oba pooly zůstaly `ONLINE` a scrub proběhl bez chyb.

## Schválený dlouhodobý směr storage

Dlouhodobým cílem je jeden společný pool ze všech čtyř 8TB SAS disků. Přesná topologie budoucího poolu zatím není schválená; starší návrh RAIDZ2 je kandidát, nikoliv doložený konečný stav.

Migrace se provede nenásilně a až podle samostatného bezpečného plánu. Ten musí předem určit:

- cílovou topologii, datasety a PVE storage;
- dočasné umístění dat během přestavby;
- ověřenou zálohu a prakticky použitelnou obnovu;
- pořadí kroků, odstávku a návratový postup;
- způsob opětovného připojení datastore k VM200.

Do realizace tohoto plánu zůstávají dva současné mirrory autoritativním provozním stavem.

## Dell / VM200 – Proxmox Backup Server

- 4 vCPU;
- 8 GB RAM;
- 64 GB systémový disk;
- PBS datastore `backup`, přibližně 6,8 TB;
- datový disk je uvnitř VM připojený na `/mnt/datastore`;
- interní IP: `192.168.100.12`.

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

| VM | Stav | Ověřená role |
|---|---|---|
| Dell / VM200 | běží | Proxmox Backup Server |
| Dell / VM400 | vypnutá | Účel zatím neznámý; nutno ověřit |
| Dell / VM401 | vypnutá | Migrační test při přesunu Nextcloudu z bare metal instalace na PVE Ryzen |
| Dell / VM402 | vypnutá | Úspěšná testovací obnova produkčního Nextcloudu z PBS |
| Dell / VM501 | vypnutá | Úspěšná testovací obnova produkční Windows VM s PREMIERem z PBS |

VM400, VM401, VM402 a VM501 jsou záměrně ponechané, dokud nebude jejich další osud jednotlivě rozhodnutý. Před odstraněním kterékoliv z nich je nutné znovu ověřit její obsah a potřebnost; nejde o samostatný jednorázový TODO.

## Ověřené DR výsledky

- Obnova Nextcloudu do Dell / VM402 byla úspěšná; VM naběhla a fungovaly Apache, MariaDB, Nextcloud i přístup k datům.
- Obnova Windows VM s PREMIERem do Dell / VM501 byla úspěšná.
- Dell / VM401 není DR obnova, ale starší migrační test.
- WireGuard a routing mezi domácí a offsite lokalitou byly prakticky ověřené.

Podrobnosti a další ověřovací úkoly jsou vedené pouze v projektu [Zálohy](../Zalohy/README.md).

## Otevřené kroky

- [ ] Zjistit původ a účel Dell / VM400.
- [ ] Ověřit aktuální verzi a konfiguraci PVE Dell proti živému systému.
- [ ] Připravit a schválit bezpečný migrační plán z dnešních dvou mirrorů na jeden pool ze čtyř 8TB disků, včetně zálohy, obnovy a návratového postupu.
