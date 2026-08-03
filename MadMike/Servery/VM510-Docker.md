# VM510 – Docker infrastruktura

## Role

Ryzen / VM510 je infrastrukturní Docker host na produkčním PVE Ryzen. Soustřeďuje reverzní proxy a současný monitorovací stack, ale nenahrazuje dokumentaci chování jednotlivých aplikací.

Poslední doložený stav k 2026-07-28:

- operační systém: Debian 13.5;
- 2 vCPU, 4 GB RAM, 20 GB disk;
- interní IP: `192.168.89.35`;
- Docker a QEMU Guest Agent byly funkční;
- Nginx Proxy Manager, Pulse, Mikr Manager a Uptime Kuma byly dostupné.

Při konsolidaci nebyla VM znovu ověřena proti živému systému. Níže jsou proto oddělené doložené údaje a otevřené body obnovy.

## Provozované služby

| Služba | Doložený způsob nasazení | Přístup z NPM | Autoritativní funkční dokumentace |
|---|---|---|---|
| Nginx Proxy Manager | Compose `/opt/npm/compose.yaml` | porty hostitele `80`, `81`, `443`; síť `npm_default` | [DNS, NPM a HTTPS](DNS-NPM-HTTPS.md) |
| Pulse | Compose `/opt/pulse/docker-compose.yml`; obraz `rcourtman/pulse:6.1.2` | `http://pulse:7655` | [Monitoring / Pulse](../Monitoring/Pulse.md) |
| Mikr Manager | Compose `/opt/mikr/docker-compose.yml`; obraz `ghcr.io/hreskiv/mikr:latest` | `http://mikr-manager:3000`; hostitelské porty `3002`, `3443`, `5514` | [Monitoring / Mikr](../Monitoring/Mikr.md) |
| Uptime Kuma | stávající Docker kontejner, nikoliv Compose | `http://192.168.89.35:3001` | [Monitoring / Uptime Kuma](../Monitoring/Uptime-Kuma.md) |

U Pulse je verze `6.1.2` doložená k 2026-07-28. Tag `latest` u Mikru ani neuvedená verze NPM a Kumy nejsou dokladem aktuálně běžící verze; tu je nutné ověřit na živé VM.

## Docker sítě

- `npm_default` vytváří Nginx Proxy Manager.
- Pulse má vlastní `pulse_default` a v Compose trvale deklarovanou externí síť `npm_default`.
- Mikr Manager má vlastní `mikr_default` a v Compose trvale deklarovanou externí síť `npm_default`.
- Uptime Kuma je z NPM dosažitelná přes IP VM a publikovaný port `3001`; její funkce proto nezávisí na ručním připojení k `npm_default`.

Ruční `docker network connect` je vhodný jen pro diagnostiku. Trvalé vazby Pulse a Mikru musí zůstat deklarované v Compose, jinak se při novém vytvoření kontejneru ztratí.

## Hranice dokumentace

- Tento soubor je zdrojem pravdy pro roli VM510, způsob nasazení kontejnerů, Compose cesty, Docker sítě a obnovitelnost hostu.
- [DNS-NPM-HTTPS.md](DNS-NPM-HTTPS.md) vlastní hostname, certifikáty a proxy upstreamy.
- Projekt [Monitoring](../Monitoring/README.md) vlastní nastavení aplikací, monitory, alarmy a Telegram.
- Projekt [Zálohy](../Zalohy/README.md) vlastní PBS joby, retenci a testy obnovy celé VM.

## Persistentní data a obnova

Samotná existence Compose souboru nestačí k obnově služby. V dokumentaci zatím nejsou živě ověřené:

- přesné image tagy všech služeb;
- hostitelské cesty, named volumes a umístění persistentních dat;
- umístění souborů `.env` a dalších neveřejných konfiguračních souborů;
- restart policy a přesné startovací parametry stávající Uptime Kumy;
- zahrnutí VM510 do současného PBS backup jobu;
- praktický postup obnovy celé VM nebo jednotlivých služeb.

Tajné hodnoty z `.env`, databází, certifikátů ani výstupu `docker compose config` se do repozitáře nekopírují. Dokumentovat lze jen názvy souborů, cesty, objemy a bezpečný postup doplnění tajných hodnot po obnově.

Uptime Kuma se nemá převádět na Compose jen kvůli sjednocení vzhledu. Nejdřív se zaznamená současný kontejner, jeho persistentní data a postup obnovení; případná změna způsobu nasazení musí mít konkrétní provozní přínos.

## Základní provozní kontrola

Po restartu VM nebo změně kontejnerů:

1. ověřit stav Dockeru a běžících kontejnerů;
2. u Compose projektů zkontrolovat stav v jejich skutečných adresářích;
3. ověřit připojení Pulse a Mikru k `npm_default`;
4. otevřít NPM a každou službu přes její interní HTTPS hostname;
5. zkontrolovat hlavní funkci aplikace, nikoliv jen odpověď webového portu.

Jde o opakovaný provozní postup, proto není vedený jako sada checkboxů v centrálním `TODO.md`.

## Otevřené kroky

- [ ] Pořídit sanitizovanou živou inventuru VM510: kontejnery, image tagy, Compose projekty, restart policy, sítě, porty, volumes a hostitelské cesty bez tajných hodnot.
- [ ] Zdokumentovat současný způsob vytvoření, startu a obnovy Uptime Kumy včetně umístění jejích persistentních dat.
- [ ] Po ověření persistentních dat doplnit stručný pořadník obnovy NPM, Pulse, Mikru a Kumy.

Zahrnutí VM510 do PBS backup jobu a test obnovy celé VM jsou vedené v [PBS a disaster recovery](../Zalohy/PBS-DR.md).
