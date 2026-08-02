# Home Assistant – Honza

## Účel a hranice

Místní Home Assistant zajišťuje automatizaci domácnosti u Honzy. Hlavními oblastmi jsou Zigbee osvětlení, fyzické ovládání světel, lokální panely a budoucí řízení podlahového topení.

Zálohy, síťové propojení, monitoring a společné zásady přístupů mají vlastní autoritativní dokumenty. V tomto projektu jsou uvedené pouze vazby potřebné pro pochopení místní instalace.

## Poslední doložený stav k 2026-08-02

Stav níže potvrdil uživatel. Nejde o živou kontrolu systému, proto přesné verze, úplný inventář a jednotlivá konfigurační nastavení zůstávají neověřené.

| Oblast | Doložený stav |
|---|---|
| Zařízení | Home Assistant Green |
| Systém | Home Assistant OS |
| Název instance | `honza` |
| IP adresa | `192.168.10.22` |
| Verze Core, OS a Supervisor | Neověřené |
| Vzdálený přístup | Site-to-site WireGuard HOME ↔ Honza funguje |
| Monitoring dostupnosti | Uptime Kuma HA Honza zatím nehlídá |

## Používané integrace a služby

| Vrstva | Doložený stav |
|---|---|
| Zigbee2MQTT | Používá se se síťovým koordinátorem SMLIGHT SLZB-06P10 |
| Mosquitto | Používá se jako MQTT broker |
| Tasmota | Používá se přes MQTT |
| Energy dashboard | Používá se |
| HACS | Používá se |
| Studio Code Server | Používá se |
| InfluxDB, Grafana a Thread | Nejsou doložené jako nasazené |

Podrobnosti zařízení, osvětlení a panelů jsou v tematických dokumentech:

- [Zigbee a osvětlení](Zigbee-a-osvetleni.md)
- [NSPanel a topení](NSPanel-a-topeni.md)

## Provozní zásady

- Fyzické ovládání základních funkcí má zůstat srozumitelné a použitelné.
- Automatizace nesmí bez vědomého návrhu vytvořit stav, ve kterém běžný uživatel nedokáže světlo nebo topení ovládat ručně.
- U důležitých automatizací se před nasazením určí chování při výpadku HA, MQTT, Zigbee2MQTT, koordinátoru nebo ovládacího panelu.
- Po návratu služby se systém musí vrátit do jednoznačného a předvídatelného režimu.
- Hesla, tokeny, Zigbee network key ani jiné tajné hodnoty se do repozitáře nezapisují.

## Otevřené kontroly

- [ ] Ověřit a doplnit aktuální verze Home Assistant Core, OS a Supervisor.

## Související dokumentace

- [Společná strategie záloh Home Assistantu](../../MadMike/Zalohy/Home-Assistant.md)
- [Síť lokality Honza](../Sit/README.md)
- [WireGuard](../../MadMike/Servery/WireGuard.md)
- [Centrální monitoring](../../MadMike/Monitoring/README.md)
- [Přístupy](../../MadMike/Pristupy/README.md)
