# Pushover notifikace

> **Stav: FUNKČNÍ PILOT.** Doručovací cesta z Uptime Kumy byla prakticky ověřena 2026-08-12. Produkční monitory ani další zdroje zatím nejsou připojené.

## Účel a role

Pushover je společný cílový kanál vybraných provozních upozornění infrastruktury MadMike. Slouží k doručení problémů vyžadujících pozornost a odpovídajících recovery zpráv na Samsung S22.

Pushover není technický log ani zdroj diagnostiky. Podrobnosti a autoritativní stav se vždy ověřují v systému, který problém zjistil.

Jde o externí doručovací službu. Na VM510 kvůli Pushoveru neběží žádný další notifikační server. Výpadek VM510 proto nezastaví samotnou službu Pushover, ale zastaví upozornění ze zdrojů běžících pouze na této VM.

## Rozhodnutí a historie

Původně navržený Telegram byl opuštěn před produkčním nasazením. Bot ani telegramová skupina nejsou součástí cílové architektury monitoringu.

Pushover byl zvolen jako jednodušší cílový kanál bez skupiny, bota a Telegram Chat ID.

## Ověřený stav

Dne 2026-08-12 bylo ověřeno:

- aplikace Pushover na Samsungu S22 přijímá zprávy;
- v Uptime Kumě existuje notifikační cíl `Pushover – Kuma`;
- vestavěná testovací zpráva z Uptime Kumy byla úspěšně doručena;
- dočasný Push monitor bezpečně vyvolal skutečný přechod `DOWN` a následný `UP`;
- dorazila právě jedna zpráva `DOWN` a jedna odpovídající zpráva `UP`;
- žádná produkční služba nebyla kvůli testu zastavena;
- dočasný testovací monitor byl následně odstraněn;
- `Pushover – Kuma` není nastavený jako výchozí pro všechny existující monitory;
- notifikační cíl zatím není přiřazený žádnému produkčnímu monitoru.

Ověřená cesta je:

```text
Uptime Kuma → Pushover → Samsung S22
```

## Bezpečnost a obnova přístupu

Pushover User Key a Application Token jsou uložené v Bitwardenu. Jejich hodnoty se nezapisují do GitHubu, chatu, screenshotů ani provozních poznámek.

Původní Application Token zachycený při nastavování na screenshotu byl resetován. Platný token zůstává pouze v Bitwardenu.

Dokumentovat lze:

- účel integrace;
- název notifikačního cíle;
- systém, který přístupové údaje používá;
- bezpečné úložiště;
- datum posledního funkčního testu.

Při podezření na kompromitaci se Application Token resetuje, aktualizuje v připojených zdrojích a následně se provede nový test. Hodnota původního ani nového tokenu se nikam nezapisuje.

## Zdroje a pořadí zapojení

1. **Uptime Kuma** – vybrané produkční monitory, delší nedostupnost a následné obnovení.
2. **Proxmox VE a PBS** – nativní selhání Backup, Verify, Prune a Garbage Collection; podle ověřených možností také problémy ZFS scrubů.
3. **Mikr Manager** – významné problémy MikroTiků a lokalit, které neduplikuje Kuma.
4. **Pulse** – pouze upozornění, která nejsou lépe pokrytá jiným zdrojem.
5. Později případně Home Assistant a další důležité systémy.

Každý zdroj se připojí až po samostatném bezpečném testu alarmu a návratu do normálu. Ověřený test Kumy s dočasným monitorem sám o sobě neznamená, že jsou produkční monitory připojené.

## Obsah a priorita zpráv

Zpráva má podle možností zdroje stručně uvést:

- stav;
- zdroj;
- objekt, službu nebo lokalitu;
- popis problému;
- čas vzniku nebo délku trvání, pokud ji zdroj zná;
- doporučenou první kontrolu nebo odkaz do zdrojového systému, pokud je bezpečně dostupný.

Příklad dostupnosti:

```text
🔴 DOWN | Uptime Kuma | Nextcloud
Služba není dostupná déle než nastavené zpoždění.
```

Recovery:

```text
🟢 UP | Uptime Kuma | Nextcloud
Služba je znovu dostupná.
```

Výchozí priorita je normální. Nouzová priorita s opakováním do potvrzení se nezapíná bez samostatného rozhodnutí a praktického testu.

## Ochrana proti šumu

Do Pushoveru nepatří:

- pravidelné zprávy typu „vše je OK“;
- každá úspěšná operace;
- běžný technický log;
- krátké výkyvy bez praktického dopadu;
- opakování stejného problému v krátkých intervalech;
- stejný problém oznámený několika nástroji;
- zprávy, ze kterých není jasné, zda vyžadují pozornost.

Standardem je jeden alarm a jedna odpovídající recovery zpráva. Při výpadku celé lokality se upřednostní jedna smysluplná událost lokality před sérií alarmů jednotlivých zařízení.

## Otevřené úkoly

- [ ] Vybrat produkční monitory Uptime Kumy, jednotlivě jim přiřadit `Pushover – Kuma` a ověřit, že nevznikají duplicitní zprávy.
- [ ] Připojit a samostatně otestovat nativní notifikace PVE/PBS.
- [ ] Připojit a samostatně otestovat vybrané alarmy Mikr Manageru.
- [ ] Pulse připojit pouze pro události nepokryté jiným zdrojem a samostatně otestovat alarm i recovery.
- [ ] Po pilotním provozu vyhodnotit četnost, priority, formát zpráv a potlačení duplicit.
