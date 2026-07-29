# Monitoring

## Účel

Jednotný a přiměřeně jednoduchý dohled nad infrastrukturou MadMike. Cílem není sledovat každý technický detail, ale včas poznat skutečný problém a mít dost informací k rozhodnutí.

## Rozdělení odpovědností

| Zdroj | Hlavní odpovědnost | Detail |
|---|---|---|
| Pulse | Přehled Proxmox VE a Proxmox Backup Serveru, kapacit, disků, ZFS a záloh | [Pulse.md](Pulse.md) |
| Nativní notifikace PVE/PBS | Autoritativní hlášení selhání Backup, Verify, Prune a Garbage Collection; podle možností také problémů ZFS scrubů | [hranice Pulse](Pulse.md#hranice-pulse) |
| Mikr Manager | Stav a historie MikroTik zařízení a lokalit | [Mikr.md](Mikr.md) |
| Uptime Kuma | Dostupnost služeb a následné obnovení | [Uptime-Kuma.md](Uptime-Kuma.md) |
| Telegram | Jedna společná schránka problémů vyžadujících pozornost | [Telegram.md](Telegram.md) |

Jeden problém má mít jedno hlavní místo detekce. Překryvy se řeší tak, aby do Telegramu nepřicházely duplicitní zprávy.

## Poslední doložený stav k 2026-07-28

- Na monitorovací VM510 běžely Pulse, Mikr Manager a Uptime Kuma; Nginx Proxy Manager zajišťoval HTTPS přístup.
- Webová rozhraní:
  - Pulse: `https://pulse.mikehub.cz`
  - Mikr Manager: `https://mikr.mikehub.cz`
  - Uptime Kuma: `https://kuma.mikehub.cz`
- Přístupy jsou určené pro interní síť nebo VPN.
- Checkmk, Zabbix, Beszel a CoreBit byly odstraněny a nejsou součástí provozního monitorovacího stacku.
- InfluxDB, Grafana, Telegraf a Prometheus nejsou součástí tohoto schváleného řešení monitoringu.
- Telegram notifikace ještě nebyly realizovány.
- Nativní notifikace PVE/PBS nebyly prakticky otestovány.

Přesná současná konfigurace VM510 nebyla při konsolidaci ověřena proti živému systému. Dokumentace serveru je v [PVE Ryzen](../Servery/PVE-Ryzen.md).

## Schválená koncepce

- Provozní stack tvoří Pulse, Mikr Manager a Uptime Kuma.
- Selhání nativních úloh PVE/PBS mají primárně hlásit samotné Proxmox VE a PBS.
- Telegram bude soukromá skupina `MadMike – infrastruktura`.
- Pro všechny zdroje notifikací se použije jeden společný bot.
- Uptime Kuma má používat přibližně pětiminutové výchozí zpoždění; podle významu služby se může upravit individuálně.
- Oznamují se skutečné problémy a následné návraty do normálu, nikoliv každý úspěšný běh nebo běžný technický log.
- Pulse se do Telegramu zapojí jen pro upozornění, která nejsou spolehlivěji pokryta jiným zdrojem.

Zabbix byl odmítnut kvůli složitosti a nadbytečnému množství dat. Beszel a CoreBit neměly v cílovém rozdělení dostatečně jedinečnou roli. Odstraněné nástroje zůstávají pouze historií rozhodování, ne otevřenými kandidáty k nasazení.

## Hranice projektu

- DNS, Nginx Proxy Manager, HTTPS a WireGuard patří do projektu [Servery](../Servery/DNS-NPM-HTTPS.md).
- Adresní plán, topologie a inventura MikroTiků patří do projektu [Síť](../Sit/MikroTik.md).
- Rozvrhy, retence, restore a disaster recovery patří do projektu [Zálohy](../Zalohy/PBS-DR.md).
- V Monitoringu jsou zachyceny jen vazby potřebné k pochopení detekce a směrování problémů.

## Otevřené kroky

- [ ] Aktualizovat Uptime Kuma a poté určit konečný seznam monitorů.
- [ ] Otestovat a nastavit nativní notifikace Proxmox VE a PBS pro události, které Pulse nepokrývá.
- [ ] Vybrat jen významné alarmy z Mikr Manageru.
- [ ] Zprovoznit společné Telegram notifikace podle schválených zásad.
