# Bitwarden

## Rozhodnutí

- Používá se Bitwarden Cloud v evropském regionu.
- Vlastní Bitwarden server se provozovat nebude.
- Zavádění probíhá jako postupný pilot, ne hromadný přesun všech účtů.
- Původní ukládání hesel se zatím ponechá, dokud nebude nový postup prakticky ověřený.
- Skutečná hesla, hlavní heslo, recovery kódy ani jiné tajné hodnoty nepatří do chatu ani do tohoto repozitáře.

## Potvrzený stav pilotu

- Windows aplikace je nainstalovaná a přihlášení funguje.
- Rozšíření v Chromu funguje včetně vyplnění přes `Ctrl+Shift+L`.
- Prakticky byly zkoušené běžné webové účty a přístupy k Proxmoxu/PBS.
- U některých formulářů může být nutné ručně doplnit uživatelské jméno.
- WinBox se zatím obsluhuje ručním zkopírováním údaje z Bitwardenu.
- MobaXterm zatím zůstává ve stávajícím režimu; jeho případná změna není součástí pilotu.

## Rozlišování webů

Výchozí porovnávání podle základní domény vedlo u interních služeb k chybným nabídkám přihlašovacích údajů mezi různými subdoménami `mikehub.cz`.

Pro tyto položky se používá porovnání podle **hostitele**, aby například:

- `pveryzen.mikehub.cz`;
- `pulse.mikehub.cz`;
- `mikr.mikehub.cz`

zůstaly oddělené. Toto nastavení prakticky odstranilo nabídku přihlášení k Ryzenu na stránce Pulse.

Při přidání další interní služby je nutné zkontrolovat URI a způsob porovnání ještě před uložením dalších podobných položek.

## Bezpečnost a recovery

- Hlavní heslo má být dlouhá náhodná slovní fráze, kterou uživatel bezpečně zvládne používat.
- MFA pro Bitwarden je plánovaná navazující etapa, zatím není vedená jako dokončená.
- Současně s MFA musí vzniknout recovery postup, který nezávisí pouze na přístupu do stejného trezoru.
- Konkrétní recovery údaje a místo jejich uložení se v repozitáři neevidují.

## Otevřené úkoly

1. Pokračovat v pilotu na omezeném počtu účtů a ověřit běžné používání na PC i telefonu.
2. Nastavit MFA a bezpečně uložit recovery údaje.
3. Teprve po úspěšném pilotu rozhodnout o širším přesunu účtů a vypnutí starého ukládání hesel.
4. Ověřit praktický postup pro GitHub, Microsoft, Seznam, Home Assistant, RouterOS/WebFig a iDRAC.
5. Postupně odstranit duplicitní nebo příliš obecné URI, které nabízejí přihlášení na nesprávných hostitelích.
