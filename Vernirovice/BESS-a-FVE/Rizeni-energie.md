# Řízení energie

## Současná automatizace původní sestavy

K 2. 8. 2026 bylo uživatelem potvrzené, že automatizace vybíjení během dvou nejdražších hodin stále běží a řídí pouze původní sestavu Deye 50 kW s baterií přibližně 50 kWh.

Naposledy doložená logika:

- cenový senzor v Home Assistantu určí dvě nejdražší hodiny; přesný název entity není v autoritativní dokumentaci zachycený;
- při SOC nad 15 % přepne původní měnič do režimu `Export First`;
- povolí export přebytků;
- po skončení drahého okna jej vrátí do režimu `Zero Export To CT`.

Současný běh byl potvrzený, ale při auditu nebylo živě otestované chování na hranici SOC, při chybě dat, ztrátě komunikace ani po restartu Home Assistantu.

## Naposledy doložené entity

| Entita nebo vstup | Role | Stav dokumentace |
|---|---|---|
| cenový senzor Home Assistantu | výběr dvou nejdražších hodin | přesný název entity je potřeba doplnit |
| `sensor.deye_stridac_battery_soc` | SOC původní baterie | historicky doložený provozní název; ověřit při změně integrace |
| `select.deye_stridac_work_mode` | pracovní režim původního měniče | historicky doložený provozní název; ověřit při změně integrace |
| `switch.sol_export_surplus` | povolení exportu přebytků | historicky doložený provozní název; ověřit při změně integrace |

Tyto názvy jsou vazbou současné automatizace, nikoli obecně stabilním rozhraním. Po změně integrace nebo migraci Home Assistantu se musí ověřit jejich význam i skutečné přijetí povelu měničem.

## Současná omezení

- Větší 215kWh sestava není plně zprovozněná a současná automatizace ji neřídí.
- Dodavatel stále řeší komunikaci mezi větší baterií a jejím střídačem.
- Pro společný exportní limit 50 kW není zdokumentovaná rychlá lokální regulační vrstva pro souběh obou měničů.
- Přesné provedení ručního režimu, fail-safe chování a návratu po chybě nebo restartu není zdokumentované.
- InfluxDB a Grafana jsou v provozu, ale pravidelné ekonomické vyhodnocování EMS není doložené.

## Schválená cílová logika

Po plném zprovoznění větší sestavy má řízení koordinovat oba bateriové systémy podle cen, výroby, spotřeby, účinnosti a provozních omezení.

Schválené pořadí priorit:

1. bezpečnost a lokální limity;
2. ruční požadavek a komfort;
3. vlastní spotřeba;
4. nákup v levných hodinách;
5. export pouze při prokazatelném čistém ekonomickém přínosu.

Koordinace větší sestavy se nesmí nasadit jen podle existence entit v Home Assistantu. Nejdřív je nutné uzavřít problém s dodavatelem, ověřit její lokální ochrany a rozhraní read-only způsobem a prokázat bezpečné dodržení společného exportního limitu.

## Ruční režim a fail-safe požadavky

- Ruční požadavek uživatele a požadavek na komfort mají mít před automatickou optimalizací prioritu.
- Po odeslání změny musí automatika ověřit, že zařízení povel skutečně přijalo a že výsledný stav odpovídá očekávání.
- Při ztrátě Home Assistantu, cenových dat, hlavního měření nebo komunikace se zařízení musí vrátit do určeného konzervativního lokálního režimu.
- Po restartu se automatika nesmí bez kontroly vrátit do předchozího výkonového stavu; nejdřív musí načíst skutečný stav zařízení a podmínky.
- Musí existovat popsaný postup bezpečného ručního provozu a návratu do automatiky.

## Plánované režimy

### Maximální záloha

Ručně aktivovatelný režim před plánovanou odstávkou má dočasně upřednostnit zásobu energie před cenovou optimalizací. Jde o schválený plán, nikoli nasazenou funkci.

### Spotové řízení

Nákup elektřiny je zatím na fixu. Smlouva je vypovězená a probíhá výběrové řízení na dodavatele se spotovým nákupem a na odběratele přetoků se spotovým výkupem. Spotové řízení je proto cílový stav a nesmí se popisovat jako současný provoz.

### Ekonomické vyhodnocování

Cílem je měsíčně vyhodnocovat alespoň nákup, prodej, výrobu FVE, spotřebu významných zátěží, cyklování baterií, odhad ztrát a čistý finanční přínos strategie. Provoz InfluxDB a Grafany je datový základ, nikoli důkaz, že tento přehled už existuje.

## Otevřené úkoly

- [ ] Zdokumentovat přesný cenový vstup, současnou automatizaci a vazbu jejích entit na původní sestavu.
- [ ] Prakticky ověřit návrat do `Zero Export To CT`, hraniční SOC, chybějící cenová data, odmítnutý povel, ztrátu komunikace a restart Home Assistantu.
- [ ] Stanovit a otestovat bezpečný ruční režim, fail-safe stav a návrat do automatiky pro obě sestavy.
- [ ] Před koordinací obou baterií prokázat bezpečné vynucení společného exportního limitu 50 kW nezávisle na pomalé nadřazené optimalizaci.
- [ ] Po vyřešení problému dodavatelem read-only způsobem ověřit rozhraní, limity a skutečné chování větší sestavy.
- [ ] Navrhnout, otestovat a zdokumentovat ručně aktivovatelný režim Maximální záloha.
- [ ] Po uzavření výběrového řízení zapsat skutečný nákupní a výkupní produkt a teprve poté připravit spotové řízení.
- [ ] Zavést měsíční ekonomické vyhodnocení a ověřovat čistý přínos jednotlivých strategií.
