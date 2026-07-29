# PVE Ryzen

## Role

Hlavní produkční Proxmox VE server v domácí lokalitě. Provozuje zejména produkční Nextcloud, účetní Windows VM s PREMIERem a infrastrukturní Docker VM.

- hostname: `pve`;
- interní IP: `192.168.89.32`;
- současná platforma: AMD AM4.

Současný hardware provozované role zvládá. Zároveň je schválený nenásilný upgrade v rámci AM4 podle vhodné nabídky; cílové parametry jsou v dokumentu [Budoucí produkční serverová platforma](Budouci-platforma.md).

## Ověřený hardware

- procesor: AMD Ryzen 3 4300G;
- paměť: 32 GB RAM;
- systémový disk: NVMe Micron 512 GB;
- rychlé datové úložiště: 2× Micron 5400 1,92 TB v ZFS mirroru `tank-ssd`;
- kapacitní úložiště: 2× WD Red 6 TB v ZFS mirroru `tank-hdd`.

Po čisté instalaci PVE 9 bylo zdokumentované rozdělení systémového NVMe:

```text
pve-root   přibližně 96 GB
pve-swap   8 GB
pve-data   přibližně 349 GB
```

## Napájení

Současný typ zdroje a chování celého serveru po úplném výpadku napájení nebyly při konsolidaci živě ověřené.

Schválený nejbližší krok je po návratu z dovolené objednat M4-ATX. Jde zatím o plánovaný prvek napájení, nikoliv o instalovaný současný stav. Po montáži musí následovat praktický test výpadku, návratu napájení a automatického spuštění serveru.

## Storage

### `tank-ssd`

- ZFS mirror ze dvou Micron 5400 1,92 TB;
- přibližně 1,68 TB využitelné kapacity;
- role: produkční VM;
- při posledním ověření `ONLINE`.

### `tank-hdd`

- ZFS mirror ze dvou WD Red 6 TB;
- přibližně 5,3 TB využitelné kapacity;
- role: archivní data;
- dataset `tank-hdd/Archiv`;
- doložená adresářová struktura: `Video`, `Synology`, `Rodina`, `Dokumenty`, `Historicke-zalohy`.

Původní WD RAID byl před zrušením sestaven pouze pro čtení, zkontrolován a teprve poté odstraněn. Přibližně 123 GB původních video dat bylo zachováno v archivu.

## Důležité virtuální stroje

### Ryzen / VM401 – produkční Nextcloud

- role: produkční Nextcloud;
- prostředky: 2 vCPU, 4 GB RAM;
- systémový disk: 64 GB na `local-lvm`;
- datový disk: 1 000 GB vedený v PVE na storage `tank-nas-zfs`;
- datový adresář: `/var/nc-data`;
- interní IP: `192.168.89.33`;
- veřejný přístup: `https://cloud.madmike.cz`;
- QEMU Guest Agent: ověřený jako funkční.

Po obnově z PBS byla ověřena produkční data, přihlášení uživatelů i HTTPS. Podrobná provozní dokumentace je v projektu [Nextcloud](../Nextcloud/README.md).

Není zatím ověřené, na jaký současný fyzický pool storage ID `tank-nas-zfs` odkazuje. Starší použití stejného názvu na Dellu nelze automaticky přenášet na Ryzen; vazba se musí potvrdit živými výpisy `pvesm` a `qm config 401`.

### Ryzen / VM501 – produkční Windows a PREMIER

- role: produkční Windows VM pro účetní systém PREMIER;
- prostředky: 4 vCPU, 8 GB RAM;
- typ stroje: `q35`;
- disk: 60 GB na `tank-ssd`;
- interní IP: `192.168.89.34`;
- QEMU Guest Agent: zapnutý a ověřený;
- PREMIER je nainstalovaný a používaný.

Poslední dokumentovaný stav uvádí veřejně publikované RDP přes MikroTik, jehož živé pravidlo je nutné ověřit. Autoritativní popis práce účetní je v projektu [PREMIER](../Premier/README.md) a výběr bezpečnějšího, ale jednoduchého vzdáleného přístupu v projektu [Přístupy](../Pristupy/README.md). Úkol se zde neduplikuje.

### Ryzen / VM510 – Docker infrastruktura

- operační systém: Debian 13.5;
- prostředky: 2 vCPU, 4 GB RAM, 20 GB disk;
- interní IP: `192.168.89.35`;
- Docker a QEMU Guest Agent byly při poslední kontrole funkční.

VM provozuje Nginx Proxy Manager, Pulse, Mikr Manager a Uptime Kuma. Compose cesty, Docker sítě, provozní hranice a otevřené body obnovy jsou v [VM510-Docker.md](VM510-Docker.md). Nastavení samotných monitorovacích aplikací patří do projektu [Monitoring](../Monitoring/README.md).

## Připojení PBS

Offsite PBS je k PVE Ryzen připojené jako storage `pbs-backup` přes WireGuard. Připojení, fingerprint, datastore i reálné zálohování a obnovy byly prakticky použité.

Autoritativní konfigurace jobů, údržby a testů obnovy je v [PBS a disaster recovery](../Zalohy/PBS-DR.md). Stav disků, ZFS a související alarmy jsou provozně sledované v projektu [Monitoring](../Monitoring/README.md); jejich kontrolní úkoly se zde neduplikují.

## Otevřené kroky

- [ ] Ověřit živými výpisy `pvesm` a `qm config 401`, na jaký fyzický ZFS pool odkazuje storage ID `tank-nas-zfs`.
- [ ] Ověřit současné rozdělení a obsazení systémového NVMe.
- [ ] Po návratu z dovolené objednat M4-ATX.
- [ ] Po instalaci M4-ATX zdokumentovat zapojení a prakticky otestovat výpadek i návrat napájení a automatický start serveru.
