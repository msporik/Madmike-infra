# Nasazení a vzdálený přístup

## Poslední doložený stav k 2026-08-03

HA Green je vypnutý a uložený u správce v šuplíku. Ještě není v produkčním provozu u Tomáše ani propojený s jeho místní sítí, GoodWe střídačem nebo dalšími zařízeními.

## Historie problému se startem

Dne 2026-05-15 se po odpojení napájení při jednom spuštění objevila pouze bílá LED a Home Assistant nebyl dostupný. Green později naběhl, ale příčina nebyla potvrzená a test se od té doby neopakoval.

Jediný neopakovaný incident zatím není důvodem Green vyřadit nebo jej rovnou nahradit Raspberry Pi 5. Před nasazením se má provést jeden kontrolovaný studený start:

1. Green zapnout a vyčkat na úplný start bez dalších zásahů.
2. Ověřit stabilní běh, lokální rozhraní a dostupné diagnostické informace.
3. Korektně jej vypnout přes Home Assistant.
4. Po úplném vypnutí odpojit a znovu připojit napájení.
5. Ověřit úplný start systému, lokální rozhraní a služby.
6. Pokud spolehlivě naběhne, považovat původní incident za neopakovaný. Pokud se problém vrátí, nejdřív provést diagnostiku a teprve podle výsledku rozhodnout o opravě nebo náhradě.

Opakované tvrdé odpojování napájení za běhu není součástí testu.

## Přístupová architektura

```text
uživatel nebo správce
→ HTTPS valtom.mikehub.cz
→ Cloudflare Tunnel
→ cloudflared na HA Green
→ Home Assistant
```

Na připravené instalaci dříve spolehlivě fungoval Cloudflare Tunnel:

- veřejný název: `valtom.mikehub.cz`;
- externí URL Home Assistantu: `https://valtom.mikehub.cz`;
- řešení nevyžaduje veřejnou IPv4 u Tomáše ani port forwarding;
- `valtom.mikehub.cz` je v domácím interním DNS výjimka a nesměřuje na Nginx Proxy Manager.

Dne 2026-08-03 vracel veřejný endpoint chybu Cloudflare `1033`. Jde o očekávaný důsledek vypnutého Green a nepřipojeného `cloudflared` konektoru, nikoli o doloženou závadu dříve funkčního tunelu.

Pro důvěru k reverzní proxy byla použita konfigurace Home Assistantu s `use_x_forwarded_for: true` a rozsahem `trusted_proxies: 172.30.33.0/24`. Cloudflare token ani jiné tajné hodnoty do repozitáře nepatří.

Cloudflare Tunnel poskytuje přístup k webovému rozhraní Home Assistantu. Nezajišťuje plný servisní přístup do Tomášovy LAN ani přímou správu GoodWe a dalších místních zařízení. MikroTik nebo WireGuard pro tento účel byly pouze zvažované a nejsou doložené jako realizované; o jejich potřebě se rozhodne až podle praxe po nasazení.

## Příprava před fyzickým přesunem

1. Ověřit originální napájecí zdroj, ethernetový kabel a fyzický stav Green.
2. Zajistit lokální přístup k zařízení a dostupnost staršího backupu před první změnou.
3. Spustit Green a zaznamenat verze Core, OS, Supervisoru a skutečně aktivní aplikace a integrace.
4. Zkontrolovat systémová varování a logy. Neodstraňovat komponenty jen proto, že jejich současná role není doložená.
5. Vytvořit nový full backup výchozího stavu a bezpečně jej stáhnout mimo Green.
6. Provést podporované aktualizace po srozumitelných krocích; po každém restartu ověřit lokální UI a logy.
7. Ověřit Cloudflare Tunnel a externí URL.
8. Provést jeden kontrolovaný studený start podle postupu výše.
9. Vytvořit nový post-update full backup a ověřit, že jej lze otevřít jako položku obnovy a že je bezpečně uložený mimo zařízení.

Přesné verze, datum obou backupů a výsledek testu se po provedení zapíší sem. Samotné backupy patří do určeného úložiště, ne do GitHubu.

## Fyzické nasazení u Tomáše

1. Umístit Green do suchého, větraného a servisně přístupného místa se stabilním napájením a ethernetem.
2. Připojit jej nejprve bez automatického řízení spotřebičů.
3. Zjistit skutečnou lokální IP adresu a vytvořit odpovídající DHCP rezervaci. IP, síť a zařízení, které rezervaci poskytuje, potom zdokumentovat.
4. Ověřit lokální přístup z Tomášovy sítě a korektní čas systému.
5. Ověřit odchozí připojení Cloudflare a přístup přes `https://valtom.mikehub.cz`.
6. Ověřit, že Home Assistant dokáže v místní síti dosáhnout na GoodWe; integrační postup pokračuje v [GoodWe a energetika](GoodWe-a-energie.md).
7. Po ustálení sítě vytvořit aktuální full backup, nastavit produkční zálohování a zapojit dostupnost do společného monitoringu.
8. Domluvit běžný uživatelský přístup, správcovskou odpovědnost, MFA/recovery a možnost místního zásahu.

## Běžný provozní postup

### Restart nebo korektní vypnutí

1. Ověřit, zda neprobíhá update, backup, restore nebo jiný zásadní zápis.
2. Restart Core použít jen při změně, která jej vyžaduje; restart hostitele použít při aktualizaci OS, Supervisoru nebo diagnostice celé appliance.
3. Pro plánované odpojení napájení nejprve provést korektní vypnutí z Home Assistantu a vyčkat na jeho dokončení.
4. Po startu ověřit lokální UI, systémová varování, Cloudflare, GoodWe a dostupnost z monitoringu.

### Aktualizace

1. Přečíst poznámky k vydání a ověřit známé breaking changes pro používané integrace.
2. Vytvořit a stáhnout full backup.
3. Aktualizovat jen jednu vrstvu nebo předem vymezený celek.
4. Po restartu ověřit lokální přihlášení, logy, Cloudflare a hlavní entity.
5. Pokud se objeví chyba, nepokračovat dalšími aktualizacemi; zaznamenat verze a použít podporovaný návrat nebo restore.
6. Po úspěšné přejímce vytvořit nový backup podle centrální strategie.

Podporované postupy a aktuální ovládání se řídí [oficiální dokumentací Home Assistant OS](https://www.home-assistant.io/common-tasks/os/).

## Diagnostika dostupnosti

Postupuje se od nejnižší vrstvy. Jedna funkční vrstva nepotvrzuje ostatní.

| Projev | První rozlišení | Další krok |
|---|---|---|
| Green je bez očekávané signalizace | napájení, zdroj, zásuvka a kabel | Nepokračovat opakovaným odpojováním; ověřit napájení a zdokumentovat stav LED. |
| Po startu svítí jen bílá LED a UI nenaběhne | opakování incidentu z 2026-05-15 | Vyčkat přiměřenou dobu, ověřit DHCP a lokální dostupnost, zachovat důkazy a zastavit nasazení před rozhodnutím o náhradě. |
| Lokální UI nefunguje | napájení, linka, DHCP/IP nebo samotný HA | Ověřit klienta ve stejné LAN, DHCP lease, linku a stav Green. Cloudflare zatím neřešit. |
| Lokální UI funguje, veřejná URL vrací `1033` | cloudflared konektor není připojený | Ověřit běh a log aplikace Cloudflared a odchozí přístup k internetu. Neměnit DNS naslepo. |
| Lokální UI funguje, veřejná URL má jinou chybu | DNS, tunel, certifikát nebo konfigurace HA | Ověřit veřejný DNS záznam, stav tunelu, log Cloudflared a proxy konfiguraci HA. |
| Veřejná URL se otevře, přihlášení selže | účet, MFA nebo stav identity | Síťovou cestu neměnit. Použít ověřený recovery postup a společné zásady přístupů. |
| HA funguje, GoodWe je nedostupné | místní síť, IP, komunikační modul nebo protokol | Pokračovat read-only diagnostikou podle dokumentu GoodWe; Cloudflare plný přístup do LAN neposkytuje. |
| Po update nefunguje hlavní funkce | konkrétní aktualizovaná vrstva | Zastavit další změny, uložit logy a verze, vyhodnotit rollback nebo restore. |

## Obnova

Autoritativní retence, externí kopie a plán restore jsou v [centrální dokumentaci záloh Home Assistantu](../../MadMike/Zalohy/Home-Assistant.md). Pro tuto instanci platí:

1. Obnovu neprovádět naslepo přes jedinou existující funkční instalaci bez ověřeného backupu a návratové cesty.
2. Vybrat backup podle data, verze a účelu; květnový master image je čistý přípravný základ, nikoli produkční obraz domu.
3. Před restore zaznamenat současný stav a zachovat dostupné diagnostické informace.
4. Po restore ověřit minimálně start, přihlášení, lokální síť, Cloudflare, GoodWe, dashboard, automatizace a vytvoření nového backupu.
5. Výsledek restore testu zapsat bez tajných hodnot, včetně použitého backupu, cílového hardwaru a ověřených funkcí.

## Přejímací kontrola nasazení

- [ ] Před fyzickým nasazením a při převzetí dokončit přejímací kontrolu HA ValTom.

Přejímka je hotová pouze tehdy, když je doložené:

1. skutečné umístění, napájení, lokální IP a DHCP rezervace;
2. aktuální verze Core, OS a Supervisoru;
3. jeden úspěšný kontrolovaný studený start;
4. funkční lokální UI a Cloudflare Tunnel;
5. síťová dosažitelnost GoodWe z Home Assistantu;
6. aktuální full backup mimo Green a nastavený produkční režim záloh;
7. dostupnost instance ve společném monitoringu a ověřené upozornění;
8. potvrzené účty, role, MFA/recovery a možnost místního zásahu;
9. zapsaný výsledek přejímky a všechny zbývající odchylky označené jako **Vyžaduje ověření v živém systému.**
