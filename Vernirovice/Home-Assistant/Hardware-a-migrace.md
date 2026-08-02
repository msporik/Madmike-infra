# Hardware a migrace

## Současný produkční stav

- Produkční Home Assistant běží na Raspberry Pi 5 jako Home Assistant OS.
- InfluxDB, Grafana a MQTT broker běží jako add-ony stejné instalace.
- Migrace na Qotom zatím nebyla provedena.

## Připravený cílový hardware

| Součást | Stav | Potvrzený údaj |
|---|---|---|
| zařízení | zakoupeno, zkušebně nabootováno, odloženo k pozdějšímu nasazení | fanless Qotom s Intel N100 |
| operační paměť | potvrzeno | 16 GB DDR5 |
| systémový disk | potvrzeno | Micron NVMe 512 GB |
| cílový systém | schváleno | Home Assistant OS přímo na hardware |
| průmyslová komunikace | plán | budoucí lokální RS485/Modbus |

Qotom má převzít roli hlavního lokálního uzlu pro Home Assistant a energetické automatizace. Dnes není součástí produkční infrastruktury a čeká na nasazení.

## Současný stav komunikace

- Žádný RS485 převodník ani jiné lokální Modbus rozhraní dnes není funkční.
- Veškerá současná komunikace Home Assistantu s Deye zařízeními probíhá přes integraci Solarman.
- Zavedení RS485/Modbus není součástí samotné migrace hostitele, pokud nebude předem samostatně připravené a ověřené.

## Předpoklady migrace

Před zahájením migrace musí být splněno:

- vytvořit aktuální zálohu Home Assistantu a ověřit, že ji lze stáhnout;
- potvrdit datum a umístění použité zálohy;
- ověřit, zda záloha obsahuje potřebná data a konfiguraci add-onů InfluxDB, Grafana a MQTT;
- zaznamenat současný funkční stav klíčových integrací, automatizací, historie a přístupů;
- připravit Qotom s Home Assistant OS;
- zachovat Raspberry Pi 5 beze změn jako dočasnou návratovou variantu;
- určit okamžik a kritéria, při kterých se migrace ukončí návratem na Raspberry Pi.

## Doporučené pořadí migrace

1. Vytvořit a ověřit aktuální zálohu současné instance.
2. Připravit Home Assistant OS na Qotomu bez zásahu do Raspberry Pi 5.
3. Obnovit zálohu na Qotomu.
4. Zabránit současnému aktivnímu provozu dvou instancí se stejnými automatizacemi a zařízeními.
5. Nejprve read-only způsobem ověřit start systému, add-ony a integrace.
6. Ověřit historii, InfluxDB, Grafanu a MQTT.
7. Teprve poté povolit automatizace a řízení fyzických zařízení.
8. Provoz prakticky sledovat a migraci uzavřít až po splnění přejímacích testů.

## Přejímací test

Migrace je dokončená až po ověření:

- opakovaného korektního startu Qotomu a Home Assistantu;
- lokálního a vzdáleného přístupu;
- běhu InfluxDB, Grafany, MQTT a dalších významných add-onů;
- dostupnosti a správnosti hlavních integrací;
- komunikace přes Solarman;
- přítomnosti a správného stavu klíčových automatizací;
- dostupnosti historie a pokračujícího zápisu do InfluxDB;
- funkčnosti hlavních Grafana dashboardů;
- správného stavu ručního a automatického režimu;
- absence nechtěných fyzických akcí po obnově a restartu;
- dostupnosti instance ve společném monitoringu;
- vytvoření nové použitelné zálohy po migraci.

## Rollback

Při zásadní závadě nebo nesplnění přejímacích testů:

1. Qotom odstavit tak, aby nemohl paralelně řídit zařízení.
2. Vrátit původní síťovou identitu, pokud byla při migraci změněna.
3. Spustit zachované Raspberry Pi 5.
4. Ověřit lokální a vzdálený přístup, Solarman, add-ony, automatizace a historii.
5. Neprovádět zpětný import novější databáze nebo konfigurace bez samostatného rozhodnutí.
6. Zaznamenat důvod návratu a změny vzniklé během testovacího provozu.

Raspberry Pi 5 se nesmí smazat ani použít k jinému účelu, dokud nebude migrace na Qotom prakticky ověřená a výslovně uzavřená.

## Otevřené úkoly

- [ ] Ověřit verzi Home Assistant OS, Core a Supervisor na současném Raspberry Pi 5.
- [ ] Ověřit obsah zálohy a ochranu dat add-onů InfluxDB, Grafana a MQTT.
- [ ] Připravit Qotom s Home Assistant OS a ověřit jeho síťové a úložné parametry.
- [ ] Doplnit konkrétní předmigrační kontrolní seznam současných funkcí.
- [ ] Stanovit konkrétní časové a funkční kritérium pro rollback.
- [ ] Po úspěšné migraci provést a zdokumentovat přejímací test a praktický restore.
