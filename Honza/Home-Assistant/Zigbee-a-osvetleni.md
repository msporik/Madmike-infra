# Zigbee a osvětlení

## Ověřený stav

- Home Assistant používá Zigbee2MQTT.
- Síťovým koordinátorem je SMLIGHT SLZB-06P10.
- V provozu jsou zařízení z oblasti Aqara osvětlení.
- Cílem je zachovat běžné fyzické ovládání světel i při použití automatizací.

Do dokumentace nepatří Zigbee network key ani jiné tajné hodnoty.

## Rozpracované oblasti

- běžné relé nebo moduly pod vypínači;
- pohybová automatizace na chodbě;
- případné zapojení zařízení Eglo Connect Z;
- přehledné rozdělení automatizací a ručního ovládání.

## Otevřené kontroly

- [ ] Vypsat skutečný seznam Zigbee zařízení a jejich umístění.
- [ ] Ověřit aktuální Zigbee kanál a provozní nastavení koordinátoru bez ukládání síťového klíče.
- [ ] Ověřit, která relé a pohybová čidla jsou fyzicky instalovaná.
- [ ] Prakticky prověřit chování světel při výpadku Home Assistantu, Zigbee2MQTT nebo koordinátoru.
