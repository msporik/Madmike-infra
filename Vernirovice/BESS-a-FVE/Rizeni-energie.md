# Řízení energie

## Účel a rozdělení odpovědností

Dokument popisuje současnou automatizaci, provozní a bezpečnostní zásady, ruční režim, diagnostiku a schválený směr budoucího EMS.

| Vrstva | Odpovědnost |
|---|---|
| měnič, BMS a lokální regulace | vlastní ochrany, pevné limity, bezpečný stav a rychlé vynucení technických omezení |
| Home Assistant | cenový plán, komfortní požadavky, koordinace a pomalá ekonomická optimalizace v povolených mantinelech |
| obsluha | ruční požadavek, servisní režim a rozhodnutí o návratu do automatiky |
| AI a analytické nástroje | návrh, simulace a vyhodnocení; nikoli nekontrolované přímé řízení |

## Současná automatizace původní sestavy

K 2. 8. 2026 bylo uživatelem potvrzeno, že automatizace vybíjení během dvou nejdražších hodin stále běží a řídí pouze původní sestavu Deye 50 kW s baterií přibližně 50 kWh.

Naposledy doložená logika:

- cenový senzor v Home Assistantu určí dvě nejdražší hodiny;
- při SOC nad 15 % přepne původní měnič do režimu `Export First`;
- povolí export přebytků;
- po skončení drahého okna vrátí měnič do režimu `Zero Export To CT`.

Současný běh byl potvrzen, ale nebylo živě otestováno chování na hranici SOC, při chybě cenových dat, nedostupném měření, odmítnutém povelu, ztrátě komunikace ani po restartu Home Assistantu.

## Provozní rozhraní automatizace

| Entita nebo vstup | Role | Stav dokumentace |
|---|---|---|
| cenový senzor Home Assistantu | výběr dvou nejdražších hodin | přesný název není autoritativně zachycen |
| `sensor.deye_stridac_battery_soc` | SOC původní baterie | historicky doložený název; ověřit význam a čerstvost |
| `select.deye_stridac_work_mode` | pracovní režim původního měniče | historicky doložený název; ověřit přijetí povelu |
| `switch.sol_export_surplus` | povolení exportu přebytků | historicky doložený název; ověřit bezpečnou vazbu |

Názvy jsou vazbou současné automatizace, nikoli obecně stabilním rozhraním. Po změně integrace, profilu nebo hostitele se musí ověřit význam, jednotky, dostupnost a skutečné přijetí povelu měničem.

Historické podklady uvádějí také `number.deye_stridac_export_limit` a `number.deye_stridac_battery_discharge_limit`. Dynamické přepisování pevných limitů bylo jako cílový přístup opuštěno; bezpečnostní limity mají zůstat lokálně.

## Kontrola současného běhu

Při read-only provozní kontrole ověřit:

1. cenový vstup obsahuje platná data pro správný den a časové pásmo;
2. SOC je aktuální, nikoli `unknown`, `unavailable` nebo zastaralý;
3. skutečný pracovní režim měniče odpovídá očekávanému časovému oknu;
4. stav exportu odpovídá skutečnému toku na hlavním měření;
5. po skončení okna je měnič zpět v `Zero Export To CT`;
6. neexistuje ruční požadavek nebo servisní stav, který má přednost;
7. větší sestava není touto automatizací řízena;
8. společný tok lokality zůstává pod potvrzeným limitem.

Přesný název automatizace, poslední změny YAML/UI konfigurace, log rozhodnutí a mechanismus potvrzení povelu nejsou doloženy. **Vyžaduje ověření v živém systému.**

## Ruční režim

Ruční zásah uživatele nebo servisního technika má před automatikou prioritu. Bezpečný provoz vyžaduje:

- jednoznačně viditelný stav `automatika / ručně / servis`;
- zaznamenaný důvod a čas ručního zásahu;
- definovaný rozsah a dobu platnosti;
- zabránění tomu, aby automatika ruční nastavení okamžitě přepsala;
- kontrolovaný návrat po načtení skutečného stavu zařízení a vstupů.

Současné technické provedení ručního režimu, blokace automatiky a návratu není zdokumentováno. **Vyžaduje ověření v živém systému.** Do té doby nelze považovat ruční override za bezpečně implementovanou funkci.

## Fail-safe požadavky

- Při ztrátě Home Assistantu, cenových dat, hlavního měření nebo komunikace se zařízení musí vrátit do určeného konzervativního lokálního režimu.
- Po restartu se automatika nesmí bez kontroly vrátit do předchozího výkonového stavu.
- Po odeslání změny se musí ověřit, že zařízení povel přijalo a skutečný stav odpovídá očekávání.
- Staré, `unknown` nebo `unavailable` vstupy se nesmějí použít jako platné hodnoty.
- Dvě integrační cesty nesmějí současně zapisovat do téhož parametru.
- Při chybě společného měření nebo nejistotě exportního limitu se koordinovaný export zastaví nebo omezí na ověřený konzervativní stav.

Konkrétní hodnoty, časové limity, watchdog a bezpečný lokální režim nejsou doloženy. **Vyžaduje ověření v živém systému.**

## Diagnostický runbook

### Automatizace nespustila očekávaný režim

1. Ověřit platnost cenových dat a zda aktuální hodina skutečně patří do vybraného okna.
2. Ověřit čerstvost SOC a podmínku nad 15 %.
3. Ověřit ruční nebo servisní blokaci.
4. Zkontrolovat poslední běh automatizace a konkrétní nesplněnou podmínku.
5. Ověřit dostupnost integrační služby a skutečný stav měniče.
6. Neobcházet podmínky ručním zápisem, dokud není znám důvod a bezpečný dopad.

### Měnič zůstal v `Export First`

1. Ověřit skutečný tok na hlavním měření a případné riziko překročení limitu.
2. Zkontrolovat, zda neskončil cenový interval, nedošlo k restartu nebo chybě integrace.
3. Použít ověřený ruční postup návratu do konzervativního režimu.
4. Ověřit přijetí povelu a skutečný režim na zařízení.
5. Do odstranění příčiny automatiku ponechat bezpečně blokovanou.

Ověřený ruční postup pro tento incident není v dokumentaci doložen. **Vyžaduje ověření v živém systému.**

### Chybí cenová data

1. Ověřit datum, časové pásmo a stáří posledního datasetu.
2. Zabránit použití včerejších nebo neúplných dat.
3. Přepnout do určeného konzervativního režimu bez spotového řízení.
4. Po obnovení dat přepočítat plán podle aktuálního SOC a skutečného stavu; neobnovovat starý plán.

### SOC nebo hlavní měření je nedostupné

1. Považovat vstup za neplatný; nedosazovat poslední hodnotu bez časového omezení.
2. Ověřit skutečný stav na zařízení nebo nezávislém měření.
3. Pozastavit akce, které tento vstup potřebují pro bezpečné rozhodnutí.
4. Po obnovení ověřit znaménka, čas a fyzikální smysl hodnot.

### Povel byl odmítnut nebo stav nepotvrzen

1. Neopakovat rychle zápis bez omezení.
2. Ověřit alarmy, lokální režim, oprávnění a komunikační cestu.
3. Zkontrolovat mapu registrů nebo integrační profil proti přesnému modelu.
4. Přejít do bezpečného lokálního režimu a incident zaznamenat.

### Home Assistant byl restartován během exportu

1. Načíst skutečný režim měniče, exportní stav, SOC a hlavní měření.
2. Ověřit, zda je cenové okno stále platné.
3. Ověřit ruční zásahy a alarmy.
4. Automatiku povolit až po splnění všech vstupních podmínek.

## Současná omezení

- Větší 215kWh sestava není plně zprovozněna a současná automatizace ji neřídí.
- Dodavatel stále řeší komunikaci mezi větší baterií a jejím střídačem.
- Pro společný exportní limit 50 kW není zdokumentována rychlá lokální regulační vrstva pro souběh obou měničů.
- Ruční režim, fail-safe chování a návrat po chybě nebo restartu nejsou prakticky doloženy.
- InfluxDB a Grafana jsou v provozu, ale pravidelné ekonomické vyhodnocování EMS není doloženo.

## Schválená cílová logika

Po plném zprovoznění větší sestavy má řízení koordinovat oba bateriové systémy podle cen, výroby, spotřeby, účinnosti a provozních omezení.

Schválené pořadí priorit:

1. bezpečnost a lokální limity;
2. ruční požadavek a komfort;
3. vlastní spotřeba;
4. nákup v levných hodinách;
5. export pouze při prokazatelném čistém ekonomickém přínosu.

Koordinace větší sestavy se nesmí nasadit jen podle existence entit. Nejdřív je nutné uzavřít problém s dodavatelem, ověřit lokální ochrany, čtení a chování při chybě a prokázat bezpečné dodržení společného exportního limitu.

## Plánované režimy

### Maximální záloha

Ručně aktivovatelný režim před plánovanou odstávkou má dočasně upřednostnit zásobu energie před cenovou optimalizací. Jde o schválený plán, nikoli nasazenou funkci.

Před implementací je nutné ověřit ostrovní/backup schopnosti obou měničů, výkon zálohovaného výstupu, přepnutí a skutečně připojené okruhy. Přítomnost baterie sama nepotvrzuje funkční zálohu objektu.

### Spotové řízení

Nákup elektřiny je zatím na fixu. Smlouva je vypovězena a probíhá výběrové řízení na dodavatele se spotovým nákupem a odběratele přetoků se spotovým výkupem. Spotové řízení je cílový stav a nesmí se popisovat jako současný provoz.

### Řízení tepelných a wellness zátěží

Budoucí optimalizace má respektovat komfort, ruční požadavek a hlavní jištění a může pracovat s akumulační nádrží, tepelným čerpadlem, bojlerem a wellness zátěžemi až po ověření jejich skutečného měření, ovládání a bezpečných blokací.

Dřívější Airtable závěr uvádí samostatné účtování wellness nájemníkům pevnou cenou 8 Kč/kWh. Současná platnost a použití této hodnoty v ekonomickém modelu nebyly při auditu potvrzeny. **Vyžaduje ověření v živém systému.**

## Ekonomické vyhodnocování

Cílem je měsíčně vyhodnocovat alespoň:

- nákup energie a skutečné náklady;
- prodej energie a výnos;
- výrobu FVE a vlastní spotřebu;
- nabíjení a vybíjení obou baterií;
- odhad ztrát, cyklů a hloubky vybíjení;
- významné tepelné a wellness odběry;
- čistý přínos strategie proti srozumitelné referenční variantě.

Provoz InfluxDB a Grafany je datový základ, nikoli důkaz, že tento přehled existuje. Přesná ekonomická simulace vyžaduje časově sladěná data, úplné poplatky, účinnost a ověřené výkonové a SOC limity.

## Postup změny algoritmu

1. Popsat důvod, výchozí stav a očekávaný přínos.
2. Určit dotčené sestavy, vstupy, výstupy a bezpečnostní limity.
3. Ověřit kvalitu dat a přesný význam použitých entit.
4. Simulovat nebo zpětně vyhodnotit změnu na historických datech, pokud jsou dostupná.
5. Připravit ruční blokaci, rollback a přejímací kritéria.
6. Nasadit nejprve v režimu bez fyzických akcí nebo s omezeným výkonem.
7. Ověřit přijetí povelů, skutečný tok a chování při chybě.
8. Změnu nerozšiřovat, dokud není stabilní a srozumitelná.
9. Zaznamenat datum, verzi, původní a novou logiku, výsledek a návrat.

Firmware, integrační profil, komunikační cesta a algoritmus se nemění v jednom kroku.

## Minimální přejímací test automatizace

- běžný vstup a výstup z drahého okna;
- SOC těsně nad a pod hranicí 15 %;
- chybějící nebo neúplná cenová data;
- `unknown` nebo `unavailable` SOC;
- nedostupné hlavní měření;
- odmítnutý nebo nepotvrzený povel;
- ztráta komunikace během aktivního režimu;
- restart Home Assistantu během aktivního režimu;
- ruční zásah a kontrolovaný návrat do automatiky;
- ověření společného exportního limitu na skutečném hlavním měření.

Test nesmí být proveden bez určeného bezpečného režimu a osoby schopné zasáhnout.

## Monitoring a notifikace

Upozornění mají vzniknout zejména při:

- ztrátě klíčového měření nebo komunikace;
- chybě cenových dat;
- nepotvrzeném povelu;
- automatizaci ponechané v neočekávaném režimu;
- alarmu baterie nebo měniče;
- riziku překročení společného exportního limitu;
- neprovedeném plánovaném návratu do konzervativního režimu.

Běžné úspěšné operace nemají vytvářet notifikační šum. Konkrétní pravidla a cíle patří do [MadMike / Monitoring](../../MadMike/Monitoring/README.md).

## Otevřené úkoly

- [ ] Zdokumentovat přesný cenový vstup, současnou automatizaci, její blokaci, log rozhodnutí a potvrzení povelu.
- [ ] Prakticky ověřit návrat do `Zero Export To CT`, hraniční SOC, chyby vstupů, odmítnutý povel, ztrátu komunikace a restart Home Assistantu.
- [ ] Stanovit a otestovat bezpečný ruční režim, fail-safe stav a návrat do automatiky pro obě sestavy.
- [ ] Před koordinací obou baterií prokázat bezpečné vynucení společného exportního limitu 50 kW nezávisle na pomalé nadřazené optimalizaci.
- [ ] Po vyřešení problému dodavatelem read-only způsobem ověřit rozhraní, limity a skutečné chování větší sestavy.
- [ ] Ověřit backup/ostrovní zapojení a navrhnout, otestovat a zdokumentovat režim Maximální záloha.
- [ ] Po uzavření výběrového řízení zapsat skutečný nákupní a výkupní produkt a teprve poté připravit spotové řízení.
- [ ] Ověřit měření, ruční požadavky a komfortní podmínky tepelných a wellness zátěží.
- [ ] Zavést měsíční ekonomické vyhodnocení a ověřovat čistý přínos jednotlivých strategií.
