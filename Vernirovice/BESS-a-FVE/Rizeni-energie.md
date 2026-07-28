# Řízení energie

## Aktuálně fungující automatizace

Automatizace vybíjí baterii během dvou nejdražších hodin. U potvrzené logiky platí:

- vybere dvě nejdražší hodiny;
- přepne měnič do režimu `Export First`;
- povolí export přebytků;
- spustí vybíjení pouze při SOC nad 15 %;
- po skončení drahého okna vrátí systém do běžného režimu.

Automatizace je podle posledního ověření funkční.

## Důležité entity

| Entita | Role |
|---|---|
| `sensor.deye_stridac_battery_soc` | stav nabití baterie |
| `select.deye_stridac_work_mode` | volba pracovního režimu měniče |
| `switch.sol_export_surplus` | povolení exportu přebytků |

Názvy entit jsou provozní vazba automatizace. Po změně integrace nebo migraci Home Assistantu je nutné ověřit, že zůstaly platné.

## Směr dalšího rozvoje

- zohlednění výroby, spotřeby, spotových cen a předpovědi;
- koordinace obou bateriových systémů;
- řízení dalších významných a skutečně ovladatelných zátěží;
- vyhodnocení přínosu algoritmu z historických dat v InfluxDB a Grafaně.

## Zásady

- Algoritmus řízení je hlavní know-how projektu.
- Automatizace nesmí obcházet ochrany měničů ani fyzické limity lokality.
- Výpadek Home Assistantu musí vést k předvídatelnému a bezpečnému stavu.
- Nová logika se nejdřív ověřuje na omezeném rozsahu a s možností ručního návratu.

## Otevřené úkoly

1. Ověřit skutečné chování automatizace při hraničním SOC a při ztrátě dat.
2. Doplnit koordinaci nového 215kWh systému až po ověření jeho rozhraní.
3. Stanovit bezpečné výchozí režimy obou měničů.
4. Přidat měřitelné vyhodnocení ekonomického přínosu jednotlivých strategií.
