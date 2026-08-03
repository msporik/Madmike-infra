# Pulse

> Poslední doložený provozní stav: **2026-07-28**. Nejde o potvrzení současného živého stavu.

## Účel a role

Pulse je hlavní přehled stavu Proxmox VE a Proxmox Backup Serveru. Slouží pro sledování hostů, VM/LXC, výkonu, kapacit, ZFS, fyzických disků a záloh.

Cílem je bez preventivního procházení několika systémů včas zjistit stav ohrožující provoz nebo obnovitelnost dat. Pulse nenahrazuje nativní diagnostiku PVE/PBS ani praktické testy obnovy.

## Hranice dokumentace

- Tento dokument je autoritativní pro roli Pulse, jeho aplikační kontrolu, aktualizaci, interpretaci zobrazených stavů a testy souvisejících notifikací.
- Docker nasazení, Compose soubor, image, porty, sítě a persistentní data jsou v [VM510 – Docker infrastruktura](../Servery/VM510-Docker.md).
- DNS, HTTPS, certifikát a směrování přes Nginx Proxy Manager jsou v [Interní DNS, NPM a HTTPS](../Servery/DNS-NPM-HTTPS.md).
- Backup joby, retence, údržba PBS a testy obnovy jsou v [PBS a disaster recovery](../Zalohy/PBS-DR.md).
- Dostupnost Pulse jako služby sleduje [Uptime Kuma](Uptime-Kuma.md).
- Směrování vybraných alarmů a recovery zpráv patří do [Telegram notifikací](Telegram.md).

Běžný přístup: `https://pulse.mikehub.cz`

## Poslední doložený stav

K 2026-07-28:

- Pulse server byl aktualizován z verze `6.0.5` na `6.1.2`;
- kontejner byl `healthy`;
- telemetrie aplikace byla vypnutá;
- Pulse správně rozpoznával Proxmox VE a PBS;
- Docker a Kubernetes nebyly cílem tohoto nasazení;
- všechny tři instalace agentů byly aktualizovány na verzi `6.1.2`.

| Zdroj | Role |
|---|---|
| `pve` | domácí PVE Ryzen |
| `pbs-madmike` | PVE Dell v offsite/DR lokalitě |
| `pbs-madmike-offsite` | PBS ve VM200 |

Stav `healthy` potvrzuje úspěšný healthcheck kontejneru. Sám o sobě nepotvrzuje dostupnost všech agentů ani správnost jejich dat.

## Pokrytí Pulse

| Oblast | Stav v doloženém snapshotu |
|---|---|
| Dostupnost PVE/PBS hostů | pokryto |
| CPU, RAM, load a uptime | pokryto |
| Stav VM a LXC | pokryto |
| Kapacita storage a PBS datastore | pokryto |
| ZFS stav `ONLINE`, `DEGRADED`, `FAULTED` | pokryto |
| ZFS read/write/checksum chyby | pokryto |
| Fyzické disky a souhrnný SMART | pokryto |
| Teploty disků a životnost SSD/NVMe | pokryto s výjimkou zobrazení WD Red |
| Poslední zálohy, jejich stáří, velikost a stav `Verified` | pokryto |
| Krátkodobá historie a grafy | pokryto |

## Fyzické disky

K 2026-07-28 Pulse zobrazoval všech deset fyzických disků, včetně SAS disků za HBA330:

- členství disků v poolech;
- souhrnný SMART stav;
- teploty;
- u SSD/NVMe také zbývající životnost.

Všechny zobrazené disky byly při kontrole `Healthy`.

| Skupina | Doložená teplota |
|---|---|
| Dell SAS HDD | přibližně 45–48 °C |
| Ryzen NVMe | přibližně 55 °C |
| Ryzen Micron SSD | přibližně 43 °C |
| systémový Intel SSD | přibližně 36 °C |
| Ryzen WD Red | 39 a 38 °C podle `smartctl` |

U obou WD Redů Pulse zobrazoval `TEMP —`, přestože disky teplotu správně poskytovaly. Šlo o omezení zobrazení Pulse 6.1.2, nikoliv o doloženou závadu disků.

## Důležité interpretační výjimky

### Kapacita `tank-pbs`

PVE pohled na storage `tank-pbs` ukazoval přibližně 97% obsazení, přestože PBS datastore `backup` byl reálně využitý přibližně ze 3 %.

Důvodem bylo započtení thick `refreservation` virtuálního disku VM200. Pro skutečnou kapacitu záloh je autoritativní PBS datastore `backup`, nikoliv procento PVE storage `tank-pbs`.

### Orphaned backups

Pulse označoval jako orphaned zálohy VM401, VM501 a LXC100:

- VM401 a VM501 mají stejná VMID na produkčním Ryzenu i u vypnutých testovacích nebo DR kopií na Dellu, takže je Pulse neumí jednoznačně spárovat;
- LXC100 už na žádném PVE hostu neexistuje, jeho zachovaná záloha je proto orphaned oprávněně.

Tento stav sám o sobě neznamená poškození záloh. Historické nebo DR objekty se nemažou bez ověření jejich původu a role.

## Interpretace záloh

Pulse zobrazoval poslední zálohy, jejich stáří, velikost a stav `Verified`. Kontrolované běhy Backup, Prune a Garbage Collection byly k 2026-07-28 `OK`.

Zobrazený rozsah ještě obsahoval CT100, který byl následně při konsolidaci monitoringu odstraněn. Současný výběr objektů backup jobu je autoritativně vedený v [PBS a disaster recovery](../Zalohy/PBS-DR.md).

Pulse nenahrazuje:

- kontrolu konkrétní chyby v PVE/PBS Tasks;
- potvrzení každého běhu Verify, Prune a Garbage Collection;
- ověření plánování a stáří ZFS scrubů;
- úplný výstup `smartctl`;
- praktický test obnovy.

## Provozní kontrola

Na VM510 přejít do Compose projektu Pulse uvedeného v [VM510 – Docker infrastruktura](../Servery/VM510-Docker.md) a spustit:

```bash
sudo docker compose config --quiet
sudo docker compose ps
sudo docker compose logs --tail=100
```

V aplikaci ověřit:

1. přihlášení přes `https://pulse.mikehub.cz`;
2. dostupnost zdrojů `pve`, `pbs-madmike` a `pbs-madmike-offsite`;
3. stav monitorovaných hostů;
4. stav ZFS poolů;
5. fyzické disky a SMART;
6. přehled posledních záloh;
7. zda známé výjimky WD Red, `tank-pbs` a orphaned backups odpovídají dokumentovanému chování.

Neupravený výstup `docker compose config` se nekopíruje do dokumentace ani chatu, protože může obsahovat hodnoty načtené z `.env`.

## Restart služby

V Compose projektu Pulse:

```bash
sudo docker compose restart
sudo docker compose ps
sudo docker compose logs --tail=100
```

Pokud běžný restart nepomůže:

```bash
sudo docker compose up -d
sudo docker compose ps
sudo docker compose logs --tail=100
```

Po restartu provést [provozní kontrolu](#provozní-kontrola). Příkaz `docker compose down -v` se nepoužívá jako běžný diagnostický krok; parametr `-v` může odstranit persistentní Docker volumes.

## Aktualizace Pulse serveru

Před aktualizací:

1. ověřit poslední použitelnou zálohu VM510 podle [PBS a disaster recovery](../Zalohy/PBS-DR.md);
2. zkontrolovat současný stav všech tří agentů;
3. zaznamenat běžící verzi serveru a agentů;
4. ověřit dostupnost PVE/PBS systémů.

V Compose projektu Pulse:

```bash
sudo docker compose config --quiet
sudo docker compose pull
sudo docker compose up -d
sudo docker compose ps
sudo docker compose logs --tail=100
```

Po aktualizaci provést [provozní kontrolu](#provozní-kontrola) a ověřit verzi serveru i všech tří agentů.

Při chybě se nejdříve zachovají logy a zjištěný stav. Kontejner, volume ani aplikační data se nemažou jako první pokus o opravu.

## Diagnostika typických stavů

| Zobrazený stav | První autoritativní kontrola |
|---|---|
| Pulse není dostupný | stav Pulse kontejneru a jeho logy na VM510 |
| Přímá služba funguje, ale HTTPS název ne | [DNS, NPM a HTTPS](../Servery/DNS-NPM-HTTPS.md) |
| Jeden agent je nedostupný | příslušný PVE/PBS host, síť a agent |
| Host je nedostupný | příslušný host a síťové propojení |
| VM nebo LXC neběží | příslušný Proxmox VE |
| ZFS `DEGRADED`, `FAULTED` nebo vykazuje chyby | `zpool status -v` na příslušném hostu |
| SMART problém | `smartctl` nad konkrétním diskem na hostu |
| Záloha chybí nebo je stará | příslušný backup job a Tasks v PVE/PBS |
| `tank-pbs` ukazuje přibližně 97 % | skutečné využití PBS datastore `backup` |
| VM401 nebo VM501 je orphaned | ověřit produkční a DR kopie; nic automaticky nemazat |
| LXC100 je orphaned | zachovaná historická záloha; nic nemazat bez samostatného rozhodnutí |

Pulse je přehledová vrstva. Při alarmu se závada potvrzuje v systému, který je pro danou oblast autoritativní.

## Obnova služby

Pokud Pulse nefunguje, stav infrastruktury se mezitím kontroluje přímo v PVE a PBS. Výpadek Pulse sám o sobě neznamená výpadek monitorovaných systémů.

Poškozený nebo chybějící kontejner se nevytváří naslepo, dokud nejsou ověřena jeho persistentní data a současná konfigurace. Infrastrukturní obnova Pulse a VM510 se řídí dokumenty:

- [VM510 – Docker infrastruktura](../Servery/VM510-Docker.md);
- [PBS a disaster recovery](../Zalohy/PBS-DR.md).

Po obnově provést [provozní kontrolu](#provozní-kontrola) a ověřit verzi serveru.

## Hranice Pulse a nativní notifikace

Pulse není jediným zdrojem jistoty pro celý zálohovací řetězec:

- není prakticky potvrzené autoritativní upozornění na každý neúspěch úloh Backup, Verify, Prune a Garbage Collection;
- nehlídá stáří posledního ZFS scrubu ani stav „scrub už dlouho neběžel“;
- SMART zobrazuje souhrnně a nenahrazuje všechny atributy a error log `smartctl`;
- Community verze poskytuje jen krátkou historii;
- žádný dashboard nenahrazuje praktickou obnovu.

Nativní notifikace PVE/PBS mají být autoritativním zdrojem pro selhání:

- Backup jobu;
- Verify;
- Prune;
- Garbage Collection;
- podle ověřených možností také ZFS scrubů.

Notifikace Pulse ani nativní notifikace PVE/PBS nebyly při poslední dokumentované kontrole prakticky otestovány.

## Otevřené úkoly

> Následující body vyžadují ověření v živém systému.

- [ ] Zdokumentovat přesný postup aktualizace Pulse agentů na PVE Ryzen, PVE Dell a PBS.
- [ ] Ověřit současnou verzi Pulse serveru a všech tří agentů.
- [ ] Zjistit současnou konfiguraci notifikačních cílů a pravidel na PVE Ryzen, PVE Dell a PBS.
- [ ] Poslat vestavěnou testovací notifikaci ze všech tří systémů.
- [ ] Bez narušení produkčních záloh ověřit hlášení neúspěšného Backup jobu.
- [ ] Ověřit hlášení neúspěšného Verify, Prune a Garbage Collection jobu.
- [ ] Ověřit plánování ZFS scrubů a způsob hlášení chyby nebo příliš starého posledního běhu.
- [ ] Ověřit, že běžné úspěšné úlohy nevytvářejí notifikační šum.

Směrování výsledných alarmů a recovery zpráv je vedené v [Telegram notifikacích](Telegram.md).
