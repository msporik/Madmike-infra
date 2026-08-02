# Služby a integrace

## Účel

Tento dokument popisuje služby, add-ony a integrační vazby produkční instance Home Assistantu ve Vernířovicích. Technologie měničů, baterií, limity lokality a vlastní algoritmus energetického řízení jsou vedené autoritativně v projektu [BESS a FVE](../BESS-a-FVE/README.md).

## Poslední doložený provozní stav

> Stav byl konsolidován při auditu 2. 8. 2026. Živá konfigurace Home Assistantu nebyla při auditu otevřena; uvedené položky proto vycházejí z posledních doložených podkladů. Položky označené jako aktivní je nutné při další živé inventuře potvrdit.

Produkční instance běží na Raspberry Pi 5 jako Home Assistant OS. Ve stejné instalaci jsou doložené tyto add-ony:

- InfluxDB – ukládání dlouhodobějších časových dat;
- Grafana – vizualizace a analýza dat;
- MQTT broker – lokální komunikační služba;
- Studio Code Server – správa konfigurace.

## Doložené integrace

| Služba nebo integrace | Poslední doložený stav | Role |
|---|---|---|
| Home Assistant | v provozu | automatizace a integrační vrstva |
| InfluxDB | v provozu jako add-on HA OS | dlouhodobější časová data |
| Grafana | v provozu jako add-on HA OS | vizualizace a analýza dat |
| MQTT broker | v provozu jako add-on HA OS | komunikační vrstva |
| Solarman | v provozu | data z Deye zařízení a současná vazba energetických automatizací |
| HACS | dříve doloženo jako aktivní | doplňkové integrace |
| Honeywell Total Connect Comfort | dříve doloženo jako aktivní | termostaty a topné zóny |
| Shelly | dříve doloženo jako aktivní | lokální měření a spínání |
| Tasmota | dříve doloženo jako aktivní | lokální zařízení, zpravidla přes MQTT |
| Spotové ceny energií ČR | dříve doloženo jako aktivní | vstup do energetických automatizací |
| Studio Code Server | dříve doloženo jako aktivní add-on | správa konfigurace |

Home Assistant získává data z Deye zařízení přes integraci Solarman. Žádná lokální RS485/Modbus komunikace dnes není doložená jako funkční. Automatizace vybíjení původní bateriové sestavy během dvou nejdražších hodin je v provozu; její logika a bezpečnostní hranice jsou popsané v [Řízení energie](../BESS-a-FVE/Rizeni-energie.md).

Větší bateriová sestava byla přidaná také do Home Assistantu, ale její technologie není plně zprovozněná kvůli trvajícímu problému komunikace baterie–střídač. Přítomnost entit v Home Assistantu proto sama o sobě nepotvrzuje plnou provozní funkčnost této sestavy.

U Deye zařízení byly historicky evidované přibližně dvě stovky entit na zařízení. Přesný počet není provozně důležitý; dokumentovat se mají pouze entity použité v automatizacích, řízení nebo diagnostice.

Home Assistant Cloud byl pro tuto instanci potvrzen 21. 7. 2026. Přesná současná cesta lokálního a vzdáleného přístupu, interní a externí URL ani návaznost na centrální monitoring nebyly při auditu živě ověřené.

## Síťový a IoT kontext

- IP adresy byly naposledy evidované jako přidělované přes DHCP se statickými leases.
- Vedle běžné Wi-Fi byla evidovaná samostatná IoT síť `IOTVL` s vlastním rozsahem; její současný stav je nutné ověřit.
- Zigbee byl v posledním souhrnném checkpointu pouze plánovaný a nesmí se označovat jako aktivní bez živého ověření.
- Obecná inventura MikroTiků zůstává v [MadMike / Síť / MikroTik](../../MadMike/Sit/MikroTik.md).

## Zásady integrací a řízení

- Preferovat lokální komunikaci bez závislosti na cloudu tam, kde je prokazatelně spolehlivější a lépe kontrolovatelná.
- Nenahrazovat funkční Solarman lokálním RS485/Modbus rozhraním bez samostatné přípravy, testu a možnosti návratu.
- Oddělit čtení dat od aktivního řízení. Novou integraci nejprve ověřit v režimu bez fyzických zásahů.
- Home Assistant řídí nadřazenou logiku, ale základní ochrany a bezpečné limity musí zůstat v měničích a koncových zařízeních.
- Ruční zásah má prioritu a musí existovat jednoznačný návrat do automatického režimu.
- Výkonové spotřebiče musí mít bezpečný stav při ztrátě dat, integrace nebo Home Assistantu.
- Nedovolit současný aktivní provoz dvou instancí Home Assistantu se stejnými automatizacemi a zařízeními.
- Tokeny, hesla, MQTT přihlašovací údaje a jiné tajné hodnoty neukládat do repozitáře.
- Automatizace musí být pojmenované, dohledatelné a pochopitelné i s časovým odstupem.
- Jednoduché a udržovatelné řešení má přednost před maximální teoretickou optimalizací.
- Duplicitní upozornění mezi Home Assistantem, Uptime Kuma, Pulse, Mikr Managerem a nativními notifikacemi potlačit podle společné koncepce monitoringu.

## Migrace na Qotom

Při plánované migraci na Qotom musí být společně s Home Assistantem ověřené také InfluxDB, Grafana, MQTT a všechny významné integrační vazby. Podrobný postup, přejímací test a rollback jsou vedené v dokumentu [Hardware a migrace](Hardware-a-migrace.md).

Samotná migrace hostitele nemá automaticky měnit způsob komunikace s měniči. Zavedení RS485/Modbus je samostatná změna a má následovat až po ověření nové platformy.

## Otevřené úkoly

- [ ] Ověřit živý seznam aktivních integrací, add-onů a jejich aktuální verze.
- [ ] Ověřit konfiguraci, retenci, velikost databází a zálohování InfluxDB.
- [ ] Ověřit hlavní Grafana dashboardy, zdroje dat a jejich obnovitelnost.
- [ ] Ověřit účel, klienty, autentizaci a zálohování MQTT brokeru bez uložení tajných údajů do dokumentace.
- [ ] Ověřit přesný stav entit a ovládání původní i větší bateriové sestavy.
- [ ] Ověřit, zda je `IOTVL` stále samostatná aktivní síť a jaký používá rozsah.
- [ ] Ověřit současný způsob lokálního a vzdáleného přístupu včetně Home Assistant Cloud.
- [ ] Zapojit dostupnost instance do společného monitoringu a schváleného notifikačního systému.
- [ ] Před případným zavedením RS485/Modbus připravit samostatný read-only test, přejímací kritéria a rollback.
- [ ] Zdokumentovat pouze entity skutečně důležité pro automatizace, řízení a diagnostiku.
