# Honza

Samostatná kapitola dokumentace lokality Honza. Zachycuje místní Home Assistant, chytrou domácnost a síťovou infrastrukturu.

> Poslední uživatelem potvrzený stav místní sítě a Home Assistantu: **2026-08-02**. Údaje označené k ověření nejsou potvrzením současného živého stavu.

## Projekty

- [Home Assistant](Home-Assistant/README.md) – HA Green, Zigbee, osvětlení, panely a budoucí řízení topení.
- [Síť](Sit/README.md) – místní LAN, MikroTik a Wi-Fi.

## Provozní orientace

Lokalita používá jednu LAN `192.168.10.0/24`. Hlavním routerem je `RB4011Honza` na `192.168.10.1`; za ním je jediné Wi-Fi AP `hAP ac3`. Místní Home Assistant Green má poslední potvrzenou adresu `192.168.10.22`.

Vzdálená správa z HOME je závislá na site-to-site WireGuardu. Výpadek tunelu sám o sobě neznamená výpadek místní LAN, Wi-Fi nebo Home Assistantu, ale znemožní jejich běžnou vzdálenou správu.

Při převzetí lokality postupovat v tomto pořadí:

1. přečíst [síťový přehled](Sit/README.md) a [Home Assistant](Home-Assistant/README.md);
2. ověřit místní nebo WireGuard přístup bez změny konfigurace;
3. zkontrolovat otevřené úkoly v tematických dokumentech;
4. před zásahem ověřit zálohu příslušného systému a nezávislou návratovou cestu;
5. provést pouze jednu logickou změnu a po ní přejímku skutečných služeb a fyzického ovládání.

## Hranice kapitoly

- Tato kapitola popisuje systémy a zařízení specifické pro lokalitu Honza.
- Společná strategie záloh Home Assistantu zůstává v [MadMike / Zálohy / Home Assistant](../MadMike/Zalohy/Home-Assistant.md).
- Centrální evidence tunelů zůstává v [MadMike / Servery / WireGuard](../MadMike/Servery/WireGuard.md).
- Obecné provozní postupy MikroTiků zůstávají v [MadMike / Síť / MikroTik](../MadMike/Sit/MikroTik.md).
- Centrální monitoring zůstává v [MadMike / Monitoring](../MadMike/Monitoring/README.md).
- Účty, MFA, recovery a společný přístupový model zůstávají v [MadMike / Přístupy](../MadMike/Pristupy/README.md) a v bezpečném správci hesel.
- Kusová hardwarová evidence zůstává v Airtable; GitHub popisuje aktivní role a topologii.

Hesla, tokeny, privátní klíče, app hesla, Zigbee network key ani neupravené exporty konfigurace do repozitáře nepatří.

