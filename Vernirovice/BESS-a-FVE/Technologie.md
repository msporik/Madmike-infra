# Technologie FVE, BESS a tepelné infrastruktury

## Potvrzené komponenty FVE a BESS

| Systém | Aktuálně známý údaj | Stav údaje |
|---|---|---|
| původní měnič | Deye 50 kW | potvrzeno |
| původní baterie | přibližně 50 kWh | orientačně potvrzeno |
| nová baterie | 215 kWh | kapacita potvrzena |
| nový měnič | Deye; přesný model a výkon neověřen | ověřit |
| hlavní jištění | 3×80 A | evidovaný současný stav |
| limit exportu | 50 kW | potvrzený současný stav |

Starší podklady uvádějí pro nový měnič rozdílné hodnoty a označení. Dokud nebude přečtený štítek nebo ověřená dokumentace, nesmí se žádná varianta vydávat za aktuální skutečnost.

Poslední souhrnný checkpoint uváděl instalovaný výkon panelů 45 kWp. Protože se lokalita mezitím rozšiřovala, údaj se zachovává jako historicky doložený a musí se ověřit proti dnešnímu zapojení.

## Tepelná infrastruktura hlavního objektu

Poslední souhrnný checkpoint eviduje:

- akumulační nádobu 1 000 l;
- automatický peletový kotel Atmos jako záložní zdroj tepla;
- 6kW elektrické topné tyče v akumulační nádobě;
- tepelné čerpadlo Hitachi;
- radiátory s termostatickými hlavicemi Honeywell;
- elektrický bojler 2 kW;
- předehřev teplé vody z akumulační nádoby.

Klíčová data byla dostupná v Home Assistantu a historicky ukládaná do InfluxDB. Skutečnou hydraulickou a elektrickou topologii je potřeba při další inventuře zakreslit.

## Wellness zóna

Součástí lokality je venkovní wellness zóna:

### Sauna

- 9kW přímotopné topení;
- vlastní ovládání mimo Home Assistant.

### Koupací sud

- 9kW elektrický ohřev;
- spínání přes Shelly integrované do Home Assistantu;
- doplňkový ohřev dřevem.

### Bazén

- vytápění tepelným čerpadlem;
- vlastní řídicí logika;
- nucené vypnutí přes chytrou zásuvku integrovanou do Home Assistantu;
- filtrace.

## Měřené elektrické větve

V posledním souhrnném checkpointu byly evidované:

- patní měření hned za elektroměrem;
- wellness zóna;
- hlavní objekt;
- tepelné čerpadlo;
- topné tyče;
- bojler.

Tyto větve tvoří důležitý kontext pro energetické řízení. Přesné typy měřidel, jejich umístění a vazby na oba měniče zatím nejsou v autoritativní dokumentaci úplné.

## Provozní princip

- Měniče, baterie a tepelné technologie musí samostatně dodržovat své ochrany a bezpečné limity.
- Home Assistant může měnit provozní režimy a požadované hodnoty, ale není jedinou bezpečnostní vrstvou.
- Exportní řízení se opírá o měření v hlavním předávacím místě a respektuje společný limit lokality.
- Ruční zásah má vždy prioritu a automatika se s uživatelem nesmí přetahovat.
- Při ztrátě dat nebo komunikace se výkonové spotřebiče musí vrátit do předem určeného bezpečného stavu.
- Předvídatelnost a udržovatelnost mají přednost před maximální optimalizací.

## Otevřené ověření

- [ ] Opsat typové štítky obou měničů a bateriových systémů.
- [ ] Ověřit současný instalovaný výkon FVE panelů.
- [ ] Získat jednopólové schéma nebo vytvořit ověřený provozní nákres.
- [ ] Ověřit místo a zdroj hlavního měření výkonu.
- [ ] Zapsat skutečnou topologii měřených větví, měřidel, měničů, baterií a hlavního předávacího místa.
- [ ] Ověřit aktuální stav akumulační nádoby, kotle Atmos, tepelného čerpadla Hitachi, topných tyčí a bojleru.
- [ ] Ověřit aktuální technické zapojení a řízení sauny, koupacího sudu a bazénu.
- [ ] Zapsat komunikační rozhraní a adresy zařízení bez hesel a klíčů.
- [ ] Ověřit chování obou systémů a výkonových spotřebičů při ztrátě komunikace s Home Assistantem.
