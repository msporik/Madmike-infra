# NSPanel a topení

## Poslední doložený stav k 2026-08-02

Stav potvrdil uživatel; nejde o živou kontrolu Home Assistantu, ESPHome ani fyzické kabeláže.

## Panely

| Panel | Umístění | Role a poslední doložený stav |
|---|---|---|
| NSPanel Pro 120 | Obývák | Je namontovaný a po spuštění automaticky otevírá Home Assistant. Slouží pouze jako místní uživatelské rozhraní, ne jako Zigbee koordinátor nebo router. |
| Běžný Sonoff NSPanel | Ložnice | Jeden ze tří fyzických panelů; přesný stav konfigurace a montáže není ověřený. |
| Běžný Sonoff NSPanel | Pracovna | Jeden ze tří fyzických panelů; přesný stav konfigurace a montáže není ověřený. |
| Běžný Sonoff NSPanel | Dětský pokoj | Jeden ze tří fyzických panelů; přesný stav konfigurace a montáže není ověřený. |

Pro běžné NSPanely byly v přípravě doložené ESPHome, Blackymas `NSPanel_HA_Blueprint`, odpovídající TFT rozhraní a Arduino framework. Z dostupných údajů nelze potvrdit, že je tato konfigurace dokončená a produkčně nasazená na všech třech panelech.

Každý běžný NSPanel má obsluhovat především vlastní místnost: čas, pokojovou teplotu, jednoduché ovládání místního světla a výhledově místní termostat. Nemá z něj vzniknout centrální dashboard celého domu.

## Topení

| Oblast | Poslední doložený stav |
|---|---|
| Zdroj tepla | Elektrický kotel Protherm 12 kW |
| Soustava | Vodní podlahové topení |
| Rozdělovač | Jeden rozdělovač, přibližně osm okruhů |
| Pohony | Nejsou osazené |
| Řízení Home Assistantem | HA zatím neřídí žádnou část topení |
| Kabeláž místností | Hluboká krabice; UTP a CYKY 5×1,5 vedené do hlavního rozvaděče vedle rozdělovače |
| Podlahová čidla | Nový kabel ani čidlo už nelze dostat do podlahy |
| Zdroje pokojové teploty | Nejsou definitivně určené a ověřené |

Kabelová příprava, namontovaný panel, osazený pohon a skutečně fungující řízení topného okruhu jsou čtyři různé stavy. Dokud nejsou pohony osazené a řízení otestované, regulace topení se považuje pouze za plán.

## Požadavky na budoucí regulaci

Před realizací se musí určit:

- mapování místností a topných okruhů;
- spolehlivý zdroj pokojové teploty pro každou zónu;
- typ, napájení a zapojení pohonů a akčních členů;
- vazba mezi NSPanelem, Home Assistantem a fyzickým výstupem;
- ruční režim a jednoduchý způsob jeho aktivace;
- jednoznačný návrat z ručního režimu do automatiky;
- bezpečný stav při výpadku HA, panelu, sítě nebo teplotního čidla;
- ochrana proti nevhodnému spínání a současným požadavkům jednotlivých zón.

## Otevřené úkoly

- [ ] Ověřit a dokončit konfiguraci každého ze tří běžných NSPanelů.
- [ ] Zmapovat místnosti na jednotlivé okruhy rozdělovače.
- [ ] Vybrat a ověřit zdroj pokojové teploty pro každou plánovanou zónu.
- [ ] Navrhnout pohony, akční členy, ruční režim a fail-safe před zahájením řízení topení.

## Související dokumentace

- [Home Assistant – Honza](README.md)
- [Zigbee a osvětlení](Zigbee-a-osvetleni.md)
