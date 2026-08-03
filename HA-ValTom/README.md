# HA ValTom

Samostatná kapitola dokumentace Home Assistantu připravovaného pro Tomáše Valentu. Krátký a jednotný název lokality v repozitáři je **HA ValTom**.

## Projekty

- [Home Assistant](Home-Assistant/README.md) – připravený HA Green, budoucí nasazení u Tomáše, vzdálený přístup a plán energetiky.

## Aktuální stav kapitoly

| Oblast | Doložený stav k 2026-08-03 |
|---|---|
| Hardware | Home Assistant Green je vypnutý a uložený u správce; u Tomáše ještě není nasazený. |
| Home Assistant | V květnu 2026 vznikla čistá instalace a jeden tehdejší full backup / master image. Současné verze a stav komponent nejsou na vypnutém zařízení ověřené. |
| Vzdálený přístup | Cloudflare Tunnel na `valtom.mikehub.cz` před vypnutím fungoval. Chyba `1033` při vypnutém Green není důkaz poruchy tunelu. |
| GoodWe a dashboard | Nerealizováno; chybí ověřený model, komunikace, entity i produkční dashboard. |
| Bojler | Pouze budoucí záměr; elektrické zapojení a bezpečnostní podmínky nejsou zmapované. |

## První orientace správce

1. Začít v [Home Assistant / README](Home-Assistant/README.md) a ověřit, zda se od posledního doloženého stavu změnilo fyzické umístění nebo provoz Green.
2. Před zapnutím nebo přesunem projít [nasazení a vzdálený přístup](Home-Assistant/Nasazeni-a-pristup.md).
3. GoodWe a bojler řešit výhradně podle [GoodWe a energetika](Home-Assistant/GoodWe-a-energie.md), nejprve pouze čtením a ověřením dat.
4. Přihlašovací údaje a tokeny hledat v určeném bezpečném úložišti, nikoli v GitHubu.
5. Výsledek každého praktického ověření zapsat do autoritativního dokumentu; kořenový `TODO.md` se upravuje automaticky.

## Hranice kapitoly

- Tato kapitola popisuje výhradně Home Assistant určený pro Tomáše Valentu.
- Údaje z domácího HA MadMike, Vernířovic nebo Honzy se sem nepřebírají.
- Společná strategie záloh Home Assistantu zůstává v [MadMike / Zálohy / Home Assistant](../MadMike/Zalohy/Home-Assistant.md).
- Centrální DNS a přístupová infrastruktura zůstávají v [MadMike / Servery / DNS, NPM a HTTPS](../MadMike/Servery/DNS-NPM-HTTPS.md).
- Společné zásady účtů, MFA, recovery a ukládání tajných hodnot zůstávají v [MadMike / Přístupy](../MadMike/Pristupy/README.md).
- Samostatný projekt sítě vznikne až tehdy, když bude místní síť skutečně řešená a zdokumentovaná.

Nový projekt se přidá až ve chvíli, kdy pro něj vznikne skutečný a samostatně udržovaný obsah.
