# Zálohy Home Assistantu

> Poslední doložené provozní údaje: **2026-07-21 až 2026-08-03**.  
> `HA Honza` a dříve používané označení `HA bratr` jsou jedna a tatáž instalace.

## Účel a hranice

Zálohy Home Assistantu nemají zůstat pouze na zařízení, na kterém daná instance běží. Tento dokument je autoritativní pro společný zálohovací řetězec, retenci a důkazy obnovitelnosti napříč instancemi.

Hardware, integrace, automatizace a aplikační přejímka každé instance zůstávají v jejím vlastním projektu. Účty, app hesla, tokeny, recovery kódy a síťové klíče do GitHubu nepatří.

## Stav jednotlivých instancí

| Instance | Platforma / stav | Poslední doložená ochrana | Praktická obnova | Stav řetězce Nextcloud → PBS |
|---|---|---|---|---|
| HA MadMike | Produkční Home Assistant OS na CWWK | Home Assistant Cloud potvrzen 2026-07-21 | Ano, obnova po migraci na CWWK skutečně proběhla | Schválený cíl. **Vyžaduje ověření v živém systému.** |
| HA Vernířovice | Produkční HA na Raspberry Pi 5; přesun na Qotom N100 je plánovaný | Home Assistant Cloud potvrzen 2026-07-21 | Nedoložena | Schválený cíl. **Vyžaduje ověření v živém systému.** |
| HA Honza | Produkční Home Assistant OS na Home Assistant Green | Poslední úspěch a retence: **Vyžaduje ověření v živém systému.** | Nedoložena | **Vyžaduje ověření v živém systému.** |
| HA ValTom | Připravený a aktuálně vypnutý Home Assistant Green, dosud neinstalovaný u Tomáše | Jednorázový master image / full backup čistého základu z května 2026; novější image nevznikl | Nedoložena | Není v produkčním provozu |

Potvrzená obnova HA MadMike je praktický restore, nikoli pouze vytvoření nebo stažení zálohy. Datum, přesný použitý backup a úplný výsledek přejímky: **Vyžaduje ověření v živém systému.**

Cloudflare chyba `1033` u `valtom.mikehub.cz` ze dne 2026-08-03 odpovídala vypnutému HA Green a sama nedokládá poruchu tunelu.

## Schválený cílový model

Schválený řetězec kombinuje:

1. lokální full backup Home Assistantu;
2. u používaných instancí dostupnou kopii v Home Assistant Cloud nebo Nextcloudu;
3. druhou offsite vrstvu prostřednictvím PBS zálohy Nextcloudu.

Pro Nextcloud vrstvu platí:

- použít samostatný prostor nebo účet `ha-backup`;
- pro jednotlivé HA instance použít oddělená app hesla; hlavní heslo účtu se do HA nezadává;
- kopie ukládat bez dalšího klientského šifrování souboru, aby obnova nebyla závislá na dalším samostatném klíči;
- jednotlivé lokality oddělit vlastními složkami a jednoznačným názvem instance;
- držet retenci 14 dní;
- chránit Nextcloud VM401 běžným PBS jobem, čímž vznikne offsite kopie HA záloh uložených v Nextcloudu;
- Home Assistant Cloud u HA MadMike a HA Vernířovice ponechat jako samostatnou použitelnou vrstvu, dokud nebude nový řetězec prakticky ověřen.

Tento model je schválený cíl. Bez živé kontroly jednotlivých HA instancí a důkazu, že soubor skutečně dorazil až do PBS snapshotu VM401, se nepovažuje za dokončenou realizaci.

## Doporučené názvy a evidence

Každý backup musí být při obnově jednoznačně přiřaditelný k instanci. Evidence má obsahovat alespoň:

- název instance a lokalitu;
- datum a čas vytvoření;
- zda jde o automatický, ruční předzměnový nebo migrační backup;
- verzi Home Assistantu v době vytvoření;
- umístění dostupných kopií;
- výsledek posledního praktického restore testu.

Konkrétní živé názvy složek a souborů se nepředpokládají bez ověření.

## Běžná provozní kontrola

Pro každou produkční instanci:

1. Ověřit poslední úspěšný full backup a jeho stáří.
2. Zkontrolovat, že lokální backup nezůstal jedinou kopií na zdrojovém zařízení.
3. U Home Assistant Cloud ověřit dostupnost konkrétního backupu z účtu, ne pouze stav předplatného.
4. U Nextcloud vrstvy ověřit přítomnost souboru ve správné složce, jeho velikost a čas poslední změny.
5. Ověřit, že příslušná Nextcloud data byla přítomná před posledním úspěšným PBS backupem VM401.
6. Zkontrolovat, zda retence nemaže poslední známý použitelný bod před dokončením nového restore testu.
7. Odchylku zaznamenat jako konkrétní stav jedné instance; chybějící důkaz se neinterpretuje jako úspěch.

Automatické backupy se považují za funkční až tehdy, když je doložená čerstvá kopie mimo zdrojové zařízení. Žádný dashboard nenahrazuje pravidelný praktický restore.

Požadovaná hranice stáří zálohy vyžadující upozornění: **Vyžaduje ověření v živém systému.**

## Backup před změnou nebo migrací

Před aktualizací, migrací hardware nebo rizikovou změnou:

1. Ověřit běžný poslední backup a vytvořit nový označený full backup.
2. Potvrdit dokončení backupu bez chyby a možnost jeho stažení.
3. Zajistit kopii mimo měněné zařízení; samotný lokální soubor není návratová cesta při poruše storage.
4. Zaznamenat výchozí verzi, hardware a klíčové funkce, které budou po obnově přejímány.
5. Neodstraňovat předchozí známý použitelný backup, dokud není nový stav stabilní a ověřený.

U HA ValTom musí před fyzickým nasazením vzniknout nový aktuální full backup. Přípravný podklad z května 2026 není pravidelným produkčním zálohováním.

## Runbook praktické obnovy

### Příprava

1. Určit správnou instanci, důvod obnovy a požadovaný bod v čase.
2. Vybrat kompatibilní náhradní nebo testovací hardware podle aktuální evidence; sklad se zde neduplikuje.
3. Zajistit stažení konkrétního backupu a zachovat původní zařízení beze změny.
4. Připravit izolovanou nebo bezpečně oddělenou síť, aby nevznikla duplicitní IP, hostname, cloudové spojení nebo automatizace ovládající produkci.
5. Připravit přejímací seznam z autoritativního projektu dané instance.

### Provedení

1. Nainstalovat podporovaný Home Assistant OS na cílový hardware.
2. Obnovit vybraný full backup standardním mechanismem Home Assistantu.
3. Vyčkat na dokončení inicializace; během obnovy neprovádět další konfigurační změny.
4. Ověřit boot, správnou síťovou identitu, lokální přístup a stav Supervisoru.
5. Zkontrolovat obnovu add-onů, integrací, automatizací, dashboardů a historických dat, která měla být součástí backupu.
6. Ručně ověřit externí závislosti, které nemusí být součástí backupu: USB zařízení, Zigbee koordinátory, síťové brány, certifikáty, cloudová přihlášení a zařízení s vlastní identitou.
7. Původní produkční instanci ponechat vypnutou nebo izolovanou, dokud není rozhodnuto, která kopie bude autoritativní.

### Aplikační přejímka

- **HA MadMike:** postup a klíčové funkce jsou v [MadMike / Home Assistant](../Home-Assistant/README.md); zvlášť ověřit síťovou identitu, Jablotron a SLZB-06P10.
- **HA Vernířovice:** přejímka je v [Vernířovice / Home Assistant](../../Vernirovice/Home-Assistant/README.md); zvlášť ověřit InfluxDB, Grafanu, MQTT a energetické vazby bez neřízeného ovládání.
- **HA Honza:** přejímka je v [Honza / Home Assistant](../../Honza/Home-Assistant/README.md); ověřit místní světla, panely a síťovou dostupnost podle skutečného rozsahu instalace.
- **HA ValTom:** před produkčním nasazením postupovat podle [Nasazení a vzdáleného přístupu](../../HA-ValTom/Home-Assistant/Nasazeni-a-pristup.md); starý přípravný image není důkazem aktuální obnovitelnosti.

### Dokončení

1. Zaznamenat instanci, datum backupu, zdroj kopie, hardware, dobu obnovy a ověřené funkce.
2. Uvést všechny ruční kroky a chybějící externí materiály bez zveřejnění tajných hodnot.
3. Určit jedinou autoritativní produkční kopii a teprve potom připojit cílové zařízení do běžné sítě.
4. Po stabilizaci vytvořit nový backup, ověřit jeho druhou kopii a aktualizovat tento dokument.

## Diagnostika

| Projev | První kontrola | Bezpečný další krok |
|---|---|---|
| Backup se nevytvořil | volné místo, Supervisor a konkrétní log úlohy | zachovat poslední známý použitelný backup; nemazat jej kvůli uvolnění místa bez návratové cesty |
| Backup existuje jen lokálně | cílový cloud/Nextcloud, autentizace a síť | vytvořit druhou kopii dříve, než se provede riziková změna |
| Soubor je v Nextcloudu, ale není potvrzen v PBS | čas posledního PBS backupu VM401 a obsah chráněných dat | nepovažovat offsite vrstvu za hotovou; ověřit další úspěšný snapshot VM401 |
| Restore úloha doběhla, HA nenaběhne | kompatibilita OS/hardware, boot a systémové logy | zachovat zdrojový backup; neprovádět opakované náhodné migrace stejného souboru |
| HA běží, ale chybí integrace nebo add-on data | rozsah backupu, Supervisor, externí závislosti | porovnat s přejímacím seznamem a autoritativním projektem instance |
| Po připojení vznikne konflikt | duplicitní IP, hostname, koordinátor nebo cloudová identita | cílovou kopii okamžitě izolovat a určit jedinou autoritativní instanci |
| Cloudová kopie není dostupná | účet, předplatné, autentizace a datum posledního úspěchu | použít jinou doloženou kopii; přístupové údaje neregenerovat naslepo během incidentu |

## Handover a odpovědnosti

Před převzetím každé instance musí být známé:

- vlastník a osoba oprávněná schválit odstávku nebo obnovu;
- hardware, síťová identita a místní možnost zásahu;
- umístění lokální, cloudové a Nextcloud kopie;
- datum posledního úspěšného backupu a praktického restore testu;
- nezastupitelné externí závislosti a bezpečné umístění přístupových materiálů;
- minimální aplikační přejímka.

Konkrétní rozdělení odpovědností mezi správcem infrastruktury a osobami v jednotlivých lokalitách: **Vyžaduje ověření v živém systému.**

## Otevřené úkoly

- [ ] Ověřit živé nastavení backupu, poslední úspěch a retenci u všech tří produkčních instancí.
- [ ] Stanovit hranici stáří HA backupu vyžadující upozornění a odpovědnost za reakci.
- [ ] Zprovoznit a ověřit prostor `ha-backup`, oddělená app hesla a složky jednotlivých lokalit.
- [ ] Ověřit, že Nextcloud kopie jsou skutečně součástí PBS zálohy VM401.
- [ ] Provést a zdokumentovat praktický restore HA Vernířovice.
- [ ] Provést a zdokumentovat praktický restore HA Honza.
- [ ] Po instalaci HA ValTom nastavit pravidelné produkční zálohování a provést restore test.
- [ ] Při příštím opakování domácí obnovy doplnit datum, použitý backup, hardware a ověřené funkce.
- [ ] Doplnit odpovědnosti a možnost místního zásahu pro jednotlivé lokality.

## Související dokumentace

- [MadMike / Home Assistant](../Home-Assistant/README.md)
- [Vernířovice / Home Assistant](../../Vernirovice/Home-Assistant/README.md)
- [Honza / Home Assistant](../../Honza/Home-Assistant/README.md)
- [HA ValTom / Home Assistant](../../HA-ValTom/Home-Assistant/README.md)
- [Nextcloud](../Nextcloud/README.md)
- [PBS a disaster recovery](PBS-DR.md)
