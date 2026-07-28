# Servery

## Účel

Aktuální přehled fyzických Proxmox serverů, jejich rolí a důležitých virtuálních strojů v infrastruktuře MadMike.

## Servery

| Server | Umístění | Hlavní role | Detail |
|---|---|---|---|
| PVE Ryzen | HOME | Produkční virtualizace | [PVE-Ryzen.md](PVE-Ryzen.md) |
| PVE Dell | u Richarda | Offsite DR host a provoz PBS ve VM | [PVE-Dell.md](PVE-Dell.md) |

## Zásady evidence

- VMID se vždy uvádí společně s hostitelem. Stejné VMID může existovat na Ryzenu i Dellu a nemusí mít stejnou roli.
- Produkční VM, migrační testy a testovací obnovy se důsledně rozlišují.
- Vypnutá VM se neoznačuje jako nepotřebná bez ověření jejího původu a účelu.
- Zálohy a DR jsou zde popsané jen v rozsahu nutném k vysvětlení role serveru; detailní politika záloh bude samostatný projekt až při její konsolidaci.

## Otevřené kontroly

1. Ověřit, na jaký fyzický ZFS pool na PVE Ryzen odkazuje storage ID `tank-nas-zfs`.
2. Zjistit původ a účel vypnuté Dell / VM400.
3. Ověřit živou konfiguraci veřejného RDP k produkční Ryzen / VM501 a navrhnout bezpečnější přístup, který zůstane pro účetní co nejjednodušší.
4. Zjistit, zda účetní používá vždy jeden stejný počítač s Windows.
