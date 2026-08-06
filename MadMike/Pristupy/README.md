# Přístupy

> Dokumentace zpracovaná k **2026-08-03**. Poslední prakticky potvrzený stav Bitwardenu a souvisejících pracovních postupů je z **2026-07-29**. Dokumentace neprokazuje živý stav všech účtů, rolí, MFA ani recovery.

## Účel a autorita

Tento projekt je společným zdrojem pravdy pro zásady přístupu, ověřování identity a správu přihlašovacích údajů v infrastruktuře MadMike.

Popisuje:

- společný přístupový model z domácí LAN a zvenku;
- hranici mezi síťovou dostupností a přihlášením do služby;
- vědomé veřejné výjimky;
- společné požadavky na správu identit, MFA, recovery a nouzový přístup;
- stav a provozní zásady pilotu Bitwarden Cloud EU.

Skutečná hesla, hlavní heslo, recovery kódy, TOTP seed, privátní klíče, preshared keys, tokeny, cookies ani obsah trezoru do GitHubu nepatří. Jejich autoritativním místem je Bitwarden nebo jiné výslovně určené bezpečné úložiště.

## Společný přístupový model

Přístup k administrační službě se skládá z několika nezávislých vrstev. Úspěch jedné vrstvy nepotvrzuje funkčnost ostatních.

| Vrstva | Úloha | Autoritativní dokument nebo systém |
|---|---|---|
| Síťová cesta | domácí LAN nebo WireGuard; u vědomých výjimek veřejná cesta | [WireGuard](../Servery/WireGuard.md), [Síť](../Sit/README.md), projekt konkrétní služby |
| Jméno a HTTPS | interní DNS, NPM, proxy host a certifikát | [Interní DNS, NPM a HTTPS](../Servery/DNS-NPM-HTTPS.md) |
| Identita a oprávnění | účet, role a přihlášení uvnitř služby | projekt konkrétní služby |
| MFA a recovery | druhý faktor a možnost bezpečné obnovy přístupu | projekt konkrétní služby; společné zásady v tomto dokumentu |
| Přihlašovací údaj | bezpečné uložení a použití tajné hodnoty | Bitwarden; stav pilotu v [Bitwardenu](Bitwarden.md) |

### Základní zásady

- Administrační a monitorovací služby mají být dostupné z domácí LAN nebo přes WireGuard, ne přímo z internetu.
- WireGuard vytváří chráněnou síťovou cestu. Nenahrazuje účet, oprávnění, MFA ani recovery uvnitř služby.
- Interní názvy a důvěryhodné HTTPS zajišťují interní DNS a Nginx Proxy Manager.
- Veřejně dostupná služba je vědomá výjimka a její úplná publikační cesta patří do dokumentace dané služby a sítě.
- Přímé veřejné RDP k PREMIERu je zděděný rizikový stav, nikoli cílový přístupový model.
- Změna přístupu musí zachovat prakticky použitelnou správu a nesmí bez ověřené náhrady zablokovat běžné uživatele služby.
- Starý funkční přístup se odstraňuje až po praktickém ověření nového postupu, oprávnění, MFA, recovery a návratové cesty.
- Nouzová cesta nesmí být jedinou neověřenou kopií stejného přístupu nebo záviset pouze na zařízení, jehož ztrátu má řešit.

## Mapa přístupů

### Interní a administrační služby

| Oblast | Současná cesta | Doložený stav a hranice | Autoritativní dokument |
|---|---|---|---|
| PVE, PBS, NPM a monitoring | domácí LAN nebo notebookový WireGuard; interní DNS a NPM | Cesta k dokumentovaným službám byla prakticky ověřená. Přihlášení, role, MFA a recovery všech služeb nejsou souhrnně inventarizované. | [Servery](../Servery/README.md), [Monitoring](../Monitoring/README.md) |
| RouterOS a WinBox | LAN nebo příslušný WireGuard; přihlašovací údaj se ručně dohledává v Bitwardenu | Administrace nemá být veřejná. Úplný stav uživatelů, oprávnění a MFA jednotlivých lokalit není ověřený. | [Síť / MikroTik](../Sit/MikroTik.md), [WireGuard](../Servery/WireGuard.md) |
| Bitwarden Cloud EU | veřejná cloudová služba poskytovatele, nikoli publikace domácí infrastruktury | Funkční pilot pouze na PC; telefon chybí, staré ukládání zůstává zapnuté a Bitwarden ještě není jediným zdrojem přihlašovacích údajů. | [Bitwarden](Bitwarden.md) |

### Vědomé veřejné výjimky

| Služba | Současná cesta | Stav a hranice | Autoritativní dokument |
|---|---|---|---|
| Nextcloud | veřejné HTTPS přímo na VM401 přes Apache | Přístup funguje. Úplná publikační cesta, stav účtů, MFA a recovery vyžadují ověření v živém systému. | [Nextcloud – přístup a uživatelé](../Nextcloud/Pristup-a-uzivatele.md) |
| PREMIER / VM501 | přímé veřejné RDP přes MikroTik | Přístup účetní funguje, ale jde o zděděné riziko. Přesné živé NAT/firewall pravidlo nebylo ověřené a cílová náhrada není vybraná. | [PREMIER – přístup a provoz](../Premier/Pristup-a-provoz.md) |
| HA ValTom | Cloudflare Tunnel na připraveném HA Green | Tunel dříve fungoval. HA Green je nyní vypnutý a ještě není produkčně nasazený; po fyzickém nasazení se musí cesta znovu ověřit. | [HA ValTom – nasazení a přístup](../../HA-ValTom/Home-Assistant/Nasazeni-a-pristup.md) |
| Domácí Home Assistant | `domov.mikehub.cz` přes Cloudflare Tunnel `homeassistant-domov` | Vzdálená cesta byla prakticky ověřená 2026-08-06. Účty, MFA a recovery Home Assistantu se tím nepovažují za souhrnně ověřené. | [Domácí Home Assistant](../Home-Assistant/README.md) |
| Home Assistant MCP | `mcp.mikehub.cz` přes stejný Cloudflare Tunnel | Tajná část URL nahrazuje samostatné přihlášení k MCP. Server má vynucený read-only režim a omezení povolených nástrojů; přístup byl prakticky ověřený z Claude.ai i ChatGPT Work 2026-08-06. | [Domácí Home Assistant](../Home-Assistant/README.md) |

Veřejná dostupnost neznamená veřejnou administraci bez autentizace. Konkrétní účty, role, MFA, recovery, NAT, firewall a publikační konfigurace zůstávají v autoritativním projektu služby nebo sítě.

### Tajná URL Home Assistant MCP

- Home Assistant MCP nepoužívá další uživatelské jméno, heslo ani token; autentizačním údajem je tajná část URL.
- Úplná MCP URL se nesmí zapisovat do GitHubu, chatu, screenshotu ani běžných poznámek. Má být uložená v Bitwardenu a zachází se s ní jako s heslem.
- Dopad případného zneužití omezuje serverově vynucený **Read Only Mode** a výběr povolených nástrojů. Tato omezení nenahrazují ochranu tajné URL.
- Při podezření na únik změnit tajnou cestu na MCP serveru, zneplatnit původní URL a aktualizovat uložené konektory v Claude.ai a ChatGPT Work.
- Po změně provést pouze čtecí test a ověřit, že stará URL již nefunguje.

## Odpovědnosti

| Role | Odpovědnost |
|---|---|
| Správce infrastruktury | společný přístupový model, Bitwarden pilot, bezpečné provedení změny, zachování návratové cesty a aktualizace dokumentace bez tajných hodnot |
| Správce konkrétní služby | účty, role, MFA, recovery a přejímka služby v jejím autoritativním projektu |
| Běžný uživatel služby | praktické ověření svého pracovního postupu po změně; nepřebírá administrátorské oprávnění bez doložené potřeby |
| Přebírající správce | nejprve ověří vrstvy přístupu a stav otevřených úkolů; neotevírá ani nekopíruje obsah trezoru jen kvůli dokumentační kontrole |

Pokud jednu roli vykonává stejná osoba, hranice odpovědností přesto zůstávají platné.

## Handover: první orientace správce

1. Přečíst tento dokument, [Bitwarden](Bitwarden.md), [WireGuard](../Servery/WireGuard.md) a [Interní DNS, NPM a HTTPS](../Servery/DNS-NPM-HTTPS.md).
2. Ověřit přístup k jedné interní službě z domácí LAN a samostatně přes notebookový WireGuard. Nezaměňovat otevření přihlašovací stránky za úspěšné přihlášení.
3. U každé důležité služby určit autoritativní dokument pro síťovou cestu, účet a oprávnění, MFA/recovery a provozní diagnostiku.
4. Bez zobrazení tajných hodnot ověřit, kdo odpovídá za kritické identity a zda je u nich doložený stav MFA a recovery.
5. Seznámit se s nedokončeným stavem Bitwarden pilotu. Dokud není ověřen telefon, MFA a nezávislý recovery podklad, nepovažovat správu přístupů za plně předatelnou.
6. Prověřit vědomé veřejné výjimky. U PREMIERu neodstraňovat funkční RDP před výběrem a praktickou přejímkou náhrady účetní.
7. Před změnou projít otevřené úkoly v tomto projektu i v dokumentu konkrétní služby.

## Bezpečná změna přístupu

Tento postup platí pro změnu účtu, hesla, role, MFA, přístupové cesty nebo veřejné publikace. Technické příkazy a konfigurace zůstávají v autoritativním projektu dané vrstvy.

1. Určit důvod změny, dotčenou službu, uživatele a autoritativní dokumenty.
2. Popsat současný funkční pracovní postup a určit, co bude důkazem úspěchu nové varianty.
3. Připravit návratovou cestu. U významné změny zachovat bezpečnou aktivní správcovskou relaci nebo jinou nezávislou ověřenou cestu.
4. Ověřit, že potřebné přihlašovací a recovery podklady existují v určeném bezpečném úložišti. Jejich obsah nekopírovat do dokumentace ani chatu.
5. Provést pouze jednu srozumitelnou změnu nebo předem vymezený celek změn.
6. Otestovat zvlášť síťovou dostupnost, HTTPS, přihlášení, oprávnění, MFA a hlavní pracovní úkon uživatele.
7. Pokud změna ovlivňuje externí účetní nebo jiného běžného uživatele, nechat jej prakticky potvrdit běžný postup včetně funkcí, které skutečně používá.
8. Původní cestu odstranit až po úspěšné přejímce nové varianty a ověření recovery.
9. Zapsat výsledný stav, datum a nevyřešené body do autoritativních dokumentů bez tajných hodnot.

## Diagnostika přístupu

| Projev | První rozlišení | Autoritativní pokračování |
|---|---|---|
| Interní název se nepřeloží | ověřit, zda klient používá domácí DNS a zda je aktivní LAN/WireGuard cesta | [Interní DNS, NPM a HTTPS](../Servery/DNS-NPM-HTTPS.md), [WireGuard](../Servery/WireGuard.md) |
| IP nebo přímý port funguje, HTTPS název ne | oddělit DNS, NPM, upstream, schéma HTTP/HTTPS a certifikát | [Interní DNS, NPM a HTTPS](../Servery/DNS-NPM-HTTPS.md) |
| Přihlašovací stránka se otevře, ale přihlášení selže | síťová cesta je pravděpodobně funkční; ověřit účet, roli, stav služby a MFA bez opakovaných pokusů, které mohou účet zamknout | projekt konkrétní služby |
| Bitwarden nabízí údaj pro jinou subdoménu | zkontrolovat přesné URI a porovnávání podle hostitele | [Bitwarden](Bitwarden.md) |
| Přihlášení funguje, ale chybí oprávnění | ověřit roli v konkrétní službě; neměnit síťovou cestu jako náhodný workaround | projekt konkrétní služby |
| Přístup z LAN funguje, přes WireGuard ne | ověřit handshake, routu, DNS klienta a firewall; samotný handshake nepotvrzuje klient↔LAN komunikaci | [WireGuard](../Servery/WireGuard.md) |
| Veřejná výjimka není dostupná | oddělit stav služby, veřejné DNS, tunel nebo NAT/firewall a HTTPS | projekt konkrétní služby a [Síť](../Sit/README.md) |
| Ztracený notebook nebo telefon | neprovádět nahodilé změny hesel bez zachované důvěryhodné cesty; použít pouze předem ověřený recovery postup | společný recovery postup zatím vyžaduje doplnění a praktický test |

Při podezření na kompromitaci se nejprve určí dotčená identita, zařízení, relace a služba. Tajné hodnoty ani neupravené bezpečnostní výpisy se nevkládají do chatu nebo GitHubu. Zneplatnění relací, změna hesla, obnova MFA a kontrola oprávnění se provádějí v autoritativním systému až s ověřenou možností zachovat nebo obnovit správcovský přístup.

## Hranice dokumentace

- WireGuard adresy, peery, směrování a DNS klientů patří do `Servery/WireGuard.md`.
- Interní DNS, NPM upstreamy a certifikáty patří do `Servery/DNS-NPM-HTTPS.md`.
- NAT, firewall, veřejná publikační cesta, uživatelé, role, MFA a recovery konkrétní služby patří do jejího projektu a podle potřeby do projektu Síť.
- Tento projekt drží společné zásady, stav Bitwardenu, společný postup změny a rozhodnutí platná napříč službami.
- Proměnlivá kusová a licenční evidence patří do Airtable. Obsah trezoru a tajné hodnoty patří do Bitwardenu.

## Informace vyžadující ověření

**Vyžaduje ověření v živém systému.**

- aktuální vlastníci a administrátorské role kritických služeb;
- stav MFA a použitelný recovery postup u kritických veřejných identit a služeb;
- úplnost položek Bitwardenu a správnost jejich URI bez inventarizace obsahu trezoru;
- přesná živá veřejná cesta k PREMIERu a Nextcloudu v jejich autoritativních projektech.

## Otevřené úkoly

- [ ] Vybrat jednoduchou cílovou náhradu přímého veřejného RDP k PREMIERu podle skutečného způsobu práce účetní.
- [ ] Definovat a prakticky ověřit minimální nouzový postup pro obnovu administrátorského přístupu po současné ztrátě notebooku a telefonu.
- [ ] Vytvořit bezpečný přehled kritických identit po kategoriích, který bez uživatelských jmen a tajných hodnot eviduje odpovědnost, stav MFA, stav recovery a datum posledního ověření.
