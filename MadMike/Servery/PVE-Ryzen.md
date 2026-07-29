# PVE Ryzen

## Role

Hlavní produkční Proxmox VE server v domácí lokalitě. Provozuje zejména produkční Nextcloud, účetní Windows VM s PREMIERem a monitorovací VM.

Současná platforma zatím pro tyto role dostačuje. Podmínky případného budoucího upgradu jsou v dokumentu [Budoucí produkční serverová platforma](Budouci-platforma.md).

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

Není zatím ověřené, zda `tank-nas-zfs` je starší storage ID odkazující na fyzický pool `tank-ssd`, nebo jiné úložiště. Tento údaj se nesmí doplnit odhadem.

### Ryzen / VM501 – produkční Windows a PREMIER

- role: produkční Windows VM pro účetní systém PREMIER;
- prostředky: 4 vCPU, 8 GB RAM;
- typ stroje: `q35`;
- disk: 60 GB na `tank-ssd`;
- interní IP: `192.168.89.34`;
- QEMU Guest Agent: zapnutý a ověřený;
- PREMIER je nainstalovaný a používaný.

RDP je aktuálně publikované do internetu přes MikroTik. Přesné současné pravidlo je potřeba ověřit. Cílové řešení má odstranit přímé veřejné RDP, ale zachovat co nejjednodušší přístup pro externí účetní.

Podrobná provozní dokumentace je v projektu [PREMIER](../Premier/README.md).

### Ryzen / VM510 – Monitoring

- operační systém: Debian 13.5;
- prostředky: 2 vCPU, 4 GB RAM, 20GB disk;
- interní IP: `192.168.89.35`;
- Docker: funkční;
- QEMU Guest Agent: nainstalovaný a ověřený.

VM provozuje zejména:

- Nginx Proxy Manager;
- Pulse;
- Mikr Manager;
- Uptime Kuma.

Podrobnosti jsou v projektu [Monitoring](../Monitoring/README.md).

## Připojení PBS

Offsite PBS je k PVE Ryzen připojené jako storage `pbs-backup` přes WireGuard. Připojení, fingerprint, datastore i reálné zálohování a obnovy byly prakticky použité.

Autoritativní konfigurace jobů a testů obnovy je v [PBS a disaster recovery](../Zalohy/PBS-DR.md).

## Otevřené kontroly

- [ ] Ověřit vazbu storage ID `tank-nas-zfs` na fyzický ZFS pool.
- [ ] Ověřit aktuální PVE konfiguraci VM401, VM501 a VM510 proti živému stavu.
- [ ] Ověřit současné rozdělení a obsazení systémového NVMe.
- [ ] Ověřit aktuální stav, poslední scrub a SMART poolů `tank-ssd` a `tank-hdd`.
- [ ] Ověřit pravidla dst-nat a firewallu pro RDP k VM501.
