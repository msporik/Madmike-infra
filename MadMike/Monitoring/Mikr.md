# Mikr Manager

## Role

Mikr Manager je hlavní nástroj pro přehled MikroTik zařízení, jejich stavu a dlouhodobého vývoje.

## Ověřený stav k 2026-07-28

- Webové rozhraní: `https://mikr.mikehub.cz`
- Evidováno: 22 zařízení
- Licence: 50 zařízení
- Interval grafů: 5 minut
- Retence historie: 90 dní
- Export konfigurací RSC je povolený.

## Zásady alertů

Do společných notifikací patří jen významné problémy zařízení nebo lokalit. Běžné provozní změny a krátké výkyvy nemají vytvářet hluk.

Výběr konkrétních alarmů zatím není uzavřený a bude proveden podle praktické hodnoty jednotlivých upozornění.

## Navazující práce

- [ ] Vybrat kritická zařízení a lokality.
- [ ] Určit významné alarmy a jejich rozumné zpoždění.
- [ ] Prověřit, které události už lépe pokrývá Uptime Kuma.
- [ ] Připojit pouze neduplicitní alarmy do Telegramu.
- [ ] Prakticky ověřit ukládání a obnovitelnost exportů konfigurací.
