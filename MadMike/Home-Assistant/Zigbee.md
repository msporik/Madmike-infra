# Zigbee

Domácí produkční Zigbee síť připojená k Home Assistantu.

## Produkční stav

- **Koordinátor:** SMLIGHT SLZB-06P10.
- **Připojení:** Ethernet.
- **Poslední doložený endpoint:** `192.168.89.56:6638`.
- **Řízení sítě:** Zigbee2MQTT.
- **Zprávová vrstva:** Mosquitto MQTT.
- Přechod z původního USB koordinátoru je dokončený.
- Zigbee2MQTT na ethernetovém koordinátoru běží a domácí Zigbee je v produkčním provozu.

Endpoint odpovídá poslednímu doloženému stavu. Jeho současná platnost není potvrzená. **Vyžaduje ověření v živém systému.**

Původní USB koordinátor je vedený jen jako možná záloha. Jeho připravenost k obnově produkční sítě nebyla ověřena.

## Architektura a závislosti

```text
Zigbee zařízení
→ SMLIGHT SLZB-06P10
→ Zigbee2MQTT
→ Mosquitto MQTT
→ Home Assistant
→ dashboardy a automatizace
```

Produkční Zigbee proto závisí na napájení a síti koordinátoru, Zigbee2MQTT, Mosquitto MQTT a Home Assistantu. NSPanel Pro není koordinátorem ani routerem této sítě; jeho interní Zigbee se záměrně nepoužívá.

## Matter a Thread

Matter/Thread je samostatná infrastruktura a nesmí se zaměňovat s produkčním Zigbee koordinátorem SLZB-06P10.

- Druhé zařízení SMLIGHT určené pro Thread je identifikováno jako **SLZB-06M**. Model podporuje Thread, Matter-over-Thread a OTBR. Konkrétní kus je evidován ve skladu HW. Jeho plánovaná role v infrastruktuře a skutečný stav konfigurace/OTBR před nasazením zatím nejsou ověřené.
- Aqara Smart Lock je koupený, ale není nainstalovaný.

Tyto prvky nejsou součástí produkční Zigbee cesty a jejich stav nesmí být používán při diagnostice současného Zigbee.

## Provozní kontrola

Při běžné kontrole ověřit:

1. dostupnost SLZB-06P10 po domácí síti;
2. stav add-onu Zigbee2MQTT;
3. stav Mosquitto MQTT;
4. připojení Zigbee2MQTT ke koordinátoru a brokeru;
5. dostupnost několika významných routerů a koncových zařízení;
6. funkci vybrané automatizace závislé na Zigbee.

Mapa a úplný dynamický seznam zařízení zůstávají v Zigbee2MQTT. Do GitHubu patří pouze zařízení významná pro provoz, diagnostiku nebo obnovu.

## Diagnostický runbook

| Projev | Postup |
|---|---|
| Nedostupná celá Zigbee síť | Ověřit napájení a síť koordinátoru, potom Zigbee2MQTT a Mosquitto. Nezahajovat párování ani reset koordinátoru. |
| Zigbee2MQTT neběží | Zkontrolovat log add-onu a jeho připojení ke koordinátoru a MQTT. Restartovat pouze dotčenou vrstvu a ověřit návrat zařízení. |
| Zigbee2MQTT běží, ale HA nemá stavy | Ověřit Mosquitto, MQTT integraci a discovery. Neměnit Zigbee network key ani znovu nepárovat zařízení. |
| Nedostupné je jedno zařízení | Ověřit napájení nebo baterii zařízení, poslední kontakt a dostupnost jeho obvyklé trasy. Reset a nové párování použít až po vyloučení běžné příčiny. |
| Výpadky části sítě | Porovnat postižená zařízení, Zigbee routery a fyzickou oblast. Neměnit kanál nebo koordinátor bez backupu a návratového postupu. |

## Bezpečná aktualizace a změny

Před aktualizací Zigbee2MQTT, firmware koordinátoru, Mosquitto nebo Home Assistantu:

1. Ověřit použitelný backup Home Assistantu podle [Záloh Home Assistantu](../Zalohy/Home-Assistant.md).
2. Ověřit, že jsou chráněná data Zigbee2MQTT potřebná k obnově sítě a že tajný network key není uložený v GitHubu.
3. Zaznamenat současný endpoint koordinátoru, verze a stav významných zařízení.
4. Aktualizovat jednu vrstvu.
5. Ověřit připojení koordinátoru, MQTT, návrat zařízení a vybrané automatizace.
6. Při neúspěchu použít backup a návratový postup; nevytvářet novou síť se stejnými zařízeními bez vědomého rozhodnutí.

Přesný rozsah a umístění současných dat Zigbee2MQTT potřebných k obnově nejsou v projektu doložené. Autoritativní řešení patří do projektu Zálohy. **Vyžaduje ověření v živém systému.**

## Obnova

Při výměně nebo obnově koordinátoru:

- zachovat původní data a identitu Zigbee sítě, pokud jsou použitelné;
- neprovádět factory reset koncových zařízení jako první krok;
- nepoužít současně dva koordinátory se stejnou produkční konfigurací;
- po obnově ověřit routery, bateriová zařízení a kritické automatizace;
- výsledek a případné ruční kroky zapsat bez zveřejnění network key nebo přihlašovacích údajů.

Původní USB koordinátor se nepovažuje za připravenou zálohu, dokud neprojde praktickým testem.

## Otevřené úkoly

- [ ] Ověřit plánované nasazení SLZB-06M pro Thread/Matter a zvolit způsob OTBR: OTBR v Home Assistantu, nebo OTBR přímo na SLZB-06M.
- [ ] Ověřit, zda je původní USB koordinátor skutečně použitelný jako nouzová záloha produkční Zigbee sítě.
