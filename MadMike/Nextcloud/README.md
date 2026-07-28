# Nextcloud

## Účel

Produkční soukromý cloud MadMike pro ukládání a sdílení dat. Služba běží jako samostatná virtuální mašina na PVE Ryzen.

## Aktuální stav

| Položka | Hodnota |
|---|---|
| Hostitel | PVE Ryzen |
| Virtuální stroj | Ryzen / VM401 |
| Prostředky | 2 vCPU, 4 GB RAM |
| Webový přístup | `https://cloud.madmike.cz` |
| Datový adresář | `/var/nc-data` |
| Stav | produkční služba |

- [Provoz a úložiště](Provoz-a-uloziste.md) – virtuální stroj, disky, datový adresář a provozní kontroly.
- [Přístup a uživatelé](Pristup-a-uzivatele.md) – vstupní adresa, potvrzené účty a bezpečnostní kontroly.
- [PBS a disaster recovery](../Zalohy/PBS-DR.md) – autoritativní dokumentace záloh a ověřené obnovy.

Fyzický hostitel a ostatní virtuální stroje jsou popsané v [PVE Ryzen](../Servery/PVE-Ryzen.md).

## Ověřená obnova

Produkční VM401 byla úspěšně obnovena z PBS jako testovací Dell / VM402. Po spuštění fungovaly Apache, MariaDB, Nextcloud i přístup k datům. Podrobnosti a rozlišení dalších migračních VM jsou v dokumentaci [PBS a disaster recovery](../Zalohy/PBS-DR.md).

## Otevřené kontroly

1. Ověřit živou verzi Nextcloudu, operačního systému a databáze.
2. Ověřit vazbu storage ID `tank-nas-zfs` na fyzický ZFS pool.
3. Zapsat používaný postup aktualizace Nextcloudu a jeho aplikací.
4. Ověřit současné nastavení administrátorských rolí, MFA a veřejného sdílení.
