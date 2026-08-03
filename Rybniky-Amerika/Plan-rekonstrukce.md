# Plán rekonstrukce

> Poslední doložená schválená architektura: **2026-07-29**. Plán neznamená, že některá etapa už byla provedena.

## Cíl

Přestavět existující funkční, ale nesourodou síť po etapách na schválenou jednoduchou architekturu:

- přijímací rádio jako bridge/CPE;
- hEX S (2025) jako jediný router, DHCP server a firewall;
- přímé směrování k HOME přes stávající sektorový rádiový přívod bez lokálního NATu a bez WireGuardu;
- přísně oddělená privátní a hostovská Wi-Fi;
- spravovaná L2 distribuce bez dalších DHCP a NAT ostrovů;
- kabelově připojená AP se společným privátním a hostovským SSID;
- centrální evidence a zálohy MikroTiků v Mikru a souhrnný alarm lokality.

Rekonstrukce nesmí sama o sobě ohrozit nezdokumentované služby. Starší varianty hEX S versus RB5009, lokální NAT a úvahy o povinném CRS326 jsou uzavřené; nejsou nadále rozhodovacími body.

## Pravidla realizace

- Mění se vždy jediná logická vrstva nebo větev.
- Před zapisující změnou musí existovat živě ověřený výchozí stav, místní přístup, použitelná záloha, test úspěchu a konkrétní rollback.
- Konfigurace se připravuje mimo produkci; servisní zásah neslouží k návrhu za pochodu.
- Sdílený sektor `AP HOME` se nemění bez posouzení dopadu na ostatní připojení.
- Tajné hodnoty, neupravené exporty, hesla a klíče zůstávají mimo GitHub.
- Po každé etapě se aktualizuje dokumentace skutečného stavu; plánovaný stav se neoznačuje jako aktivní před přejímkou.
- Nesplněný přejímací test nebo ztráta správy je důvod k návratu, nikoli k rozšíření zásahu.

## Etapy

### 0. Inventura a návratový základ

**Vstupní podmínka:** přístup ke všem aktivním bodům, možnost bezpečně pořídit konfigurace a domluvené servisní okno pro případné krátké ověřovací testy.

**Práce:**

- získat exporty a binární zálohy aktivních MikroTiků bez uložení tajných hodnot do GitHubu;
- zaznamenat modely, identity, management IP, RouterOS, firmware, role, napájení a fyzické umístění;
- zmapovat porty, kabely, optiku, AP, DHCP, NAT, firewall, port-forwardy a statické klienty;
- ověřit NVR, zařízení „Stavba“ a další klienty citlivé na změnu adresace;
- identifikovat všechny klienty a závislosti sdíleného sektoru `AP HOME`;
- změřit parametry a reálnou propustnost rádiového přívodu;
- vytvořit aktuální topologii, portový plán, fotografie uzlů a původní schéma zapojení pro návrat;
- ověřit možnost místního zásahu, přístupová oprávnění a osobu dostupnou během změny;
- porovnat aktivní kusy s Airtable a stavem v Mikru.

**Test úspěchu:** každý aktivní prvek a kritická služba mají známou roli, záloha je čitelná, kabeláž je dohledatelná, management funguje a existuje jednoznačný výchozí stav pro porovnání po změně.

**Rollback:** etapa je primárně čtecí. Pokud inventura není úplná nebo záloha není použitelná, produkční zapojení se nemění.

### 1. Příprava hEX S (2025)

**Vstupní podmínka:** dokončená inventura, přidělený cílový LAN prefix, v Airtable rezervovaný konkrétní hEX S a známé nutné výjimky pro provoz.

**Práce:**

- připravit konfiguraci mimo produkci;
- ověřit RouterOS, firmware, porty, SFP, napájení a resetovací postup cílového kusu;
- nastavit lokální DHCP, DNS forwarding, směrování, firewall a bezpečný management;
- připravit směrování mezi HOME a Rybníky bez WireGuardu a lokálního NATu;
- povolit správu z HOME;
- zablokovat privátní síti Rybníků přístup do HOME kromě jednotlivých schválených výjimek;
- hostům povolit pouze internet, zakázat HOME, privátní síť i management a zapnout izolaci klientů;
- nastavit hostům počátečně 15 Mb/s na klienta a 70–80 Mb/s celkem;
- připravit testovací klienty privátní i hostovské sítě a přesný záznam očekávaných výsledků;
- vytvořit backup a `.rsc` připravené konfigurace bez zveřejnění jejich obsahu.

**Test úspěchu:** konfigurace se bez chyby načte do cílového kusu, hEX S je spravovatelný pouze zamýšlenou cestou, DHCP používá správný rozsah a pro každý bezpečnostní směr existuje konkrétní test.

**Rollback:** v produkci se ještě nic nemění. Předchozí konfigurace cílového kusu zůstane zálohovaná a kus lze vrátit do původního stavu.

### 2. Přechod rádiového přívodu a core

**Vstupní podmínka:** potvrzený model a režim přijímací jednotky, zálohy současného rádia i core, popsané původní zapojení, připravený hEX S, fyzická přítomnost u zásahu a předem stanovený časový limit pro návrat.

**Práce:**

- převést přijímací rádio do režimu bridge/CPE;
- zapojit připravený hEX S jako jediný místní L3 core;
- aktivovat přímé směrování na HOME;
- ponechat sdílený sektor `AP HOME` v jeho ověřené provozní konfiguraci;
- připojit nejprve jediného testovacího klienta nebo předem vybranou větev;
- další větve přidat až po úspěšném základním testu.

**Test úspěchu:**

- fungují internet, DNS a očekávané služby;
- správa z HOME do Rybníků je dostupná;
- privátní síť Rybníků se do HOME nedostane bez položky v allowlistu;
- hosté se nedostanou do privátní sítě, HOME ani managementu a nevidí se navzájem;
- na přijímacím rádiu ani jinde nezůstal skrytý DHCP, NAT nebo další firewall;
- NVR a zařízení „Stavba“ fungují stejně jako před změnou;
- ostatní připojení sdíleného sektoru zůstala funkční;
- Mikr a logy neukazují neočekávanou chybu.

**Rollback:** odpojit nový hEX S, obnovit původní zapojení a konfiguraci přijímací jednotky i původního core podle fotografií a záloh z etapy 0. Po předem stanoveném časovém limitu se bez dalšího ladění vrací původní stav.

### 3. Odstranění NAT ostrovů

**Vstupní podmínka:** core je stabilní, každá větev má portovou mapu a seznam očekávaných klientů. Začít jedinou pilotní větví.

**Práce:** postupovat samostatně po větvích Obývák, Včelín, Hospoda a Dílna. SOHO routery převést do AP/bridge režimu, nahradit nebo odstranit. V jednom servisním kroku měnit pouze jednu větev.

**Test úspěchu:** všichni známí klienti pilotní větve dostanou adresu z centrálního DHCP, fungují očekávané služby a Wi-Fi a v dané větvi není další DHCP ani NAT.

**Rollback:** vrátit původní zařízení, konfiguraci a kabeláž pouze měněné větve. Dokud pilotní větev neprojde testy a není stabilní, nepokračovat na další.

### 4. L2 distribuce a Wi-Fi

**Vstupní podmínka:** známý počet portů, PoE rozpočet, stav optiky, změřené pokrytí, vybrané konkrétní skladové kusy a rozhodnutý způsob centrální správy AP.

**Práce:**

- Včelín provozovat pouze jako L2 distribuční bod;
- doplnit spravované switche podle skutečného počtu portů, optiky a PoE;
- nastavit identity, management IP, popisy portů, RSTP a zálohy konfigurací;
- rozmístit kabelově připojená AP podle měření, s důrazem na stabilní 2,4GHz pokrytí;
- na vhodných AP vysílat jednotné privátní a hostovské SSID;
- koordinovat kanály a vysílací výkony podle skutečného prostředí;
- umožnit centrální změnu údajů hostovské sítě a připravit QR kód bez zveřejnění tajné hodnoty v GitHubu;
- VLAN a CAPsMAN použít jen tehdy, pokud jsou potřebné pro bezpečné oddělení nebo prokazatelně zjednoduší správu;
- nepoužívat mesh ani repeatery jako náhradu dostupné kabeláže.

**Test úspěchu:** distribuce nemá smyčky ani další L3 funkce, všechny porty odpovídají portové mapě, pokrytí je použitelné a bezpečnostní testy privátní a hostovské sítě projdou na každém AP.

**Rollback:** vracet vždy jen poslední změněnou větev nebo AP na původní zařízení a konfiguraci; stabilní dokončené větve ponechat beze změny.

### 5. Sloup a mobilhome

**Vstupní podmínka:** základní síť je stabilní a jsou ověřené optika, napájení, uzemnění, přepěťová ochrana, PoE rozpočet, trasa, přímá viditelnost, Fresnelova zóna, vegetace a požadovaná kapacita.

**Práce:** teprve podle výsledků průzkumu vybrat venkovní distribuční prvek a případný 5GHz nebo 60GHz uplink k mobilhome. Pro hlavní přívod HOME → Rybníky se nyní 60 GHz neplánuje.

**Test úspěchu:** nová část dosáhne stanovené propustnosti a stability, neovlivní základní síť a projde testem napájení, vzdálené správy a bezpečnostního oddělení.

**Rollback:** novou větev fyzicky a logicky odpojit bez zásahu do stabilní základní sítě.

### 6. Správa, monitoring a zálohy

**Vstupní podmínka:** finální identity, management adresy a závislosti všech nasazených zařízení jsou zapsané.

**Práce:**

- přidat do Mikru všechny MikroTiky lokality;
- aktivně hlídat hEX S, rádiový přívod a klíčovou distribuci;
- nastavit závislosti a souhrnný alarm lokality tak, aby výpadek upstreamu nevyvolal lavinu alarmů všech AP;
- nepřidávat aktivní alarm na každou metriku a každý nekritický prvek;
- nastavit exporty a pravidelné zálohy konfigurací podle [autoritativního dokumentu záloh](../MadMike/Zalohy/MikroTik.md);
- zapsat finální topologii, adresaci, portovou mapu a výsledky provozních testů do GitHubu.

**Test úspěchu:** kontrolovaný výpadek vhodného prvku vyvolá očekávaný souhrnný alarm a recovery bez duplicit, záloha je dostupná a obnova je prakticky ověřená na náhradním nebo testovacím zařízení.

**Rollback:** chybné monitorovací pravidlo nebo zálohovací úlohu odstranit a obnovit předchozí konfiguraci; tato etapa nesmí měnit datovou cestu lokality.

### 7. Stabilizační období a předání

**Vstupní podmínka:** všechny provedené etapy prošly přejímkou a dokumentace odpovídá skutečnému stavu.

**Práce:**

- sledovat stabilitu rádiového přívodu, hEX S, větví, DHCP, Wi-Fi a alarmů po dohodnuté období;
- ověřit běžný provoz i reprezentativní zatížení hostovské sítě;
- zkontrolovat stáří exportů a vznik druhé kopie podle dokumentace záloh;
- odstranit pouze prokazatelně nepoužívané dočasné routy, výjimky a rollback prvky;
- předat správci aktuální topologii, portovou mapu, přístupové cesty, postup místního zásahu a seznam otevřených úkolů.

**Test úspěchu:** nový správce dokáže podle GitHub dokumentace provést běžnou kontrolu, diagnostikovat výpadek po vrstvách a dohledat rollback a zálohu bez znalosti historie chatů.

**Rollback:** pokud stabilizační období odhalí závažnou regresi, vrátit pouze poslední příčinnou změnu. Neobnovovat plošně starou nesourodou topologii, pokud problém patří jedné větvi.

## Souhrnný přejímací test

Po každé relevantní etapě otestovat pouze dotčený rozsah; po dokončení core a Wi-Fi provést celý test:

### Konektivita a služby

- hEX S má očekávané routy a dostupnou správu z HOME.
- Klient získá správnou IP, gateway a DNS z lokálního DHCP.
- Internet a DNS fungují na skutečném privátním i hostovském klientovi.
- NVR, „Stavba“ a známé statické klienty jsou dostupné podle schválené politiky.
- Obývák, Včelín, Hospoda a Dílna fungují a nemají další DHCP ani NAT.

### Bezpečnost

- Privátní síť se do HOME nedostane bez konkrétní allowlist výjimky.
- Management z HOME funguje pouze zamýšlenou cestou.
- Host se nedostane do privátní sítě, HOME ani managementu.
- Dva hosté spolu nemohou komunikovat.
- Hostovské limity odpovídají aktuálně schváleným hodnotám.

### Wi-Fi a rádio

- Privátní i hostovské SSID fungují na každém zamýšleném AP.
- Přechod mezi oblastmi nevyžaduje ruční volbu jiného názvu sítě.
- Kanály, výkony a pokrytí odpovídají měření.
- Rádiový přívod je stabilní a ostatní klienti sdíleného sektoru nebyli změnou ovlivněni.

### Správa a obnova

- Identity, portové popisy, čas a management adresy jsou zapsané.
- Mikr zobrazuje očekávaná zařízení a kořenový výpadek nevytváří lavinu alarmů.
- Existuje označený známý funkční `.backup` a `.rsc` po změně.
- GitHub odpovídá skutečné topologii a aktivnímu stavu.
- Rollback byl během přípravy prakticky prověřen v bezpečném rozsahu.

## Otevřené přípravné úkoly

> Následující body **vyžadují ověření v živém systému**. Navazující výsledek se dokončí v uvedeném autoritativním dokumentu.

- [ ] Přidělit cílový LAN prefix Rybníků v rámci společného adresního plánu.
- [ ] Po inventuře sepsat jednotlivé nutné výjimky z privátní sítě Rybníků do HOME; bez doložené potřeby zůstane výchozí `deny`.
- [ ] Podle inventury doplnit konkrétní testovací checklist, časový limit a kabelový postup rollbacku pro etapu 2.
- [ ] Vybrat pilotní větev pro odstranění prvního NAT ostrova.
- [ ] Vybrat způsob centrální správy AP a ověřit kompatibilitu konkrétních modelů.
- [ ] V dokumentu Mikr navrhnout závislosti a souhrnný alarm lokality.
- [ ] V dokumentaci záloh MikroTiků doplnit a prakticky ověřit obnovu konfigurace Rybníků.

## Hlavní rizika

- neznámé statické IP a port-forwardy;
- výpadek NVR nebo zařízení „Stavba“;
- změna více částí v jednom zásahu;
- nechtěný dopad změny sdíleného sektoru na další připojení;
- smíšené RouterOS a Wi-Fi generace;
- přepětí na venkovních metalických trasách;
- zbytečné VLAN, CAPsMAN nebo nový monitoring bez konkrétního přínosu;
- neověřený vzdálený přístup bez místní návratové cesty.

Každá etapa musí mít zálohu konfigurace, testovací checklist, časový limit a jasný rollback.
