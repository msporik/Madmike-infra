# Servery

## Účel

Aktuální přehled fyzických Proxmox serverů, jejich rolí, důležitých virtuálních strojů a infrastruktury potřebné pro přístup k serverovým službám v prostředí MadMike.

## Servery

| Server | Umístění | Hlavní role | Detail |
|---|---|---|---|
| PVE Ryzen | HOME | Produkční virtualizace | [PVE-Ryzen.md](PVE-Ryzen.md) |
| PVE Dell | u Richarda | Offsite DR host a provoz PBS ve VM | [PVE-Dell.md](PVE-Dell.md) |

## Roadmapa

- [Budoucí produkční serverová platforma](Budouci-platforma.md) – podmínky případného upgradu PVE Ryzen, požadovaný charakter nástupce a dosud otevřené volby.

## Přístup k serverovým službám

- [Interní DNS, NPM a HTTPS](DNS-NPM-HTTPS.md) – jmenné přístupy, wildcard DNS, Nginx Proxy Manager, upstreamy a certifikát.
- [WireGuard](WireGuard.md) – aktivní tunely, serverové routy a známé ověřovací úkoly.

Obecný adresní plán a MikroTik infrastruktura patří do projektu [Síť](../Sit/README.md).

## Zásady evidence

- VMID se vždy uvádí společně s hostitelem. Stejné VMID může existovat na Ryzenu i Dellu a nemusí mít stejnou roli.
- Produkční VM, migrační testy a testovací obnovy se důsledně rozlišují.
- Vypnutá VM se neoznačuje jako nepotřebná bez ověření jejího původu a účelu.
- Zálohy a DR jsou zde popsané jen v rozsahu nutném k vysvětlení role serveru; autoritativní dokumentace je v projektu [Zálohy](../Zalohy/README.md).
- Interní IP adresy a směrování mohou být evidované, ale hesla, tokeny a klíče se do dokumentace neukládají.

## Otevřené kontroly

1. Ověřit, na jaký fyzický ZFS pool na PVE Ryzen odkazuje storage ID `tank-nas-zfs`.
2. Zjistit původ a účel vypnuté Dell / VM400.
3. Ověřit živou konfiguraci veřejného RDP k produkční Ryzen / VM501 a navrhnout bezpečnější přístup, který zůstane pro účetní co nejjednodušší.
4. Zjistit, zda účetní používá vždy jeden stejný počítač s Windows.
5. Dokončit živou inventuru WireGuard peerů a současných LAN rozsahů všech vzdálených lokalit.
