# Technologie FVE, BESS a tepelné infrastruktury

## Účel a přesnost údajů

Dokument je autoritativním místem pro stabilní technologické údaje, měření, komunikační vazby, provozní kontrolu a diagnostiku fyzických systémů. Technologický stav byl konsolidován při auditu 2. 8. 2026 bez živé kontroly měničů, baterií, rozvaděče a měřidel.

Údaj označený jako naposledy doložený není náhradou typového štítku, jednopólového schématu nebo živého read-only ověření. Výrobní čísla, servisní kódy, hesla a tajné komunikační údaje do repozitáře nepatří.

## FVE a BESS sestavy

| Sestava | Naposledy doložené komponenty | Provozní stav |
|---|---|---|
| původní | Deye 50 kW; baterie přibližně 50 kWh | v provozu; automatizace dvou nejdražších hodin řídí pouze tuto sestavu |
| větší | baterie přibližně 215 kWh; vlastní měnič | fyzicky přidána a přidána do Home Assistantu, ale není plně zprovozněna; problém komunikace baterie–střídač trvá a řeší jej dodavatel |

Novější schválený souhrn označuje větší měnič jako druhý Deye. Starší podklady však uvádějí Deye 80 kW, Deye přibližně 100 kW i Growatt WIT 100 kW. Do ověření typového štítku, dokumentace dodavatele a skutečného zapojení zůstávají výrobce, model a výkon neuzavřené.

Poslední souhrnný checkpoint uváděl instalovaný výkon panelů 45 kWp. Protože se lokalita mezitím rozšiřovala, jde o historický údaj, nikoli potvrzený současný výkon.

## Provozní topologie

Naposledy doložená logická vazba je:

```text
Distribuční síť / předávací místo
        │
hlavní elektroměr a hlavní jištění 3×80 A
        │
hlavní měření lokality Shelly
        │
        ├── objektová a tepelná spotřeba
        ├── původní Deye 50 kW + baterie cca 50 kWh
        └── větší měnič + baterie cca 215 kWh
```

Toto není jednopólové schéma. Skutečné připojení, jištění jednotlivých větví, měřicí transformátory, smartmetery, zálohované výstupy a rychlá regulační vazba nejsou kompletně zdokumentovány. **Vyžaduje ověření v živém systému.**

## Měření, jištění a exportní limit

| Prvek | Naposledy doložený stav | Co je potřeba ověřit |
|---|---|---|
| hlavní měření lokality | Shelly za hlavním elektroměrem měří celý objekt | přesný model; Shelly EM versus Shelly Pro 3EM; znaménka, fáze, kalibrace a vazba na regulační smyčku |
| smartmeter původního měniče | vlastní smartmeter ve stejném místě; Home Assistant jej nezobrazuje | přesný typ, zapojení, nastavení a význam vůči hlavnímu Shelly měření |
| smartmeter většího měniče | naposledy nebyl osazen nebo doložen | skutečný stav; cílové společné měření, master/slave nebo externí export controller |
| společný export lokality | naposledy potvrzený limit 50 kW | smluvní základ, místo nastavení a rychlé vynucení při souběhu obou měničů |
| hlavní jištění objektu | naposledy evidované 3×80 A | fyzické ověření a oddělení od jištění jednotlivých měničů a zařízení |

Samotná existence hlavního měření nebo entity v Home Assistantu nedokládá, že je společný limit 50 kW bezpečně regulován. Dva nezávislé regulátory připojené ke stejnému bodu měření se mohou ovlivňovat nebo rozkmitat. Rychlá lokální regulační vrstva pro souběh obou měničů zatím není zdokumentována.

## Komunikace a integrační vrstvy

- Původní sestava je monitorována a řízena současnou integrací Home Assistantu přes Solarman.
- Větší sestava byla do Home Assistantu přidána, ale existence entit nedokládá funkční komunikaci baterie–střídač ani bezpečné nabíjení a vybíjení.
- Přesný typ loggerů, komunikační cesta, firmware, Modbus ID a mapy registrů nejsou potvrzeny.
- Qotom N100 s RS485 je určen pro budoucí read-only pilot. Produkční kabeláž, topologie sběrnice, převodníky a přímé řízení nejsou realizovány ani uzavřeny.
- InfluxDB a Grafana jsou podle projektu Home Assistant v provozu. To nedokládá pravidelné ekonomické vyhodnocování EMS.

### Pravidla pro read-only RS485/Modbus pilot

1. Potvrdit přesný model, firmware a oficiální mapu registrů.
2. Zdokumentovat fyzickou topologii, galvanické oddělení, stínění, zakončení a slave ID.
3. Pilotovat nejprve jeden přístroj a omezený seznam registrů.
4. Nepovolovat žádné zápisy.
5. Porovnat hodnoty se Solarmanem, lokálním displejem a hlavním měřením.
6. Ověřit škály, znaménka, časovou odezvu, timeouty a chování po přerušení linky.
7. Zaznamenat verzi mapy registrů a přejímací výsledek.
8. Zápisové testy připravit jako samostatnou změnu s návratem a bezpečným parametrem.

## Tepelná infrastruktura – historický snapshot

Následující inventura pochází ze starších souhrnných podkladů a při auditu 2. 8. 2026 nebyla živě ověřena:

| Technologie | Historicky evidovaný stav | Měření nebo ovládání | Zapojení do EMS |
|---|---|---|---|
| akumulační nádoba | 1 000 l; elektrické topné tyče 6 kW | klíčová data byla dostupná v Home Assistantu | současný stav a logiku ověřit |
| kotel | automatický peletový Atmos jako záložní zdroj | neověřeno | neověřeno |
| tepelné čerpadlo | Hitachi | samostatně měřená větev | současnou řiditelnost ověřit |
| vytápění | radiátory s termostatickými hlavicemi Honeywell | stav integrace neověřen | neověřeno |
| teplá voda | elektrický bojler 2 kW a předehřev z akumulační nádoby | samostatně měřená větev | současnou řiditelnost ověřit |

## Wellness zóna – historický snapshot

| Technologie | Historicky evidovaný stav | Měření nebo ovládání | Zapojení do EMS |
|---|---|---|---|
| sauna | elektrické topení 9 kW | vlastní ovládání mimo Home Assistant | nedoloženo |
| koupací sud | elektrický ohřev; podklady si odporují mezi 9 kW a přibližně 12 kW; doplňkový ohřev dřevem | spínání přes Shelly bylo integrované do Home Assistantu | současný stav a využití v EMS nejsou potvrzeny |
| bazén | vytápění tepelným čerpadlem, filtrace a vlastní řídicí logika | nucené vypnutí přes chytrou zásuvku bylo integrované do Home Assistantu | současný stav a využití v EMS nejsou potvrzeny |

Historicky byly evidovány měřené větve hlavního objektu, wellness zóny, tepelného čerpadla, topných tyčí a bojleru. Přesné typy měřidel, jejich umístění, znaménka, měřicí interval a současná dostupnost se musí ověřit.

## Provozní principy

- Měniče, baterie a tepelné technologie musí samostatně dodržovat své ochrany a bezpečné limity.
- Home Assistant může měnit provozní režimy a požadované hodnoty, ale nesmí být jedinou bezpečnostní vrstvou.
- Ruční zásah má vždy prioritu a automatika se s uživatelem nesmí přetahovat.
- Při ztrátě dat nebo komunikace se systém musí vrátit do předem určeného konzervativního lokálního režimu.
- Předvídatelnost a udržovatelnost mají přednost před maximální optimalizací.
- Změna firmware, komunikační mapy, měření a řídicího algoritmu se neprovádí současně.

## Běžná provozní kontrola

### Každá sestava

- lokální displej nebo servisní rozhraní nehlásí nový alarm;
- stav baterie, SOC, nabíjecí a vybíjecí výkon dávají fyzikální smysl;
- teploty, napětí a proudy nejsou mimo běžný rozsah;
- pracovní režim odpovídá očekávanému ručnímu nebo automatickému stavu;
- hodnoty v Home Assistantu nejsou zjevně zastaralé.

### Společné měření

- směr a řád hlavního toku odpovídají známé výrobě a spotřebě;
- součet dostupných dílčích toků nemá nevysvětlený významný rozpor vůči hlavnímu měření;
- není překročen společný exportní limit;
- měření jednotlivých fází neukazuje zjevnou chybu nebo chybějící fázi.

### Větší sestava

- stav komunikace baterie–střídač a servisní případ dodavatele;
- potvrzení, že sestava není automaticky řízena jen podle přítomnosti entit;
- jakákoli změna provedená dodavatelem, nový firmware a výsledek testu nabíjení/vybíjení.

Přesné normální rozsahy, alarmové kódy, intervaly a servisní kontakty nejsou v repozitáři doloženy. **Vyžaduje ověření v živém systému.**

## Diagnostický runbook

### Komunikace větší baterie a střídače

1. Zaznamenat přesný čas, lokální alarmy, stav BMS a měniče a poslední známý funkční stav.
2. Ověřit napájení a fyzickou komunikaci pouze v rozsahu bezpečném pro kvalifikovanou osobu.
3. Ověřit modely, firmware a kompatibilitu podle dokumentace dodavatele.
4. Nezaměňovat problém integrace Home Assistantu s interní komunikací baterie–střídač.
5. Nepřepisovat parametry, adresy nebo firmware bez pokynu dodavatele a připraveného návratu.
6. Po zásahu dodavatele doložit bezpečný lokální režim a test nabíjení, vybíjení, alarmu a restartu.

### Nesoulad hlavního měření a měničů

1. Porovnat časovou značku a interval aktualizace všech zdrojů.
2. Ověřit znaménka, fáze, převody CT a jednotky.
3. Rozlišit okamžitý výkon od kumulativní energie.
4. Ověřit, které zátěže leží mimo jednotlivá měření.
5. Změnu kalibrace provést až po nezávislém porovnání a záznamu původního nastavení.

### Riziko překročení exportního limitu

1. Zastavit nebo omezit nadřazenou optimalizaci a použít ověřený konzervativní lokální režim.
2. Ověřit skutečný tok na hlavním měření, nikoli jen požadované setpointy.
3. Ověřit, zda oba měniče současně nereagují na rozdílné nebo zpožděné měření.
4. Dokud není příčina odstraněna, nevracet koordinovaný export a nezvyšovat limity.
5. Incident zdokumentovat včetně maximálního toku, režimů obou měničů a stavu komunikace.

### Hodnota v Home Assistantu je nedostupná

1. Ověřit skutečný stav přímo na zařízení.
2. Rozlišit závadu zařízení, loggeru, sítě a integrace.
3. Při nedostupné řídicí hodnotě nepokračovat podle starého stavu.
4. Po obnovení komunikace ověřit režim a tok energie před návratem automatiky.

## Údržba a změny

Před firmwarem, změnou měření, smartmeteru, regulátoru nebo komunikační cesty:

1. zaznamenat modely, verze, původní nastavení a současné alarmy;
2. ověřit schéma, odpovědnost dodavatele a návratovou cestu;
3. určit přejímací test včetně ztráty komunikace a restartu;
4. měnit jednu logickou vrstvu;
5. po změně nejdřív ověřit lokální bezpečnost a měření;
6. teprve potom obnovit integraci a nadřazenou automatiku;
7. zdokumentovat výsledek, nové verze a případné omezení.

## Otevřená ověření

- [ ] S dodavatelem vyřešit komunikaci baterie–střídač větší sestavy a doložit skutečné nabíjení, vybíjení, alarmy a bezpečný lokální režim.
- [ ] Opsat typové štítky obou měničů a bateriových systémů a uzavřít rozpory v modelech, výkonech a kapacitách.
- [ ] Ověřit současný instalovaný výkon FVE panelů.
- [ ] Získat jednopólové schéma nebo vytvořit ověřený provozní nákres včetně jištění jednotlivých zařízení a zálohovaných okruhů.
- [ ] Ověřit model, zapojení, znaménka a kalibraci hlavního Shelly a smartmeterů obou měničů.
- [ ] Ověřit, kde a jak je při souběhu obou měničů rychle vynucován společný exportní limit 50 kW.
- [ ] Ověřit současný stav, měření, ruční ovládání a fyzickou řiditelnost tepelné a wellness infrastruktury.
- [ ] Zapsat komunikační rozhraní a adresy zařízení bez tajných údajů a teprve poté připravit read-only RS485 pilot.
