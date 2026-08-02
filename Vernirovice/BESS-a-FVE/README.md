# BESS a FVE – Vernířovice

## Účel

Projekt spojuje technologie FVE a bateriových systémů s nadřazeným řízením energie. Cílem je využívat baterie podle cen a provozní situace, dodržet limity lokality a zachovat bezpečné autonomní chování měničů.

## Naposledy doložený stav

> Stav byl konsolidován při auditu 2. 8. 2026. Živé měniče, měření ani rozvaděč nebyly při auditu ověřovány; níže jsou proto od sebe oddělené doložené skutečnosti a otevřená ověření.

- Původní sestava používá měnič Deye 50 kW a baterii přibližně 50 kWh.
- Automatizace vybíjení ve dvou nejdražších hodinách stále běží a řídí pouze původní sestavu.
- Větší baterie přibližně 215 kWh a její vlastní měnič jsou fyzicky přidané; systém byl přidaný také do Home Assistantu.
- Větší sestava není plně zprovozněná. Problém komunikace baterie–střídač trvá a řeší jej dodavatel.
- Přesný výrobce a model větší baterie ani přesný model a výkon jejího měniče nejsou potvrzené. Starší podklady si odporují a žádná z variant se nesmí vydávat za skutečnost bez ověření štítku a zapojení.
- Společný limit exportu lokality byl naposledy potvrzený jako 50 kW. Není doložené, kde a jak je tento limit při souběhu obou měničů rychle vynucován.
- Hlavní jištění objektu bylo naposledy evidované jako 3×80 A; nejde o údaj o jištění jednotlivých měničů.
- Nákup elektřiny je zatím na fixu. Smlouva je vypovězená a probíhá výběrové řízení na spotový nákup i spotový výkup přetoků.

## Schválený cílový stav

Po plném zprovoznění větší sestavy má nadřazené řízení koordinovat oba bateriové systémy podle cen, výroby, spotřeby a provozních omezení. Spotový režim je cíl, nikoli současná provozovaná funkce.

Schválené pořadí priorit cílového řízení:

1. bezpečnost a lokální limity;
2. ruční požadavek a komfort;
3. vlastní spotřeba;
4. nákup v levných hodinách;
5. export pouze při prokazatelném čistém ekonomickém přínosu.

## Podrobnosti a hranice projektu

- [Technologie](Technologie.md) – sestavy, měření, jištění, komunikace a datovaný technologický snapshot.
- [Řízení energie](Rizeni-energie.md) – současná automatizace, bezpečnostní zásady a cílová logika.
- [Home Assistant](../Home-Assistant/README.md) – platforma, integrace, migrace a provoz HA.

Otevřená ověření a realizační úkoly jsou vedené v příslušných podrobných dokumentech, nikoli duplicitně v tomto rozcestníku.
