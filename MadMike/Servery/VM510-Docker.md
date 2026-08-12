# VM510 – Docker infrastruktura

> Poslední souhrnný stav VM a stacku: **2026-07-28**.  
> Kontejner Uptime Kuma byl znovu ověřen **2026-08-03**. Ostatní údaje bez novější živé kontroly nejsou vydávány za aktuální měření.

## Role

Ryzen / VM510 je infrastrukturní Docker host na produkčním PVE Ryzen. Soustřeďuje reverzní proxy a monitorovací stack, ale nenahrazuje dokumentaci chování jednotlivých aplikací.

Poslední doložená konfigurace VM:

- operační systém: Debian 13.5;
- 2 vCPU, 4 GB RAM, 20 GB disk;
- interní IP: `192.168.89.35`;
- Docker a QEMU Guest Agent byly funkční;
- Nginx Proxy Manager, Pulse, Mikr Manager a Uptime Kuma byly dostupné.

## Provozované služby

| Služba | Doložené nasazení | Přístup z NPM | Autoritativní funkční dokumentace |
|---|---|---|---|
| Nginx Proxy Manager | Compose `/opt/npm/compose.yaml`; přesný image tag a persistence vyžadují živé ověření | hostitelské porty `80`, `81`, `443`; síť `npm_default` | [DNS, NPM a HTTPS](DNS-NPM-HTTPS.md) |
| Pulse | Compose `/opt/pulse/docker-compose.yml`; image `rcourtman/pulse:6.1.2`; volume `pulse_data` doložené 2026-07-28 | `http://pulse:7655` | [Monitoring / Pulse](../Monitoring/Pulse.md) |
| Mikr Manager | Compose `/opt/mikr/docker-compose.yml`; image `ghcr.io/hreskiv/mikr:latest`; bind mounty `/opt/mikr/data` a `/opt/mikr/exports` doložené 2026-07-28 | `http://mikr-manager:3000`; hostitelské porty `3002`, `3443`, `5514` | [Monitoring / Mikr](../Monitoring/Mikr.md) |
| Uptime Kuma | samostatný kontejner `uptime-kuma`, image `louislam/uptime-kuma:2`, verze aplikace `2.5.0`, restart policy `always`; volume `uptime-kuma` → `/app/data` | `http://192.168.89.35:3001` | [Monitoring / Uptime Kuma](../Monitoring/Uptime-Kuma.md) |

Uptime Kuma byla 2026-08-03 ve stavu `healthy`. Kontejner byl připojený k sítím `bridge` a `npm_default`, ale NPM ji používá přes IP VM a publikovaný port; její funkce na členství v `npm_default` nezávisí.

Tag `latest` u Mikru není dokladem konkrétní běžící verze. Stejně tak image tag `:2` Kumy určuje hlavní větev, zatímco konkrétní ověřená verze aplikace je `2.5.0` k uvedenému datu.

## Docker sítě

- `npm_default` vytváří Nginx Proxy Manager.
- Pulse má vlastní `pulse_default` a v Compose trvale deklarovanou externí síť `npm_default`.
- Mikr Manager má vlastní `mikr_default` a v Compose trvale deklarovanou externí síť `npm_default`.
- Uptime Kuma má `bridge` a při poslední kontrole také `npm_default`; NPM ji však oslovuje přes `192.168.89.35:3001`.

Ruční `docker network connect` je vhodný jen pro diagnostiku. Trvalé vazby Pulse a Mikru musí zůstat deklarované v Compose, jinak se při novém vytvoření kontejneru ztratí.

## Hranice dokumentace

- Tento soubor je zdrojem pravdy pro roli VM510, způsob nasazení kontejnerů, Compose cesty, Docker sítě, persistence a pořadí infrastrukturní obnovy.
- [DNS-NPM-HTTPS.md](DNS-NPM-HTTPS.md) vlastní hostname, certifikáty a proxy upstreamy.
- Projekt [Monitoring](../Monitoring/README.md) vlastní nastavení aplikací, monitory, alarmy a Pushover.
- Projekt [Zálohy](../Zalohy/README.md) vlastní PBS joby, retenci a testy obnovy celé VM.

## Bezpečná inventura

Následující příkazy nemění konfiguraci:

```bash
hostnamectl
ip -brief address
df -hT
systemctl --failed
sudo systemctl status docker --no-pager
sudo docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}'
sudo docker network ls
sudo docker volume ls
```

Pro konkrétní kontejner lze použít sanitizovaný výpis:

```bash
sudo docker inspect --format 'Image={{.Config.Image}} Restart={{.HostConfig.RestartPolicy.Name}} Networks={{range $k,$v := .NetworkSettings.Networks}}{{$k}} {{end}} Mounts={{range .Mounts}}{{.Type}}:{{.Name}}{{.Source}} -> {{.Destination}} {{end}}' KONTEJNER
```

U Compose projektů:

```bash
cd /opt/npm   && sudo docker compose config --quiet && sudo docker compose ps
cd /opt/pulse && sudo docker compose config --quiet && sudo docker compose ps
cd /opt/mikr  && sudo docker compose config --quiet && sudo docker compose ps
```

Neupravený `docker compose config` může načíst `.env` a vypsat tajné hodnoty. Do chatu nebo repozitáře se kopíruje pouze sanitizovaný výsledek.

## Běžná provozní kontrola

Po restartu VM nebo změně kontejnerů:

1. ověřit stav VM, QEMU Guest Agentu, filesystému a Dockeru;
2. ověřit všechny běžící kontejnery, jejich image a health stav;
3. u Compose projektů zkontrolovat stav v jejich skutečných adresářích;
4. ověřit, že `npm_default` existuje a Pulse i Mikr jsou připojené ke své projektové i externí síti;
5. otevřít NPM a každou službu přes její interní HTTPS hostname;
6. ověřit hlavní funkci aplikace, nikoliv jen odpověď webového portu;
7. zkontrolovat poslední úspěšný PBS backup VM510.

## Korektní restart

### Celá VM

1. Ověřit, zda nejde pouze o poruchu jedné služby.
2. Zkontrolovat poslední backup a volné místo.
3. VM restartovat standardně z operačního systému nebo přes Guest Agent; vynucené zastavení použít pouze při incidentu.
4. Po startu projít celou provozní kontrolu.

### Jedna Compose služba

V příslušném adresáři:

```bash
sudo docker compose restart
sudo docker compose ps
sudo docker compose logs --tail=100
```

Pokud restart nepomůže, nejprve zachovat logy a ověřit konfiguraci. `docker compose down -v` se nepoužívá jako diagnostický krok; `-v` může odstranit persistentní volumes.

### Uptime Kuma

Kuma není doložená jako Compose projekt. Běžný restart:

```bash
sudo docker restart uptime-kuma
sudo docker ps --filter name=uptime-kuma
sudo docker logs --tail=100 uptime-kuma
```

Kontejner se nemaže ani nevytváří znovu, dokud není ověřený volume `uptime-kuma` a zamýšlený startovací příkaz.

## Aktualizace kontejnerů

1. Ověřit poslední použitelný backup VM510 a persistentní data měněné služby.
2. Zaznamenat současný image a aplikační verzi.
3. Přečíst poznámky k cílové verzi a určit návratovou cestu.
4. Aktualizovat pouze jednu službu a použít způsob odpovídající jejímu nasazení.
5. U Compose projektu použít `docker compose pull` a `docker compose up -d`; u samostatné Kumy postupovat podle jejího autoritativního dokumentu.
6. Ověřit volumes, sítě, porty, health, přihlášení a hlavní funkci aplikace.
7. U Pulse a Mikru ověřit členství v `npm_default`; u Kumy ověřit publikovaný port `3001` a HTTPS cestu přes NPM.
8. Po stabilizaci zkontrolovat následující PBS backup.

## Persistentní data a obnova

Samotný image nebo Compose soubor nestačí k obnově služby. Poslední doložené persistentní prvky jsou:

| Služba | Doložená persistence | Stav důkazu |
|---|---|---|
| NPM | **Vyžaduje ověření v živém systému.** | přesné volumes/bind mounty a obnova certifikátů nejsou v GitHubu doložené |
| Pulse | named volume `pulse_data` | doloženo 2026-07-28; živě znovu ověřit |
| Mikr | `/opt/mikr/data`, `/opt/mikr/exports` | doloženo 2026-07-28; živě znovu ověřit |
| Uptime Kuma | named volume `uptime-kuma` připojený na `/app/data` | ověřeno 2026-08-03 |

Tajné hodnoty z `.env`, databází, certifikátů ani výstupu Compose se do repozitáře nekopírují. Dokumentovat lze názvy souborů, cesty, volumes a bezpečný způsob doplnění tajných hodnot po obnově.

## Pořadí obnovy VM510

Po obnově celé VM z PBS:

1. Ověřit síťovou identitu VM, disk, filesystém, čas a Docker.
2. Ověřit přítomnost `/opt/npm`, `/opt/pulse`, `/opt/mikr` a všech doložených persistentních dat.
3. Spustit NPM jako první, protože vytváří síť `npm_default`.
4. Ověřit `npm_default` a poté spustit Pulse a Mikr z jejich Compose projektů.
5. Ověřit nebo spustit existující kontejner Uptime Kuma; nevytvářet prázdný nový volume stejného jména.
6. Ověřit interní porty a potom všechny HTTPS názvy.
7. V aplikacích zkontrolovat konfiguraci a historická data: proxy hosty a certifikáty, zdroje Pulse, zařízení Mikru, monitory Kumy.
8. Teprve po úplné přejímce považovat VM510 za obnovenou a vytvořit nový backup.

Pokud chybí NPM persistence nebo jiný volume, služba se neinicializuje naslepo. Zastaví se další zápisy a vybere se jiný snapshot nebo řízená aplikační obnova.

## Diagnostika

| Projev | První kontrola | Další postup |
|---|---|---|
| Všechny služby VM510 jsou nedostupné | stav VM, IP, disk a Docker | ověřit hostitele PVE Ryzen a systémové logy VM |
| Přímý port funguje, HTTPS název ne | NPM kontejner, `npm_default`, proxy host a certifikát | pokračovat v [DNS, NPM a HTTPS](DNS-NPM-HTTPS.md) |
| Pulse nebo Mikr vrací `502` | členství kontejneru v `npm_default` | opravit deklaraci v Compose, nikoliv pouze trvalý ruční workaround |
| Kuma vrací `502` | `uptime-kuma`, port `3001`, cíl NPM `192.168.89.35:3001` | členství Kumy v `npm_default` není pro současný upstream podmínkou |
| Kontejner se restartuje | `docker ps`, health a poslední logy | ověřit disk, paměť, konfiguraci a persistence před novým vytvořením |
| Po aktualizaci zmizela data | skutečně připojený volume nebo bind mount | zastavit další inicializaci; neobnovovat do prázdného cíle bez určení správné kopie |
| Docker nenaběhne | volné místo, `systemctl status docker`, journal | neodstraňovat `/var/lib/docker` ani volumes jako první pokus |

## Otevřené kontroly

**Vyžaduje ověření v živém systému.**

- [ ] Pořídit úplnou sanitizovanou inventuru NPM, Pulse a Mikru: běžící image/verze, restart policy, sítě, porty, volumes, bind mounty a umístění `.env` bez jejich obsahu.
- [ ] Ověřit a zdokumentovat persistentní data NPM včetně databáze, proxy hostů, certifikátů a bezpečného způsobu obnovy Cloudflare DNS challenge.
- [ ] Ověřit, že Pulse stále používá `pulse_data` a Mikr `/opt/mikr/data` a `/opt/mikr/exports`.

Zahrnutí VM510 do PBS jobu a testovací restore celé VM jsou evidované pouze v [PBS a disaster recovery](../Zalohy/PBS-DR.md).
