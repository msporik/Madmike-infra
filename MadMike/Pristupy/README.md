# Přístupy

> Stav dokumentace ověřen k **2026-07-29**. Přehled vychází z auditované dokumentace a prakticky potvrzených kroků; neprokazuje živý stav všech pravidel, rolí, MFA ani recovery.

Průřezová dokumentace přístupů, ověřování identity a správy přihlašovacích údajů v infrastruktuře MadMike.

Tento projekt popisuje společné zásady a stav zavádění. Technická konfigurace jednotlivých tunelů, proxy hostů a služeb zůstává v jejich vlastních dokumentech.

## Základní zásady

- Administrační a monitorovací služby mají být dostupné z domácí LAN nebo přes WireGuard, ne přímo z internetu.
- WireGuard vytváří chráněnou síťovou cestu. Nenahrazuje přihlášení, oprávnění, MFA ani recovery uvnitř konkrétní služby.
- Interní názvy a důvěryhodné HTTPS zajišťují interní DNS a Nginx Proxy Manager.
- Veřejně dostupná služba je vědomá výjimka a její cesta musí být popsaná u konkrétního projektu.
- Přímé veřejné RDP k PREMIERu je současný zděděný stav a evidované riziko, nikoli cílový přístupový model.
- Změna přístupu nesmí bez praktické náhrady zablokovat běžné uživatele služby.
- Hesla, privátní klíče, recovery kódy, tokeny ani jiné tajné hodnoty se do repozitáře nezapisují.

## Interní a administrační přístupy

| Oblast | Současná cesta | Ověřený stav a hranice | Autoritativní dokument |
|---|---|---|---|
| PVE, PBS, NPM a monitoring | domácí LAN nebo notebookový WireGuard; interní DNS a NPM | Cesta k dokumentovaným službám byla prakticky ověřená. Přihlášení, role, MFA a recovery jednotlivých služeb tento projekt neinventarizuje. | [Servery](../Servery/README.md), [Monitoring](../Monitoring/README.md) |
| RouterOS a WinBox | LAN nebo příslušný WireGuard; přihlašovací údaj se zatím ručně dohledává v Bitwardenu | Administrace nemá být veřejná. Úplný stav uživatelů, oprávnění a MFA jednotlivých lokalit není ověřený. | [Síť / MikroTik](../Sit/MikroTik.md), [WireGuard](../Servery/WireGuard.md) |
| Bitwarden Cloud EU | veřejná cloudová služba poskytovatele, nikoli publikace domácí infrastruktury | Funkční pilot pouze na PC; telefon chybí, staré ukládání zůstává zapnuté a Bitwarden ještě není jediným zdrojem přihlašovacích údajů. | [Bitwarden](Bitwarden.md) |

## Vědomé veřejné výjimky

| Služba | Současná cesta | Stav a hranice | Autoritativní dokument |
|---|---|---|---|
| Nextcloud | veřejné HTTPS přímo na VM401 přes Apache | Přístup funguje. Úplná publikační cesta, MFA a recovery zatím nejsou ověřené. | [Nextcloud – přístup a uživatelé](../Nextcloud/Pristup-a-uzivatele.md) |
| PREMIER / VM501 | přímé veřejné RDP přes MikroTik | Přístup účetní funguje, ale jde o zděděné riziko. Přesné živé NAT/firewall pravidlo nebylo ověřené a cílová náhrada není vybraná. | [PREMIER – přístup a provoz](../Premier/Pristup-a-provoz.md) |
| HA ValTom | Cloudflare Tunnel na připraveném HA Green | Veřejný přístup byl na připravené instalaci zprovozněný. HA ještě není produkčně nasazený u Tomáše a po přesunu se musí cesta znovu ověřit. | [HA ValTom – nasazení a přístup](../../HA-ValTom/Home-Assistant/Nasazeni-a-pristup.md) |

## Hranice dokumentace

- WireGuard adresy, peery, směrování a DNS klientů patří do `Servery/WireGuard.md`.
- Interní DNS, NPM upstreamy a certifikáty patří do `Servery/DNS-NPM-HTTPS.md`.
- NAT, firewall, veřejná publikační cesta, uživatelé, role, MFA a recovery konkrétní služby patří do jejího projektu a podle potřeby do projektu Síť.
- Tento projekt drží společné zásady, stav Bitwardenu a rozhodnutí platná napříč službami.

## Nejbližší kroky

- [ ] Vybrat jednoduchou cílovou náhradu přímého veřejného RDP k PREMIERu podle skutečného způsobu práce účetní.
- [ ] Definovat a prakticky ověřit minimální nouzový postup pro obnovu administrátorského přístupu po současné ztrátě notebooku a telefonu.
