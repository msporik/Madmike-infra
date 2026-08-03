# Provoz a úložiště

## Stav dokumentace

Níže uvedená konfigurace je poslední doložený stav z dostupné dokumentace. Při auditu 29. 7. 2026 nebyla porovnána s živou konfigurací VM401.

## Nasazení

Nextcloud je vedený jako produkční **Ryzen / VM401** na PVE Ryzen.

- 2 vCPU;
- 4 GB RAM;
- systémový disk 64 GB na `local-lvm`;
- samostatný datový disk 1 000 GB, historicky ext4, vedený v Proxmoxu na storage ID `tank-nas-zfs`;
- datový adresář `/var/nc-data`.

Storage ID `tank-nas-zfs` je doložené z konfigurace VM, ale zatím není ověřené, na který fyzický ZFS pool na současném hostiteli odkazuje. Nesmí být automaticky zaměněné za `tank-ssd` ani `tank-hdd`. Fyzické mapování storage patří do dokumentace [PVE Ryzen](../Servery/PVE-Ryzen.md).

## Aplikační vrstvy

Při ověřené obnově VM byly funkční:

- Apache;
- MariaDB;
- Nextcloud;
- přístup k uživatelským datům.

Přesné živé verze operačního systému, Nextcloudu, PHP, Apache a MariaDB nejsou ověřené. Stejně tak není ověřené nastavení background jobs a cronu.

## Aktualizace a údržba

Pravidelné aktualizace Nextcloudu ani jeho aplikací se v současnosti neprovádějí. Jde o známé provozní a bezpečnostní riziko.

Před první aktualizací je nutné připravit a ověřit postup, který minimálně zahrne:

1. kontrolu aktuální úspěšné PBS zálohy VM401;
2. zjištění živých verzí a podporované aktualizační cesty;
3. kontrolu kompatibility používaných aplikací;
4. aktualizaci pouze po podporovaných krocích;
5. následnou kontrolu `occ status`, ukončení maintenance mode, přihlášení, práce se soubory, background jobs a aplikačních logů.

Historicky úspěšná obnova sama o sobě nenahrazuje kontrolu aktuální zálohy před konkrétní aktualizací.

## Zálohování a obnova

Autoritativní dokumentace záloh, retence a obnov je v [PBS a disaster recovery](../Zalohy/PBS-DR.md). Je doložená úspěšná testovací obnova produkční VM401 na Dell jako VM402 i pozdější obnova VM401 na PVE Ryzen.

## Otevřené kontroly

Kontrola celé PVE konfigurace VM401 včetně fyzického mapování storage ID `tank-nas-zfs` je vedená v [PVE Ryzen](../Servery/PVE-Ryzen.md).

- [ ] Ověřit živé verze operačního systému, Nextcloudu, PHP, Apache a MariaDB.
- [ ] Ověřit obsazení a volnou kapacitu systémového i datového disku.
- [ ] Ověřit nastavení background jobs a cronu; chybějící doporučený způsob následně doplnit.
- [ ] Připravit, bezpečně otestovat a zapsat aktualizační postup včetně kontrol před aktualizací a po ní.
- [ ] Ověřit, zda Uptime Kuma hlídá webový endpoint a základní aplikační stav Nextcloudu.
