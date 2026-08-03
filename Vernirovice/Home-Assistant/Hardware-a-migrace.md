# Hardware a migrace

## Účel dokumentu

Dokument popisuje současný a cílový hostitel Home Assistantu, bezpečnou přípravu migrace, přejímací test a návrat na původní platformu. Neřeší změnu komunikační architektury energetiky; RS485/Modbus je samostatný projektový krok.

## Současný produkční stav

- Produkční Home Assistant běží na Raspberry Pi 5 jako Home Assistant OS.
- Poslední starší projektový stav uvádí Raspberry Pi 5 s 16 GB RAM a NVMe 256 GB. Tyto parametry nebyly při auditu živě ověřeny. **Vyžaduje ověření v živém systému.**
- InfluxDB, Grafana a MQTT broker běží jako add-ony stejné instalace.
- Migrace na Qotom zatím nebyla provedena.
- Současná verze Home Assistant OS, Core a Supervisor není zdokumentována. **Vyžaduje ověření v živém systému.**

## Připravený cílový hardware

| Součást | Stav | Doložený údaj |
|---|---|---|
| zařízení | zakoupeno, zkušebně nabootováno, odloženo k pozdějšímu nasazení | fanless Qotom s Intel N100 |
| operační paměť | potvrzeno | 16 GB DDR5 |
| systémový disk | potvrzeno | Micron NVMe 512 GB |
| cílový systém | schváleno | Home Assistant OS přímo na hardware |
| průmyslová komunikace | plán | budoucí lokální RS485/Modbus |

Qotom dnes není produkčním hostitelem. Jeho síťová identita, aktuální obsah disku, stav Home Assistant OS, boot po výpadku napájení a monitoring nejsou doložené. **Vyžaduje ověření v živém systému.**

## Rozdělení změn

### Migrace hostitele

Zahrnuje přesun stejné funkční HA instalace, add-onů, databází a integrací z Raspberry Pi 5 na Qotom. Cílem je zachovat provozní chování.

### Změna komunikace na RS485/Modbus

Zahrnuje novou kabeláž, mapy registrů, polling, případné zápisy a chování při výpadku. Nesmí být skrytou součástí migrace hostitele. Nejprve se stabilizuje Qotom se současným Solarmanem, potom se připraví samostatný read-only pilot.

## Předmigrační záznam

Před zahájením vytvořit stručný záznam s těmito údaji:

| Položka | Požadovaný záznam |
|---|---|
| zdrojový hostitel | model, úložiště, verze HA OS/Core/Supervisor |
| cílový hostitel | model, úložiště, síťová identita, stav bootu |
| záloha | datum, čas, velikost a bezpečné umístění mimo zdrojový hostitel |
| služby | stav InfluxDB, Grafany, MQTT a dalších významných add-onů |
| integrace | seznam provozně významných integrací a jejich stav, bez tajných údajů |
| automatizace | seznam aktivních energetických automatizací a jejich aktuální režim |
| přístup | lokální a vzdálená cesta bez tajných údajů |
| monitoring | současné monitory a poslední úspěšná kontrola |
| návrat | kdo rozhodne o rollbacku a jaký je nejzazší čas rozhodnutí |

## Předpoklady migrace

Migraci nezahajovat, dokud není splněno:

- existuje aktuální záloha Home Assistantu a lze ji stáhnout;
- je potvrzeno, zda záloha obsahuje potřebnou konfiguraci a data InfluxDB, Grafany a MQTT;
- oddělená kopie zálohy není uložena pouze na migrovaném hostiteli;
- je zaznamenán současný funkční stav klíčových integrací, automatizací, historie a přístupů;
- Qotom korektně startuje, jeho úložiště je zdravé a je připraven Home Assistant OS;
- Raspberry Pi 5 zůstane beze změn jako dočasná návratová varianta;
- je určena údržbová doba, odpovědná osoba, přejímací kritéria a okamžik návratu;
- je zajištěno, že dvě instance nebudou současně řídit stejné zařízení.

Společná strategie retence, druhých kopií a restore testů je v [Zálohách Home Assistantu](../../MadMike/Zalohy/Home-Assistant.md).

## Doporučené pořadí migrace

1. Provedení migrace oznámit dotčeným osobám a zahájit záznam změny.
2. Vytvořit aktuální plnou zálohu a uložit oddělenou kopii.
3. Zaznamenat aktuální režimy energetiky a případné ruční blokace.
4. Korektně ukončit produkční Raspberry Pi 5 nebo jej síťově oddělit tak, aby nemohlo souběžně řídit zařízení.
5. Nainstalovat Home Assistant OS na Qotom a obnovit připravenou zálohu.
6. Ověřit síť, čas, DNS a lokální přístup; síťovou identitu měnit pouze podle připraveného plánu.
7. Se zakázanými nebo bezpečně blokovanými výkonovými automatizacemi ověřit start, Supervisor a add-ony.
8. Ověřit InfluxDB, Grafanu, MQTT, historii a Solarman pouze čtecím způsobem.
9. Ověřit lokální a vzdálený přístup a monitoring.
10. Povolit automatizace postupně a vždy ověřit skutečný stav zařízení.
11. Provoz sledovat po stanovenou zkušební dobu.
12. Až po úplné přejímce vytvořit novou zálohu Qotomu a migraci uzavřít.

## Přejímací test

Migrace je dokončena až po doložení:

- opakovaného korektního startu Qotomu a Home Assistantu;
- správného času, DNS a síťového připojení;
- lokálního a vzdáleného přístupu;
- zdravého stavu Supervisoru a dostatečného volného místa;
- běhu InfluxDB, Grafany, MQTT a dalších významných add-onů;
- dostupnosti a správnosti hlavních integrací;
- aktuálnosti komunikace přes Solarman;
- přítomnosti a správného stavu klíčových automatizací;
- dostupnosti historie a pokračujícího zápisu do InfluxDB;
- funkčnosti hlavních Grafana dashboardů;
- správného ručního a automatického režimu;
- absence nechtěných fyzických akcí po obnově a restartu;
- dostupnosti instance ve společném monitoringu;
- doručení testovacího upozornění, pokud je bezpečný test připraven;
- vytvoření nové použitelné zálohy po migraci.

Konkrétní délka zkušebního provozu a časový limit pro rollback nejsou schválené. **Vyžaduje ověření v živém systému.**

## Rollback

Rollback zahájit při nechtěné fyzické akci, nestabilním startu, ztrátě zásadní služby, nekonzistentních datech nebo nesplnění předem určených kritérií.

1. Zastavit nebo síťově oddělit Qotom tak, aby nemohl řídit zařízení.
2. Ověřit, že žádná druhá zapisující integrační cesta nezůstala aktivní.
3. Vrátit původní síťovou identitu, pokud byla při migraci změněna.
4. Spustit zachované Raspberry Pi 5.
5. Ověřit lokální a vzdálený přístup, Solarman, add-ony, automatizace a historii.
6. Ověřit skutečný režim měničů a dalších výkonových zařízení.
7. Neprovádět zpětný import novější databáze nebo konfigurace bez samostatného rozhodnutí o ztrátě a slučování dat.
8. Zaznamenat důvod návratu, čas, dopad a změny vzniklé během testovacího provozu.

Raspberry Pi 5 se nesmí smazat, aktualizovat kvůli jinému účelu ani rozebrat, dokud nebude migrace na Qotom prakticky ověřena a výslovně uzavřena.

## Diagnostika hostitele

### Home Assistant není dostupný

1. Ověřit napájení, stav linky a dostupnost hostitele v síti.
2. Ověřit, zda nejde pouze o problém DNS nebo vzdálené cesty; vyzkoušet známou lokální cestu.
3. Zkontrolovat stav hostitele a Home Assistant OS bez opakovaných tvrdých restartů.
4. Pokud hostitel běží, ověřit Supervisor a stav Core.
5. Pokud je úložiště nebo systém poškozen, rozhodnout mezi opravou a obnovou podle stáří zálohy a dopadu na data.
6. Po obnovení ověřit automatizace a skutečný stav fyzických zařízení.

Přesné lokální IP adresy, hostname a fyzické umístění obou hostitelů nejsou autoritativně doložené. **Vyžaduje ověření v živém systému.**

### Po restartu neběží add-on

1. Ověřit volné místo, čas a stav Supervisoru.
2. Zkontrolovat stav a poslední protokol pouze dotčeného add-onu.
3. Ověřit, zda problém není v závislosti, například úložišti, databázi nebo síti.
4. Nerestartovat opakovaně všechny služby bez určení příčiny.
5. Po nápravě ověřit stáří dat, klienty MQTT a dashboardy.

### Úložiště se zaplňuje

1. Zjistit, zda roste recorder, InfluxDB, zálohy nebo protokoly.
2. Před mazáním ověřit retenci, zálohu a dopad na historii.
3. Neupravovat retenci nebo neprovádět purge jako nouzový pokus bez zaznamenání původního stavu.
4. Po uvolnění místa ověřit konzistenci databází a další růst.

## Aktualizace produkční instance

Před aktualizací Home Assistant OS, Core, Supervisoru nebo add-onů:

1. přečíst poznámky k verzi a breaking changes pro dotčené integrace;
2. ověřit aktuální zálohu a návratovou cestu;
3. zaznamenat verze a výchozí stav služeb;
4. nemíchat aktualizaci s migrací hostitele ani změnou komunikační cesty;
5. aktualizovat po jedné logické vrstvě;
6. po každém kroku provést přiměřený přejímací test;
7. při chybě zastavit další změny a rozhodnout o opravě nebo návratu.

Konkrétní ověřený aktualizační postup a běžně používané pořadí pro tuto instanci nejsou zdokumentované. **Vyžaduje ověření v živém systému.**

## Otevřené úkoly

- [ ] Ověřit a doplnit verze Home Assistant OS, Core a Supervisoru a skutečné parametry produkčního Raspberry Pi 5.
- [ ] Ověřit obsah zálohy a ochranu dat add-onů InfluxDB, Grafana a MQTT.
- [ ] Ověřit Qotom, připravit na něm Home Assistant OS a zdokumentovat síťové, úložné a bootovací parametry.
- [ ] Doplnit konkrétní předmigrační kontrolní seznam současných funkcí, údržbovou dobu a funkční kritéria rollbacku.
- [ ] Po úspěšné migraci provést a zdokumentovat přejímací test podle tohoto dokumentu.

Samostatný praktický restore test instance zůstává vedený v [Zálohách Home Assistantu](../../MadMike/Zalohy/Home-Assistant.md).
