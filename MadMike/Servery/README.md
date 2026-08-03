# Servery

> Poslední doložený stav fyzických hostů a VM: **2026-07-28**.  
> Nasazení Uptime Kumy bylo znovu ověřeno **2026-08-03**. Údaje bez novější živé kontroly nejsou vydávány za aktuální měření.

## Účel

Autoritativní přehled fyzických Proxmox serverů, důležitých virtuálních strojů a podpůrné infrastruktury potřebné pro jejich bezpečný provoz a správu.

Dokumentace má správci umožnit:

- určit, kde běží produkce a kde je pouze záloha nebo testovací obnova;
- provést základní kontrolu a plánovanou údržbu hostů;
- rozlišit poruchu hostitele, VM, storage, sítě, reverzní proxy a aplikace;
- bezpečně zahájit obnovu bez spuštění dvou produkčních kopií stejné VM;
- dohledat autoritativní dokument pro zálohy, aplikace, síť a přístupy.

## Provozní architektura

| Prvek | Umístění | Hlavní role | Detail |
|---|---|---|---|
| PVE Ryzen | HOME | Hlavní produkční virtualizace | [PVE-Ryzen.md](PVE-Ryzen.md) |
| PVE Dell | u Richarda | Offsite DR host a provoz PBS ve VM200 | [PVE-Dell.md](PVE-Dell.md) |
| Ryzen / VM510 | PVE Ryzen | Docker host pro NPM a monitoring | [VM510-Docker.md](VM510-Docker.md) |

Základní princip je:

```text
PVE Ryzen = běžná produkce
PVE Dell   = offsite PBS, test obnovy a dočasná DR kapacita
```

Dell není druhý trvale aktivní produkční host. Produkční VM401 a VM501 mají běžet na Ryzenu; kopie na Dellu jsou vypnuté testovací, migrační nebo DR objekty.

## Související serverová infrastruktura

- [Interní DNS, NPM a HTTPS](DNS-NPM-HTTPS.md) – interní názvy, wildcard DNS, Nginx Proxy Manager, upstreamy a certifikát.
- [WireGuard](WireGuard.md) – tunely, serverové trasy a přístup do offsite sítě.
- [Budoucí produkční serverová platforma](Budouci-platforma.md) – schválený nenásilný upgrade PVE Ryzen v rámci AM4.

## Přístup a odpovědnost

- Za oba PVE hosty, VM a změny serverové infrastruktury odpovídá správce MadMike.
- Běžný webový přístup k PVE a PBS vede přes interní HTTPS názvy z LAN nebo po WireGuardu; nouzově zůstává možný přímý přístup přes interní IP a port.
- Konzolový nebo SSH přístup se používá jen z důvěryhodné správcovské cesty.
- Hesla, tokeny, fingerprinty, privátní klíče, recovery klíče a licenční údaje se do repozitáře neukládají. Dokumentovat lze pouze jejich vlastnictví a bezpečné umístění.
- **Vyžaduje ověření v živém systému.** Přesné umístění všech recovery materiálů hostitelů dosud není potvrzené; úkol je vedený v [PBS a disaster recovery](../Zalohy/PBS-DR.md).

## Hranice projektu

- Hardware hostů, jejich storage, napájení, umístění a konfigurace VM patří do projektu **Servery**.
- Docker, Compose soubory, sítě a obnovitelnost služeb na VM510 patří do [VM510-Docker.md](VM510-Docker.md).
- Chování monitorovacích aplikací, monitory a alarmy patří do projektu [Monitoring](../Monitoring/README.md).
- Backup joby, retence, Verify, Prune, Garbage Collection, restore testy a DR patří do projektu [Zálohy](../Zalohy/README.md).
- Provoz Nextcloudu patří do projektu [Nextcloud](../Nextcloud/README.md).
- PREMIER a práce účetní patří do projektu [PREMIER](../Premier/README.md); bezpečný vzdálený přístup do projektu [Přístupy](../Pristupy/README.md).
- Adresní plán, firewall, NAT a MikroTik infrastruktura patří do projektu [Síť](../Sit/README.md).

## Provozní priority

Po úplném výpadku se infrastruktura kontroluje v tomto pořadí:

1. síť, RB5009 a WireGuard;
2. fyzický host a jeho systémové storage;
3. ZFS pooly a dostupnost storage;
4. produkční VM401 Nextcloud a VM501 Windows/PREMIER podle aktuální provozní potřeby;
5. VM510, NPM a monitorovací služby;
6. offsite PBS a poslední použitelné zálohy.

Pořadí není automatický příkaz ke spuštění všech VM. Před startem obnovené nebo DR kopie se vždy vyloučí, že stejná produkční VM už neběží jinde.

## První kontrola při incidentu

1. Určit rozsah: jedna aplikace, jedna VM, celý host, storage, domácí síť nebo propojení do offsite lokality.
2. Neprovádět současně restart hostitele, změnu sítě a zásah do storage; nejprve zachovat důkazy a stav.
3. Ověřit hostitele podle jeho detailního dokumentu.
4. Pokud host a VM fungují, pokračovat v autoritativním dokumentu aplikace.
5. Pokud je ohrožena produkce nebo data, zkontrolovat poslední použitelnou zálohu a postupovat podle [PBS a disaster recovery](../Zalohy/PBS-DR.md).
6. Obnovenou kopii nepřipojit do produkční sítě, dokud nejsou vyřešeny kolize VMID, IP a autoritativní kopie dat.

## Zásady evidence a změn

- VMID se vždy uvádí společně s hostitelem. Stejné VMID může existovat na Ryzenu i Dellu a nemusí mít stejnou roli.
- Produkční VM, migrační testy a testovací obnovy se důsledně rozlišují.
- Vypnutá VM se neoznačuje jako nepotřebná bez ověření jejího původu a účelu.
- Ověřený aktuální stav se odděluje od schváleného plánu a od údajů vyžadujících živou kontrolu.
- Před změnou hostitele se ověří poslední použitelný backup, dopad na závislé služby, návratová cesta a přejímací test.
- Po změně se kontrolují host, storage, VM, aplikace i následující backup; samotný stav `running` není úplná přejímka.

## Handover minimum

Přebírající správce musí před samostatným zásahem umět dohledat:

- fyzické umístění obou hostů a způsob místního zásahu;
- interní IP a běžné HTTPS názvy PVE Ryzen, PVE Dell a PBS;
- rozdělení produkčních, testovacích a DR VM;
- storage layout obou hostů a vazbu PBS datastore;
- způsob přístupu přes WireGuard a nouzový přímý přístup;
- poslední použitelné zálohy a DR runbook;
- umístění přístupových a recovery materiálů mimo GitHub.

Nejasnost v posledním bodě je důvodem zastavit rizikový zásah, nikoli improvizovat s přístupy nebo mazat existující konfiguraci.

Otevřené úkoly jsou vedené pouze v detailních dokumentech a v generovaném kořenovém `TODO.md`.
