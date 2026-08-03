# Home Assistant

Domácí produkční instance Home Assistantu a její hlavní integrace.

## Účel a hranice

Home Assistant je integrační a automatizační vrstva domácnosti MadMike. Propojuje lokální technologie, poskytuje rodinné a technické přehledy a řídí vybrané automatizace.

Základní bezpečnost, vytápění, lokální zvonění a záznam kamer nesmějí být existenčně závislé na Home Assistantu. Tento projekt se netýká instancí ve Vernířovicích, u Honzy ani HA ValTom.

## Aktuální stav

| Oblast | Stav |
|---|---|
| Platforma | CWWK X86-P6 |
| Procesor | Intel N150 |
| Paměť | 8 GB RAM |
| Architektura | x86-64 |
| Úložiště | NVMe |
| Systém | Home Assistant OS |
| Role | hlavní domácí automatizace |
| Provoz | produkční a běžně používaná instance |

Migrace z HA Green je dokončená. Původní HA Green je vypnutý a není produkční instancí. Obnova zálohy na CWWK byla prakticky provedena. Opakovatelný postup, retence a další testy obnovy jsou autoritativně vedené v projektu [Zálohy Home Assistantu](../Zalohy/Home-Assistant.md).

## Uživatelská rozhraní

- **IIyama ProLite TW1023ASC + Fully Kiosk Browser:** hlavní nástěnné rozhraní.
- **NSPanel Pro v zahradním domku:** sekundární Android rozhraní s automatickým spuštěním Home Assistantu; jeho interní Zigbee se nepoužívá.
- **Technický mobilní dashboard:** schválený princip je jeden dashboard s více pohledy, jednoduchým a předvídatelným rozložením.

Rodinný dashboard a technické pohledy se při údržbě nemají bez důvodu nahrazovat novým rozvržením. Změna vzhledu nesmí zakrýt nedostupnou entitu nebo poruchu integrace.

## Síť a přístup

Home Assistant běží jako samostatné zařízení v domácí síti spravované RB5009. Síťové adresy zařízení jsou přidělované pomocí DHCP se statickými leases. Autoritativní topologie a adresace jsou v projektu [Síť](../Sit/README.md).

Současná lokální IP adresa nebo lokální URL domácího Home Assistantu není v dostupných autoritativních zdrojích uvedená. **Vyžaduje ověření v živém systému.**

Aktuálně používaná vzdálená přístupová cesta není zdokumentovaná. **Vyžaduje ověření v živém systému.** Přístupové účty, MFA, recovery a uložení přihlašovacích údajů patří do projektu [Přístupy](../Pristupy/README.md); tajné hodnoty se do GitHubu nezapisují.

## Hlavní integrační vrstvy

| Vrstva | Doložená role | Autoritativní detail |
|---|---|---|
| Zigbee2MQTT + Mosquitto MQTT | produkční domácí Zigbee a lokální zprávová vrstva | [Zigbee](Zigbee.md) |
| SolaX + Energy dashboard | měření FVE, spotřeby a energetický přehled; řízení je zatím poloautomatické | [FVE SolaX](FVE-SolaX.md) |
| Jablotron přes USB | lokální integrace zabezpečení a PG výstup pro domácí zvonění | [Hikvision](Hikvision.md) |
| Fully Kiosk Browser | hlavní nástěnný panel | tento dokument |
| Hikvision | stav interkomu a vazba na lokální zvonění | [Hikvision](Hikvision.md) |

Dále byly v červenci 2026 evidované Tasmota, HACS, Denon HEOS, Ecowitt, ESPHome, MikroTik Router, ONVIF, Philips AirPurifier, Shelly, Sonoff a Studio Code Server. Nejde o živě potvrzený seznam. Před změnou nebo odstraněním integrace je nutné její skutečné použití ověřit v Home Assistantu.

## Provozní závislosti

Home Assistant závisí zejména na:

- napájení domácího racku a CWWK;
- RB5009 a domácí LAN;
- Mosquitto MQTT pro MQTT klienty a Zigbee2MQTT;
- ethernetovém koordinátoru SMLIGHT SLZB-06P10;
- lokální dostupnosti integrovaných zařízení;
- USB připojení Jablotronu;
- použitelném backupu mimo samotné CWWK.

Výpadek PVE Ryzen nemá sám o sobě zastavit domácí Home Assistant, protože Home Assistant běží na samostatném miniPC. Budoucí zálohovací řetězec přes Nextcloud však závisí na infrastruktuře popsané v projektu [Zálohy](../Zalohy/Home-Assistant.md).

## První provozní kontrola

Při hlášeném problému postupovat od nejmenšího rozsahu:

1. Ověřit, zda běží CWWK, domácí síť a napájení racku.
2. Ověřit lokální dostupnost Home Assistantu z domácí LAN; nepoužívat pouze vzdálenou cestu.
3. V Home Assistantu zkontrolovat **Settings → System → Repairs**, systémové logy a stav dotčené integrace nebo add-onu.
4. Určit, zda je problém v Home Assistant Core, konkrétním add-onu, síti, MQTT, koordinátoru nebo cílovém zařízení.
5. Restartovat pouze dotčenou vrstvu. Celý host nebo rack se nerestartuje jako první diagnostický krok.
6. Po zásahu ověřit skutečnou funkci dotčené oblasti, ne pouze otevření webového rozhraní.

### Minimální přejímka po zásahu

- přihlášení a načtení hlavního dashboardu;
- funkce hlavního nástěnného panelu a NSPanelu Pro;
- dostupnost Mosquitto a Zigbee2MQTT;
- dostupnost významných Zigbee zařízení;
- hodnoty SolaX a Energy dashboardu;
- stav Jablotronu a interkomu;
- kritické automatizace a jejich ruční režim;
- vytvoření použitelné zálohy podle projektu Zálohy.

## Aktualizace a změny

Před aktualizací Home Assistant OS, Core, add-onu, HACS komponenty nebo vlastní integrace:

1. Ověřit poslední použitelný backup a jeho kopii mimo CWWK podle [Záloh Home Assistantu](../Zalohy/Home-Assistant.md).
2. Zkontrolovat poznámky k vydání a známé breaking changes dotčené komponenty.
3. Zaznamenat výchozí verzi a stav klíčových funkcí.
4. Aktualizovat jednu vrstvu nebo integraci, ne několik rizikových částí současně.
5. Po aktualizaci provést minimální přejímku uvedenou výše.
6. Pokud nelze rozlišit iniciační zpoždění od chyby, neprovádět současně další konfigurační zásahy.
7. Při neúspěchu použít připravený návratový postup nebo obnovu; nepřepisovat funkční backup novým neověřeným stavem.

Zvláštní pozornost vyžadují HACS komponenty, vlastní integrace, ESPHome balíčky a vlastní dashboardové karty. Jejich instalace nesmí být aktualizovaná bez kontroly dopadu na používané entity a automatizace.

## Obnova služby

Autoritativní stav záloh, cílová retence a testy obnovy jsou v [Zálohách Home Assistantu](../Zalohy/Home-Assistant.md). Tento projekt pouze stanovuje přejímku domácí instance.

Při ztrátě CWWK:

1. Vybrat kompatibilní náhradní hardware podle aktuální evidence v Airtable; nevytvářet zde druhou skladovou evidenci.
2. Nainstalovat Home Assistant OS a obnovit poslední ověřený backup.
3. Zachovat nebo znovu správně přidělit původní síťovou identitu.
4. Ověřit USB připojení Jablotronu a síťovou dostupnost SLZB-06P10.
5. Provést úplnou přejímku včetně dashboardů, add-onů, integrací, automatizací a přístupů.
6. Výsledek obnovy zapsat do autoritativního dokumentu Záloh bez tajných hodnot.

Původní HA Green ani jiné náhradní zařízení se nesmí připojit se stejnou IP adresou současně s produkčním CWWK.

## Kamerový systém

- Nainstalované jsou 4 neznačkové čínské 8Mpx PoE kamery.
- Připravené k výměně jsou 2 Hikvision 8Mpx PoE kamery; montáž vyžaduje plošinu.
- Současně nahrává původní čínské NVR i Hikvision NVR.
- Home Assistant poskytuje pouze náhled a stav; samotný záznam nesmí být na Home Assistantu závislý.

Detailní správa NVR, retence záznamu a úplný kamerový kusovník jsou mimo hranice tohoto projektu.

## Zásady automatizací

- Stabilita má přednost před experimentem.
- Lokální řešení se preferuje tam, kde přináší spolehlivost a kontrolu.
- Automatizace musí mít jasný účel a být pochopitelná i s časovým odstupem.
- Ruční zásah má vždy prioritu a musí existovat jednoznačný návrat do automatického režimu.
- Ruční override má být omezený časem nebo stavem, pokud by trvalé ponechání mohlo být nebezpečné nebo nechtěné.
- Výkonové spotřebiče musí mít definované podmínky zapnutí i vypnutí a bezpečný stav při ztrátě dat.
- Automatizace nesmí záviset na nedokumentovaném implicitním stavu ani vytvářet nekontrolovatelné smyčky.
- Základní bezpečnost, vytápění a záznam kamer nesmějí být existenčně závislé na Home Assistantu.
- Jednoduché a udržovatelné řešení má přednost před teoreticky chytřejším.

## Dokumentační pravidla

- Dynamický úplný seznam zařízení a entit zůstává v živém systému; do GitHubu patří jen entity významné pro automatizace, diagnostiku a obnovu.
- Hesla, tokeny, network keys, privátní klíče, recovery kódy ani neupravené konfigurace se do repozitáře neukládají.
- Změna skutečného hardware, přístupu, hlavní integrace, automatizace nebo obnovovacího postupu se zapíše do příslušného autoritativního dokumentu.
- Otevřený úkol se vede pouze v dokumentu, kam věcně patří; kořenový `TODO.md` se generuje automaticky.

## Související dokumentace

- [Zigbee](Zigbee.md)
- [FVE SolaX](FVE-SolaX.md)
- [Hikvision](Hikvision.md)
- [Síť](../Sit/README.md)
- [Přístupy](../Pristupy/README.md)
- [Monitoring](../Monitoring/README.md)
- [Uptime Kuma](../Monitoring/Uptime-Kuma.md)
- [Zálohy Home Assistantu](../Zalohy/Home-Assistant.md)

## Otevřené úkoly

- [ ] Ověřit živý seznam aktivních integrací a vyřadit z evidence již nepoužívané položky.
- [ ] Ověřit a zdokumentovat aktuálně používanou vzdálenou přístupovou cestu k domácímu Home Assistantu.
- [ ] Ověřit, zda Uptime Kuma hlídá dostupnost domácího Home Assistantu a zda upozornění směřují do schváleného notifikačního systému.
- [ ] S využitím plošiny vyměnit připravené 2 kamery za Hikvision, ověřit jejich záznam na Hikvision NVR a dokončit migraci kamerového systému na Hikvision.
