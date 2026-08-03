# NSPanel a topení

> Poslední uživatelem potvrzený stav: **2026-08-02**. Nejde o živou kontrolu Home Assistantu, ESPHome, panelů ani fyzické kabeláže.

## Panely

| Panel | Umístění | Role a poslední doložený stav |
|---|---|---|
| NSPanel Pro 120 | obývák | namontovaný; po spuštění automaticky otevírá Home Assistant; pouze místní UI, ne Zigbee koordinátor nebo router |
| běžný Sonoff NSPanel | ložnice | jeden ze tří fyzických panelů; přesný stav konfigurace a montáže není ověřený |
| běžný Sonoff NSPanel | pracovna | jeden ze tří fyzických panelů; přesný stav konfigurace a montáže není ověřený |
| běžný Sonoff NSPanel | dětský pokoj | jeden ze tří fyzických panelů; přesný stav konfigurace a montáže není ověřený |

Pro běžné NSPanely byly při přípravě použity ESPHome, Blackymas `NSPanel_HA_Blueprint`, odpovídající TFT rozhraní a Arduino framework. Není doloženo, že je konfigurace dokončená a produkčně nasazená na všech třech panelech.

Každý běžný NSPanel má obsluhovat především vlastní místnost: čas, pokojovou teplotu, jednoduché ovládání místního světla a výhledově místní termostat. Nemá z něj vzniknout centrální dashboard celého domu.

Preferované pojmenování zařízení je podle lokality a místnosti, například `nspanel_honza_decak`; skutečná jména vyžadují živé ověření.

## Běžná provozní kontrola panelů

1. Ověřit fyzické napájení a stav displeje každého panelu.
2. U NSPanel Pro ověřit připojení k síti, automatické otevření HA a ovládání pouze očekávaných funkcí.
3. U běžného NSPanelu ověřit dostupnost v ESPHome, API spojení, verzi firmware a přiřazení správnému zařízení a místnosti.
4. Ověřit TFT/blueprint, lokální tlačítka, zobrazení teploty a místní světlo.
5. Prověřit chování po restartu panelu, HA a sítě.
6. Nefunkční plánovanou termostatickou kartu nepovažovat za poruchu produkční regulace; topení zatím HA neřídí.

## Bezpečná změna ESPHome, blueprintu a TFT

1. Ověřit HA full backup a bezpečně uložený aktuální ESPHome YAML bez secrets.
2. Zaznamenat identitu panelu, místnost, běžící firmware, blueprint a TFT.
3. Ověřit, že konfigurace používá pro zvolený Blackymas blueprint požadovaný Arduino framework; nepřenášet bez kontroly konfiguraci z jiné instance.
4. Aktualizovat a testovat vždy pouze jeden panel s fyzickým přístupem.
5. Zachovat OTA i servisní fallback přístup a znát postup kabelového znovunahrání firmware.
6. Po změně otestovat boot, API, displej, tlačítka, místní světlo, teplotu a návrat po výpadku sítě.
7. Další panely aktualizovat až po stabilním ověření prvního kusu.

Do GitHubu se neukládají Wi-Fi hesla, API/OTA klíče ani jiné secrets. Produkční YAML musí mít bezpečnou obnovovací kopii mimo jedinou flash paměť panelu.

## Topení – doložený fyzický stav

| Oblast | Poslední doložený stav |
|---|---|
| Zdroj tepla | elektrický kotel Protherm 12 kW |
| Soustava | vodní podlahové topení |
| Rozdělovač | jeden rozdělovač, přibližně osm okruhů |
| Pohony | nejsou osazené |
| Řízení Home Assistantem | HA zatím neřídí žádnou část topení |
| Kabeláž místností | hluboká krabice; UTP a CYKY 5×1,5 vedené do hlavního rozvaděče vedle rozdělovače |
| Podlahová čidla | nový kabel ani čidlo už nelze dostat do podlahy |
| Zdroje pokojové teploty | nejsou definitivně určené a ověřené |

Kabelová příprava, namontovaný panel, osazený pohon a skutečně fungující řízení topného okruhu jsou čtyři různé stavy. Dokud nejsou pohony osazené a řízení otestované, regulace topení je pouze plán.

## Požadavky před realizací regulace

- zmapovat místnosti na jednotlivé okruhy rozdělovače;
- určit spolehlivý zdroj pokojové teploty pro každou zónu bez nového podlahového čidla;
- vybrat typ, napájení, klidový stav a zapojení pohonů a akčních členů;
- určit vazbu mezi NSPanelem, Home Assistantem, kotlem a fyzickým výstupem;
- navrhnout ruční režim a jednoznačný návrat do automatiky;
- určit bezpečný stav při výpadku HA, panelu, sítě, napájení nebo teplotního čidla;
- vyřešit minimální dobu sepnutí, případné souběhy zón a ochranu zdroje tepla;
- připravit elektrické schéma, jištění a přejímací test; práci na síťovém napětí provede kvalifikovaná osoba.

Bez těchto bodů se nepřipojují pohony a nevytváří produkční automatizace topení.

## Diagnostika

| Projev | První kontrola | Bezpečný další krok |
|---|---|---|
| NSPanel Pro se nespustí | napájení, boot a síť | ověřit fyzicky panel; neměnit HA nebo Zigbee |
| NSPanel Pro běží, ale neotevře HA | síť, adresa HA, aplikace/kiosk a autentizace | ověřit HA z jiného klienta a následně panel |
| Běžný NSPanel je offline | napájení, Wi-Fi, ESPHome API a firmware | ověřit lokálně; další OTA pokus až po určení stavu |
| Displej a API fungují, tlačítko neovládá světlo | blueprint, entita nebo automatizace | zachovat fyzicky bezpečný stav a ověřit mapování entity |
| Po TFT update je panel nestabilní | kompatibilita TFT, blueprintu a firmware | vrátit známou kombinaci; neaktualizovat další panely |
| Teplota je chybná nebo chybí | zdroj senzoru, kalibrace nebo komunikace | nepoužít hodnotu pro řízení topení, dokud není ověřena |
| Topení nereaguje na HA | v současném stavu očekávané | HA zatím topení neřídí; nezasahovat do kotle ani rozdělovače jako do hotové integrace |

## Rollback a obnova panelu

Při chybě po změně zastavit rozšiřování na další panely. Vrátit známý YAML, blueprint/TFT kombinaci nebo firmware podle připraveného postupu. Pokud OTA není dostupné, použít místní kabelový přístup; nevytvářet dočasnou veřejnou správu.

Po obnově otestovat identitu panelu, místnost, API, displej, tlačítka, místní světlo, teplotu a chování po restartu. Obnovený panel se nesmí přihlásit pod identitou jiného panelu.

## Handover minimum

Před samostatnou správou musí být známé:

- přesný model, umístění, napájení, síťová identita a stav každého panelu;
- aktuální ESPHome YAML, framework, blueprint a TFT verze;
- bezpečné umístění secrets a obnovovacích podkladů;
- způsob OTA, fallback a kabelového flashování;
- mapování místních světel a skutečných teplotních zdrojů;
- fyzická mapa topných okruhů, elektrické schéma a fail-safe před jakýmkoli nasazením regulace.

## Otevřené úkoly

> Následující body **vyžadují ověření v živém systému**.

- [ ] Ověřit model, umístění, napájení, síťovou identitu a stav konfigurace každého ze tří běžných NSPanelů.
- [ ] Ověřit a zdokumentovat běžící verze ESPHome, Blackymas blueprintu a TFT a bezpečné umístění obnovovacích YAML.
- [ ] Dokončit a prakticky otestovat místní dashboard každého skutečně nasazeného panelu bez rozšiřování na centrální dashboard domu.
- [ ] Zmapovat místnosti na jednotlivé okruhy rozdělovače.
- [ ] Vybrat a ověřit zdroj pokojové teploty pro každou plánovanou zónu.
- [ ] Navrhnout pohony, akční členy, elektrické schéma, ruční režim a fail-safe před zahájením řízení topení.

## Související dokumentace

- [Home Assistant – Honza](README.md)
- [Zigbee a osvětlení](Zigbee-a-osvetleni.md)
- [Zálohy Home Assistantu](../../MadMike/Zalohy/Home-Assistant.md)
