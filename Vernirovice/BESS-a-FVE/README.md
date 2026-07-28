# BESS a FVE – Vernířovice

## Účel

Projekt spojuje technologie FVE a bateriových systémů s nadřazeným řízením energie. Cílem je využívat baterie podle cen a provozní situace, dodržet limity lokality a zachovat bezpečné autonomní chování měničů.

## Aktuálně potvrzený stav

- V lokalitě je původní systém s měničem Deye 50 kW a baterií přibližně 50 kWh.
- Novější bateriový systém má kapacitu 215 kWh.
- Přesný model nové baterie není potvrzený.
- Přesný model a jmenovitý výkon nového měniče je potřeba ověřit; starší podklady si v tomto údaji odporují.
- Současný limit exportu lokality je 50 kW.
- Hlavní jištění je evidované jako 3×80 A.
- Automatizace vybíjení během dvou nejdražších hodin funguje.

## Podrobnosti

- [Technologie](Technologie.md)
- [Řízení energie](Rizeni-energie.md)
- [Home Assistant](../Home-Assistant/README.md)

## Otevřené úkoly

1. Ověřit přesný model, výkon a zapojení nového měniče.
2. Ověřit výrobce, model a technické parametry baterie 215 kWh.
3. Zapsat skutečnou topologii měření, měničů, baterií a hlavního předávacího místa.
4. Ověřit, které limity jsou pevně nastavené v jednotlivých měničích a které mění Home Assistant.
5. Doplnit bezpečný postup pro ruční provoz při výpadku Home Assistantu.
