# Služby a integrace

## Aktuální služby

| Služba nebo integrace | Poslední doložený stav | Role |
|---|---|---|
| Home Assistant | v provozu | automatizace a integrační vrstva |
| InfluxDB | v provozu | dlouhodobá časová data |
| Grafana | v provozu | vizualizace a analýza dat |
| Solarman | v provozu | data a řízení Deye zařízení |
| HACS | aktivní | doplňkové integrace |
| Honeywell Total Connect Comfort | aktivní | termostaty a topné zóny |
| Shelly | aktivní | lokální měření a spínání |
| MQTT | aktivní | komunikační vrstva |
| Tasmota | aktivní | lokální zařízení přes MQTT |
| Spotové ceny energií ČR | aktivní | vstup do energetických automatizací |
| Studio Code Server | aktivní | správa konfigurace |

Tabulka slučuje poslední souhrnný checkpoint s později potvrzeným provozem Home Assistantu, InfluxDB, Grafany a Solarmanu. Při další živé inventuře se má potvrdit, které doplňkové integrace jsou stále aktivně používané.

U Deye zařízení jsou historicky evidované přibližně dvě stovky entit na zařízení. Přesný počet není provozně důležitý; dokumentují se pouze entity použité v automatizacích nebo diagnostice.

## Síťový a IoT kontext

- IP adresy se přidělují přes DHCP se statickými leases.
- Vedle běžné Wi-Fi je evidovaná samostatná IoT síť `IOTVL` s vlastním rozsahem.
- Zigbee byl v posledním souhrnném checkpointu pouze plánovaný; nemá se označovat jako aktivní bez živého ověření.
- Obecná inventura MikroTiků zůstává v [MadMike / Síť / MikroTik](../../MadMike/Sit/MikroTik.md).

## Principy řízení a dat

- Home Assistant řídí nadřazenou logiku, ale základní ochrany a bezpečné limity zůstávají v měničích a koncových zařízeních.
- Pro důležité řízení se preferuje místní komunikace před závislostí na cloudu.
- Historická data mají sloužit k vyhodnocování výsledků řízení, ne jen k vytváření grafů.
- Ruční zásah má prioritu a musí existovat jednoznačný návrat do automatického režimu.
- Výkonové spotřebiče musí mít bezpečný stav při ztrátě dat, integrace nebo Home Assistantu.
- Automatizace musí být pojmenované, dohledatelné a pochopitelné i s časovým odstupem.
- Jednoduché a udržovatelné řešení má přednost před maximální teoretickou optimalizací.

## Otevřené úkoly

- [ ] Zapsat skutečné umístění a způsob provozu InfluxDB a Grafany.
- [ ] Ověřit jejich retenci, velikost databází a zálohování.
- [ ] Ověřit živý seznam doplňkových integrací a vyřadit již nepoužívané položky.
- [ ] Ověřit, zda je `IOTVL` stále samostatná aktivní síť a jaký používá rozsah.
- [ ] Po přechodu na RS485 porovnat stabilitu a možnosti řízení se současnou integrací.
- [ ] Zdokumentovat pouze entity skutečně důležité pro automatizace a diagnostiku.
