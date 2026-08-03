# Nasazení a vzdálený přístup

## Poslední doložený stav k 2026-08-03

HA Green je vypnutý a uložený u správce v šuplíku. Ještě není v produkčním provozu u Tomáše ani propojený s jeho místní sítí, GoodWe střídačem nebo dalšími zařízeními.

## Historie problému se startem

Dne 2026-05-15 se po odpojení napájení při jednom spuštění objevila pouze bílá LED a Home Assistant nebyl dostupný. Green později naběhl, ale příčina nebyla potvrzená a test se od té doby neopakoval.

Jediný neopakovaný incident zatím není důvodem Green vyřadit nebo jej rovnou nahradit Raspberry Pi 5. Před nasazením se má provést jeden kontrolovaný studený start:

1. Green zapnout, aktualizovat a ověřit jeho stabilní běh.
2. Korektně jej vypnout přes Home Assistant.
3. Odpojit a znovu připojit napájení.
4. Ověřit úplný start systému, lokální rozhraní a služby.
5. Pokud spolehlivě naběhne, považovat původní incident za neopakovaný. Pokud se problém vrátí, nejdřív provést diagnostiku a teprve podle výsledku rozhodnout o opravě nebo náhradě.

Opakované tvrdé odpojování napájení za běhu není součástí testu.

## Vzdálený přístup

Na připravené instalaci dříve spolehlivě fungoval Cloudflare Tunnel:

- veřejný název: `valtom.mikehub.cz`;
- externí URL Home Assistantu: `https://valtom.mikehub.cz`;
- řešení nevyžaduje veřejnou IPv4 u Tomáše;
- `valtom.mikehub.cz` je v domácím interním DNS výjimka a nesměřuje na Nginx Proxy Manager.

Dne 2026-08-03 vracel veřejný endpoint chybu Cloudflare `1033`. Jde o očekávaný důsledek vypnutého Green a nepřipojeného `cloudflared` konektoru, nikoli o doloženou závadu dříve funkčního tunelu.

Pro důvěru k reverzní proxy byla použita konfigurace Home Assistantu s `use_x_forwarded_for: true` a rozsahem `trusted_proxies: 172.30.33.0/24`. Cloudflare token ani jiné tajné hodnoty do repozitáře nepatří.

Cloudflare Tunnel poskytuje přístup k webovému rozhraní Home Assistantu. Nezajišťuje plný servisní přístup do Tomášovy LAN ani přímou správu GoodWe a dalších místních zařízení. MikroTik nebo WireGuard pro tento účel byly pouze zvažované a nejsou doložené jako realizované; o jejich potřebě se rozhodne až podle praxe po nasazení.

## Přejímací kontrola nasazení

- [ ] Před fyzickým nasazením a při převzetí dokončit přejímací kontrolu HA ValTom.

Přejímací kontrola zahrnuje:

1. aktualizaci Home Assistant Core, OS, Supervisoru a potřebných komponent;
2. jeden kontrolovaný studený start podle postupu výše;
3. fyzické nasazení, zjištění lokální IP adresy a nastavení její rezervace;
4. ověření síťové dostupnosti GoodWe z Home Assistantu;
5. ověření lokálního přístupu k Home Assistantu;
6. ověření Cloudflare Tunnelu, interní a externí URL;
7. vytvoření nového aktuálního full backupu;
8. zapojení dostupnosti instance do společného monitoringu.

Pravidelné produkční zálohování a praktický restore se vedou v [centrální dokumentaci záloh Home Assistantu](../../MadMike/Zalohy/Home-Assistant.md).
