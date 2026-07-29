# Telegram notifikace

> **Stav: NÁVRH** – koncepce je schválená, implementace ještě nezačala.

## Cíl

Telegram má být jedna přehledná schránka skutečných problémů infrastruktury MadMike, které vyžadují pozornost. Nemá sloužit jako technický log.

## Základní koncepce

- jeden soukromý chat nebo skupina `MadMike – infrastruktura`;
- jeden společný bot, pokud se při implementaci neobjeví praktický důvod pro více botů;
- společné místo pro alarm a následnou informaci o návratu do normálu;
- stručné zprávy, ze kterých je patrné co se stalo, kde a zda je potřeba zásah.

## Předpokládané zdroje

- Uptime Kuma – delší nedostupnost služby a následné obnovení;
- Proxmox VE a PBS – významné nativní události, které Pulse nepokrývá;
- Pulse – jen upozornění, která nejsou lépe řešená jinde;
- Mikr Manager – významné problémy MikroTiků a lokalit;
- později případně Home Assistant a další důležité systémy.

## Co do Telegramu nepatří

- každá úspěšná operace;
- běžný technický log;
- krátké výkyvy bez praktického dopadu;
- stejný problém oznámený několika nástroji;
- zprávy, ze kterých není jasné, zda vyžadují pozornost.

## Navazující práce

- [ ] Vytvořit soukromý chat nebo skupinu.
- [ ] Vytvořit bota a bezpečně uložit jeho token mimo repozitář.
- [ ] Připojit jako první Uptime Kuma a otestovat alarm i návrat do normálu.
- [ ] Otestovat nativní notifikace PVE a PBS.
- [ ] Postupně připojit Mikr Manager a případně Pulse.
- [ ] Po pilotním provozu upravit obsah zpráv a potlačit duplicity.
