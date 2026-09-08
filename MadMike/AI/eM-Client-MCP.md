# eM Client MCP – napojení e-mailu do ChatGPT

> Stav prakticky ověřen 8. 9. 2026.
>
> Pilot byl proveden pouze pro čtení. Nebylo povoleno odesílání, mazání, přesouvání ani jiná změna zpráv.

## Účel

Cílem pilotu je ověřit, zda může být e-mail jedním ze vstupů AI workspace vedle Projektově, Todoistu, GitHubu a dalších systémů.

První ověřený scénář je večerní briefing:

- zprávy vyžadující odpověď;
- termíny a slíbené kroky;
- urgentní záležitosti;
- riziko, že úkol nebo očekávaná reakce zapadne;
- potlačení reklam a newsletterů.

## Ověřená konfigurace

| Položka | Hodnota |
|---|---|
| Operační systém | Windows |
| Původní eM Client | 10.4.5674 (fcbf2a4) |
| Ověřený eM Client | 11.0.282 (ff9ca14) |
| MCP server | MailClient 11.0.0.0 |
| Transport | lokální proces přes STDIO |
| Spouštěcí soubor | `C:\Users\admin\AppData\Local\Microsoft\WindowsApps\eMClientStore.exe` |
| Přístup | pouze čtení |
| Nutná podmínka | spuštěný počítač a eM Client |

Secret ani spouštěcí argumenty obsahující secret se do repozitáře neukládají.

## Architektura pilotu

```text
ChatGPT na notebooku
        |
        | spustí lokální proces a předá tři argumenty
        v
eMClientStore.exe – MCP server
        |
        v
spuštěný eM Client a jeho lokální data
```

## Síťové řešení a transport

Pro pilot eM Client MCP nebylo vytvořeno žádné síťové spojení.

Použité připojení:

- transport `STDIO`;
- MCP server je lokální proces `eMClientStore.exe`;
- proces spouští klient na stejném Windows počítači;
- nebyl použit Cloudflare Tunnel ani Nginx Proxy Manager;
- nebyla vytvořena veřejná URL ani DNS záznam;
- nebyl otevřen žádný síťový port;
- komunikace není dostupná z internetu ani po vypnutí notebooku.

Jde o lokální desktopovou integraci, nikoliv o vzdálenou MCP službu. Mobilní funkce Remote v eM Clientu lokální MCP server nezpřístupňuje ChatGPT v cloudu.

Tím se řešení liší od MikroTik MCP a OpenProject MCP, které běží jako síťové služby dostupné přes Cloudflare Tunnel.

## Zprovoznění

### 1. Záloha a aktualizace eM Clienta

Ve verzi `10.4.5674 (fcbf2a4)` nebyla v nastavení dostupná sekce Umělá inteligence ani MCP.

Před aktualizací byla vytvořena záloha. Následně byl eM Client aktualizován na `11.0.282 (ff9ca14)`.

Po aktualizaci se objevilo:

`Nastavení → Umělá inteligence → MCP`

### 2. Omezení oprávnění

V nastavení MCP byly ponechány pouze nástroje pro čtení.

Účet může v běžném eM Clientu podporovat odesílání a metadata účtu mohou uvádět „odesílání povoleno“. Rozhodující je ale seznam nástrojů skutečně zpřístupněných přes MCP. V pilotu nebyl registrován žádný nástroj pro odeslání, přesun nebo smazání zprávy.

### 3. Konfigurace klienta

eM Client zobrazuje samostatně:

- cestu ke spouštěcímu souboru;
- typ připojení `STDIO`;
- spouštěcí argumenty;
- secret.

Cesta a argumenty nejsou jeden společný PowerShell příkaz. MCP klientovi je nutné předat cestu a tři argumenty přesně jako samostatné hodnoty.

### 4. Ověření komunikace

Úspěšný diagnostický test vrátil:

`Initialize OK – server: MailClient 11.0.0.0`

Server zpřístupnil 12 nástrojů:

- `DisplayConversation`
- `DisplayEmail`
- `GetConversationData`
- `GetEmailAttachmentContent`
- `GetEmailData`
- `CheckEmailFolderStatus`
- `ListEmailAccounts`
- `ListEmailFolders`
- `ListSpecialEmailFoldersOnly`
- `SearchEmailConversations`
- `SearchEmails`
- `SearchEmailsInConversation`

Tím byl potvrzen funkční MCP handshake a read-only sada nástrojů.

## Viditelný účet

Při ověření byl přes MCP dostupný jeden účet:

- `info@kompletelektro.cz`;
- název: Michal Šporik;
- stav: online;
- ID pozorované při testu: `e4477621-a775-4339-af95-7c350ef4fb1b`.

ID je provozní identifikátor eM Clienta a může se změnit například po odebrání a opětovném přidání účtu. Přestože eM Client obsahoval více účtů, ostatní účty MCP při testu nevrátil.

## Viditelné složky

```text
Doručená pošta (INBOX)
├── SMS Elektro
│   └── SMS elektro faktury
└── Hilti

Rozepsané (Drafts)
Junk
Odeslané (Sent)
Nevyžádaná pošta (Junk E-mail)
Koš (Trash)
```

`ListEmailFolders` neposkytl samostatné ID složky. Jako jednoznačný identifikátor se používá úplná cesta:

| Složka | Cesta pozorovaná při testu |
|---|---|
| Doručená pošta | `/e4477621-a775-4339-af95-7c350ef4fb1b.INBOX` |
| SMS Elektro | `/e4477621-a775-4339-af95-7c350ef4fb1b.INBOX.SMS Elektro` |
| SMS elektro faktury | `/e4477621-a775-4339-af95-7c350ef4fb1b.INBOX.SMS Elektro.SMS elektro faktury` |
| Hilti | `/e4477621-a775-4339-af95-7c350ef4fb1b.INBOX.Hilti` |
| Rozepsané | `/e4477621-a775-4339-af95-7c350ef4fb1b.Drafts` |
| Junk | `/e4477621-a775-4339-af95-7c350ef4fb1b.Junk` |
| Odeslané | `/e4477621-a775-4339-af95-7c350ef4fb1b.Sent` |
| Nevyžádaná pošta | `/e4477621-a775-4339-af95-7c350ef4fb1b.Junk E-mail` |
| Koš | `/e4477621-a775-4339-af95-7c350ef4fb1b.Trash` |

## Záseky a jejich řešení

| Projev | Příčina | Řešení |
|---|---|---|
| V nastavení nebyla Umělá inteligence ani MCP | eM Client 10.4 MCP nepodporoval | Vytvořit zálohu a aktualizovat na eM Client 11 |
| PowerShell hlásil „Cesta obsahuje neplatné znaky“ | Schránka obsahovala celý konfigurační text místo samotné cesty | Cestu a argumenty kopírovat z jednotlivých polí samostatně |
| Diagnostika našla jen jeden argument | Argumenty byly chybně rozděleny nebo načteny jako jeden řetězec | Zachovat tři samostatné argumenty přesně podle konfigurace eM Clienta |
| MCP proces se ihned ukončil s kódem 0 | Server nebyl spuštěn se správnou úplnou sadou argumentů | Opravit předání argumentů; poté proběhl `initialize` úspěšně |
| Server běžel, ale nebyl automaticky dostupný v každém chatu | Spuštění procesu samo o sobě nestačí; MCP musí být připojeno k používanému klientovi | Ověřit připojení v konkrétním prostředí ChatGPT/Codex |
| MCP není dostupné z telefonu nebo po vypnutí notebooku | Server používá lokální STDIO, nikoliv síťový transport | Pro pilot je to očekávané; trvalý vzdálený provoz vyžaduje jinou mailovou službu |
| Není jisté, zda briefing prošel všechny podsložky | Vypsání složek a prohledávání zpráv jsou samostatné operace | V zadání briefingu explicitně uvést složky nebo požadovat rekurzivní průchod |
| Briefing trval přibližně tři minuty | Vyhledávání, čtení konverzací a kontextová analýza vyžadují více MCP volání | Omezit období a složky; porovnat režim Chat a Work |

## Výsledek prvního briefingu

První praktický test:

- našel 19 zpráv v 18 konverzacích;
- pro kontext přečetl jednu související odeslanou zprávu;
- potlačil šest reklamních nebo newsletterových zpráv;
- neotevíral přílohy;
- trval přibližně tři minuty.

Správně zachytil například:

- chybějící podklady a koordinaci zakázky Ostrava Výstavní A1, A2;
- přímou otázku od Projektově.cz;
- riziko zapomenutí expedice a faktury Pamitech;
- bezpečnostní incident Partners;
- již vyřešené proformy a daňové doklady.

Výsledek byl uživatelem vyhodnocen jako věcně správný a prakticky užitečný. Ve schránce nebyla provedena žádná změna.

## Omezení současného řešení

- Funguje pouze při spuštěném Windows počítači a eM Clientu.
- Nejde o vzdálenou ani cloudovou mailovou službu.
- Přes MCP byl viditelný pouze účet `info@kompletelektro.cz`.
- Přístup je nyní pouze pro čtení.
- Přílohy jsou dostupné přes samostatný nástroj, ale při prvním briefingu se neotevíraly.
- Rozsah podsložek je vhodné uvádět explicitně v zadání.

## Bezpečnostní pravidla

- Nikdy neukládat MCP secret ani úplný konfigurační příkaz do GitHubu.
- Výchozí režim zůstává read-only.
- Nepovolovat mazání, přesun do koše ani expunge.
- Případný budoucí přesun zpráv povolit pouze do předem schválených složek, s auditním záznamem a podle rizika po potvrzení uživatele.
- Odesílání zpráv řešit samostatně a vždy s potvrzením.

## Další testy

- [ ] Upravit zadání briefingu tak, aby explicitně procházelo zvolené složky.
- [ ] Porovnat dobu běhu v režimech Chat a Work.
- [ ] Ověřit práci s přílohami na vybraném testovacím e-mailu.
- [ ] Ověřit, proč nejsou přes MCP viditelné ostatní účty.
- [ ] Vyzkoušet projektový inbox v Gmailu pro projekt BESS GuZu.
- [ ] Teprve podle přínosu rozhodnout o trvalé službě nebo malé VM.

## Architektonický závěr

eM Client MCP je vhodný pro rychlý pilot a interaktivní práci na zapnutém počítači. Není vhodný jako nepřetržitý vstup do AI workspace.

Pro další pilot je jednodušší vyzkoušet samostatný projektový e-mail, například pro BESS GuZu, napojený přímo na ChatGPT. Do něj lze přeposílat e-maily, dokumenty a fotografie také z telefonu.

Pokud se scénář osvědčí, lze následně navrhnout modelově nezávislou službu:

1. samostatnou read-only vrstvu pro příjem, indexaci a analýzu pošty;
2. oddělenou, výrazně omezenou službu pro schválené přesuny zpráv;
3. zákaz mazání;
4. audit všech provedených akcí.
