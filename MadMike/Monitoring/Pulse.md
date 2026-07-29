# Pulse

## Role

Pulse je hlavní přehled stavu Proxmox VE a Proxmox Backup Server. Slouží pro kapacitu, vytížení, stav VM/LXC, zálohy, ZFS, fyzické disky, teploty a základní zdravotní stav infrastruktury.

Nejde o monitoring „pro monitoring“. Cílem je bez preventivního procházení několika systémů včas poznat stav ohrožující provoz nebo obnovitelnost záloh.

## Ověřený stav k 2026-07-28

- Pulse server na Ryzen / VM510 byl aktualizován z `6.0.5` na `6.1.2`.
- Kontejner je `healthy`.
- Webové rozhraní: `https://pulse.mikehub.cz`.
- Telemetrie aplikace je vypnutá.
- Na `6.1.2` byly aktualizovány všechny tři agenty:
  - `pve` – domácí PVE Ryzen;
  - `pbs-madmike` – PVE Dell;
  - `pbs-madmike-offsite` – PBS ve VM200.
- Pulse správně rozpoznává Proxmox VE a PBS; Docker a Kubernetes nejsou cílem tohoto nasazení.

## Fyzické disky

Pulse vidí všech 10 fyzických disků, včetně SAS disků za HBA330:

- členství disků v poolech;
- souhrnný SMART stav;
- teploty;
- u SSD/NVMe také zbývající životnost.

Všechny zobrazené disky byly při kontrole `Healthy`.

| Skupina | Ověřená teplota |
|---|---|
| Dell SAS HDD | přibližně 45–48 °C |
| Ryzen NVMe | přibližně 55 °C |
| Ryzen Micron SSD | přibližně 43 °C |
| systémový Intel SSD | přibližně 36 °C |
| Ryzen WD Red | 39 a 38 °C podle `smartctl` |

U obou WD Redů Pulse zobrazuje `TEMP —`, přestože disky teplotu správně poskytují. Jde o omezení zobrazení Pulse 6.1.2, nikoli závadu disků.

## Pokrytí Pulse

| Požadavek | Stav |
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

Pulse proto zůstává hlavním přehledem. Kvůli jeho hranicím není důvod vracet Zabbix, Checkmk ani Beszel.

## Důležitá interpretační výjimka

PVE pohled na storage `tank-pbs` ukazoval přibližně 97% obsazení, přestože PBS datastore byl reálně zaplněný jen přibližně ze 3 %. Důvodem bylo započtení thick `refreservation` virtuálního disku VM200.

Skutečná využitelná kapacita záloh se proto posuzuje podle PBS datastore `backup`, nikoli podle červeného procenta PVE storage `tank-pbs`.

## Ověřený zálohovací řetězec

Při kontrole 2026-07-28 Pulse zobrazoval:

- denní zálohy CT100, VM401, VM501 a VM510 s posledními běhy `OK`;
- backup job z PVE Ryzen na PBS denně ve 02:00;
- poslední zálohy, jejich stáří, velikost a stav `Verified`;
- denní Prune;
- denní Garbage Collection s posledním kontrolovaným během `OK`;
- Verify nových záloh a opakované ověření již ověřených dat po 30 dnech.

Přesný poslední ověřený rozvrh, retence a storage architektura jsou v [PBS a disaster recovery](../Zalohy/PBS-DR.md). CT100 byl následně při konsolidaci monitoringu odstraněn; živý rozsah backup jobu je proto potřeba znovu zkontrolovat.

Obnova Nextcloudu i Windows byla prakticky ověřena. Dashboard však skutečný test obnovy nenahrazuje.

## Hranice Pulse

Pulse není jediným zdrojem jistoty pro celý zálohovací řetězec:

- není potvrzené autoritativní upozornění na každý neúspěch úloh Backup, Verify, Prune a Garbage Collection;
- nehlídá stáří posledního ZFS scrubu ani stav „scrub už dlouho neběžel“;
- SMART zobrazuje souhrnně a nenahrazuje všechny atributy a error log `smartctl`;
- Community verze poskytuje jen krátkou historii, nikoli dlouhodobé kapacitní trendy;
- žádný dashboard nenahrazuje praktickou obnovu.

## Rozdělení odpovědností

- **Pulse:** hlavní přehled PVE/PBS, výkon, kapacity, fyzické disky, SMART, teploty, ZFS a přehled záloh.
- **Nativní notifikace PVE/PBS:** autoritativní hlášení neúspěchu Backup, Verify, Prune a Garbage Collection; podle možností také problémy scrubu.
- **Uptime Kuma:** dostupnost služeb a upozornění při výpadku hostu nebo Pulse.
- **Mikr:** monitoring a správa MikroTiků.
- **Ruční test obnovy:** občasný důkaz skutečné obnovitelnosti.

## Orphaned backups

Pulse označuje jako orphaned zálohy VM401, VM501 a LXC100:

- VM401 a VM501 mají stejné VMID na produkčním Ryzenu i u vypnutých testovacích/DR kopií na Dellu, takže je Pulse neumí jednoznačně spárovat;
- LXC100 už na žádném PVE hostu neexistuje, jeho zachovaná záloha je proto orphaned oprávněně.

Tento stav sám o sobě neznamená poškození záloh. Historické a DR objekty se nemažou bez určení jejich role.

## Navazující práce

- [ ] Zjistit současnou konfiguraci nativních notifikačních cílů a pravidel zvlášť na PVE Ryzen, PVE Dell a PBS.
- [ ] Poslat vestavěnou testovací notifikaci ze všech tří systémů.
- [ ] Bez narušení produkčních záloh ověřit hlášení neúspěšného Backup, Verify, Prune a Garbage Collection jobu.
- [ ] Ověřit plánování ZFS scrubů na `tank-pbs`, `tank-nas`, `tank-ssd` a `tank-hdd` a způsob hlášení chyby nebo příliš starého běhu.
- [ ] Rozdělit události mezi Pulse a nativní notifikace bez duplicit a úspěšné běhy neposílat jako šum.
- [ ] Vybrané problémy a následné obnovení směrovat do Telegramu.
