# Přístupy

Průřezová dokumentace přístupů, ověřování identity a správy přihlašovacích údajů v infrastruktuře MadMike.

Tento projekt popisuje společné zásady a stav zavádění. Technická konfigurace jednotlivých tunelů, proxy hostů a služeb zůstává v jejich vlastních dokumentech.

## Základní zásady

- Administrační a monitorovací služby mají být dostupné z domácí LAN nebo přes WireGuard, ne přímo z internetu.
- Interní názvy a důvěryhodné HTTPS zajišťují interní DNS a Nginx Proxy Manager.
- Veřejně dostupná služba je vědomá výjimka a její cesta musí být popsaná u konkrétního projektu.
- Přímé veřejné RDP k PREMIERu je současný zděděný stav a evidované riziko, nikoli cílový přístupový model.
- Změna přístupu nesmí bez praktické náhrady zablokovat běžné uživatele služby.
- Hesla, privátní klíče, recovery kódy, tokeny ani jiné tajné hodnoty se do repozitáře nezapisují.

## Současný model

| Oblast | Stav | Autoritativní dokument |
|---|---|---|
| Administrace zvenku | funguje přes WireGuard | [WireGuard](../Servery/WireGuard.md) |
| Interní názvy a HTTPS | funguje přes RB5009 a NPM | [Interní DNS, NPM a HTTPS](../Servery/DNS-NPM-HTTPS.md) |
| Správa hesel | probíhá pilot Bitwarden Cloud EU | [Bitwarden](Bitwarden.md) |
| PREMIER / RDP | přímé veřejné RDP; cílová náhrada není vybraná | [PREMIER – přístup a provoz](../Premier/Pristup-a-provoz.md) |
| Nextcloud | veřejný webový přístup funguje; MFA a celá publikační cesta nejsou ověřené | [Nextcloud – přístup a uživatelé](../Nextcloud/Pristup-a-uzivatele.md) |

## Hranice dokumentace

- WireGuard adresy, peery, směrování a DNS klientů patří do `Servery/WireGuard.md`.
- Interní DNS, NPM upstreamy a certifikáty patří do `Servery/DNS-NPM-HTTPS.md`.
- Výjimky a provozní požadavky konkrétní služby patří do jejího projektu.
- Tento projekt drží společné zásady, stav Bitwardenu a rozhodnutí platná napříč službami.

## Nejbližší kroky

- [ ] Dokončit pilot Bitwardenu na několika běžných a administračních účtech.
- [ ] Nastavit MFA pro Bitwarden a bezpečný recovery postup.
- [ ] Ověřit a popsat aktuální veřejné RDP pravidlo pro PREMIER.
- [ ] Vybrat jednoduchou náhradu přímého veřejného RDP podle skutečného způsobu práce účetní.
- [ ] Postupně ověřit MFA a recovery u veřejně dostupných služeb.
