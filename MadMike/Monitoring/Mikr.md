# Mikr Manager

## Role

Mikr Manager je monitorovací nástroj pro přehled stavu MikroTik zařízení a lokalit, krátkodobé i dlouhodobější grafy a výběr událostí, které skutečně vyžadují pozornost.

Není autoritativní dokumentací celé sítě ani zálohovacím systémem. Inventura, topologie a RouterOS patří do [dokumentace MikroTik sítě](../Sit/MikroTik.md); exporty konfigurací a jejich obnova do [záloh MikroTiků](../Zalohy/MikroTik.md).

## Poslední doložený stav k 2026-07-28

- Webové rozhraní: `https://mikr.mikehub.cz`
- Evidováno: 22 zařízení
- Licence: 50 zařízení
- Interval grafů: 5 minut
- Retence historie: 90 dní
- Export konfigurací RSC byl povolený.

Povolený RSC export ještě sám o sobě nepotvrzuje praktickou obnovitelnost. Ta zůstává k ověření v projektu Zálohy.

## Zásady alarmů

- Do společných notifikací patří jen významné problémy kritických zařízení nebo celých lokalit.
- Běžné provozní změny a krátké výkyvy nemají vytvářet hluk.
- Událost, kterou spolehlivěji detekuje Uptime Kuma, se nemá z Mikru posílat duplicitně.
- Konkrétní prahové hodnoty a zpoždění se zapíší jako realizované až po praktickém nastavení a ověření.

Výběr kritických zařízení, lokalit a konkrétních alarmů zatím není uzavřený.

## Navazující práce

- [ ] Vybrat kritická zařízení a lokality.
- [ ] Určit významné alarmy a jejich rozumné zpoždění.
- [ ] Prověřit, které události už lépe pokrývá Uptime Kuma.
- [ ] Připojit pouze neduplicitní alarmy do Telegramu.
- [ ] Prakticky ověřit ukládání a obnovitelnost exportů konfigurací v projektu Zálohy.
