# AI workspace a integrace

Tato oblast dokumentuje propojení AI s provozními systémy MadMike. Cílem je praktická úspora práce a architektura pokud možno nezávislá na konkrétním AI modelu.

## Integrace

| Integrace | Stav | Dokumentace |
|---|---|---|
| eM Client MCP | Lokální read-only pilot ověřen | [eM Client MCP](eM-Client-MCP.md) |
| MikroTik MCP | Provozní read-only pilot | [MikroTik MCP](../Servery/MikroTik-MCP.md) |
| Projektový e-mail BESS GuZu | Zvažovaný další pilot | zatím bez samostatné dokumentace |

## Společné zásady

- Nejprve ověřit přínos na úzkém pilotu a teprve potom budovat trvalou službu.
- Oddělovat čtení a analýzu od nástrojů, které mění zdrojový systém.
- Mazání nepovolovat bez samostatného bezpečnostního návrhu.
- Zápisové operace mají být omezené, auditované a podle rizika potvrzené uživatelem.
- Hesla, tokeny, MCP secrety a jiné tajné údaje neukládat do GitHubu.
- U každé integrace rozlišovat lokální STDIO připojení od vzdálené HTTP služby.
- Zachovat možnost vyměnit používaný AI model bez přestavby celé integrační vrstvy.
