# Telegram notifikace

> **Stav: SCHVÁLENÁ KONCEPCE.** Implementace nebyla v dostupných zdrojích doložena.

## Účel a role

Telegram bude jedna přehledná schránka skutečných problémů infrastruktury MadMike, které vyžadují pozornost. Nebude sloužit jako technický log ani jako náhrada přístupu do zdrojových systémů.

## Schválená architektura

- jedna soukromá skupina `MadMike – infrastruktura`;
- jeden společný bot pro všechny zdroje notifikací;
- správce infrastruktury zůstává administrátorem skupiny;
- alarm a následná recovery zpráva přicházejí do stejné skupiny;
- token bota je uložený v bezpečném úložišti mimo GitHub a mimo přímo verzované Compose soubory.

V dokumentaci se může uvést název bezpečného úložiště, nikdy hodnota tokenu ani chat ID.

## Zdroje a pořadí zapojení

1. **Uptime Kuma** – delší nedostupnost služby a následné obnovení.
2. **Proxmox VE a PBS** – selhání Backup, Verify, Prune a Garbage Collection; podle ověřených možností také problémy ZFS scrubů.
3. **Mikr Manager** – významné problémy MikroTiků a lokalit, které neduplikuje Kuma.
4. **Pulse** – pouze upozornění, která nejsou lépe pokrytá jiným zdrojem.
5. Později případně Home Assistant a další důležité systémy.

Každý zdroj se připojí až po samostatném testu alarmu a návratu do normálu.

## Obsah zprávy

Alarm má stručně uvést:

- stav;
- zdroj;
- objekt, službu nebo lokalitu;
- popis problému;
- čas vzniku nebo délku trvání, pokud ji zdroj zná;
- doporučenou první kontrolu.

Příklad dostupnosti:

```text
🔴 DOWN | Uptime Kuma | Nextcloud
Služba není dostupná déle než 5 minut.
Lokalita: MadMike
Akce: ověřit VM401 a PVE Ryzen
```

Recovery:

```text
🟢 RECOVERY | Uptime Kuma | Nextcloud
Služba je znovu dostupná.
Délka výpadku: 8 minut
```

Příklad nativní úlohy:

```text
🔴 FAILED | PBS | Verify job
Úloha skončila chybou.
Objekt: datastore backup
Akce: otevřít PBS Tasks a zjistit konkrétní chybu
```

Formát se může přizpůsobit možnostem zdroje. Musí však zůstat srozumitelný bez čtení technického logu.

## Ochrana proti šumu

Do Telegramu nepatří:

- pravidelné zprávy typu „vše je OK“;
- každá úspěšná operace;
- běžný technický log;
- krátké výkyvy bez praktického dopadu;
- opakování stejného problému v krátkých intervalech;
- stejný problém oznámený několika nástroji;
- zprávy, ze kterých není jasné, zda vyžadují pozornost.

Standardem je jeden alarm a jedna odpovídající recovery zpráva. Při výpadku celé lokality se upřednostní jedna smysluplná zpráva o lokalitě před sérií alarmů jednotlivých zařízení.

## Bezpečnost a vlastnictví

Musí být doloženo:

- pod kterým Telegram účtem byl bot vytvořen;
- kdo je administrátorem skupiny;
- ve kterém bezpečném úložišti je token uložen;
- které systémy token používají.

Při podezření na kompromitaci se token regeneruje přes BotFather a následně se vymění ve všech integracích. Hodnota původního ani nového tokenu se nezapisuje do dokumentace.

Existence Telegram skupiny nenahrazuje dokumentovaný přístup do PVE, PBS, Pulse, Mikru, Kumy ani dalších zdrojových systémů.

## Otevřené úkoly

> Následující body tvoří implementační a přejímací pořadí a vyžadují ověření v živém systému.

- [ ] Ověřit, zda již existuje soukromá skupina `MadMike – infrastruktura`; pokud ne, vytvořit ji.
- [ ] Ověřit existenci a vlastníka společného bota; pokud neexistuje, vytvořit ho.
- [ ] Ověřit administrátory skupiny, bezpečné umístění tokenu a systémy, které ho používají.
- [ ] Odeslat testovací zprávu.
- [ ] Připojit Uptime Kumu a prakticky otestovat skutečný `DOWN` i odpovídající recovery.
- [ ] Připojit otestované nativní notifikace PVE/PBS.
- [ ] Připojit vybrané alarmy Mikr Manageru.
- [ ] Pulse připojit pouze pro události nepokryté jiným zdrojem.
- [ ] Po pilotním provozu ověřit potlačení duplicit a opakovaných zpráv a upravit četnost.
