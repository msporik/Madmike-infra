# Monitoring

> Poslední doložený provozní stav: **2026-07-28**. Dílčí živé ověření backup coverage VM510 proběhlo **2026-08-12**.

## Účel

Projekt zajišťuje jednoduchý a spolehlivý dohled nad infrastrukturou MadMike. Cílem není shromažďovat každý technický údaj, ale včas rozpoznat problém, určit jeho zdroj a mít dost informací pro bezpečný zásah.

Každou oblast přednostně sleduje nástroj, který jí přirozeně rozumí. Jeden problém má mít jedno hlavní místo detekce.

## Rozdělení odpovědností

| Zdroj | Autoritativní odpovědnost |
|---|---|
| [Pulse](Pulse.md) | Přehled Proxmox VE, PBS, VM/LXC, kapacit, ZFS, fyzických disků a záloh |
| Nativní notifikace PVE/PBS | Selhání Backup, Verify, Prune a Garbage Collection; podle ověřených možností také problémy ZFS scrubů |
| [Mikr Manager](Mikr.md) | Stav, historie a významné alarmy MikroTik zařízení a lokalit |
| [Uptime Kuma](Uptime-Kuma.md) | Dostupnost služeb a následný návrat do provozu |
| [Telegram](Telegram.md) | Společné doručení problémů vyžadujících pozornost |

Překryvy se omezují tak, aby stejný problém nebyl oznamován několika nástroji.

## Provozní umístění

Monitorovací aplikace běží na infrastrukturní Docker VM510 na domácím PVE Ryzen.

| Služba | Běžný webový vstup |
|---|---|
| Pulse | `https://pulse.mikehub.cz` |
| Mikr Manager | `https://mikr.mikehub.cz` |
| Uptime Kuma | `https://kuma.mikehub.cz` |

Služby jsou určené pro přístup z domácí sítě nebo přes WireGuard. Nejsou veřejně publikované.

Parametry VM510, Compose projekty, kontejnery, porty, Docker sítě a persistentní data jsou autoritativně vedené v [VM510 – Docker infrastruktura](../Servery/VM510-Docker.md). DNS, certifikát a proxy hosty jsou v [Interní DNS, NPM a HTTPS](../Servery/DNS-NPM-HTTPS.md).

## Poslední doložený stav

K 2026-07-28:

- běžely Pulse, Mikr Manager, Uptime Kuma a Nginx Proxy Manager;
- Pulse server a všechny tři agenty byly ve verzi `6.1.2`;
- Mikr evidoval 22 zařízení a licenci pro 50 zařízení;
- Uptime Kuma byla dostupná, ale její verze a živý seznam monitorů nebyly ověřeny;
- Telegram notifikace ještě nebyly realizovány;
- nativní notifikace PVE/PBS nebyly prakticky otestovány;
- Checkmk, Zabbix, Beszel a CoreBit byly odstraněny;
- InfluxDB, Grafana, Telegraf a samostatný Prometheus nejsou součástí schváleného monitorovacího stacku.

Dílčí kontrola 2026-08-12 potvrdila, že VM510 je stále zahrnuta v automatickém PBS backup jobu na PVE Ryzen. Aktuální snapshot VM510 fyzicky existuje na PBS datastore a kontrolovaný backup i následný Verify skončily `OK`. Tato kontrola neověřovala stav Dockeru ani jednotlivých kontejnerů uvnitř VM510.

Odstraněné nástroje nejsou otevřenými kandidáty k opětovnému nasazení.

## První provozní kontrola

Přihlášení na VM510:

```bash
ssh madmike@192.168.89.35
```

Základní kontrola hostu:

```bash
uptime
df -h
free -h
systemctl is-active docker
sudo docker ps
sudo docker ps -a
sudo docker stats --no-stream
```

Pořadí diagnostiky:

1. Pokud není dostupná VM510, ověřit PVE Ryzen a stav VM510.
2. Pokud VM510 běží, ale Docker ne, řešit službu Docker.
3. Pokud Docker běží, zkontrolovat konkrétní aplikaci a její logy.
4. Pokud funguje přímý port, ale ne HTTPS hostname, pokračovat podle [DNS, NPM a HTTPS](../Servery/DNS-NPM-HTTPS.md).
5. Po zásahu ověřit hlavní funkci Pulse, Mikru i Kumy, nikoliv jen otevření jejich webu.

## Provozní zásady

- Při problému jedné aplikace se bezdůvodně nerestartuje celá VM510 ani všechny kontejnery.
- Před aktualizací nebo zásahem do persistentních dat se ověří použitelná záloha VM510.
- Nepoužívají se neověřené hromadné příkazy odstraňující kontejnery, volumes nebo aplikační data.
- Hesla, API tokeny, Telegram bot token, recovery údaje ani neupravený výstup `docker compose config` se neukládají do GitHubu.
- Alarm je podnět k ověření v autoritativním systému, nikoliv oprávnění k automatické změně infrastruktury.
- Po zásahu se ověří příčina a výsledek. Případná změna se zapíše do dokumentu, který je pro danou oblast autoritativní.

## Hranice projektu

- Docker infrastruktura a obnova VM510: [VM510 – Docker infrastruktura](../Servery/VM510-Docker.md)
- DNS, HTTPS, NPM a vzdálený přístup: [Interní DNS, NPM a HTTPS](../Servery/DNS-NPM-HTTPS.md)
- Proxmox hosté a virtuální stroje: [Servery](../Servery/README.md)
- Backup joby, retence a testy obnovy: [PBS a disaster recovery](../Zalohy/PBS-DR.md)
- Síťová topologie a inventura MikroTiků: [MikroTik](../Sit/MikroTik.md)
- Obnovitelnost konfigurací MikroTiků: [Zálohy MikroTiků](../Zalohy/MikroTik.md)

## Otevřené úkoly

> Následující body vyžadují ověření v živém systému.

- [ ] Ověřit současný stav VM510, Dockeru a všech provozovaných kontejnerů.
- [x] Ověřit, že je VM510 stále zahrnuta v automatickém PBS backup jobu. — 2026-08-12 ověřeno; VM510 je součástí jobu a aktuální backup i Verify skončily `OK`.
