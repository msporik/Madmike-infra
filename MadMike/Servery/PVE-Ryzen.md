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

## Důležité virtuální stroje

### Ryzen / VM401 – produkční Nextcloud

- role: produkční Nextcloud;
- prostředky: 2 vCPU, 4 GB RAM;
- systémový disk: 64 GB na `local-lvm`;
- datový disk: 1 000 GB vedený v Proxmoxu na storage `tank-nas-zfs`;
- datový adresář: `/var/nc-data`;
- veřejný přístup: `https://cloud.madmike.cz`.

Podrobná provozní dokumentace služby je v projektu [Nextcloud](../Nextcloud/README.md).

Není zatím ověřené, zda je `tank-nas-zfs` starší storage ID odkazující na fyzický pool `tank-ssd`, nebo jiné úložiště. Tento údaj se nesmí doplnit odhadem.

### Ryzen / VM501 – produkční Windows a PREMIER

- role: produkční Windows VM pro účetní systém PREMIER;
- prostředky: 4 vCPU, 8 GB RAM;
- typ stroje: `q35`;
- disk: 60 GB na `tank-ssd`;
- PREMIER je nainstalovaný a používaný.

RDP je aktuálně publikované do internetu přes MikroTik. Přesné současné pravidlo je potřeba ověřit. Cílové řešení má odstranit přímé veřejné RDP, ale zachovat co nejjednodušší přístup pro externí účetní.

Podrobná provozní dokumentace služby je v projektu [PREMIER](../Premier/README.md).

### Ryzen / VM510 – Monitoring

Monitorovací VM provozuje zejména:

- Nginx Proxy Manager;
- Pulse;
- Mikr Manager;
- Uptime Kuma.

Podrobnosti jsou v projektu [Monitoring](../Monitoring/README.md).

## Otevřené kontroly

- [ ] Ověřit vazbu storage ID `tank-nas-zfs` na fyzický ZFS pool.
- [ ] Ověřit aktuální PVE konfiguraci VM401, VM501 a VM510 proti živému stavu.
- [ ] Ověřit pravidla dst-nat a firewallu pro RDP k VM501.
