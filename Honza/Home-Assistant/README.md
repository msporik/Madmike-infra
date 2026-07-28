# Home Assistant – Honza

## Role

Místní Home Assistant zajišťuje automatizaci domácnosti u Honzy. Hlavními oblastmi jsou Zigbee osvětlení, fyzické ovládání světel, lokální panely a budoucí řízení podlahového topení.

## Ověřený stav k 2026-07-28

- zařízení: Home Assistant Green;
- systém: Home Assistant OS;
- název instance: `honza`;
- IP adresa: `192.168.10.22`;
- Zigbee: Zigbee2MQTT se síťovým koordinátorem SMLIGHT SLZB-06P10;
- potvrzená zařízení zahrnují Aqara světla a NSPanel Pro 120;
- vzdálená správa lokality funguje přes site-to-site WireGuard.

## Témata projektu

- [Zigbee a osvětlení](Zigbee-a-osvetleni.md)
- [NSPanel a topení](NSPanel-a-topeni.md)

## Otevřené kontroly

1. Ověřit aktuální verzi Home Assistantu a seznam aktivních integrací.
2. Zjistit skutečný stav automatických záloh a jejich druhé kopie mimo HA Green.
3. Provést a zdokumentovat praktický test obnovy.
4. Doplnit přesnou inventuru zařízení až podle živého stavu.

## Související dokumentace

- [Společná strategie záloh Home Assistantu](../../MadMike/Zalohy/Home-Assistant.md)
- [Síť lokality Honza](../Sit/README.md)
- [Centrální monitoring](../../MadMike/Monitoring/README.md)
