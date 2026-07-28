# PVE Dell

## Role

Offsite DR host provozující Proxmox Backup Server ve VM200. Detailní síťové údaje, vzdálená správa a další bezpečnostně citlivé informace nejsou součástí tohoto dokumentu.

## Virtuální stroje

| VM | Stav | Ověřená role |
|---|---|---|
| Dell / VM200 | běží | Proxmox Backup Server |
| Dell / VM400 | vypnutá | Účel zatím neznámý; nutno ověřit |
| Dell / VM401 | vypnutá | Migrační test při přesunu Nextcloudu z bare metal instalace na PVE Ryzen; přenos dat a nastavení |
| Dell / VM402 | vypnutá | Úspěšná testovací obnova produkčního Nextcloudu z PBS |
| Dell / VM501 | vypnutá | Úspěšná testovací obnova produkční Windows VM s PREMIERem z PBS |

VM400, VM401, VM402 a VM501 jsou záměrně ponechané, dokud nebude jejich další osud jednotlivě rozhodnutý. Nejde je souhrnně označit za nepotřebné.

## Ověřené DR výsledky

- Obnova Nextcloudu do Dell / VM402 byla úspěšná; VM naběhla a byly funkční Apache, MariaDB, Nextcloud i přístup k datům.
- Obnova Windows VM s PREMIERem do Dell / VM501 byla úspěšná.
- Dell / VM401 není DR obnova, ale starší migrační test.

## Otevřené kontroly

1. Zjistit původ a účel Dell / VM400.
2. Ověřit aktuální stav PVE, PBS a datastore proti živému systému.
3. Před případným odstraněním kterékoliv vypnuté VM znovu ověřit její obsah a potřebnost.
