# Zigbee

Domácí Zigbee síť připojená k Home Assistantu.

## Produkční stav

- **Koordinátor:** SMLIGHT SLZB-06P10.
- **Připojení:** Ethernet.
- **Adresa:** `192.168.89.56:6638`.
- **Řízení sítě:** Zigbee2MQTT.
- Přechod z původního USB koordinátoru je dokončený.
- Zigbee2MQTT na ethernetovém koordinátoru běží a domácí Zigbee je v produkčním provozu.

Původní USB koordinátor je vedený jen jako možná záloha. Jeho současná připravenost k obnově produkční Zigbee sítě nebyla ověřena.

## Matter a Thread

Matter/Thread je samostatná infrastruktura a nesmí se zaměňovat s produkčním Zigbee koordinátorem SLZB-06P10.

- Samostatné zařízení SMLIGHT určené pro Matter/Thread je pořízené, ale jeho přesný model a stav nasazení OTBR zatím nejsou potvrzené.
- Aqara Smart Lock je koupený, ale není nainstalovaný.

## Otevřené úkoly

- [ ] Zjistit přesný model druhého zařízení SMLIGHT/SLZB určeného pro Matter/Thread a ověřit jeho zamýšlenou roli a stav OTBR.
- [ ] Ověřit, zda je původní USB koordinátor skutečně použitelný jako nouzová záloha produkční Zigbee sítě.
