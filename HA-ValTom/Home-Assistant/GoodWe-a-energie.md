# GoodWe a energetika

## Cíl

První užitečnou funkcí HA ValTom má být přehled GoodWe FVE:

- aktuální výroba;
- spotřeba domu;
- odběr ze sítě a přetok do sítě;
- základní historické energetické údaje;
- jednoduchý a srozumitelný dashboard.

Pozdější rozšíření může řídit bojler podle výroby, přetoků nebo jiného schváleného energetického pravidla.

## Poslední doložený stav k 2026-08-03

Od předchozí přípravy nenastal posun. Přesný model GoodWe střídače, komunikační rozhraní a lokální IP adresa nejsou ověřené. Integrace GoodWe není zprovozněná, skutečné entity nejsou potvrzené a produkční dashboard neexistuje. Bojler není zmapovaný ani řízený Home Assistantem.

## Energetické veličiny k ověření

| Veličina | Požadovaný význam | Zdroj dat | Entity | Stav |
|---|---|---|---|---|
| Výroba FVE | Okamžitý výkon a vyrobená energie | Neověřený | Neověřené | Nerealizováno |
| Spotřeba domu | Okamžitý příkon a spotřebovaná energie domu | Neověřený | Neověřené | Nerealizováno |
| Odběr ze sítě | Tok a energie převzatá z distribuční sítě | Neověřený | Neověřené | Nerealizováno |
| Přetok do sítě | Tok a energie dodaná do distribuční sítě | Neověřený | Neověřené | Nerealizováno |

Při zprovoznění je nutné ověřit také jednotky, znaménka, aktualizační interval a to, zda jednotlivé hodnoty pocházejí přímo ze střídače, z jeho měření nebo z jiného měřicího prvku.

## Otevřené kroky

- [ ] Zjistit přesný model GoodWe střídače, jeho lokální IP adresu, dostupný způsob komunikace a skutečné zdroje výroby, spotřeby, odběru a přetoku.
- [ ] Zprovoznit nejprve čtecí integraci GoodWe, ověřit význam, jednotky a znaménka skutečných entit a vytvořit základní produkční FVE dashboard s přiměřenou historií.
- [ ] Zmapovat typ, výkon, HDO, stykač, termostat a současné ruční ovládání bojleru; teprve potom navrhnout bezpečné automatické řízení.

## Bezpečnostní rámec řízení bojleru

- Home Assistant nesmí nahrazovat nezávislý termostat, havarijní tepelnou ochranu ani ostatní povinné elektrické ochrany.
- Spínací nebo regulační prvek musí být vhodný pro skutečný příkon a způsob zapojení bojleru a odborně nainstalovaný.
- Musí existovat srozumitelný ruční režim nezávislý na běhu automatizace.
- Při výpadku Home Assistantu, komunikace nebo potřebného měření musí systém přejít do předem určeného bezpečného stavu.
- Návrat z ručního nebo poruchového režimu do automatiky musí být jednoznačný a předvídatelný.
- Zápisové řízení se nemá aktivovat, dokud nejsou ověřené energetické hodnoty, konkrétní hardware a schválená provozní logika.
