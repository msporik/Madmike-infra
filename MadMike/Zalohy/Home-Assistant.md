# Zálohy Home Assistantu

## Cíl

Zálohy Home Assistantu mají být součástí společného zálohovacího řetězce přes domácí infrastrukturu a offsite PBS, aby nezůstaly pouze na zařízení, na kterém daný Home Assistant běží.

## Aktuálně potvrzený stav

- Domácí Home Assistant je produkční a běží na samostatném zařízení s Home Assistant OS.
- Ve Vernířovicích běží Home Assistant na Raspberry Pi 5; přesun na Qotom N100 je plánovaný.
- U Honzy běží Home Assistant OS na Home Assistant Green.
- Existuje záměr vést zálohy HA přes PVE Ryzen a následně do offsite PBS.

Není zatím potvrzené, že je celý tento řetězec pro všechny HA instance skutečně dokončený a pravidelně ověřovaný.

## Úkoly k ověření a realizaci

1. Zjistit současný způsob a umístění záloh každé HA instance.
2. Ověřit automatické vytváření záloh a jejich retenci.
3. Zajistit druhou kopii mimo zařízení s Home Assistantem.
4. Ověřit přenos do offsite PBS nebo jiného rovnocenného DR cíle.
5. Provést praktický test obnovy alespoň domácího HA.
6. Dokumentovat rozdíly mezi domácí instancí a ostatními lokalitami až podle skutečného stavu.

## Související dokumentace

- Podrobnosti domácí instance jsou v projektu [MadMike / Home Assistant](../Home-Assistant/README.md).
- Podrobnosti instance ve Vernířovicích jsou v projektu [Vernířovice / Home Assistant](../../Vernirovice/Home-Assistant/README.md).
- Podrobnosti instance u Honzy jsou v projektu [Honza / Home Assistant](../../Honza/Home-Assistant/README.md).
