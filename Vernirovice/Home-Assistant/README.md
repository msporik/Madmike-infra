# Home Assistant – Vernířovice

## Účel a provozní role

Home Assistant je lokální integrační a nadřazená řídicí vrstva pro technologie ve Vernířovicích. Zajišťuje zejména sběr dat, vizualizaci, historii, cenové vstupy a energetické automatizace. Rychlé ochrany, pevné výkonové limity a bezpečné chování měničů a baterií nesmějí být závislé pouze na Home Assistantu.

Dokumentace je určená pro převzetí správy jiným zkušeným administrátorem. Úplná živá konfigurace, databáze, tajné hodnoty a dynamický seznam entit zůstávají v Home Assistantu a v určených bezpečných úložištích.

## Rychlá orientace

| Oblast | Poslední doložený stav | Autoritativní dokument |
|---|---|---|
| produkční hostitel | Raspberry Pi 5, Home Assistant OS | [Hardware a migrace](Hardware-a-migrace.md) |
| cílový hostitel | připravený Qotom N100; migrace neprovedena | [Hardware a migrace](Hardware-a-migrace.md) |
| lokální služby | InfluxDB, Grafana a MQTT jako add-ony stejné HA OS instalace | [Služby a integrace](Sluzby-a-integrace.md) |
| komunikace s Deye | Solarman; funkční lokální RS485/Modbus není doložený | [Služby a integrace](Sluzby-a-integrace.md) |
| energetická automatizace | dvě nejdražší hodiny, pouze původní sestava | [Řízení energie](../BESS-a-FVE/Rizeni-energie.md) |
| vzdálený přístup | Home Assistant Cloud potvrzen 21. 7. 2026; současná cesta nebyla živě ověřena | [Služby a integrace](Sluzby-a-integrace.md) |
| zálohy a obnova | společná strategie existuje; realizace a restore této instance nejsou doložené | [Zálohy Home Assistantu](../../MadMike/Zalohy/Home-Assistant.md) |
| monitoring | má být součástí společného monitoringu a notifikací | [MadMike / Monitoring](../../MadMike/Monitoring/README.md) |

> Uvedený stav byl konsolidován z dokumentace a podkladů při auditu 2. 8. 2026. Nebyl při něm ověřen přímým přístupem do živé instance. Každá položka označená jako poslední doložený stav vyžaduje před rizikovou změnou read-only kontrolu.

## Poslední doložený provozní stav

- Produkční Home Assistant běží na Raspberry Pi 5 jako Home Assistant OS.
- InfluxDB, Grafana a MQTT broker běží jako add-ony stejné instalace.
- Home Assistant získává data z Deye zařízení přes integraci Solarman.
- Žádná lokální RS485/Modbus komunikace není doložená jako funkční.
- Automatizace vybíjení původní baterie během dvou nejdražších hodin je v provozu.
- Větší bateriová sestava je v Home Assistantu viditelná, ale není plně zprovozněná; přítomnost entit není důkazem provozní funkčnosti.
- Home Assistant Cloud byl pro tuto instanci potvrzen 21. 7. 2026.

## Schválený cílový stav

- Přesunout Home Assistant z Raspberry Pi 5 na připravený Qotom N100.
- Na Qotomu provozovat Home Assistant OS přímo na hardware.
- Zachovat Raspberry Pi 5 jako dočasnou návratovou variantu, dokud nebude migrace prakticky ověřena a výslovně uzavřena.
- Zavádět lokální RS485/Modbus jako samostatnou změnu až po stabilizaci nové platformy, nejprve pouze pro čtení.
- Preferovat jednoduché, lokální, předvídatelné a servisovatelné řešení.

## Závislosti a hranice projektu

- Měniče, baterie, měření, exportní limit, bezpečnostní limity a algoritmus energetického řízení jsou autoritativně vedené v [BESS a FVE](../BESS-a-FVE/README.md).
- Společná strategie záloh, retence, druhé kopie a restore testy jsou v [Zálohách Home Assistantu](../../MadMike/Zalohy/Home-Assistant.md).
- Síťová topologie, DHCP, VLAN a adresní plán patří do [MadMike / Síť](../../MadMike/Sit/README.md).
- Centrální dohled a notifikace patří do [MadMike / Monitoring](../../MadMike/Monitoring/README.md).
- Účty, MFA a recovery patří do [MadMike / Přístupy](../../MadMike/Pristupy/README.md).
- Úplné konfigurace, tajné hodnoty a dynamická data zůstávají v živých systémech nebo bezpečném úložišti.

## Bezpečnostní zásady správy

- Neprovádět dvě významné změny současně. Migrace hostitele a změna komunikace na RS485/Modbus jsou dvě oddělené akce.
- Nikdy nespouštět dvě instance se stejnými automatizacemi a přístupem ke stejným fyzickým zařízením.
- Novou integraci nebo komunikační cestu nejdřív ověřit pouze pro čtení.
- Před povolením zápisu uložit původní stav, určit přejímací kritéria a připravit návrat.
- Ruční zásah má prioritu; automatizace musí mít jednoznačný návrat do automatického režimu.
- Po restartu nebo výpadku nesmí automatizace slepě obnovit předchozí výkonový stav bez načtení skutečného stavu zařízení.
- Hesla, tokeny, MQTT přihlašovací údaje, recovery kódy ani neupravené diagnostické exporty neukládat do repozitáře.

## První postup při převzetí správy

1. Přečíst tento dokument, [Hardware a migraci](Hardware-a-migrace.md), [Služby a integrace](Sluzby-a-integrace.md) a přehled [BESS a FVE](../BESS-a-FVE/README.md).
2. Bez změn ověřit, který hostitel je produkční a že Qotom není paralelně aktivní vůči stejným zařízením.
3. Ověřit dostupnost Home Assistantu, stav Supervisoru a zdraví hostitele.
4. Ověřit běh InfluxDB, Grafany a MQTT a stáří posledních dat.
5. Ověřit aktuálnost dat Solarman a stav energetické automatizace bez jejího spuštění.
6. Ověřit datum poslední zálohy a existenci oddělené kopie; praktickou obnovu nespouštět bez samostatného plánu.
7. Ověřit současnou cestu lokálního a vzdáleného přístupu a dohled dostupnosti.
8. Nejasnosti zapsat do příslušného autoritativního dokumentu, nikoli do nového paralelního seznamu.

## Běžná provozní kontrola

Při pravidelné kontrole nebo před změnou ověřit:

- hostitel, Home Assistant Core, Supervisor a OS nevykazují chybu;
- volné místo a zatížení hostitele nejsou kritické;
- InfluxDB, Grafana a MQTT běží a jejich data se aktualizují;
- klíčová data Solarman nejsou `unknown`, `unavailable` ani zjevně zastaralá;
- automatizace nezůstala v neočekávaném režimu;
- poslední záloha je přiměřeně aktuální;
- monitoring nezobrazuje výpadek a notifikace nemají nevyřešenou chybu.

Přesné prahy, verze a očekávané intervaly aktualizace nejsou autoritativně doložené. **Vyžaduje ověření v živém systému.**

## Postup při incidentu

1. Určit dopad: nedostupnost rozhraní, výpadek add-onu, zastaralá data, neprovedená automatizace nebo nechtěná fyzická akce.
2. Pokud hrozí nežádoucí řízení, přejít na bezpečný lokální nebo ruční režim podle dokumentace konkrétní technologie; neimprovizovat zápisem registrů.
3. Zabránit souběhu dvou HA instancí nebo dvou zapisujících integračních cest.
4. Zaznamenat čas, poslední známý funkční stav a provedené zásahy.
5. Diagnostikovat od hostitele přes Home Assistant a add-ony až ke konkrétní integraci.
6. Obnovu ze zálohy použít až po vyloučení jednodušší závady a po určení dopadu na novější data.
7. Po nápravě ověřit přístup, služby, data, automatizace, ruční režim a monitoring.

Podrobné diagnostické postupy jsou v [Službách a integracích](Sluzby-a-integrace.md); obnova a migrace v [Hardwaru a migraci](Hardware-a-migrace.md).

## Dokumentace projektu

- [Hardware a migrace](Hardware-a-migrace.md) – hostitelé, příprava migrace, přejímka a rollback.
- [Služby a integrace](Sluzby-a-integrace.md) – add-ony, integrační vazby, provozní kontrola a diagnostika.
- [BESS a FVE](../BESS-a-FVE/README.md) – fyzická energetika a řízení energie.

Otevřené kroky jsou vedené jen v příslušných autoritativních dokumentech.
