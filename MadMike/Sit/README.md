# Síť

## Účel

Projekt popisuje společné síťové principy MadMike:

- současné známé a budoucí IP rozsahy;
- domácí síťovou infrastrukturu;
- obecnější rozhodnutí platná pro MikroTik.

Podrobná topologie a zařízení ostatních lokalit patří do jejich vlastních kapitol. Tento projekt z nich nevytváří druhou centrální inventuru.

## Dokumenty

- [Adresní plán](Adresni-plan.md) – současné, historické nebo neověřené rozsahy a dlouhodobý návrh sjednocení.
- [MikroTik](MikroTik.md) – domácí síťová infrastruktura a obecné zásady pro MikroTik.

## Hranice vůči ostatním projektům

- Interní DNS, Nginx Proxy Manager, HTTPS a provozní dokumentace WireGuardu zůstávají v projektu [Servery](../Servery/README.md).
- Mikr Manager, jeho grafy a alerty zůstávají v projektu [Monitoring](../Monitoring/Mikr.md).
- Exporty konfigurací a postup obnovy RouterOS zůstávají v projektu [Zálohy](../Zalohy/MikroTik.md).
- Topologie, zařízení a lokální rozhodnutí jiné lokality se zapisují do kapitoly dané lokality.
- Detailní kusová evidence hardwaru a skladových zásob zůstává v Airtable. Postupně může zahrnout nejen MikroTik, ale také miniPC, disky, paměti a komponenty Home Assistantu.

## Autorita a stavy údajů

GitHub je autoritativní publikovaná dokumentace. Skutečný provozní stav se při změně nebo pochybnosti ověřuje v živé konfiguraci zařízení.

Při konsolidaci historických podkladů platí:

1. novější schválené rozhodnutí nebo checkpoint v Library;
2. není-li, schválený závěr v Airtable / Brainstorming;
3. starší pracovní exporty a poznámky pouze jako historický podklad.

Detailní HW evidence v Airtable není zdrojem aktivní topologie. Mikr je zdrojem dostupnosti a monitoringu, ne autoritativním inventářem sítě.

Dokumenty rozlišují:

- **aktivní / potvrzené** – doložený současný provoz;
- **naposledy evidované** – poslední známý stav bez nového živého ověření;
- **plánované** – schválený budoucí stav, který ještě nemusí být nasazený;
- **historické / neověřené** – stopa vyžadující ověření nebo rozhodnutí.

## Zásady

- Současný stav a budoucí plán se nesmí směšovat.
- Nová IP adresa se neoznačí jako přidělená, dokud není ověřena v živé konfiguraci nebo výslovně schválena jako rezervace.
- Přesné interní IP adresy a směrování mohou být v tomto soukromém repozitáři evidované.
- Hesla, tokeny, privátní klíče, preshared keys, sériová čísla a jiné tajné nebo zbytečně citlivé údaje do repozitáře nepatří.
