# Zigbee a osvětlení

> Poslední uživatelem potvrzený stav: **2026-08-02**. Nejde o živý export Zigbee2MQTT ani Home Assistantu.

## Architektura

```text
Zigbee zařízení
  ↕
SMLIGHT SLZB-06P10 (Ethernet)
  ↕
Zigbee2MQTT ↔ Mosquitto ↔ Home Assistant
```

NSPanel Pro není koordinátor ani router této Zigbee sítě. Do dokumentace nepatří Zigbee network key, MQTT heslo, coordinator backup ani jiné tajné hodnoty.

## Významná zařízení

| Zařízení / skupina | Poslední doložený stav |
|---|---|
| Aqara Ceiling Light T1M | dva kusy jsou integrované |
| Eglo Connect Z | světla jsou integrovaná; přesný počet, modely a umístění nejsou zdokumentované |
| Pohybové čidlo na chodbě | je integrované |
| Sonoff relé na chodbě | fyzická montáž a integrace nejsou potvrzené |
| Skupiny světel | přesná současná konfigurace není ověřená |

Chytrá Zigbee světla nemají být při běžném používání tvrdě odpojována od napájení klasickým vypínačem.

## Běžná provozní kontrola

1. Ověřit běh Mosquitto a Zigbee2MQTT v Home Assistantu.
2. V Zigbee2MQTT ověřit spojení s koordinátorem, jeho adresu bez zapisování citlivých hodnot a čas posledního přijatého stavu.
3. Zkontrolovat nedostupná zařízení, LQI a opakované chyby v logu; samotná nízká okamžitá hodnota LQI není důvodem k náhodnému přepárování.
4. Prakticky otestovat jedno světlo z HA a jeho fyzické ovládání.
5. U automatizované funkce ověřit spouštěč, podmínky, akce, ruční zásah a návrat do běžného režimu.
6. Po zásahu ověřit, že zařízení znovu hlásí stav a nevznikly duplicitní entity.

## Bezpečné párování zařízení

1. Před zásahem ověřit použitelný HA full backup a bezpečnou kopii Zigbee2MQTT databáze, konfigurace a coordinator backupu mimo GitHub.
2. Určit přesný model, místnost, napájení a požadovanou roli zařízení.
3. Povolit párování pouze na nezbytnou dobu a párovat po jednom zařízení.
4. Po úspěchu zařízení jednoznačně pojmenovat, přiřadit do místnosti a vypnout permit join.
5. Ověřit ovládání, reporting stavu a fyzické chování při výpadku HA/MQTT.
6. Teprve potom zařízení zapojit do skupiny nebo automatizace.

Existující zařízení se nemaže a nepáruje znovu jen proto, že dočasně neodpovídá. Nejprve se ověří napájení, dosah, Zigbee2MQTT, MQTT a koordinátor.

## Chodba – schválená koncepce a přejímka

Schválená koncepce propojuje pohybové čidlo, chytré světlo, případné relé pod vypínačem a Home Assistant tak, aby zůstalo zachované běžné fyzické ovládání.

Pohybové čidlo je integrované, ale automatizace čidlo → světla není dokončená. Stav Sonoff relé není potvrzený, proto se nepovažuje za namontované ani funkční.

Před implementací jednoznačně určit:

- která světla automatizace ovládá;
- skutečný typ, zapojení a bezpečnost relé;
- jak se chová ruční vypínač a zda neodpojuje napájení chytrému světlu;
- kdy se světla rozsvítí a zhasnou;
- jak ruční zásah dočasně přebije automatiku a jak se automatika obnoví;
- chování při výpadku HA, MQTT, Zigbee2MQTT, koordinátoru nebo čidla;
- výchozí stav po obnovení napájení a služeb.

Přejímka je hotová až po praktickém testu pohybu, běžného odchodu, ručního vypínače, restartu HA/MQTT a návratu služby. Elektrické zapojení síťového napětí provádí kvalifikovaná osoba.

## Aktualizace a změna koordinátoru

- Zigbee2MQTT, firmware koordinátoru a Home Assistant se neaktualizují současně.
- Před aktualizací se ověří kompatibilita adaptéru a Zigbee2MQTT, backup koordinátoru a návratová verze.
- Změna kanálu nebo koordinátoru je zásah do celé sítě; neprovádí se jako první pokus při problému jednoho zařízení.
- Po změně se kontrolují routery i bateriová zařízení v časovém odstupu, ne pouze bezprostředně po startu.

## Diagnostika

| Projev | První kontrola | Bezpečný další krok |
|---|---|---|
| Všechna Zigbee zařízení jsou nedostupná | Zigbee2MQTT, Mosquitto, SLZB-06P10 a Ethernet | ověřit vrstvy v tomto pořadí; nemažte síť ani zařízení |
| Zigbee2MQTT nevidí koordinátor | napájení, Ethernet, IP/hostname a kompatibilita | ověřit dostupnost adaptéru a log; neměnit firmware naslepo |
| Jedno zařízení je nedostupné | napájení, dosah, routery sítě nebo samotné zařízení | ověřit okolní zařízení a historii; přepárování až jako řízený krok |
| Ovládání funguje, stav se nevrací | reporting, binding, MQTT nebo entita | porovnat Zigbee2MQTT stav a HA entitu |
| Světla reagují jednotlivě a nesynchronně | způsob skupiny a počet příkazů | ověřit, zda je použita HA Light Group nebo Zigbee group podle záměru |
| Automatizace přepisuje ruční zásah | logika triggerů, časovač a režim automatizace | automatizaci dočasně vypnout, zachovat fyzické ovládání a opravit logiku |
| Problém vznikl po aktualizaci | kompatibilita Zigbee2MQTT/adaptéru | zastavit další změny a vrátit připravenou verzi nebo backup |

## Handover minimum

Před samostatnou správou musí být známé:

- fyzické umístění, napájení a síťová adresa SLZB-06P10;
- verze Zigbee2MQTT a firmware koordinátoru;
- bezpečné umístění Zigbee2MQTT databáze, network key a coordinator backupu;
- inventář významných zařízení s modely, místnostmi a typem napájení;
- které skupiny a automatizace jsou skutečně produkční;
- očekávané ruční a fail-safe chování světel.

## Otevřené úkoly

> Následující body **vyžadují ověření v živém systému**.

- [ ] Dokončit a prakticky otestovat automatizaci pohybového čidla a světel na chodbě včetně ručního režimu a návratu do automatiky.
- [ ] Ověřit fyzickou montáž, přesný typ, elektrické zapojení, umístění a funkci Sonoff relé.
- [ ] Doplnit inventuru významných Zigbee zařízení, jejich modely, umístění, napájení a případné skupiny.
- [ ] Ověřit verzi Zigbee2MQTT, firmware a síťové umístění SLZB-06P10 a existenci použitelných obnovovacích podkladů.
- [ ] Prakticky prověřit chování osvětlení při výpadku Home Assistantu, MQTT, Zigbee2MQTT a koordinátoru.

## Související dokumentace

- [Home Assistant – Honza](README.md)
- [NSPanel a topení](NSPanel-a-topeni.md)
- [Zálohy Home Assistantu](../../MadMike/Zalohy/Home-Assistant.md)

