# Home Assistant – Honza

> Poslední uživatelem potvrzený stav: **2026-08-02**. Nejde o živou kontrolu systému; verze, úplný inventář a jednotlivá konfigurační nastavení vyžadují ověření.

## Účel a hranice

Místní Home Assistant zajišťuje automatizaci domácnosti u Honzy. Hlavními oblastmi jsou Zigbee osvětlení, fyzické ovládání světel, lokální panely, Energy dashboard a budoucí řízení podlahového topení.

Zálohy, síťové propojení, monitoring a společné zásady přístupů mají vlastní autoritativní dokumenty. V tomto projektu jsou uvedené pouze vazby potřebné pro provoz a aplikační přejímku této instance.

## Doložený stav

| Oblast | Doložený stav |
|---|---|
| Zařízení | Home Assistant Green |
| Systém | Home Assistant OS |
| Název instance | `honza` |
| IP adresa | `192.168.10.22` |
| Verze Core, OS a Supervisor | **Vyžaduje ověření v živém systému.** |
| Vzdálený přístup | Site-to-site WireGuard HOME ↔ Honza funguje |
| Monitoring dostupnosti | Uptime Kuma HA Honza zatím nehlídá |

## Používané integrace a služby

| Vrstva | Doložený stav |
|---|---|
| Zigbee2MQTT | používá se se síťovým koordinátorem SMLIGHT SLZB-06P10 |
| Mosquitto | používá se jako MQTT broker |
| Tasmota | používá se přes MQTT |
| Energy dashboard | používá se |
| HACS | používá se |
| Studio Code Server | používá se |
| InfluxDB, Grafana a Thread | nejsou doložené jako nasazené |

Podrobnosti zařízení, osvětlení a panelů jsou v dokumentech [Zigbee a osvětlení](Zigbee-a-osvetleni.md) a [NSPanel a topení](NSPanel-a-topeni.md).

## Provozní zásady a dopad výpadku

- Fyzické ovládání základních funkcí musí zůstat srozumitelné a použitelné.
- Automatizace nesmí bez vědomého návrhu vytvořit stav, ve kterém běžný uživatel nedokáže světlo nebo topení ovládat ručně.
- U důležitých funkcí se před nasazením určí chování při výpadku HA, MQTT, Zigbee2MQTT, koordinátoru, sítě nebo panelu.
- Po návratu služby se systém musí vrátit do jednoznačného a předvídatelného režimu.
- Výpadek HA nemá být důvodem k náhodné změně routeru, MQTT nebo Zigbee konfigurace.
- Hesla, tokeny, Zigbee network key ani jiné tajné hodnoty se do repozitáře nezapisují.

## První provozní kontrola

1. Z místní LAN ověřit webové rozhraní na poslední potvrzené IP `192.168.10.22`; konkrétní schéma a port: **Vyžaduje ověření v živém systému.** Vzdáleně nejprve ověřit WireGuard a teprve potom HA.
2. V **Settings → System** zkontrolovat stav systému, opravy, storage a dostupné logy.
3. Zaznamenat verze Core, Supervisor a OS bez provádění aktualizace.
4. V add-onech ověřit běh Mosquitto, Zigbee2MQTT a Studio Code Serveru.
5. V integracích ověřit MQTT, Zigbee zařízení, Tasmotu a počet nefunkčních entit.
6. Ověřit Energy dashboard a načtení očekávaných dat.
7. Prakticky otestovat alespoň jedno světlo, místní fyzické ovládání a NSPanel Pro; nedokončené topení se netestuje jako produkční funkce.
8. Ověřit poslední použitelný full backup a kopii mimo HA Green podle [centrálního zálohovacího dokumentu](../../MadMike/Zalohy/Home-Assistant.md).

## Bezpečný restart a změna

Při dostupném rozhraní použít standardní restart Home Assistantu nebo hostitele z **Settings → System**. Tvrdé odpojení napájení se nepoužívá jako první diagnostický krok.

Před aktualizací nebo rizikovou změnou:

1. vytvořit označený full backup a ověřit jeho kopii mimo HA Green;
2. zaznamenat aktuální verze a funkční přejímací body;
3. měnit po jedné vrstvě – Core, OS, add-on, HACS komponenta nebo zařízení;
4. před aktualizací HACS, Zigbee2MQTT, ESPHome nebo blueprintu ověřit změny a kompatibilitu;
5. po každém kroku provést provozní kontrolu, zejména MQTT, Zigbee, světla, panely a Energy dashboard;
6. předchozí použitelný backup nemažte, dokud není nový stav stabilní.

## Diagnostika

| Projev | První rozlišení | Bezpečný další krok |
|---|---|---|
| HA nejde místně ani vzdáleně | HA Green, napájení, boot nebo LAN | ověřit napájení, link a místní adresu; neměnit WireGuard jako první |
| HA jde místně, z HOME ne | WireGuard, route nebo firewall | pokračovat v [WireGuard runbooku](../../MadMike/Servery/WireGuard.md#diagnostika) |
| Web funguje, MQTT zařízení ne | Mosquitto, MQTT integrace nebo klienti | ověřit add-on, integraci a logy; neměnit přihlašovací údaje naslepo |
| Zigbee zařízení jsou nedostupná | Zigbee2MQTT, MQTT, koordinátor nebo Ethernet | pokračovat v [Zigbee diagnostice](Zigbee-a-osvetleni.md#diagnostika) |
| Jeden panel je nedostupný | napájení, Wi-Fi/LAN, ESPHome nebo aplikace | pokračovat v [NSPanel diagnostice](NSPanel-a-topeni.md#diagnostika) |
| Energy dashboard nemá data | zdrojová integrace, entity nebo statistiky | určit první chybějící zdroj; nemažte statistiky jako první krok |
| Po aktualizaci chybí funkce | změněná komponenta nebo kompatibilita | zastavit další aktualizace, zkontrolovat logy a použít připravený rollback |
| Storage je plné | backupy, databáze, logy nebo add-on data | nejprve určit obsah; nemažte poslední použitelný backup |

## Obnova a aplikační přejímka

Kompletní restore se provádí podle [Runbooku praktické obnovy Home Assistantu](../../MadMike/Zalohy/Home-Assistant.md#runbook-praktické-obnovy). Obnovovaná kopie musí být do rozhodnutí o produkčním nasazení izolovaná od původní instance, aby nevznikla duplicitní IP, hostname, koordinátor nebo automatizace.

Minimální přejímka HA Honza:

- správná identita instance a síťová dostupnost;
- běh Supervisoru a doložených add-onů;
- MQTT a Zigbee2MQTT včetně spojení se SLZB-06P10;
- známá světla, fyzické ovládání a pohybové čidlo v rozsahu skutečně dokončené konfigurace;
- NSPanel Pro a produkčně nasazené běžné NSPanely;
- Energy dashboard;
- nový full backup a kopie mimo obnovený hardware.

## Handover minimum

Přebírající správce musí znát:

- fyzické umístění HA Green, napájení a místní možnost zásahu;
- aktuální verze a síťovou identitu;
- bezpečně uložené správcovské a recovery podklady bez jejich kopírování do dokumentace;
- poslední použitelný full backup, druhou kopii a výsledek restore testu;
- externí závislosti: Mosquitto, Zigbee2MQTT, SLZB-06P10, Tasmota a WireGuard;
- které automatizace jsou produkční a které jsou pouze plánem;
- očekávané ruční chování světel a budoucího topení při výpadku HA.

## Otevřené kontroly

> Následující body **vyžadují ověření v živém systému**.

- [ ] Ověřit a doplnit aktuální verze Home Assistant Core, OS a Supervisor a datum poslední bezpečné aktualizace.
- [ ] Ověřit fyzické umístění, napájení a možnost místního zásahu u HA Green.
- [ ] Provést aplikační inventuru podle první provozní kontroly a zaznamenat pouze odchylky od doloženého stavu.

## Související dokumentace

- [Společná strategie záloh Home Assistantu](../../MadMike/Zalohy/Home-Assistant.md)
- [Síť lokality Honza](../Sit/README.md)
- [WireGuard](../../MadMike/Servery/WireGuard.md)
- [Centrální monitoring](../../MadMike/Monitoring/README.md)
- [Přístupy](../../MadMike/Pristupy/README.md)
