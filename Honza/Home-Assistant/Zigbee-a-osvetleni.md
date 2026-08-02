# Zigbee a osvětlení

## Poslední doložený stav k 2026-08-02

Stav potvrdil uživatel; nejde o živý export Zigbee2MQTT ani Home Assistantu.

Základní komunikační cesta je:

`Zigbee zařízení ↔ SMLIGHT SLZB-06P10 ↔ Zigbee2MQTT ↔ Mosquitto ↔ Home Assistant`

Koordinátor SMLIGHT SLZB-06P10 je připojený po Ethernetu. Do dokumentace nepatří Zigbee network key, MQTT heslo ani jiné tajné hodnoty.

## Významná zařízení

| Zařízení / skupina | Poslední doložený stav |
|---|---|
| Aqara Ceiling Light T1M | Dva kusy jsou integrované |
| Eglo Connect Z | Světla jsou integrovaná; přesný počet, modely a umístění nejsou zdokumentované |
| Pohybové čidlo na chodbě | Je integrované |
| Sonoff relé na chodbě | Fyzická montáž a integrace nejsou potvrzené |
| Skupiny světel | Přesná současná konfigurace není ověřená |

Chytrá Zigbee světla nemají být při běžném používání tvrdě odpojována od napájení klasickým vypínačem.

## Chodba

Schválená koncepce je propojit pohybové čidlo, chytré světlo, případné relé pod vypínačem a Home Assistant tak, aby zůstalo zachované běžné fyzické ovládání.

Pohybové čidlo je už integrované, ale automatizace čidlo → světla není dokončená. Stav Sonoff relé není potvrzený, proto se nepovažuje za namontované ani funkční.

Před dokončením se musí jednoznačně určit:

- která světla automatizace ovládá;
- jak se chová ruční vypínač;
- kdy se světla rozsvítí a zhasnou;
- jak se zabrání konfliktu ručního zásahu s automatizací;
- jaký stav zůstane při výpadku HA, MQTT, Zigbee2MQTT nebo koordinátoru;
- jak se automatizace vrátí do běžného režimu po obnovení služby.

## Otevřené úkoly

- [ ] Dokončit a prakticky otestovat automatizaci pohybového čidla a světel na chodbě.
- [ ] Ověřit fyzickou montáž, typ, umístění a funkci Sonoff relé.
- [ ] Doplnit přesnou inventuru významných Zigbee zařízení, jejich umístění a případné skupiny.
- [ ] Prakticky prověřit chování osvětlení při výpadku Home Assistantu, MQTT, Zigbee2MQTT a koordinátoru.

## Související dokumentace

- [Home Assistant – Honza](README.md)
- [NSPanel a topení](NSPanel-a-topeni.md)
