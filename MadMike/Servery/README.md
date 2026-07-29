# Servery

## Účel

Aktuální přehled fyzických Proxmox serverů, důležitých virtuálních strojů a podpůrné infrastruktury potřebné pro bezpečný přístup k serverovým službám MadMike.

## Provozní architektura

| Prvek | Umístění | Hlavní role | Detail |
|---|---|---|---|
| PVE Ryzen | HOME | Produkční virtualizace | [PVE-Ryzen.md](PVE-Ryzen.md) |
| PVE Dell | u Richarda | Offsite DR host a provoz PBS ve VM | [PVE-Dell.md](PVE-Dell.md) |
| Ryzen / VM510 | PVE Ryzen | Docker host pro NPM a monitoring | [VM510-Docker.md](VM510-Docker.md) |

## Související serverová infrastruktura

- [Interní DNS, NPM a HTTPS](DNS-NPM-HTTPS.md) – jmenné přístupy, wildcard DNS, Nginx Proxy Manager, upstreamy a certifikát.
- [WireGuard](WireGuard.md) – současná evidence tunelů, serverových tras i dalších lokalit; rozsah dokumentu zatím zůstává beze změny.
- [Budoucí produkční serverová platforma](Budouci-platforma.md) – schválený směr nenásilného upgradu PVE Ryzen v rámci AM4.

## Hranice projektu

- Hardware hostů, jejich storage a umístění VM patří do projektu **Servery**.
- Nasazení Dockeru, Compose soubory, sítě a obnova služeb na VM510 patří do [VM510-Docker.md](VM510-Docker.md).
- Chování monitorovacích aplikací a jejich alarmy patří do projektu [Monitoring](../Monitoring/README.md).
- Rozvrhy záloh, retence, Verify, Prune, Garbage Collection, testy obnovy a DR patří do projektu [Zálohy](../Zalohy/README.md).
- Provoz Nextcloudu patří do projektu [Nextcloud](../Nextcloud/README.md).
- PREMIER a práce účetní patří do projektu [PREMIER](../Premier/README.md); způsob vzdáleného přístupu do projektu [Přístupy](../Pristupy/README.md).
- Obecný adresní plán a MikroTik infrastruktura patří do projektu [Síť](../Sit/README.md).

## Zásady evidence

- VMID se vždy uvádí společně s hostitelem. Stejné VMID může existovat na Ryzenu i Dellu a nemusí mít stejnou roli.
- Produkční VM, migrační testy a testovací obnovy se důsledně rozlišují.
- Vypnutá VM se neoznačuje jako nepotřebná bez ověření jejího původu a účelu.
- Ověřený aktuální stav se odděluje od schváleného budoucího plánu a od údajů, které je ještě nutné potvrdit.
- Interní IP adresy a směrování mohou být evidované, ale hesla, tokeny a klíče se do dokumentace neukládají.

Otevřené úkoly jsou vedené pouze v příslušných detailních dokumentech. Tento přehled je záměrně neduplikuje.
