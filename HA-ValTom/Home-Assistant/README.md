# Home Assistant – HA ValTom

## Role

Instance je připravovaná pro Tomáše Valentu. Prvním praktickým cílem je zobrazit výrobu a provoz GoodWe FVE v jednoduchém dashboardu. Později může Home Assistant řídit bojler podle energetické situace.

## Ověřený stav k 2026-07-28

- hardware: Home Assistant Green;
- systém: Home Assistant OS;
- proběhla čistá instalace a vznikl připravený základní obraz / záloha;
- HA Green zatím není nainstalovaný u Tomáše a není propojený s jeho zařízeními;
- zařízení je u správce a čeká na nasazení;
- v připravené instalaci byly potvrzené HACS, Advanced SSH & Web Terminal, Matter, Matter Server, Google Cast, Thread, Radio Browser, Google Translate TTS a Cloudflared;
- vzdálený přístup byl zprovozněný přes Cloudflare Tunnel na `https://valtom.mikehub.cz`;
- integrace GoodWe, skutečné FVE entity, produkční dashboard a řízení bojleru nejsou dosud ověřené jako dokončené.

## Témata projektu

- [Nasazení a vzdálený přístup](Nasazeni-a-pristup.md)
- [GoodWe a energetika](GoodWe-a-energie.md)

## Bezprostřední další kroky

- [ ] Ověřit spolehlivý start HA Green a aktuálnost připravené instalace.
- [ ] Nainstalovat HA Green u Tomáše a připojit ho do místní sítě.
- [ ] Po přesunu ověřit lokální i vzdálený přístup.
- [ ] Zjistit přesný model a způsob komunikace GoodWe střídače.
- [ ] Připojit GoodWe, potvrdit skutečné entity a vytvořit základní FVE dashboard.
- [ ] Teprve potom navrhnout řízení bojleru podle konkrétního hardwaru a požadované logiky.
- [ ] Nastavit pravidelné zálohy a prakticky ověřit obnovu.

## Související dokumentace

- [Společná strategie záloh Home Assistantu](../../MadMike/Zalohy/Home-Assistant.md)
- [Centrální DNS, NPM a HTTPS](../../MadMike/Servery/DNS-NPM-HTTPS.md)
