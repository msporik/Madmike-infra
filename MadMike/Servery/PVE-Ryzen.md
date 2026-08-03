# PVE Ryzen

> Poslední doložený technický stav: **2026-07-28**. Při tomto zpracování nebyl host znovu porovnán s živým systémem.

## Role

Hlavní produkční Proxmox VE server v domácí lokalitě. Provozuje zejména produkční Nextcloud, účetní Windows VM s PREMIERem a infrastrukturní Docker VM.

- hostname: `pve`;
- interní IP: `192.168.89.32`;
- běžný HTTPS přístup: `https://pveryzen.mikehub.cz`;
- současná platforma: AMD AM4, základní deska A520 a Ryzen 3 4300G.

Současný hardware provozované role zvládá. Schválený nenásilný upgrade je v dokumentu [Budoucí produkční serverová platforma](Budouci-platforma.md).

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

Toto rozdělení a jeho současné obsazení vyžadují živé ověření.

## Napájení

Domácí rack používá DC systém Mean Well DRS-240-12 s baterií. Současný typ napájení Ryzenu a úplný výpadkový cyklus nebyly při konsolidaci živě ověřené.

Schválený cílový zdroj je Mini-Box M4-ATX 6–30 V / 250 W, standardní varianta, nikoliv M4-ATX-HV. Má:

- nahradit současné napájení serveru;
- přijímat signál AC OK/AC FAIL z DRS přes vstup IGNITION;
- po nastavené prodlevě vyvolat korektní ACPI shutdown přes POWER SW;
- po další bezpečnostní prodlevě případně provést hard-off;
- po návratu sítě umožnit automatický start serveru.

Kritická vypínací cesta nemá záviset na Home Assistantu, síti ani běžící VM. USB M4-ATX má sloužit pro konfiguraci prodlev a napěťových mezí, případně monitoring, nikoliv jako jediná vypínací logika.

Do instalace a praktického testu jde o plán, nikoliv současný stav.

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
- doložená struktura: `Video`, `Synology`, `Rodina`, `Dokumenty`, `Historicke-zalohy`.

Původní WD RAID byl před zrušením sestaven pouze pro čtení, zkontrolován a teprve poté odstraněn. Přibližně 123 GB původních video dat bylo zachováno v archivu.

## Důležité virtuální stroje

| Objekt | Role | Poslední doložená konfigurace |
|---|---|---|
| Ryzen / VM401 | produkční Nextcloud | 2 vCPU, 4 GB RAM, 64GB systémový disk, 1TB datový disk, IP `192.168.89.33` |
| Ryzen / VM501 | produkční Windows a PREMIER | 4 vCPU, 8 GB RAM, `q35`, 60GB disk na `tank-ssd`, IP `192.168.89.34` |
| Ryzen / VM510 | NPM a monitoring | Debian 13.5, 2 vCPU, 4 GB RAM, 20GB disk, IP `192.168.89.35` |

### Ryzen / VM401 – produkční Nextcloud

- systémový disk: 64 GB na `local-lvm`;
- datový disk: 1 000 GB vedený v PVE na storage `tank-nas-zfs`;
- datový adresář: `/var/nc-data`;
- veřejný přístup: `https://cloud.madmike.cz`;
- QEMU Guest Agent: ověřený jako funkční.

Po obnově z PBS byla ověřena produkční data, přihlášení uživatelů i HTTPS. Podrobný provozní runbook je v projektu [Nextcloud](../Nextcloud/README.md).

**Vyžaduje ověření v živém systému:** na jaký současný fyzický pool storage ID `tank-nas-zfs` odkazuje. Starší použití stejného názvu na Dellu nelze přenášet na Ryzen.

### Ryzen / VM501 – produkční Windows a PREMIER

- disk: 60 GB na `tank-ssd`;
- QEMU Guest Agent: zapnutý a ověřený;
- PREMIER je nainstalovaný a používaný.

VM501 byla úspěšně obnovena z PBS zpět na Ryzen a po obnově proběhl další úspěšný inkrementální backup. Aplikační provoz, práce účetní a přejímka jsou v projektu [PREMIER](../Premier/README.md). Cílový bezpečný vzdálený přístup je v projektu [Přístupy](../Pristupy/README.md).

### Ryzen / VM510 – Docker infrastruktura

VM provozuje Nginx Proxy Manager, Pulse, Mikr Manager a Uptime Kuma. Nasazení, persistence, sítě, provoz a pořadí obnovy jsou v [VM510-Docker.md](VM510-Docker.md). Nastavení monitorovacích aplikací patří do projektu [Monitoring](../Monitoring/README.md).

## Připojení PBS

Offsite PBS je k PVE Ryzen připojené jako storage `pbs-backup` přes WireGuard. Připojení, fingerprint, datastore i reálné zálohování a obnovy byly prakticky použité.

Autoritativní konfigurace jobů, retence, údržby a testů obnovy je v [PBS a disaster recovery](../Zalohy/PBS-DR.md). Citlivé údaje připojení se do tohoto dokumentu neduplikují.

## Bezpečná základní kontrola

Bez změny konfigurace:

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

Konfigurace důležitých VM:

```bash
qm config 401
qm config 501
qm config 510
```

Očekávaný zdravý stav:

- `tank-ssd` a `tank-hdd` jsou `ONLINE` bez nových read/write/checksum chyb;
- všechny očekávané storage jsou dostupné;
- běží pouze zamýšlené produkční VM;
- Guest Agent odpovídá u VM401, VM501 a VM510;
- nejsou zaplněné systémové filesystémy ani storage;
- PVE je dostupný přes interní IP i `pveryzen.mikehub.cz`.

Výpisy se před sdílením kontrolují; mohou obsahovat interní adresy, identifikátory a další neveřejné údaje.

## Běžný restart hostitele

1. Domluvit odstávku dotčených aplikací a ověřit, že neprobíhá backup, restore, scrub ani jiná dlouhá storage úloha.
2. Ověřit poslední úspěšné PBS backupy VM401, VM501 a VM510.
3. Korektně ukončit aplikace a VM; vynucené zastavení použít pouze při incidentu.
4. Restartovat hostitele standardně.
5. Po startu nejprve ověřit síť, `pvesm status`, `zpool status -x` a systémové chyby.
6. VM spouštět podle provozní potřeby, ne bezmyšlenkovitě všechny najednou.
7. U každé VM provést aplikační kontrolu v jejím autoritativním projektu.
8. Ověřit NPM, interní HTTPS a Pulse.

## Plánovaná aktualizace PVE

1. Ověřit podporovanou verzi a správné repozitáře pro současnou instalaci.
2. Zkontrolovat stav ZFS, storage, volné místo a systémové chyby.
3. Ověřit poslední použitelné offsite backupy a dostupnost PVE Dell/PBS.
4. Zaznamenat výchozí verzi a seznam čekajících balíčků:

```bash
apt update
apt list --upgradable
```

5. Předem určit, zda aktualizace vyžaduje restart, dobu odstávky a rollback.
6. Aktualizovat pouze ze správně nakonfigurovaných Proxmox/Debian repozitářů. Přechod hlavní verze se neprovádí jako běžný balíčkový update a vyžaduje samostatný oficiální postup.
7. Po aktualizaci zopakovat základní kontrolu, ověřit VM a aplikace a zkontrolovat následující backup.

Oficiální provozní reference: [Proxmox VE – Host System Administration](https://pve.proxmox.com/pve-docs/chapter-sysadmin.html).

## Diagnostika

| Projev | První kontrola | Bezpečný další krok |
|---|---|---|
| PVE web není dostupný | ping/IP, SSH, `pveproxy`, disk a síť | oddělit problém hostitele od NPM; zkusit přímou interní IP |
| HTTPS jméno nefunguje, IP ano | DNS a NPM | pokračovat v [DNS, NPM a HTTPS](DNS-NPM-HTTPS.md) |
| Jedna VM neběží | `qm status VMID`, `qm config VMID`, Tasks | neobnovovat ani nevytvářet druhou VM před určením příčiny |
| Storage není dostupné | `pvesm status`, `zpool status -v`, mounty | nic neinicializovat, neimportovat pool naslepo a nezapisovat do neověřeného cíle |
| ZFS je `DEGRADED` nebo má chyby | `zpool status -v`, fyzické disky a SMART | zachovat výstupy, omezit změny a naplánovat opravu s použitelným backupem |
| Dochází místo | `df -hT`, `pvesm status`, `zfs list` | určit skutečný filesystem/dataset; nemažte náhodné volumes ani backupy |
| VM běží, aplikace ne | Guest Agent, konzole a projekt aplikace | hostitelský restart není první volba |
| PBS storage je nedostupné | WireGuard, PVE Dell, VM200 a datastore | pokračovat v projektu Zálohy; lokální VM mohou běžet, ale nejsou řádně chráněné |

## Obnova po ztrátě hostitele

Autoritativní DR pořadník je v [PBS a disaster recovery](../Zalohy/PBS-DR.md). Na úrovni hostitele platí:

1. Původní disky zachovat beze změny, dokud není známý rozsah poruchy.
2. Ověřit Dell, VM200, datastore `backup`, WireGuard a poslední snapshoty.
3. Rozhodnout mezi opravou původního hostitele, náhradní A520 + 4300G a dočasným provozem na Dellu.
4. Před obnovou vyřešit VMID, storage mapování, IP a zákaz souběhu původní a obnovené produkční kopie.
5. Po obnově provést aplikační přejímku a teprve potom přesměrovat provoz.

## Otevřené kontroly

**Vyžaduje ověření v živém systému.**

- [ ] Ověřit aktuální PVE konfiguraci VM401 živými výpisy `pvesm` a `qm config 401`, včetně prostředků, disků a fyzického ZFS poolu za storage ID `tank-nas-zfs`.
- [ ] Ověřit současné rozdělení a obsazení systémového NVMe.
- [ ] Ověřit přesný model základní desky A520, současný zdroj a zapojení napájení před instalací M4-ATX.
- [ ] Po návratu z dovolené objednat standardní Mini-Box M4-ATX 6–30 V / 250 W a potřebné kabely.
- [ ] Před instalací M4-ATX ověřit práh baterie DRS a připravit zapojení AC OK/AC FAIL → IGNITION → POWER SW.
- [ ] Po instalaci nastavit prodlevy a prakticky otestovat celý cyklus výpadek → korektní shutdown → bezpečný hard-off → návrat sítě → automatický start.
