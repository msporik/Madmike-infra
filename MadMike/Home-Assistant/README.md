# Home Assistant

Domácí instance Home Assistantu a její hlavní integrace.

## Aktuální stav

- **Platforma:** CWWK X86-P6.
- **Procesor:** zdroje si odporují mezi Intel N100 a N150; přesnou variantu je potřeba ověřit na živém zařízení.
- **Paměť:** 8 GB RAM.
- **Architektura:** x86-64.
- **Úložiště:** NVMe.
- **Systém:** Home Assistant OS.
- **Role:** hlavní domácí automatizace.
- **Stav:** produkční a běžně používaná instance.
- Migrace z HA Green je dokončená; starý HA Green je vypnutý a mimo produkční provoz.

Zobrazovací zařízení:

- hlavní wall tablet IIyama ProLite TW1023ASC;
- NSPanel Pro v zahradním domku.

## Síťové vazby

Domácí Home Assistant běží v síti spravované hlavním RB5009. Podrobná inventura routerů, switchů a AP zůstává v projektu [Síť](../Sit/README.md), aby se zde neduplikovala.

IP adresy zařízení se přidělují přes DHCP se statickými leases.

## Hlavní aktivní integrace

Poslední souhrnný checkpoint uvádí jako aktivní:

- Zigbee2MQTT;
- Jablotron přes USB;
- Mosquitto MQTT;
- Tasmota přes MQTT;
- SolaX;
- Energy dashboard;
- HACS;
- Denon HEOS;
- Ecowitt;
- ESPHome;
- Fully Kiosk Browser;
- MikroTik Router;
- ONVIF;
- Philips AirPurifier;
- Shelly;
- Sonoff;
- Studio Code Server.

Seznam je užitečná inventura posledního souhrnného stavu, nikoli záruka, že každá integrace je dnes aktivně používaná. Při příští živé kontrole se má potvrdit a případně zredukovat.

Plánované nebo samostatně řešené oblasti:

- Thread a Matter;
- Aqara Smart Lock;
- Modbus a DS18B20 přes převodník;
- dlouhodobá data v InfluxDB/Grafaně.

## Oblasti projektu

- [Zigbee](Zigbee.md) – produkční ethernetový koordinátor SMLIGHT SLZB-06P10 a Zigbee2MQTT.
- [FVE SolaX](FVE-SolaX.md) – domácí fotovoltaika a hlavní měření energie.
- [Hikvision](Hikvision.md) – domácí dveřní interkom a jeho napojení na Home Assistant.

## Energie a vytápění

Domácí technologický kontext zahrnuje:

- FVE SolaX;
- akumulační nádobu s vnořeným bojlerem;
- krbová kamna s výměníkem;
- podlahové vytápění v přízemí a patře;
- jedno společné oběhové čerpadlo.

Data jsou dostupná v Home Assistantu. Směr další práce je postupná optimalizace řízení podle stavu domu a dostupné energie, nikoli složitost sama pro sebe.

## DC infrastruktura racku

Domácí infrastruktura používá dva sousedící 6U racky:

- **síťový rack:** router, switche a PoE patch panely;
- **napájecí rack:** 18Ah zálohovací baterie, zálohovaný zdroj 230 V → 12 V a DC/DC měniče.

Doložené komponenty:

- Mean Well DRS-240-12;
- Mean Well DDR-120A-48;
- Mean Well DDR-60G-24;
- Mean Well DDR-30G-5.

Zásady:

- DC-first tam, kde to dává smysl;
- minimum samostatných AC adaptérů;
- jištění jednotlivých větví;
- přehlednost a servisovatelnost před improvizovaným bastlením.

## Kamerová infrastruktura

Poslední souhrnný checkpoint uvádí:

- 4× 8Mpx kamery neurčeného čínského výrobce;
- samostatné NVR;
- v Home Assistantu pouze náhled a stav.

Jako plánovaný upgrade byly evidované:

- 2× Hikvision DS-2CD2087G3-LI2UY/SL, 2.8 mm;
- 1× Hikvision DS-2CD2387G3-LIS2UY/SL, 2.8 mm;
- NVR Hikvision DS-7608NXI-I2/S(E).

Interkom DS-KB8113-IME1(B) je již nasazený; jeho aktuální stav je v [Hikvision](Hikvision.md). Stav realizace plánovaného kamerového upgradu je potřeba ověřit samostatně.

## Zásady automatizací

- Stabilita má přednost před experimentem.
- Lokální řešení se preferuje tam, kde přináší spolehlivost a kontrolu.
- Automatizace musí mít jasný účel a být pochopitelná i s časovým odstupem.
- Ruční zásah má vždy prioritu a musí existovat jednoznačný návrat do automatického režimu.
- Výkonové spotřebiče musí mít definované podmínky zapnutí i vypnutí a bezpečný stav při ztrátě dat.
- Automatizace nesmí záviset na nedokumentovaném implicitním stavu ani vytvářet nekontrolovatelné smyčky.
- Jednoduché a udržovatelné řešení má přednost před teoreticky chytřejším.

## Hranice projektu

Tento projekt popisuje pouze domácí instalaci MadMike. Home Assistant ve Vernířovicích a dalších lokalitách patří do jejich vlastních kapitol.

Zálohování Home Assistantu je autoritativně v projektu [Zálohy](../Zalohy/Home-Assistant.md).

## Otevřené body

- [ ] Ověřit, zda má CWWK X86-P6 procesor Intel N100 nebo N150, a odstranit rozpor ze zdrojů.
- [ ] Ověřit živý seznam aktivních integrací a vyřadit z evidence již nepoužívané položky.
- [ ] Ověřit současný stav plánovaného Hikvision kamerového upgradu.
- [ ] Ověřit přesný model, roli a stav nasazení samostatného zařízení SMLIGHT určeného pro Matter/Thread a plánovaný zámek Aqara.
