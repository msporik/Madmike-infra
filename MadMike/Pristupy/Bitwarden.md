# Bitwarden

> Dokumentace zpracovaná k **2026-08-03**. Poslední prakticky potvrzený stav pilotu je z **2026-07-29**. Bitwarden je funkční pilot na počítači, nikoli jediný ani plně zavedený zdroj přihlašovacích údajů.

## Účel a hranice

Bitwarden slouží jako postupně zaváděný bezpečný zdroj přihlašovacích údajů. Tento dokument popisuje rozhodnutí, stav pilotu, bezpečné pracovní postupy a podmínky dokončení.

Neeviduje obsah trezoru, uživatelská jména, hesla, hlavní heslo, recovery kódy, TOTP seed, tokeny ani přesné místo nouzové kopie. Tyto údaje nepatří do GitHubu ani chatu.

## Rozhodnutí

- Používá se oficiální Bitwarden Cloud v evropském regionu.
- Vlastní Bitwarden nebo Vaultwarden server se provozovat nebude.
- Zavádění probíhá jako postupný pilot, ne hromadný přesun všech účtů.
- Původní ukládání hesel v Chromu se zatím ponechá, dokud nebude nový postup prakticky ověřený na PC i telefonu včetně recovery.
- MobaXterm zatím zůstává ve stávajícím režimu; Bitwarden jej v současném pilotu nenahrazuje.
- WinBox používá ruční dohledání a zkopírování údaje z Bitwardenu.
- Hlavní heslo má být dlouhá unikátní náhodná slovní fráze. Jeho obsah se nikde v dokumentaci nezaznamenává.

## Potvrzený stav pilotu

| Oblast | Potvrzený stav | Význam |
|---|---|---|
| Windows aplikace | nainstalovaná; přihlášení fungovalo | Potvrzuje funkční klient na PC, ne nouzovou obnovu ani úplnou migraci. |
| Chrome | rozšíření fungovalo včetně `Ctrl+Shift+L` | U některých formulářů může být nutné ručně doplnit uživatelské jméno. Staré ukládání hesel zůstává zapnuté. |
| Telefon | aplikace není nainstalovaná | Přihlášení, synchronizace, odemykání a automatické vyplňování na telefonu nejsou ověřené. |
| Seznam | praktické přihlášení bylo úspěšné | Jde o jednorázově ověřený pracovní postup, ne důkaz úplnosti trezoru. |
| Proxmox VE a PBS | praktické přihlášení přes interní jmenné adresy fungovalo | Ověřený test konkrétních administračních přístupů, ne všech interních účtů. |
| WinBox | údaj se ručně dohledává a kopíruje z Bitwardenu | Automatické vyplňování není součástí současného postupu. |
| MobaXterm | zůstává ve stávajícím režimu | Jeho případná změna není součástí pilotu. |

Uvedené body zachycují praktické testy a současný způsob práce. Samy o sobě nedokládají běžné používání na všech zařízeních, úplnost trezoru ani možnost obnovy po ztrátě zařízení.

## Handover minimum

Přebírající správce musí před prací vědět:

1. Bitwarden účet používá evropský cloudový region.
2. Pilot není dokončený: telefon, MFA a nezávislý recovery podklad chybí.
3. Chrome může stále obsahovat původní uložené přístupy a Bitwarden není jediným zdrojem.
4. Interní služby na `*.mikehub.cz` musí být v Bitwardenu rozlišované přesným hostitelem.
5. WinBox vyžaduje ruční dohledání údaje; MobaXterm se nemění v rámci tohoto pilotu.
6. Bez zobrazení tajných hodnot lze ověřovat existenci položky, její zamýšlený hostitel a stav pracovního postupu. Obsah položek se kvůli handover kontrole neotevírá ani neexportuje.
7. Dokud není prakticky ověřený nouzový postup, nesmí se vypnout poslední funkční starý způsob ukládání ani uzavřít všechny stávající důvěryhodné relace během bezpečnostní změny.

## Rozlišování webů

Výchozí porovnávání podle základní domény vedlo u interních služeb k chybným nabídkám přihlašovacích údajů mezi různými subdoménami `mikehub.cz`.

Pro interní položky se používá porovnání podle **hostitele**, aby například:

- `pveryzen.mikehub.cz`;
- `pulse.mikehub.cz`;
- `mikr.mikehub.cz`

zůstaly oddělené. Toto nastavení prakticky odstranilo konkrétní nabídku přihlášení k Ryzenu na stránce Pulse.

Není doložené, že už byly stejným způsobem zkontrolovány všechny existující položky. Při přidání další interní služby je nutné ověřit přesné URI a způsob porovnání.

## Běžné pracovní postupy

### Přihlášení na webu

1. Otevřít přesný očekávaný hostname služby.
2. Před vyplněním zkontrolovat, že jde o správnou službu a důvěryhodné HTTPS.
3. Použít nabídku rozšíření nebo `Ctrl+Shift+L`.
4. Zkontrolovat, že Bitwarden vybral položku pro daného hostitele, ne pouze pro základní doménu.
5. Pokud formulář doplní jen heslo, uživatelské jméno doplnit ručně pouze z bezpečného zdroje; neměnit kvůli tomu bez ověření obecná pravidla automatického vyplňování.
6. Po přihlášení ověřit očekávanou roli a hlavní funkci služby.

### Přidání nebo úprava webové položky

1. Ověřit přesný běžný hostname a zda služba používá samostatnou identitu.
2. Nevytvářet příliš obecné URI pro celou základní doménu, pokud by nabídlo údaj jiným službám.
3. U interních služeb zvolit porovnávání podle hostitele.
4. Uložit pouze nezbytné údaje a nevkládat do poznámky recovery kódy nebo jiné tajné materiály, které mají mít nezávislou kopii.
5. Prakticky otestovat nabídku údaje na správném hostiteli a zároveň ověřit, že se nenabízí na jiné interní službě.
6. Starou funkční položku nebo staré ukládání odstranit až po úspěšném testu nové varianty a ověření recovery.

### WinBox

1. V Bitwardenu vyhledat položku podle jednoznačného názvu zařízení, lokality nebo adresy.
2. Ověřit, že jde o zamýšlené zařízení.
3. Přenést potřebný údaj ručně bez ukládání do dokumentace, příkazové historie nebo chatu.
4. Po přihlášení ověřit skutečnou identitu zařízení a rozsah oprávnění.

Automatické vyplňování WinBoxu není v současném pracovním postupu podporované.

### Nové zařízení nebo telefon

Tento postup zatím nebyl prakticky ověřený a při prvním provedení musí být zaznamenaný pouze jeho výsledek, nikoli tajné údaje.

1. Použít oficiálního klienta a před přihlášením zvolit správný evropský region.
2. Zachovat funkční přihlášení na dosavadním důvěryhodném zařízení.
3. Ověřit přihlášení, synchronizaci a odemčení trezoru.
4. Nastavit bezpečný a prakticky použitelný způsob místního odemykání zařízení.
5. Ověřit automatické vyplňování na malé pilotní skupině služeb.
6. Ověřit, že nesprávná interní subdoména nenabízí cizí přihlašovací údaj.
7. Teprve poté považovat zařízení za použitelnou druhou pracovní cestu.

## MFA a recovery

| Oblast | Současný stav |
|---|---|
| MFA Bitwardenu | není zapnuté |
| Nezávislý recovery podklad | není připravený mimo telefon, počítač a samotný trezor |
| Nouzový přístup po ztrátě notebooku i telefonu | pouze plánovaný; nebyl prakticky ověřený |
| Staré ukládání hesel v Chromu | zapnuté; Bitwarden zatím není jediným zdrojem |

MFA se nesmí vydávat za dokončené, dokud současně neexistuje použitelný recovery postup. Přesný druh druhého faktoru zatím není v dokumentaci vybraný.

### Bezpečný postup zavedení MFA

1. Ověřit přístup k Bitwardenu a primární identitě potřebné pro obnovu bez změny jejich údajů.
2. Připravit nezávislý recovery podklad mimo telefon, počítač a samotný trezor. Přesné místo ani obsah se do GitHubu nezapisují.
3. Zachovat jednu funkční důvěryhodnou relaci, dokud nejsou další kroky úspěšně ověřené.
4. Zapnout vybraný druh MFA podle podporovaného postupu Bitwardenu.
5. Ověřit nové přihlášení z druhého důvěryhodného zařízení.
6. Prakticky ověřit recovery postup bez zveřejnění nebo znehodnocení tajného materiálu.
7. Zaznamenat pouze datum testu, výsledek, odpovědnost a stav ano/ne.

Dokud tento postup není dokončený, ztráta notebooku i telefonu zůstává nevyřešeným rizikem.

## Diagnostika

| Projev | Pravděpodobná oblast | Bezpečný postup |
|---|---|---|
| Bitwarden nabízí jinou interní službu | příliš obecné URI nebo porovnávání základní domény | ověřit přesný hostname a nastavit porovnávání podle hostitele; současně otestovat správnou i nesprávnou subdoménu |
| Bitwarden nic nenabízí | chybějící nebo neshodné URI, zamčené rozšíření, jiný profil prohlížeče | ověřit stav rozšíření a hostname; nevytvářet duplicitní položku bez kontroly existující |
| Vyplní se heslo, ale ne uživatelské jméno | vlastnost konkrétního formuláře nebo neúplná položka | doplnit jméno bezpečně ručně; obsah položky měnit až po ověření příčiny |
| Přihlášení selže, web je dostupný | účet, heslo, role, MFA nebo stav služby | neopakovat pokusy, které mohou účet zamknout; pokračovat v autoritativním projektu služby |
| PC klient funguje, telefon ne | mobilní klient, region, přihlášení, odemykání nebo autofill nejsou dokončené | dokončit pilot telefonu podle postupu výše; nevypínat starý zdroj hesel |
| Hlavní heslo není přijato | nesprávný region, překlep nebo problém účtu | nezkoušet náhodné varianty; ověřit region a použít pouze připravený recovery postup |
| Notebook i telefon nejsou dostupné | nouzový postup nebyl ověřený | použít pouze bezpečně uložený nezávislý podklad a důvěryhodné zařízení; pokud podklad neexistuje, stav neobcházet improvizací |

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

Společný nouzový postup a bezpečný přehled kritických identit jsou vedené v [Přístupech](README.md).

## Otevřené úkoly

- [ ] Nainstalovat Bitwarden na telefon a ověřit přihlášení, synchronizaci, odemykání a automatické vyplňování.
- [ ] Zapnout MFA a připravit nezávislý recovery podklad mimo telefon, počítač a samotný trezor; poté prakticky ověřit recovery postup.
- [ ] Přenést vybrané důležité účty a zkontrolovat jejich přesná URI a porovnávání podle hostitele; zejména GitHub, Microsoft, Home Assistant, RouterOS/WebFig a iDRAC.
- [ ] Po splnění podmínek pilotu rozhodnout o vypnutí starého ukládání hesel v Chromu.
