# BESS a FVE – Vernířovice

## Účel a provozní role

Projekt dokumentuje fyzické FVE a bateriové sestavy ve Vernířovicích, společné měření a limity lokality a nadřazené řízení energie. Cílem je bezpečně využívat baterie podle výroby, spotřeby, cen a provozních potřeb, zachovat ruční zásah a dodržet společný exportní limit i při výpadku Home Assistantu nebo komunikace.

Home Assistant je ekonomická a koordinační vrstva. Ochrany baterií, proudové a výkonové limity a rychlé vynucení exportního limitu musejí zůstat v lokálních technologiích nebo v samostatné rychlé regulační vrstvě.

## Rychlá orientace

| Oblast | Poslední doložený stav | Autoritativní dokument |
|---|---|---|
| původní sestava | Deye 50 kW, baterie přibližně 50 kWh, v provozu | [Technologie](Technologie.md) |
| větší sestava | baterie přibližně 215 kWh a vlastní měnič; není plně zprovozněna | [Technologie](Technologie.md) |
| otevřená závada | komunikace baterie–střídač větší sestavy; řeší dodavatel | [Technologie](Technologie.md) |
| společný export | naposledy potvrzený limit 50 kW pro celou lokalitu | [Technologie](Technologie.md) |
| hlavní jištění | naposledy evidované 3×80 A | [Technologie](Technologie.md) |
| současná automatizace | dvě nejdražší hodiny; pouze původní sestava | [Řízení energie](Rizeni-energie.md) |
| obchodní režim | nákup zatím fixní; smlouva vypovězena; probíhá výběr spotového nákupu a výkupu | [Řízení energie](Rizeni-energie.md) |
| platforma řízení | produkční Home Assistant na Raspberry Pi 5; cílový Qotom N100 | [Home Assistant](../Home-Assistant/README.md) |

> Stav byl konsolidován při auditu 2. 8. 2026. Živé měniče, baterie, měření ani rozvaděč nebyly při auditu ověřeny. Před změnou je nutná read-only kontrola skutečného zařízení a zapojení.

## Naposledy doložený stav

- Původní sestava používá Deye 50 kW a baterii přibližně 50 kWh.
- Automatizace vybíjení ve dvou nejdražších hodinách stále běží a řídí pouze původní sestavu.
- Větší baterie přibližně 215 kWh a její vlastní měnič jsou fyzicky přidány a systém je přidán také do Home Assistantu.
- Větší sestava není plně zprovozněna. Problém komunikace baterie–střídač trvá a řeší jej dodavatel.
- Výrobce, model a výkon většího měniče ani přesný model baterie nejsou potvrzeny. Starší podklady si odporují mezi Deye 80 kW, Deye přibližně 100 kW a Growatt WIT 100 kW.
- Společný limit exportu lokality byl naposledy potvrzen jako 50 kW. Není doloženo, kde a jak je při souběhu obou měničů rychle vynucován.
- Hlavní jištění objektu bylo naposledy evidováno jako 3×80 A; nejde o údaj o jištění jednotlivých měničů.
- Nákup elektřiny je zatím na fixu. Smlouva je vypovězena a probíhá výběrové řízení na spotový nákup i spotový výkup přetoků.

## Schválený cílový stav

Po plném zprovoznění větší sestavy má nadřazené řízení koordinovat oba bateriové systémy podle cen, výroby, spotřeby a provozních omezení. Spotový režim je cíl, nikoli současná provozovaná funkce.

Schválené pořadí priorit:

1. bezpečnost a lokální limity;
2. ruční požadavek a komfort;
3. vlastní spotřeba;
4. nákup v levných hodinách;
5. export pouze při prokazatelném čistém ekonomickém přínosu.

## Kritické bezpečnostní zásady

- Společný exportní limit 50 kW se vztahuje na celou lokalitu a oba měniče dohromady.
- Samotná existence Shelly měření nebo entit v Home Assistantu nedokládá bezpečné vynucení limitu.
- Koordinované řízení obou sestav se nesmí zapnout, dokud není vyřešena závada větší sestavy a prokázána rychlá lokální regulace společného exportu.
- Home Assistant nesmí být jedinou vrstvou ochrany baterií ani exportního limitu.
- Neověřený model zařízení, registr nebo parametr se nesmí použít pro zápis.
- Ruční zásah má prioritu; automatika se nesmí s obsluhou přetahovat.
- Po restartu nebo obnovení komunikace se nejdřív načte skutečný stav a teprve potom se smí obnovit automatika.
- Při ztrátě cen, hlavního měření, komunikace nebo Home Assistantu musí zařízení zůstat v určeném konzervativním lokálním režimu. Jeho přesná realizace není doložena. **Vyžaduje ověření v živém systému.**

## Co při incidentu nedělat

- Neměnit naslepo pracovní režim, exportní limit, SOC limity ani Modbus registry.
- Nepovažovat dostupnou entitu za důkaz, že měnič nebo baterie fyzicky pracují správně.
- Nezapínat koordinaci obou měničů bez potvrzeného společného měření a rychlé regulační vrstvy.
- Neprovádět současně změnu integrace, firmware a algoritmu.
- Neobcházet dodavatele u trvající závady komunikace větší baterie a střídače neověřeným servisním zásahem.
- Neodpojovat nebo neotevírat výkonové části bez kvalifikace, dokumentace výrobce a příslušného bezpečného pracovního postupu.

## První postup při převzetí správy

1. Přečíst [Technologie](Technologie.md), [Řízení energie](Rizeni-energie.md) a [Home Assistant](../Home-Assistant/README.md).
2. Na místě nebo z bezpečného read-only rozhraní identifikovat oba měniče, baterie, měřidla a jejich aktuální provozní stav.
3. Ověřit, že větší sestava není mylně považována za plně provozní.
4. Ověřit skutečný režim původní sestavy a zda automatizace neuvízla v `Export First`.
5. Ověřit hlavní měření a porovnat jeho směr a řád hodnot s údaji měničů.
6. Ověřit, kde je nastaven a jak je vynucován společný exportní limit; pokud to nelze doložit, nezvyšovat výkon ani nerozšiřovat automatiku.
7. Ověřit dostupné alarmy zařízení a otevřený servisní případ větší sestavy.
8. Zapsat pouze ověřené modely, rozhraní a výsledky; tajné a servisní kódy do repozitáře nepatří.

## Postup při incidentu

1. Určit, zda je problém v jedné sestavě, společném měření, komunikaci, Home Assistantu nebo fyzické elektroinstalaci.
2. Při riziku překročení limitu nebo nechtěného nabíjení/vybíjení přejít na ověřený bezpečný lokální nebo ruční režim.
3. Zaznamenat čas, alarmy, režimy, SOC, směr toku na hlavním měření a poslední automatický zásah.
4. Ověřit skutečný stav přímo na zařízení nebo v jeho důvěryhodném lokálním rozhraní; nespoléhat jen na zpožděnou entitu.
5. U větší sestavy respektovat odpovědnost dodavatele a neprovádět neodsouhlasené zásahy do komunikace baterie–střídač.
6. Po nápravě ověřit bezpečný režim, skutečný tok energie, exportní limit, ruční ovládání a návrat automatiky.
7. Zaznamenat příčinu, zásah, výsledek a případnou potřebu změny dokumentace.

## Dokumentace projektu

- [Technologie](Technologie.md) – sestavy, měření, jištění, komunikace, provozní kontrola a diagnostika.
- [Řízení energie](Rizeni-energie.md) – současná automatizace, ruční režim, fail-safe, změny a cílová logika.
- [Home Assistant](../Home-Assistant/README.md) – platforma, služby, integrace, migrace a zálohy HA.

Otevřená ověření a realizační úkoly jsou vedeny v příslušných podrobných dokumentech, nikoli duplicitně v tomto rozcestníku.
