# Bitwarden

> Stav ověřen k **2026-07-29**. Bitwarden je funkční pilot na počítači, nikoli jediný ani plně zavedený zdroj přihlašovacích údajů.

## Rozhodnutí

- Používá se Bitwarden Cloud v evropském regionu.
- Vlastní Bitwarden server se provozovat nebude.
- Zavádění probíhá jako postupný pilot, ne hromadný přesun všech účtů.
- Původní ukládání hesel v Chromu se zatím ponechá, dokud nebude nový postup prakticky ověřený.
- Skutečná hesla, hlavní heslo, recovery kódy ani jiné tajné hodnoty nepatří do chatu ani do tohoto repozitáře.

## Potvrzený stav pilotu

| Oblast | Potvrzený stav | Význam |
|---|---|---|
| Windows aplikace | nainstalovaná; přihlášení fungovalo | Potvrzuje funkční klient na PC, ne nouzovou obnovu ani úplnou migraci. |
| Chrome | rozšíření fungovalo včetně `Ctrl+Shift+L` | U některých formulářů může být nutné ručně doplnit uživatelské jméno. Staré ukládání hesel zůstává zapnuté. |
| Telefon | aplikace není nainstalovaná | Přihlášení, synchronizace, odemykání a automatické vyplňování na telefonu nejsou ověřené. |
| Seznam | praktické přihlášení bylo úspěšné | Nejde už o neověřený postup. |
| Proxmox VE a PBS | praktické přihlášení přes interní jmenné adresy fungovalo | Ověřený test konkrétních administračních přístupů, ne všech interních účtů. |
| WinBox | údaj se ručně dohledává a kopíruje z Bitwardenu | Automatické vyplňování není součástí současného postupu. |
| MobaXterm | zůstává ve stávajícím režimu | Jeho případná změna není součástí pilotu. |

Uvedené body zachycují praktické testy a současný způsob práce. Samy o sobě nedokládají běžné používání na všech zařízeních ani úplnost trezoru.

## Rozlišování webů

Výchozí porovnávání podle základní domény vedlo u interních služeb k chybným nabídkám přihlašovacích údajů mezi různými subdoménami `mikehub.cz`.

Pro interní položky se používá porovnání podle **hostitele**, aby například:

- `pveryzen.mikehub.cz`;
- `pulse.mikehub.cz`;
- `mikr.mikehub.cz`

zůstaly oddělené. Toto nastavení prakticky odstranilo konkrétní nabídku přihlášení k Ryzenu na stránce Pulse.

Není doložené, že už byly stejným způsobem zkontrolovány všechny existující položky. Při přidání další interní služby je nutné ověřit přesné URI a způsob porovnání.

## Bezpečnost a recovery

| Oblast | Současný stav |
|---|---|
| Staré ukládání hesel v Chromu | zapnuté; Bitwarden zatím není jediným zdrojem |
| MFA Bitwardenu | není zapnuté |
| Nezávislý recovery podklad | není připravený mimo telefon, počítač a samotný trezor |
| Nouzový přístup po ztrátě notebooku i telefonu | pouze plánovaný; nebyl prakticky ověřený |

Hlavní heslo má být dlouhá náhodná slovní fráze, kterou uživatel bezpečně zvládne používat. Konkrétní recovery údaje a místo jejich uložení se v repozitáři neevidují.

Společný nouzový postup pro obnovu administrátorského přístupu je vedený v [Přístupech](README.md), aby se neduplikoval mezi projekty.

## Podmínky dokončení pilotu

Pilot lze považovat za dokončený teprve po splnění všech těchto podmínek:

- Bitwarden funguje na PC i telefonu;
- na telefonu je ověřené přihlášení, synchronizace, odemykání a automatické vyplňování;
- MFA je zapnuté a existuje nezávislý recovery podklad;
- nouzová obnova administrátorského přístupu po ztrátě notebooku i telefonu byla prakticky ověřená;
- vybrané důležité účty jsou přenesené a jejich URI nabízejí správné přihlášení pouze na zamýšlených hostitelích.

Staré ukládání hesel lze vypnout až poté, co jsou důležité účty dostupné z obou zařízení a nouzový postup je ověřený.

## Související tajné údaje

Ověření, že je Cloudflare API token uložený v Bitwardenu a případný nezašifrovaný TXT soubor odstraněný, je vedené pouze v [Interní DNS, NPM a HTTPS](../Servery/DNS-NPM-HTTPS.md). Zde se tento úkol neduplikuje.

## Otevřené úkoly

- [ ] Nainstalovat Bitwarden na telefon a ověřit přihlášení, synchronizaci, odemykání a automatické vyplňování.
- [ ] Zapnout MFA a připravit nezávislý recovery podklad mimo telefon, počítač a samotný trezor.
- [ ] Přenést vybrané důležité účty a zkontrolovat jejich přesná URI a porovnávání podle hostitele; zejména GitHub, Microsoft, Home Assistant, RouterOS/WebFig a iDRAC.
- [ ] Po splnění podmínek pilotu rozhodnout o vypnutí starého ukládání hesel v Chromu.
