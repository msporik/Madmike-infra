# FVE SolaX

Napojení domácí fotovoltaiky SolaX do Home Assistantu.

## Aktuální stav

- **Hlavní měnič:** SolaX X3-Hybrid G4, 10 kW.
- **Hlavní měření spotřeby domu:** Smart Meter náležející k FVE SolaX.
- Data z FVE jsou dostupná v domácím Home Assistantu.
- SolaX a Energy dashboard jsou provozně používané.

## Měření a zobrazení

Home Assistant přebírá data z FVE a používá je pro energetický přehled. Doložené měření samo o sobě neznamená, že Home Assistant automaticky řídí všechny související spotřebiče nebo nastavení střídače.

## Řízení

Energetické řízení je zatím v poloautomatickém režimu. Dokumentace proto neoznačuje jednotlivé topné patrony, společné oběhové čerpadlo, bojler ani nastavení FVE za plně automaticky řízené, dokud nebude dokončená a prakticky ověřená konkrétní logika.

Cílová automatika musí zachovat tyto zásady:

- ruční zásah má vyšší prioritu než automatika;
- ruční override musí být časově nebo stavově omezený;
- návrat do automatického režimu musí být jednoznačný;
- při ztrátě dat nebo integrace musí zařízení přejít do definovaného bezpečného stavu;
- výkonové spotřebiče musí mít jasné podmínky zapnutí i vypnutí;
- základní vytápění nesmí být existenčně závislé na Home Assistantu.

## Dlouhodobá data

Malý pilot InfluxDB a Grafany pro domácí energetická data zůstává schváleným plánem k realizaci. Před nasazením je potřeba určit rozsah ukládaných dat, retenci a zálohování.

## Uzavřená historie

- Po aktualizaci Home Assistantu na verzi 2026.07.1 dočasně chyběly některé SolaX entity. Stav se následně obnovil a incident není otevřeným úkolem.
- SolaX X1-Micro 2200 nebyl koupen ani nasazen. Šlo pouze o dřívější úvahu a není součástí aktuální infrastruktury.

## Otevřené úkoly

- [ ] Dotáhnout energetické řízení do plně automatického režimu a zdokumentovat skutečně řízené prvky, podmínky, ruční režim, bezpečný stav a návrat do automatiky.
- [ ] Realizovat malý pilot InfluxDB a Grafany pro domácí energetická data včetně stanovení retence a zálohování.
