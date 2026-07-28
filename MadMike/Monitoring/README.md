# Monitoring

## Účel

Jednotný a přiměřeně jednoduchý dohled nad infrastrukturou MadMike. Cílem není sledovat každý technický detail, ale včas poznat skutečný problém a mít dost informací k rozhodnutí.

## Rozdělení odpovědností

| Nástroj | Odpovědnost | Detail |
|---|---|---|
| Pulse | Proxmox VE a Proxmox Backup Server | [Pulse.md](Pulse.md) |
| Mikr Manager | MikroTik zařízení a lokality | [Mikr.md](Mikr.md) |
| Uptime Kuma | Dostupnost služeb a návraty do provozu | [Uptime-Kuma.md](Uptime-Kuma.md) |
| Telegram | Jedna schránka problémů vyžadujících pozornost | [Telegram.md](Telegram.md) |

Nginx Proxy Manager zajišťuje jednotný HTTPS přístup k webovým rozhraním. Není samostatným monitorovacím nástrojem.

## Aktuální přístupy

- Pulse: `https://pulse.mikehub.cz`
- Mikr Manager: `https://mikr.mikehub.cz`
- Uptime Kuma: `https://kuma.mikehub.cz`

Přístupy jsou určené pro interní síť nebo VPN.

## Aktuální rozhodnutí o nástrojích

Používaný monitoring tvoří Pulse, Mikr Manager a Uptime Kuma. Telegram bude jejich společným cílem pro vybrané notifikace.

Dříve zkoušené nástroje už nejsou součástí provozního stacku:

- Checkmk byl odstraněn;
- Zabbix byl odstraněn včetně agentů;
- Beszel a CoreBit byly odstraněny při konsolidaci monitoringu.

Tyto nástroje se zachovávají pouze jako historie rozhodování, ne jako otevření kandidáti k nasazení.

## Principy

- Jeden problém má mít jedno hlavní místo detekce.
- Telegram nemá být technický log ani přehled každé úspěšné operace.
- Obnovení služby se oznamuje tam, kde bylo oznámeno její selhání.
- Detail konkrétního nástroje patří do jeho souboru; společná pravidla zůstávají zde.
- Neověřené údaje se nedoplňují odhadem.
- Hesla, tokeny a neupravené výpisy s tajnými hodnotami se neukládají.

## Otevřené kroky

1. Aktualizovat Uptime Kuma a poté určit konečný seznam monitorů.
2. Otestovat a nastavit nativní notifikace Proxmox VE a PBS pro události, které Pulse nepokrývá.
3. Vybrat jen významné alarmy z Mikr Manageru.
4. Zprovoznit společné Telegram notifikace podle schválených zásad.
