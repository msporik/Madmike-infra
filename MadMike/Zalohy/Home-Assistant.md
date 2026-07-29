# Zálohy Home Assistantu

> Poslední doložené provozní údaje: **2026-07-21 až 2026-07-29**.  
> `HA Honza` a dříve používané označení `HA bratr` jsou jedna a tatáž instalace.

## Cíl

Zálohy Home Assistantu nemají zůstat pouze na zařízení, na kterém daná instance běží. Schválený cílový řetězec kombinuje:

1. lokální zálohu Home Assistantu;
2. u používaných instancí dostupnou cloudovou nebo Nextcloud kopii;
3. druhou offsite vrstvu prostřednictvím PBS zálohy Nextcloudu.

## Stav jednotlivých instancí

| Instance | Platforma / stav | Poslední doložená ochrana | Praktická obnova | Stav řetězce Nextcloud → PBS |
|---|---|---|---|---|
| HA MadMike | Produkční Home Assistant OS na CWWK | Home Assistant Cloud potvrzen 2026-07-21 | Ano, obnova po migraci na CWWK skutečně proběhla | Schválený cíl, realizace živě neověřena |
| HA Vernířovice | Produkční HA na Raspberry Pi 5; přesun na Qotom N100 je plánovaný | Home Assistant Cloud potvrzen 2026-07-21 | Nedoložena | Schválený cíl, realizace živě neověřena |
| HA Honza | Produkční Home Assistant OS na Home Assistant Green | Současný cíl, poslední úspěch a retence nejsou doložené | Nedoložena | Nutno ověřit |
| HA ValTom | Připravený Home Assistant Green, dosud neinstalovaný u Tomáše | Jednorázová přípravná záloha / základní obraz | Nedoložena | Není v produkčním provozu |

Potvrzená obnova HA MadMike je praktický restore, nikoli pouze vytvoření nebo stažení zálohy. Podrobnosti testu se mají při příštím opakování doplnit do provozního projektu domácího Home Assistantu.

## Schválený cílový model

- V Nextcloudu použít samostatný prostor nebo účet `ha-backup`.
- Pro jednotlivé HA instance použít oddělená app hesla; hlavní heslo účtu se do HA nezadává.
- Kopie v Nextcloudu ukládat bez dalšího klientského šifrování souboru, aby obnova nebyla závislá na dalším samostatném klíči.
- Jednotlivé lokality oddělit vlastními složkami a jednoznačným názvem instance.
- Pro Nextcloud kopie držet retenci 14 dní.
- Nextcloud VM401 chránit běžným PBS jobem; tím vznikne offsite kopie HA záloh uložených v Nextcloudu.
- Home Assistant Cloud u HA MadMike a HA Vernířovice ponechat jako samostatnou použitelnou vrstvu, dokud nebude nový řetězec prakticky ověřen.

Tento model je schválený cíl. Bez živé kontroly jednotlivých HA instancí se nepovažuje za dokončenou realizaci.

## Minimální test obnovy

Při testu každé instance:

1. vybrat konkrétní zálohu a zaznamenat její datum a umístění;
2. ověřit, že ji lze stáhnout z cílového úložiště;
3. obnovit ji na odděleném nebo náhradním zařízení;
4. zkontrolovat start HA, klíčové integrace, add-ony, automatizace a přístup;
5. zaznamenat výsledek a případné ruční kroky bez ukládání hesel nebo tokenů do GitHubu.

## Otevřené úkoly

- [ ] Ověřit živé nastavení backupu, poslední úspěch a retenci u všech tří produkčních instancí.
- [ ] Zprovoznit a ověřit prostor `ha-backup`, oddělená app hesla a složky jednotlivých lokalit.
- [ ] Ověřit, že Nextcloud kopie jsou skutečně součástí PBS zálohy VM401.
- [ ] Provést a zdokumentovat praktický restore HA Vernířovice.
- [ ] Provést a zdokumentovat praktický restore HA Honza.
- [ ] Po instalaci HA ValTom nastavit pravidelné produkční zálohování a provést restore test.
- [ ] Při příštím opakování domácí obnovy doplnit datum, použitý backup a ověřené funkce.

## Související dokumentace

- Podrobnosti domácí instance jsou v projektu [MadMike / Home Assistant](../Home-Assistant/README.md).
- Podrobnosti instance ve Vernířovicích jsou v projektu [Vernířovice / Home Assistant](../../Vernirovice/Home-Assistant/README.md).
- Podrobnosti instance u Honzy jsou v projektu [Honza / Home Assistant](../../Honza/Home-Assistant/README.md).
- Podrobnosti připravované instance HA ValTom jsou v projektu [HA ValTom / Home Assistant](../../HA-ValTom/Home-Assistant/README.md).
