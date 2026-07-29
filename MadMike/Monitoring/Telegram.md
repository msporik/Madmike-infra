# Telegram notifikace

> **Stav: SCHVÁLENÁ KONCEPCE** – implementace ještě nezačala.

## Cíl

Telegram má být jedna přehledná schránka skutečných problémů infrastruktury MadMike, které vyžadují pozornost. Nemá sloužit jako technický log.

## Schválená koncepce

- jedna soukromá skupina `MadMike – infrastruktura`;
- jeden společný bot pro všechny zdroje notifikací;
- společné místo pro alarm a následnou informaci o návratu do normálu;
- stručné zprávy, ze kterých je patrné, co se stalo, kde a zda je potřeba zásah;
- token bota se ukládá bezpečně mimo repozitář.

## Minimální obsah zprávy

- zdroj upozornění;
- objekt, služba nebo lokalita;
- stručný popis problému;
- čas vzniku nebo délka trvání, pokud ji zdroj poskytuje;
- aktuální stav a informace, zda je potřeba zásah.

Recovery zpráva má jednoznačně navazovat na původní problém a potvrdit návrat do normálu.

## Zdroje a pořadí zapojení

1. **Uptime Kuma** – delší nedostupnost služby a následné obnovení.
2. **Proxmox VE a PBS** – významné nativní události, zejména selhání Backup, Verify, Prune a Garbage Collection.
3. **Mikr Manager** – významné problémy MikroTiků a lokalit, které neduplikuje Kuma.
4. **Pulse** – pouze upozornění, která nejsou lépe řešena jiným zdrojem.
5. Později případně Home Assistant a další důležité systémy.

## Co do Telegramu nepatří

- každá úspěšná operace;
- běžný technický log;
- krátké výkyvy bez praktického dopadu;
- stejný problém oznámený několika nástroji;
- zprávy, ze kterých není jasné, zda vyžadují pozornost.

## Navazující práce

- [ ] Vytvořit soukromou skupinu `MadMike – infrastruktura`.
- [ ] Vytvořit jednoho společného bota a bezpečně uložit jeho token mimo repozitář.
- [ ] Připojit jako první Uptime Kuma a otestovat alarm i návrat do normálu.
- [ ] Otestovat nativní notifikace PVE a PBS.
- [ ] Postupně připojit Mikr Manager a případně Pulse.
- [ ] Po pilotním provozu upravit obsah zpráv a potlačit duplicity.
