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
