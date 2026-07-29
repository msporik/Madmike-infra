# Pulse

## Role

Pulse je hlavní přehled stavu Proxmox VE a Proxmox Backup Serveru. Slouží pro kapacitu, vytížení, stav VM/LXC, zálohy, ZFS, fyzické disky, teploty a základní zdravotní stav infrastruktury.

Nejde o monitoring „pro monitoring“. Cílem je bez preventivního procházení několika systémů včas poznat stav ohrožující provoz nebo obnovitelnost záloh.

## Poslední doložený stav k 2026-07-28

- Pulse server na VM510 byl aktualizován z `6.0.5` na `6.1.2`.
- Kontejner byl `healthy`.
- Webové rozhraní: `https://pulse.mikehub.cz`.
- Telemetrie aplikace byla vypnutá.
- Na verzi `6.1.2` byly aktualizovány všechny tři agenty:
  - `pve` – domácí PVE Ryzen;
  - `pbs-madmike` – PVE Dell;
  - `pbs-madmike-offsite` – PBS ve VM200.
- Pulse správně rozpoznával Proxmox VE a PBS; Docker a Kubernetes nejsou cílem tohoto nasazení.

Tento stav je datovaný snapshot. Při konsolidaci nebyl znovu ověřen proti živé VM510.

## Pokrytí Pulse

| Požadavek | Stav v doloženém snapshotu |
|---|---|
| Dostupnost Proxmox/PBS hostů | pokryto |
| CPU, RAM, load a uptime | pokryto |
| Stav VM a LXC | pokryto |
| Kapacita storage a PBS datastore | pokryto |
| ZFS stav `ONLINE / DEGRADED / FAULTED` | pokryto |
| ZFS read/write/checksum chyby | pokryto |
| Fyzické disky a souhrnný SMART | pokryto |
| Teploty disků a životnost SSD/NVMe | pokryto s výjimkou zobrazení WD Red |
| Poslední zálohy, stáří, velikost a `Verified` | pokryto |
| Krátkodobá historie a grafy | pokryto |

Pulse proto zůstává hlavním přehledem PVE/PBS. Kvůli jeho hranicím není důvod vracet Zabbix, Checkmk ani Beszel.

## Fyzické disky – snapshot 2026-07-28

Pulse zobrazoval všech 10 fyzických disků, včetně SAS disků za HBA330:

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

### `tank-pbs`

PVE pohled na storage `tank-pbs` ukazoval přibližně 97% obsazení, přestože PBS datastore byl reálně zaplněný jen přibližně ze 3 %. Důvodem bylo započtení thick `refreservation` virtuálního disku VM200.

Skutečná využitelná kapacita záloh se proto posuzuje podle PBS datastore `backup`, nikoliv podle červeného procenta PVE storage `tank-pbs`.

### Orphaned backups

Pulse označoval jako orphaned zálohy VM401, VM501 a LXC100:

- VM401 a VM501 mají stejné VMID na produkčním Ryzenu i u vypnutých testovacích/DR kopií na Dellu, takže je Pulse neumí jednoznačně spárovat;
- LXC100 už na žádném PVE hostu neexistuje, jeho zachovaná záloha je proto orphaned oprávněně.

Tento stav sám o sobě neznamená poškození záloh. Historické a DR objekty se nemažou bez určení jejich role.

## Zálohy – snapshot 2026-07-28

Pulse zobrazoval poslední zálohy, jejich stáří, velikost a stav `Verified`; kontrolované běhy Backup, Prune a Garbage Collection byly `OK`. Zobrazený rozsah ještě obsahoval CT100, který byl následně při konsolidaci monitoringu odstraněn. Živý výběr objektů backup jobu proto zůstává k ověření.

Přesné rozvrhy, retence, storage architektura a testy obnovy jsou v [PBS a disaster recovery](../Zalohy/PBS-DR.md). Dashboard skutečný test obnovy nenahrazuje.

## Hranice Pulse

Pulse není jediným zdrojem jistoty pro celý zálohovací řetězec:

- není prakticky potvrzené autoritativní upozornění na každý neúspěch úloh Backup, Verify, Prune a Garbage Collection;
- nehlídá stáří posledního ZFS scrubu ani stav „scrub už dlouho neběžel“;
- SMART zobrazuje souhrnně a nenahrazuje všechny atributy a error log `smartctl`;
- Community verze poskytuje jen krátkou historii, nikoliv dlouhodobé kapacitní trendy;
- žádný dashboard nenahrazuje praktickou obnovu.

Notifikace Pulse ani nativní notifikace PVE/PBS nebyly při poslední dokumentované kontrole prakticky otestovány.

## Rozdělení odpovědností

- **Pulse:** hlavní přehled PVE/PBS, výkon, kapacity, fyzické disky, SMART, teploty, ZFS a přehled záloh.
- **Nativní notifikace PVE/PBS:** autoritativní hlášení neúspěchu Backup, Verify, Prune a Garbage Collection; podle možností také problémů scrubů.
- **Uptime Kuma:** dostupnost služeb a upozornění při delším výpadku hostu nebo Pulse.
- **Mikr Manager:** monitoring MikroTiků.
- **Ruční test obnovy:** občasný důkaz skutečné obnovitelnosti.

## Navazující práce

- [ ] Zjistit současnou konfiguraci nativních notifikačních cílů a pravidel zvlášť na PVE Ryzen, PVE Dell a PBS.
- [ ] Poslat vestavěnou testovací notifikaci ze všech tří systémů.
- [ ] Bez narušení produkčních záloh ověřit hlášení neúspěšného Backup, Verify, Prune a Garbage Collection jobu.
- [ ] Ověřit plánování ZFS scrubů na `tank-pbs`, `tank-nas`, `tank-ssd` a `tank-hdd` a způsob hlášení chyby nebo příliš starého běhu.
- [ ] Rozdělit události mezi Pulse a nativní notifikace bez duplicit a úspěšné běhy neposílat jako šum.
- [ ] Vybrané problémy a následné obnovení směrovat do Telegramu.
