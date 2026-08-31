# MadMike – rychlý index dokumentace

Tento soubor je **navigační vrstva**, nikoli další zdroj technických detailů. Autoritativní informace zůstávají v příslušných `README.md` a tematických dokumentech.

## Jak tento index používat

Při práci s projektem `MadMike` postupuj v tomto pořadí:

1. Nejprve přečti tento index.
2. Podle tématu otevři příslušný autoritativní `README.md`.
3. Teprve potom otevři konkrétní tematické soubory uvedené níže nebo odkazované z daného README.
4. `TODO.md` používej pro průřezový přehled otevřených úkolů; jednotlivé checkboxy mají zdroj pravdy ve svých autoritativních dokumentech.
5. Globální hledání v celém repozitáři použij až tehdy, když předchozí kroky nestačí nebo je úkol výslovně průřezový.
6. Pro práci mimo `MadMike` (např. `Honza`, `Vernirovice`, `HA-ValTom`, `Rybniky-Amerika`) začni jejich vlastním `README.md`; neprohledávej je automaticky při dotazu pouze na MadMike.

Pravidla zápisu a bezpečnosti jsou v [`AGENTS.md`](AGENTS.md).

## Rychlá mapa MadMike

| Téma / dotaz | Začni zde | Detail podle potřeby |
|---|---|---|
| Celkový přehled MadMike | [`MadMike/README.md`](MadMike/README.md) | příslušná oblast níže |
| Servery, PVE, VM, Docker, platforma | [`MadMike/Servery/README.md`](MadMike/Servery/README.md) | `PVE-Ryzen.md`, `PVE-Dell.md`, `VM510-Docker.md`, `Budouci-platforma.md` |
| WireGuard, DNS, HTTPS, NPM | [`MadMike/Servery/README.md`](MadMike/Servery/README.md) | `WireGuard.md`, `DNS-NPM-HTTPS.md` |
| Zálohy a disaster recovery | [`MadMike/Zalohy/README.md`](MadMike/Zalohy/README.md) | `PBS-DR.md`, `Home-Assistant.md`, `MikroTik.md` |
| Nextcloud | [`MadMike/Nextcloud/README.md`](MadMike/Nextcloud/README.md) | `Provoz-a-uloziste.md`, `Pristup-a-uzivatele.md` |
| Monitoring a notifikace | [`MadMike/Monitoring/README.md`](MadMike/Monitoring/README.md) | `Pulse.md`, `Mikr.md`, `Uptime-Kuma.md`, `Pushover.md` |
| Síť, MikroTik, adresace | [`MadMike/Sit/README.md`](MadMike/Sit/README.md) | `MikroTik.md`, `Adresni-plan.md` |
| Home Assistant | [`MadMike/Home-Assistant/README.md`](MadMike/Home-Assistant/README.md) | `FVE-SolaX.md`, `Zigbee.md`, `Hikvision.md` |
| PREMIER / Windows služba | [`MadMike/Premier/README.md`](MadMike/Premier/README.md) | `Pristup-a-provoz.md` |
| Přístupy a tajné údaje | [`MadMike/Pristupy/README.md`](MadMike/Pristupy/README.md) | `Bitwarden.md` |
| Co je ještě otevřené | [`TODO.md`](TODO.md) | následovat odkaz na autoritativní dokument položky |

## Hranice oblastí

### Servery
Použij pro fyzické a virtualizační hosty, VM/CT, storage hostitele, Docker VM, budoucí serverovou platformu a serverovou část WireGuard/DNS/HTTPS. Síťovou topologii a MikroTik zařízení řeš primárně v `MadMike/Sit`.

### Zálohy / DR
Použij pro PBS, backup joby, retenci, Verify/GC, restore testy a disaster-recovery postupy. Stav samotného produkčního hostitele patří do `MadMike/Servery`.

### Nextcloud
Použij pro VM401 jako aplikační službu, její data, webový přístup, uživatele a klienty. Obecný stav PVE hostitele hledej v `Servery`; backup/restore VM401 v `Zalohy`.

### Monitoring
Použij pro Pulse, Mikr, Uptime Kuma a Pushover. Dokumentace má popisovat, co která vrstva sleduje a kudy chodí alerty; samotná spravovaná zařízení patří do svých oblastí.

### Síť
Použij pro MikroTik infrastrukturu, topologii, adresní plán a síťové změny. Zálohování konfigurací MikroTik je v `MadMike/Zalohy/MikroTik.md`.

### Home Assistant
Použij pro domácí HA instanci a její integrace. Zálohovací strategie HA je samostatně v `MadMike/Zalohy/Home-Assistant.md`. Ostatní lokality mají vlastní kapitoly repozitáře a nemají se automaticky míchat s MadMike.

### PREMIER
Použij pro provoz Windows/PREMIER a uživatelský přístup k této službě. Obecná VM infrastruktura patří do `Servery`.

### Přístupy
Použij pro společná pravidla účtů, oprávnění a správu tajných údajů. Tajné hodnoty se do GitHubu neukládají.

## Zásada pro AI / Work

Cílem tohoto indexu je omezit opakované prohledávání celého repozitáře. Pokud zadání míří na jednu oblast, načti nejprve pouze tento index + její README a další soubory vybírej cíleně. Celorepozitářové hledání je fallback, nikoli výchozí krok.

Index nesmí začít suplovat detailní dokumentaci. Při vzniku nové dlouhodobé oblasti nebo přesunu autoritativního dokumentu aktualizuj pouze příslušný řádek mapy.