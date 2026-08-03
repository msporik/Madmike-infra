# Nextcloud

## Účel

Produkční soukromý cloud MadMike pro ukládání a synchronizaci souborů. Služba běží jako samostatná virtuální mašina na PVE Ryzen.

## Aktuální provozní obraz

| Položka | Stav |
|---|---|
| Hostitel | PVE Ryzen |
| Virtuální stroj | Ryzen / VM401 |
| Interní IP | `192.168.89.33` |
| Webový přístup | `https://cloud.madmike.cz` |
| Publikace | přímo na VM401 přes Apache, nikoli přes interní NPM |
| Datový adresář | `/var/nc-data` |
| Současné využití | soubory uživatele `madmike` |
| Stav služby | produkční |

Podrobné parametry VM a úložiště jsou posledním doloženým stavem z dostupné dokumentace; při auditu 29. 7. 2026 nebyly ověřeny proti živé VM.

## Základní provozní závislosti

Pro správnou funkci služby jsou potřeba:

1. běžící PVE Ryzen a VM401;
2. dostupný systémový i datový disk a připojený datový adresář `/var/nc-data`;
3. funkční Apache, PHP, MariaDB a Nextcloud;
4. interní síť VM401;
5. veřejné DNS, směrování a HTTPS pro `cloud.madmike.cz`;
6. použitelná záloha VM401 na offsite PBS pro obnovu po havárii.

Ztráta veřejného přístupu nemusí znamenat ztrátu aplikace nebo dat. Při diagnostice se proto odděluje stav VM, aplikace, interního přístupu a veřejné publikační cesty.

## Rozhodnutí platná pro současné nasazení

- Produkční službou je VM401 na PVE Ryzen.
- Nextcloud je publikovaný přímo přes Apache na VM401. Interní Nginx Proxy Manager se na jeho veřejné cestě nepoužívá.
- Pro případ budoucí zásadní přestavby je doložené rozhodnutí vytvořit čistou instalaci a migrovat pouze uživatelská data, nikoli bez kontroly přenést starou aplikační instalaci. Nejde o náhradu běžné obnovy celé VM401 z PBS ani o tvrzení, že už byla tato přestavba provedena.
- Zálohování a disaster recovery se popisují autoritativně v projektu [Zálohy](../Zalohy/PBS-DR.md), nikoli duplicitně zde.
- Fyzické mapování Proxmox storage se popisuje autoritativně v projektu [Servery](../Servery/PVE-Ryzen.md).

## Skutečné a plánované využití

V současnosti Nextcloud používá pouze `madmike` pro vlastní soubory. Účetní jej nepoužívá a služba není součástí workflow PREMIER.

Schválený další rozvoj:

- opravit přístup Katky;
- později přidat účty pro dvě děti;
- zavést rodinný archiv a zálohování fotografií z telefonů;
- ukládat kopie záloh Home Assistantu a konfigurací MikroTiků.

Tyto body jsou plán, nikoli potvrzený současný provoz. Autoritativní popis zálohovacího řetězce Home Assistantu a MikroTiků zůstává v projektu [Zálohy](../Zalohy/README.md).

## Ověřená obnova

Dostupné checkpointy dokládají:

- úspěšnou testovací obnovu produkční VM401 na Dell jako VM402;
- funkční Apache, MariaDB, Nextcloud a přístup k uživatelským datům v obnovené VM402;
- pozdější úspěšnou obnovu produkční VM401 na nově nainstalovaný PVE Ryzen;
- funkční `cloud.madmike.cz`, přihlášení a uživatelská data po této obnově.

Podrobnosti, klasifikace jednotlivých migrací a aktuální DR postup jsou v dokumentaci [PBS a disaster recovery](../Zalohy/PBS-DR.md).

## Mapa dokumentace pro převzetí

- [Provoz a úložiště](Provoz-a-uloziste.md) – VM401, aplikační vrstvy, provozní kontroly, aktualizace, diagnostika a přejímka po obnově.
- [Přístup a uživatelé](Pristup-a-uzivatele.md) – veřejná publikace, HTTPS, účty, MFA, aplikační hesla, klienti a sdílení.
- [PVE Ryzen](../Servery/PVE-Ryzen.md) – fyzický hostitel, Proxmox storage a parametry VM.
- [PBS a disaster recovery](../Zalohy/PBS-DR.md) – zálohovací joby, retence, obnovy a DR postup.
- [Uptime Kuma](../Monitoring/Uptime-Kuma.md) – monitoring dostupnosti Nextcloudu.
- [Přístupy](../Pristupy/README.md) – společné zásady přihlašovacích údajů a veřejných výjimek.

## Handover: první orientace správce

Při převzetí služby:

1. ověřit stav PVE Ryzen a VM401;
2. ověřit dostupnost `https://cloud.madmike.cz` bez provádění změn;
3. uvnitř VM ověřit připojení `/var/nc-data`, stav služeb a `occ status` podle [Provozu a úložiště](Provoz-a-uloziste.md);
4. ověřit poslední úspěšnou zálohu VM401 v PBS podle autoritativního dokumentu;
5. projít otevřené kontroly v obou provozních dokumentech;
6. nezapisovat do repozitáře hesla, tokeny, recovery kódy, aplikační hesla ani soukromá data.

Dokud nejsou živě ověřené verze, mounty, účty a veřejná publikační cesta, považují se údaje označené v podřízených dokumentech za poslední doložený stav, nikoli za automaticky potvrzenou současnost.
