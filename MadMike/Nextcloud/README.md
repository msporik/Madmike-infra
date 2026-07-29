# Nextcloud

## Účel

Produkční soukromý cloud MadMike pro ukládání a synchronizaci souborů. Služba běží jako samostatná virtuální mašina na PVE Ryzen.

## Aktuální provozní obraz

| Položka | Stav |
|---|---|
| Hostitel | PVE Ryzen |
| Virtuální stroj | Ryzen / VM401 |
| Webový přístup | `https://cloud.madmike.cz` |
| Publikace | přímo na VM401 přes Apache, nikoli přes interní NPM |
| Datový adresář | `/var/nc-data` |
| Současné využití | soubory uživatele `madmike` |
| Stav služby | produkční |

Podrobné parametry VM a úložiště jsou posledním doloženým stavem z dostupné dokumentace; při auditu 29. 7. 2026 nebyly ověřeny proti živé VM.

- [Provoz a úložiště](Provoz-a-uloziste.md) – virtuální stroj, disky, datový adresář, aktualizace a provozní kontroly.
- [Přístup a uživatelé](Pristup-a-uzivatele.md) – publikace služby, současní a plánovaní uživatelé a bezpečnostní kontroly.
- [PBS a disaster recovery](../Zalohy/PBS-DR.md) – autoritativní dokumentace záloh a ověřených obnov.
- [PVE Ryzen](../Servery/PVE-Ryzen.md) – fyzický hostitel, storage a ostatní virtuální stroje.

## Skutečné a plánované využití

V současnosti Nextcloud používá pouze `madmike` pro vlastní soubory. Účetní jej nepoužívá a služba není součástí workflow PREMIER.

Schválený další rozvoj:

- opravit přístup Katky;
- později přidat účty pro dvě děti;
- zavést rodinný archiv a zálohování fotografií z telefonů;
- ukládat kopie záloh Home Assistantu a konfigurací MikroTiků.

Tyto body jsou plán, nikoli potvrzený současný provoz.

## Ověřená obnova

Dostupné checkpointy dokládají úspěšnou testovací obnovu produkční VM401 na Dell jako VM402 a pozdější obnovu produkční VM401 na PVE Ryzen. Při testu VM402 fungovaly Apache, MariaDB, Nextcloud i přístup k uživatelským datům. Podrobnosti jsou v dokumentaci [PBS a disaster recovery](../Zalohy/PBS-DR.md).
