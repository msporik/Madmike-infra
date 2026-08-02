# Home Assistant

Domácí produkční instance Home Assistantu a její hlavní integrace.

## Aktuální stav

- **Platforma:** CWWK X86-P6.
- **Procesor:** Intel N150.
- **Paměť:** 8 GB RAM.
- **Architektura:** x86-64.
- **Úložiště:** NVMe.
- **Systém:** Home Assistant OS.
- **Role:** hlavní domácí automatizace.
- **Stav:** produkční a běžně používaná instance.

Migrace z HA Green je dokončená. Původní HA Green je vypnutý a není produkční instancí. Obnova zálohy na CWWK byla prakticky provedena; opakovatelný postup a další testy obnovy patří do projektu [Zálohy](../Zalohy/Home-Assistant.md).

## Uživatelská rozhraní

- **IIyama ProLite TW1023ASC + Fully Kiosk Browser:** hlavní nástěnné rozhraní.
- **NSPanel Pro:** sekundární rozhraní v zahradním domku.

## Síť, přístup a dohled

Domácí Home Assistant běží v síti spravované hlavním RB5009. IP adresy zařízení se přidělují přes DHCP se statickými leases. Podrobná síťová topologie a adresace zůstává v projektu [Síť](../Sit/README.md).

Přístupové účty, MFA a nouzové přístupové postupy patří do projektu [Přístupy](../Pristupy/README.md). Kontrola dostupnosti a směrování upozornění patří do projektu [Monitoring](../Monitoring/README.md).

## Hlavní integrace

Poslední souhrnný stav z července 2026 uvádí jako hlavní používané vrstvy:

- Zigbee2MQTT;
- Mosquitto MQTT;
- Jablotron přes USB;
- SolaX a Energy dashboard;
- Fully Kiosk Browser.

Dále byly evidované integrace Tasmota, HACS, Denon HEOS, Ecowitt, ESPHome, MikroTik Router, ONVIF, Philips AirPurifier, Shelly, Sonoff a Studio Code Server. Tento seznam je datovaná inventura, nikoli záruka, že je každá položka stále aktivně používaná.

## Oblasti projektu

- [Zigbee](Zigbee.md) – produkční ethernetový koordinátor SMLIGHT SLZB-06P10, Zigbee2MQTT a oddělení budoucího Matter/Thread řešení.
- [FVE SolaX](FVE-SolaX.md) – měření domácí fotovoltaiky, energetický přehled a poloautomatické řízení.
- [Hikvision](Hikvision.md) – dokončené nasazení domácího dveřního interkomu a jeho vazba na Home Assistant.

## Energie a automatizace

SolaX poskytuje hlavní měření FVE a spotřeby domu. Energetické řízení je zatím poloautomatické; jeho současný stav, bezpečnostní zásady a navazující úkoly jsou v [FVE-SolaX.md](FVE-SolaX.md). InfluxDB a Grafana zůstávají schváleným plánem malého pilotu pro dlouhodobá energetická data.

## Kamerový systém

- Nainstalované jsou 4 neznačkové čínské 8Mpx PoE kamery.
- Připravené k výměně jsou 2 Hikvision 8Mpx PoE kamery; montáž vyžaduje plošinu.
- Současně nahrává původní čínské NVR i Hikvision NVR.
- Home Assistant poskytuje pouze náhled a stav; samotný záznam nesmí být na Home Assistantu závislý.

Tato část zachycuje pouze vazbu kamerového systému na Home Assistant. Detailní správa NVR, retence záznamu a úplný kamerový kusovník jsou mimo hranice tohoto projektu.

## Infrastrukturní závislosti

Home Assistant závisí na domácí síti, napájení racku a dostupnosti ethernetového Zigbee koordinátoru. V tomto projektu se eviduje pouze jejich dopad na provoz HA; podrobný kusovník zdrojů, měničů, routerů a switchů patří do příslušných infrastrukturních projektů.

## Zásady automatizací

- Stabilita má přednost před experimentem.
- Lokální řešení se preferuje tam, kde přináší spolehlivost a kontrolu.
- Automatizace musí mít jasný účel a být pochopitelná i s časovým odstupem.
- Ruční zásah má vždy prioritu a musí existovat jednoznačný návrat do automatického režimu.
- Výkonové spotřebiče musí mít definované podmínky zapnutí i vypnutí a bezpečný stav při ztrátě dat.
- Automatizace nesmí záviset na nedokumentovaném implicitním stavu ani vytvářet nekontrolovatelné smyčky.
- Základní bezpečnost, vytápění a záznam kamer nesmí být existenčně závislé na Home Assistantu.
- Jednoduché a udržovatelné řešení má přednost před teoreticky chytřejším.

## Hranice projektu

Tento projekt popisuje pouze domácí instalaci MadMike. Home Assistant ve Vernířovicích a dalších lokalitách patří do jejich vlastních kapitol.

Zálohování Home Assistantu je autoritativně v projektu [Zálohy](../Zalohy/Home-Assistant.md).

## Otevřené úkoly

- [ ] Ověřit živý seznam aktivních integrací a vyřadit z evidence již nepoužívané položky.
- [ ] Ověřit a zdokumentovat aktuálně používanou vzdálenou přístupovou cestu k domácímu Home Assistantu.
- [ ] Ověřit, zda Uptime Kuma hlídá dostupnost domácího Home Assistantu a zda upozornění směřují do schváleného notifikačního systému.
- [ ] S využitím plošiny vyměnit připravené 2 kamery za Hikvision, ověřit jejich záznam na Hikvision NVR a dokončit migraci kamerového systému na Hikvision.
