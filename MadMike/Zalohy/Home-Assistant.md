# Zálohy Home Assistantu

## Cíl

Zálohy Home Assistantu mají být součástí společného zálohovacího řetězce přes domácí infrastrukturu a offsite PBS, aby nezůstaly pouze na zařízení, na kterém daný Home Assistant běží.

## Aktuálně potvrzený stav

- Domácí Home Assistant je produkční a běží na samostatném zařízení s Home Assistant OS.
- Ve Vernířovicích běží Home Assistant na Raspberry Pi 5; přesun na Qotom N100 je plánovaný.
- U Honzy běží Home Assistant OS na Home Assistant Green.
- HA ValTom je připravený na Home Assistant Green, ale dosud není nainstalovaný u Tomáše; existuje připravený základní obraz / záloha, pravidelné produkční zálohování však není potvrzené.
- Existuje záměr vést zálohy HA přes PVE Ryzen a následně do offsite PBS.

Není zatím potvrzené, že je celý tento řetězec pro všechny HA instance skutečně dokončený a pravidelně ověřovaný.

## Úkoly k ověření a realizaci

- [ ] Zjistit současný způsob a umístění záloh každé HA instance.
- [ ] Ověřit automatické vytváření záloh a jejich retenci.
- [ ] Zajistit druhou kopii mimo zařízení s Home Assistantem.
- [ ] Ověřit přenos do offsite PBS nebo jiného rovnocenného DR cíle.
- [ ] Provést praktický test obnovy alespoň domácího HA.
- [ ] Dokumentovat rozdíly mezi domácí instancí a ostatními lokalitami až podle skutečného stavu.

## Související dokumentace

- Podrobnosti domácí instance jsou v projektu [MadMike / Home Assistant](../Home-Assistant/README.md).
- Podrobnosti instance ve Vernířovicích jsou v projektu [Vernířovice / Home Assistant](../../Vernirovice/Home-Assistant/README.md).
- Podrobnosti instance u Honzy jsou v projektu [Honza / Home Assistant](../../Honza/Home-Assistant/README.md).
- Podrobnosti připravované instance HA ValTom jsou v projektu [HA ValTom / Home Assistant](../../HA-ValTom/Home-Assistant/README.md).
