# Přístup a uživatelé

## Webový přístup

Produkční Nextcloud je dostupný na:

`https://cloud.madmike.cz`

Podle potvrzení správce z 29. 7. 2026 je služba publikovaná přímo na VM401 přes Apache, nikoli přes interní Nginx Proxy Manager. Přesná cesta veřejného DNS, NAT/firewallu, HTTPS certifikátu a jeho obnovy zatím není v dokumentaci živě ověřená.

## Současní a plánovaní uživatelé

| Uživatel | Provozní stav |
|---|---|
| `madmike` | jediný současný uživatel; ukládání a synchronizace vlastních souborů fungují |
| `katka` | účet a data jsou historicky doložené, nyní má problém s přihlášením |
| `djlobo` | vyřazen ze současného používání; technická existence a stav účtu nejsou živě ověřené |
| dvě děti | účty jsou plán, nikoli současný stav |

Tento přehled popisuje skutečné používání potvrzené správcem. Neprokazuje aktuální technickou existenci všech účtů ani jejich oprávnění. Administrátorská role zatím není živě ověřená.

Účetní Nextcloud nepoužívá a služba není součástí předávání dat pro PREMIER.

## Bezpečnostní hranice

- Hesla, recovery kódy, aplikační hesla, tokeny ani obsah soukromých dat se do repozitáře neukládají.
- Stav MFA a recovery postupu není ověřený.
- Veřejné odkazy a externí sdílení nejsou inventarizované.
- Aplikační hesla a připojení klienti nejsou inventarizované.
- Administrátorské účty a jejich role nejsou ověřené.

Společné zásady správy přístupů a přihlašovacích údajů jsou v projektu [Přístupy](../Pristupy/README.md).

## Otevřené kontroly

- [ ] Opravit přihlášení Katky a ověřit následnou synchronizaci.
- [ ] Ověřit aktivní účty, administrátorskou roli a potvrdit, že `djlobo` nemá aktivní přístup.
- [ ] Ověřit stav MFA a bezpečný recovery postup.
- [ ] Ověřit používaná aplikační hesla a připojené klienty bez zápisu jejich tajných hodnot.
- [ ] Ověřit současné veřejné odkazy a pravidla externího sdílení.
- [ ] Popsat a ověřit úplnou přímou publikační cestu `cloud.madmike.cz`, včetně DNS, NAT/firewallu, HTTPS certifikátu a jeho obnovy.
- [ ] Později založit účty pro dvě děti podle schváleného rozšíření služby.
