# Provoz a úložiště

## Nasazení

Nextcloud běží jako produkční **Ryzen / VM401** na PVE Ryzen.

- 2 vCPU;
- 4 GB RAM;
- systémový disk 64 GB na `local-lvm`;
- datový disk 1 000 GB vedený v Proxmoxu na storage `tank-nas-zfs`;
- datový adresář `/var/nc-data`.

Storage ID `tank-nas-zfs` je doložené z konfigurace VM, ale zatím není ověřené, na který fyzický ZFS pool skutečně odkazuje. Nesmí být automaticky zaměněné za `tank-ssd` ani `tank-hdd`.

## Aplikační vrstvy

Při ověřené obnově VM byly funkční:

- Apache;
- MariaDB;
- Nextcloud;
- přístup k uživatelským datům.

Přesné verze operačního systému, Nextcloudu, PHP, Apache a MariaDB zatím nejsou v živé dokumentaci ověřené.

## Zálohování a obnova

Autoritativní dokumentace je v [PBS a disaster recovery](../Zalohy/PBS-DR.md). Je potvrzená úspěšná obnova produkční VM401 na Dell jako testovací VM402.

Aktuální rozvrh, retence a pravidelnost budoucích testů obnovy se doplní až po kontrole živé konfigurace PBS.

## Provozní kontroly

- [ ] Ověřit aktuální PVE konfiguraci VM401 proti živému stavu.
- [ ] Ověřit obsazení systémového a datového disku.
- [ ] Ověřit fyzický pool za storage ID `tank-nas-zfs`.
- [ ] Zapsat postup aktualizace a kontroly po aktualizaci.
- [ ] Ověřit, zda monitoring hlídá dostupnost webu a základní stav služby.
