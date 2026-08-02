# Technologie FVE, BESS a tepelné infrastruktury

## Stav a přesnost údajů

Technologický stav byl konsolidován při auditu 2. 8. 2026. Audit neobsahoval živou kontrolu měničů, rozvaděče ani měřidel. Údaje označené jako naposledy doložené je proto nutné při budoucí fyzické inventuře ověřit.

## FVE a BESS sestavy

| Sestava | Naposledy doložené komponenty | Provozní stav |
|---|---|---|
| původní | Deye 50 kW; baterie přibližně 50 kWh | v provozu; automatizace dvou nejdražších hodin řídí pouze tuto sestavu |
| větší | baterie přibližně 215 kWh; vlastní měnič | fyzicky přidaná a přidaná do Home Assistantu, ale není plně zprovozněná; problém komunikace baterie–střídač trvá a řeší jej dodavatel |

Novější schválený souhrn označuje větší měnič jako druhý Deye. Starší podklady však uvádějí varianty Deye 80 kW, Deye přibližně 100 kW i Growatt WIT 100 kW. Do ověření typového štítku, dokumentace dodavatele a skutečného zapojení zůstávají výrobce, model a výkon neuzavřené.

Poslední souhrnný checkpoint uváděl instalovaný výkon panelů 45 kWp. Protože se lokalita mezitím rozšiřovala, jde o historický údaj, nikoli potvrzený současný výkon.

## Měření, jištění a exportní limit

| Prvek | Naposledy doložený stav | Co je potřeba ověřit |
|---|---|---|
| hlavní měření lokality | Shelly za hlavním elektroměrem měří celý objekt | přesný model; podklady uvádějí Shelly EM i Shelly Pro 3EM, dále znaménka měření a vazbu na regulační smyčku |
| smartmeter původního měniče | vlastní smartmeter ve stejném místě; Home Assistant jej nezobrazuje | přesný typ, zapojení a význam vůči hlavnímu Shelly měření |
| smartmeter většího měniče | naposledy nebyl osazený nebo doložený | cílové společné měření, případný master/slave režim nebo externí export controller |
| společný export lokality | naposledy potvrzený limit 50 kW | kde je limit nastavený a jak je rychle vynucován při souběhu obou měničů |
| hlavní jištění objektu | naposledy evidované 3×80 A | fyzické ověření a jasné oddělení od jištění jednotlivých měničů a dalších zařízení |

Samotná existence hlavního měření nebo entity v Home Assistantu nedokládá, že je společný limit 50 kW bezpečně regulovaný. Rychlá lokální regulační vrstva pro souběh obou měničů zatím není zdokumentovaná.

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
| koupací sud | elektrický ohřev; podklady si odporují mezi 9 kW a přibližně 12 kW; doplňkový ohřev dřevem | spínání přes Shelly bylo integrované do Home Assistantu | současný stav a využití v EMS nejsou potvrzené |
| bazén | vytápění tepelným čerpadlem, filtrace a vlastní řídicí logika | nucené vypnutí přes chytrou zásuvku bylo integrované do Home Assistantu | současný stav a využití v EMS nejsou potvrzené |

Historicky byly evidované měřené větve hlavního objektu, wellness zóny, tepelného čerpadla, topných tyčí a bojleru. Přesné typy měřidel, jejich umístění a současná dostupnost se musí ověřit.

## Integrace a komunikace

- Původní sestava je řízená současnou integrací Home Assistantu.
- Větší sestava byla do Home Assistantu přidaná, ale existence entit nedokládá plné zprovoznění; komunikaci baterie–střídač stále řeší dodavatel.
- Qotom N100 s RS485 je určený pro bezpečný read-only pilot. Produkční kabeláž, přímé řízení a konečná komunikační architektura zatím nejsou realizované ani rozhodnuté.
- InfluxDB a Grafana jsou podle projektu Home Assistant v provozu. To samo o sobě nedokládá pravidelné ekonomické vyhodnocování EMS.

## Provozní principy

- Měniče, baterie a tepelné technologie musí samostatně dodržovat své ochrany a bezpečné limity.
- Home Assistant může měnit provozní režimy a požadované hodnoty, ale nesmí být jedinou bezpečnostní vrstvou.
- Ruční zásah má vždy prioritu a automatika se s uživatelem nesmí přetahovat.
- Při ztrátě dat nebo komunikace se systém musí vrátit do předem určeného konzervativního lokálního režimu.
- Předvídatelnost a udržovatelnost mají přednost před maximální optimalizací.

## Otevřená ověření

- [ ] S dodavatelem vyřešit komunikaci baterie–střídač větší sestavy a potvrdit skutečné nabíjení, vybíjení a bezpečný lokální režim.
- [ ] Opsat typové štítky obou měničů a bateriových systémů a uzavřít rozpory v modelech, výkonech a kapacitách.
- [ ] Ověřit současný instalovaný výkon FVE panelů.
- [ ] Získat jednopólové schéma nebo vytvořit ověřený provozní nákres včetně jištění jednotlivých zařízení.
- [ ] Ověřit přesný model hlavního Shelly, znaménka měření, smartmetery obou měničů a jejich skutečnou vazbu na regulaci.
- [ ] Ověřit, kde a jak je při souběhu obou měničů vynucován společný exportní limit 50 kW.
- [ ] Ověřit současný stav, měření a fyzickou řiditelnost tepelné a wellness infrastruktury.
- [ ] Zapsat komunikační rozhraní a adresy zařízení bez hesel a klíčů a teprve poté připravit read-only RS485 pilot.
