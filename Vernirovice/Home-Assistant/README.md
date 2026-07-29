# Home Assistant – Vernířovice

## Účel

Lokální řídicí a integrační vrstva pro FVE, baterie, energetické automatizace a další technologie ve Vernířovicích. Preferovaný směr je spolehlivé místní řízení s omezenou závislostí na cloudu.

## Aktuálně potvrzený stav

- Home Assistant stále běží na Raspberry Pi 5.
- InfluxDB i Grafana jsou v provozu.
- Home Assistant získává energetická data mimo jiné z Deye zařízení přes integraci Solarman.
- Automatizace vybíjení baterie během dvou nejdražších hodin funguje; její logika je popsána v [Řízení energie](../BESS-a-FVE/Rizeni-energie.md).

## Plán

- Přesunout Home Assistant z Raspberry Pi 5 na připravený Qotom N100.
- Využívat lokální RS485/Modbus tam, kde poskytne spolehlivější a lépe kontrolovatelnou komunikaci než cloudové rozhraní.
- Zachovat možnost bezpečného návratu na původní stav během migrace.

## Podrobnosti

- [Hardware a migrace](Hardware-a-migrace.md)
- [Služby a integrace](Sluzby-a-integrace.md)
- [BESS a FVE](../BESS-a-FVE/README.md)
- [Společná strategie záloh Home Assistantu](../../MadMike/Zalohy/Home-Assistant.md)

## Otevřené úkoly

- [ ] Ověřit současný způsob, umístění a retenci záloh této instance.
- [ ] Připravit konkrétní migrační a návratový postup pro Qotom.
- [ ] Ověřit, kde fyzicky běží InfluxDB a Grafana a jak jsou zálohovaná jejich data.
- [ ] Po migraci ověřit všechny klíčové integrace, automatizace a historická data.
