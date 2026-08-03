# FVE SolaX

Napojení domácí fotovoltaiky SolaX do Home Assistantu.

## Účel a hranice

Home Assistant přebírá data domácí FVE, používá je v Energy dashboardu a poskytuje základ pro postupné řízení využití energie. Tento dokument rozlišuje měření, zobrazení a skutečné řízení.

Elektrické ochrany, limity střídače, termostaty a základní vytápění nesmějí být závislé pouze na Home Assistantu.

## Aktuální stav

- **Hlavní měnič:** SolaX X3-Hybrid G4, 10 kW.
- **Hlavní měření spotřeby domu:** Smart Meter náležející k FVE SolaX.
- Data z FVE jsou dostupná v domácím Home Assistantu.
- SolaX a Energy dashboard jsou provozně používané.
- Energetické řízení je zatím poloautomatické.

Přesný název použité integrace, její komunikační cesta a klíčové produkční entity nejsou v dostupných autoritativních zdrojích uvedené. **Vyžaduje ověření v živém systému.**

## Měření a zobrazení

Home Assistant přebírá data z FVE a používá je pro energetický přehled. Doložené měření samo o sobě neznamená, že Home Assistant automaticky řídí všechny související spotřebiče nebo nastavení střídače.

Při přejímce musí být význam hodnot a znamének ověřen proti živému stavu domu. Zvlášť je nutné odlišit:

- výrobu FVE;
- spotřebu domu;
- odběr ze sítě;
- přetok do sítě;
- případné hodnoty baterie;
- kumulativní energii používanou v dlouhodobých statistikách.

Dokud nejsou konkrétní entity a jejich význam potvrzené, nesmějí být použité jako jediný podklad pro výkonové řízení.

## Řízení

Dokumentace neoznačuje jednotlivé topné patrony, společné oběhové čerpadlo, bojler ani nastavení FVE za plně automaticky řízené, dokud nebude dokončená a prakticky ověřená konkrétní logika.

Cílová automatika musí zachovat tyto zásady:

- ruční zásah má vyšší prioritu než automatika;
- ruční override musí být časově nebo stavově omezený;
- návrat do automatického režimu musí být jednoznačný;
- při ztrátě dat nebo integrace musí zařízení přejít do definovaného bezpečného stavu;
- výkonové spotřebiče musí mít jasné podmínky zapnutí i vypnutí;
- základní vytápění nesmí být existenčně závislé na Home Assistantu;
- hardwarové ochrany a lokální limity se automatizací neobcházejí.

Konkrétní současný způsob ručního přepnutí, ovládané výstupy, podmínky a bezpečný stav nejsou úplně zdokumentované. **Vyžaduje ověření v živém systému.**

## Provozní kontrola

Při běžné kontrole ověřit:

1. dostupnost SolaX zařízení a Smart Meteru;
2. stav použité integrace v Home Assistantu;
3. aktuálnost hlavních hodnot a jejich rozumnou vzájemnou vazbu;
4. načtení Energy dashboardu a dlouhodobých statistik;
5. stav automatizací, ručního režimu a případných nedostupných vstupů;
6. zda žádný výkonový výstup nezůstal v nežádoucím stavu po restartu nebo výpadku dat.

## Diagnostický runbook

| Projev | Postup |
|---|---|
| Chybí všechna data SolaX | Ověřit stav zařízení, domácí sítě a integrace. Potom zkontrolovat logy Home Assistantu. Nerestartovat bezdůvodně celý Home Assistant. |
| Chybí jen některé entity | Porovnat entity zařízení a stav integrace; ověřit, zda nejde o iniciační zpoždění nebo změnu po aktualizaci. Neupravovat současně dashboard i integraci. |
| Energy dashboard ukazuje nesmyslný tok | Ověřit význam a znaménka zdrojových entit proti okamžité realitě domu a Smart Meteru. Do vyjasnění nepoužívat hodnotu pro automatické výkonové řízení. |
| Automatizace reaguje neočekávaně | Přejít do existujícího ručního nebo bezpečného režimu, ověřit všechny vstupy, časování, hysterezi a unavailable stavy. Konkrétní ovládání ručního režimu vyžaduje živé ověření. |
| Po restartu zůstal sepnutý výkonový prvek | Použít místní bezpečné ovládání, ověřit fyzický stav a teprve potom analyzovat automatizaci. Bezpečnostní termostat nebo lokální ochrana se neobchází. |

## Aktualizace

Před aktualizací Home Assistantu, SolaX integrace nebo související HACS komponenty:

1. Ověřit použitelný backup podle [Záloh Home Assistantu](../Zalohy/Home-Assistant.md).
2. Zaznamenat používanou verzi integrace a dostupnost klíčových hodnot.
3. Zkontrolovat poznámky k vydání a breaking changes.
4. Aktualizovat pouze jednu významnou vrstvu.
5. Po aktualizaci ověřit zařízení, entity, znaménka, Energy dashboard, statistiky a automatizace.
6. Při chybě neprovádět několik dalších změn současně; podle potřeby použít návratový postup.

Po aktualizaci Home Assistantu na verzi 2026.07.1 dočasně chyběly některé SolaX entity. Stav se následně obnovil. Incident je uzavřený, ale potvrzuje nutnost rozlišit iniciační zpoždění od trvalé chyby.

## Dlouhodobá data

Malý pilot InfluxDB a Grafany pro domácí energetická data zůstává schváleným plánem. Před nasazením je potřeba určit:

- které hodnoty mají provozní význam;
- retenci;
- očekávanou velikost dat;
- zálohování a obnovu;
- jeden konkrétní použitelný dashboard.

Pilot nesmí vytvářet druhý zdroj pravdy pro okamžité řízení ani novou závislost základního provozu domu.

## Uzavřená historie

- Dočasný výpadek některých SolaX entit po aktualizaci 2026.07.1 se sám upravil a není otevřeným úkolem.
- SolaX X1-Micro 2200 nebyl koupen ani nasazen. Šlo pouze o dřívější úvahu a není součástí aktuální infrastruktury.

## Otevřené úkoly

- [ ] Ověřit a zdokumentovat přesný název a komunikační cestu používané SolaX integrace a klíčové entity pro diagnostiku, Energy dashboard a automatizace.
- [ ] Dotáhnout energetické řízení do plně automatického režimu a zdokumentovat skutečně řízené prvky, podmínky, ruční režim, bezpečný stav a návrat do automatiky.
- [ ] Realizovat malý pilot InfluxDB a Grafany pro domácí energetická data včetně stanovení retence a zálohování.
