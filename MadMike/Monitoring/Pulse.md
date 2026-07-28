# Pulse

## Role

Pulse je hlavní přehled stavu Proxmox VE a Proxmox Backup Server. Slouží pro kapacitu, vytížení, teploty a základní zdravotní stav infrastruktury.

## Ověřený stav k 2026-07-28

- Verze: `6.1.2`
- Webové rozhraní: `https://pulse.mikehub.cz`
- Telemetrie aplikace je vypnutá.
- Připojené systémy:
  - PVE Ryzen;
  - PVE Dell;
  - PBS provozovaný ve VM 200.
- Pulse správně rozpoznává Proxmox; Docker a Kubernetes nejsou cílem tohoto nasazení.
- V přehledu jsou dostupné také teploty disků.

## Hranice odpovědnosti

Pulse nenahrazuje nativní události Proxmox VE a PBS. Samostatně je potřeba ověřit a nastavit zejména upozornění na:

- selhání zálohy;
- selhání Verify;
- problémy Prune nebo Garbage Collection;
- stav ZFS a scrub;
- SMART a další významné diskové události.

Přesné události a jejich podmínky se zapíší až po praktickém testu nativních notifikací.

## Bezpečnostní poznámka

Historické nebo DR kopie a položky označené jako orphaned backups se nemažou bez předchozího určení jejich původu a účelu.

## Navazující práce

1. Otestovat nativní notifikační systém PVE a PBS.
2. Rozdělit události mezi Pulse a nativní notifikace bez duplicit.
3. Nastavit pouze alarmy, které vyžadují pozornost.
4. Vybrané problémy a jejich vyřešení směrovat do Telegramu.
