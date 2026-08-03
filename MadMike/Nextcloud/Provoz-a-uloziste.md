# Provoz a úložiště

## Stav dokumentace

Níže uvedená konfigurace je poslední doložený stav z dostupné dokumentace. Při auditu 29. 7. 2026 nebyla porovnána s živou konfigurací VM401. Neověřené údaje jsou výslovně označené.

## Nasazení

Nextcloud je vedený jako produkční **Ryzen / VM401** na PVE Ryzen.

| Parametr | Poslední doložený stav |
|---|---|
| vCPU | 2 |
| RAM | 4 GB |
| Systémový disk | 64 GB na `local-lvm` |
| Datový disk | 1 000 GB, historicky ext4, v PVE vedený na storage ID `tank-nas-zfs` |
| Datový adresář | `/var/nc-data` |
| Interní IP | `192.168.89.33` |
| QEMU Guest Agent | funkční |

Storage ID `tank-nas-zfs` je doložené z konfigurace VM, ale zatím není ověřené, na který fyzický ZFS pool na současném hostiteli odkazuje. Nesmí být automaticky zaměněné za `tank-ssd` ani `tank-hdd`. Fyzické mapování storage patří do dokumentace [PVE Ryzen](../Servery/PVE-Ryzen.md).

## Aplikační vrstvy

Při ověřené obnově VM byly funkční:

- Apache;
- MariaDB;
- Nextcloud;
- přístup k uživatelským datům.

**Vyžaduje ověření v živém systému.** Přesné verze operačního systému, Nextcloudu, PHP, Apache a MariaDB, cesta instalace Nextcloudu, PHP handler, název databáze a databázového uživatele, nastavení Redis či jiné cache a způsob spouštění background jobs.

Příkazy níže předpokládají Debian/Ubuntu, `systemd` a standardní konzolový nástroj Nextcloudu `occ`. Pokud se živá instalace liší, nejprve se zjistí skutečné názvy služeb a cesta instalace; příkazy se nespouštějí naslepo.

## Bezpečná základní kontrola

### Na PVE Ryzen

Bez změny konfigurace:

```bash
qm status 401
qm config 401
pvesm status
```

Kontroluje se, že VM401 běží, její disky odpovídají dokumentaci a storage jsou dostupné. Výstupy mohou obsahovat neveřejné údaje a před zápisem do GitHubu nebo chatu se musí zkontrolovat.

### Uvnitř VM401

```bash
hostnamectl
ip -brief address
findmnt /var/nc-data
df -hT
systemctl status apache2 --no-pager
systemctl status mariadb --no-pager
```

Stav Nextcloudu se ověří z jeho skutečného instalačního adresáře. Typický příkaz je:

```bash
sudo -u www-data php occ status
```

Pokud `occ` v aktuálním adresáři není, nejprve se cesta dohledá v konfiguraci Apache; nevytváří se druhá instalace a nic se nepřesouvá.

Očekávaný výsledek:

- VM má správnou síťovou identitu;
- `/var/nc-data` je skutečně připojený datový filesystem, nikoli prázdný adresář na systémovém disku;
- oba disky mají dostatečnou volnou kapacitu;
- Apache a MariaDB jsou aktivní;
- Nextcloud je nainstalovaný, není nechtěně v maintenance mode a nehlásí potřebu nedokončené aktualizace.

## Provozní diagnostika

### Web neodpovídá

1. Ověřit, zda VM401 běží a odpovídá na interní síti.
2. Ověřit `findmnt /var/nc-data` a kapacitu disků.
3. Ověřit Apache a MariaDB.
4. Ověřit `occ status`.
5. Zkontrolovat poslední relevantní záznamy bez zveřejnění citlivého obsahu:

```bash
journalctl -u apache2 -n 100 --no-pager
journalctl -u mariadb -n 100 --no-pager
```

6. Pokud interní služba funguje, pokračovat kontrolou veřejné cesty podle [Přístupu a uživatelů](Pristup-a-uzivatele.md).

Restart služby se používá až po zjištění příčiny nebo jako kontrolovaný obnovovací krok. Samotný restart není diagnóza.

### Datový disk není připojený

Pokud `findmnt /var/nc-data` nic nevrátí:

1. zastavit zápisy do Nextcloudu; podle stavu služby lze dočasně zastavit Apache;
2. ověřit, zda je datový disk viditelný v `qm config 401` a uvnitř VM;
3. zkontrolovat skutečné blokové zařízení, filesystem a konfiguraci mountu;
4. nepřipojovat zařízení podle odhadu a nevytvářet nový filesystem;
5. po bezpečném obnovení mountu ověřit vlastnictví, přístup k existujícím datům, `occ status` a funkci webu.

Nextcloud se nespouští nad prázdným `/var/nc-data`, protože by mohl vytvořit nebo používat náhradní stav na systémovém disku.

### Dochází místo

```bash
df -hT
du -xhd1 /var 2>/dev/null
du -xhd1 /var/nc-data 2>/dev/null
```

Před mazáním se určí, zda je plný systémový nebo datový disk a co kapacitu spotřebovalo. Ručně se nemažou soubory z datového adresáře, databáze ani interních adresářů Nextcloudu. Koš, verze a aplikační data se spravují podporovanými funkcemi Nextcloudu až po ověření aktuální verze a zálohy.

### MariaDB neběží

1. zkontrolovat kapacitu systémového disku;
2. přečíst stav služby a poslední logy;
3. ověřit, zda incident nesouvisí s filesystemem nebo náhlým výpadkem;
4. neprovádět opravu databázových tabulek, inicializaci ani obnovu bez aktuální zálohy a určení příčiny;
5. po obnovení databáze ověřit `occ status`, přihlášení a práci se soubory.

### Maintenance mode nebo nedokončená aktualizace

Nejprve se zjistí příčina a stav aktualizace. Maintenance mode se nevypíná automaticky, pokud probíhá databázová migrace nebo je aktualizace neúplná. Podporované `occ` příkazy se použijí až po ověření živé verze a oficiálního aktualizačního postupu pro danou verzi.

## Aktualizace a údržba

Pravidelné aktualizace Nextcloudu ani jeho aplikací se v současnosti neprovádějí. Jde o známé provozní a bezpečnostní riziko.

### Před aktualizací

1. potvrdit poslední úspěšnou PBS zálohu VM401 a její stáří;
2. ověřit volné místo na systémovém i datovém disku;
3. zaznamenat živé verze OS, Nextcloudu, PHP, Apache, MariaDB a používaných aplikací;
4. podle oficiální dokumentace určit podporovanou aktualizační cestu; hlavní verze se nepřeskakují bez výslovné podpory;
5. ověřit kompatibilitu aplikací, PHP a databáze;
6. stanovit návratový bod a dobu odstávky;
7. předem určit správný instalační adresář a způsob aktualizace současného nasazení.

Snapshot běžící VM není náhradou PBS zálohy ani databázově konzistentního návratového postupu.

### Provedení

- Použít jediný podporovaný aktualizační mechanismus odpovídající živé instalaci.
- Neprovádět souběžně aktualizaci OS, databáze, PHP a několika hlavních verzí Nextcloudu bez mezikontrol.
- Po každém požadovaném mezikroku ověřit stav aplikace a dokončit případné databázové migrace podle dokumentace dané verze.
- Neukončovat násilně proces jen proto, že delší dobu běží; nejprve ověřit jeho stav a logy.

### Kontrola po aktualizaci

1. `occ status` a správná verze;
2. maintenance mode je vypnutý;
3. přihlášení administrátora a běžného uživatele;
4. zobrazení, stažení, nahrání, přejmenování a smazání testovacího souboru;
5. synchronizace alespoň jednoho používaného klienta;
6. background jobs a cron;
7. stav aplikací a administrační přehled;
8. aplikační, Apache a databázové logy;
9. HTTPS z veřejné i interní strany;
10. následná úspěšná PBS záloha.

## Background jobs

**Vyžaduje ověření v živém systému.** Není doložené, zda Nextcloud používá AJAX, Webcron nebo doporučený systémový cron ani pod jakým uživatelem běží.

Při převzetí se v administračním rozhraní ověří nastavený režim a poslední běh. Pokud cron chybí, doplní se až podle živé verze a skutečné cesty instalace. Tajné nebo uživatelské údaje z výstupů se do repozitáře nekopírují.

## Zálohování a obnova

Autoritativní dokumentace záloh, retence a obnov je v [PBS a disaster recovery](../Zalohy/PBS-DR.md). Tento dokument pouze stanovuje aplikační přejímku VM401.

### Přejímka po obnově

1. Zabránit souběžnému spuštění původní a obnovené produkční VM se stejnou identitou.
2. Ověřit parametry VM, síť a dostupnost obou disků.
3. Ověřit, že `/var/nc-data` je správný připojený filesystem a obsahuje očekávaná data.
4. Ověřit Apache, MariaDB a `occ status`.
5. Ověřit HTTPS a přihlášení.
6. S běžným účtem ověřit čtení i zápis testovacího souboru a následnou synchronizaci klienta.
7. Ověřit background jobs, logy a volnou kapacitu.
8. Teprve po úspěšné přejímce přesměrovat produkční provoz.
9. Po stabilizaci vytvořit novou zálohu a zkontrolovat její výsledek.

## Otevřené kontroly

> Následující body **vyžadují ověření v živém systému**.

- [ ] Ověřit aktuální PVE konfiguraci VM401 a fyzický ZFS pool za storage ID `tank-nas-zfs` v [PVE Ryzen](../Servery/PVE-Ryzen.md).
- [ ] Ověřit živé verze operačního systému, Nextcloudu, PHP, Apache a MariaDB.
- [ ] Ověřit skutečnou cestu instalace, PHP handler, databázovou konfiguraci a cache bez zveřejnění tajných hodnot.
- [ ] Ověřit obsazení a volnou kapacitu systémového i datového disku.
- [ ] Ověřit trvalé připojení `/var/nc-data`, zařízení, filesystem a mount po restartu VM.
- [ ] Ověřit nastavení background jobs a cronu; chybějící doporučený způsob následně doplnit.
- [ ] Připravit, bezpečně otestovat a zapsat konkrétní aktualizační postup pro zjištěnou živou verzi.
- [ ] Ověřit v [Uptime Kuma](../Monitoring/Uptime-Kuma.md), zda je aktivní monitor webového endpointu Nextcloudu a zda jeho zpoždění odpovídá schválenému chování alarmů.
