# Plán rekonstrukce

## Cíl

Přestavět existující funkční, ale nesourodou síť po etapách na schválenou jednoduchou architekturu:

- přijímací rádio jako bridge/CPE;
- hEX S (2025) jako jediný router, DHCP server a firewall;
- přímé směrování k HOME přes stávající sektorový rádiový přívod bez lokálního NATu a bez WireGuardu;
- přísně oddělená privátní a hostovská Wi-Fi;
- spravovaná L2 distribuce bez dalších DHCP a NAT ostrovů.

Rekonstrukce nesmí sama o sobě ohrozit nezdokumentované služby. Starší varianty hEX S versus RB5009 a úvahy o povinném CRS326 jsou uzavřené; nejsou nadále rozhodovacími body.

## Etapy

### 0. Inventura a návratový základ

**Vstupní podmínka:** přístup ke všem aktivním bodům, možnost bezpečně pořídit konfigurace a domluvené servisní okno pro případné krátké ověřovací testy.

**Práce:**

- získat exporty a binární zálohy aktivních MikroTiků bez uložení tajných hodnot do GitHubu;
- zaznamenat modely, identity, IP, RouterOS, role, napájení a fyzické umístění;
- zmapovat porty, kabely, optiku, AP, DHCP, NAT, firewall, port-forwardy a statické klienty;
- ověřit NVR, zařízení „Stavba“ a další klienty citlivé na změnu adresace;
- změřit parametry a reálnou propustnost rádiového přívodu;
- vytvořit aktuální topologii, portový plán a původní schéma zapojení pro návrat.

**Test úspěchu:** každý aktivní prvek a kritická služba mají známou roli, záloha je čitelná, kabeláž je dohledatelná a existuje jednoznačný výchozí stav pro porovnání po změně.

**Rollback:** etapa je primárně čtecí. Pokud inventura není úplná nebo záloha není použitelná, produkční zapojení se nemění.

### 1. Příprava hEX S (2025)

**Vstupní podmínka:** dokončená inventura, přidělený cílový LAN prefix, v Airtable rezervovaný konkrétní hEX S a známé nutné výjimky pro provoz.

**Práce:**

- připravit konfiguraci mimo produkci;
- nastavit lokální DHCP, DNS forwarding, směrování, firewall a bezpečný management;
- připravit směrování mezi HOME a Rybníky bez WireGuardu a lokálního NATu;
- povolit správu z HOME;
- zablokovat privátní síti Rybníků přístup do HOME kromě jednotlivých schválených výjimek;
- hostům povolit pouze internet, zakázat HOME, privátní síť i management a zapnout izolaci klientů;
- nastavit hostům počátečně 15 Mb/s na klienta a 70–80 Mb/s celkem.

**Test úspěchu:** konfigurace se bez chyby načte do cílového kusu, hEX S je spravovatelný pouze zamýšlenou cestou, DHCP používá správný rozsah a pro každý bezpečnostní směr existuje konkrétní test.

**Rollback:** v produkci se ještě nic nemění. Předchozí konfigurace cílového kusu zůstane zálohovaná a kus lze vrátit do původního stavu.

### 2. Přechod rádiového přívodu a core

**Vstupní podmínka:** potvrzený model a režim přijímací jednotky, zálohy současného rádia i core, popsané původní zapojení, připravený hEX S a fyzická přítomnost u zásahu.

**Práce:**

- převést přijímací rádio do režimu bridge/CPE;
- zapojit připravený hEX S jako jediný místní L3 core;
- aktivovat přímé směrování na HOME;
- ponechat sektor `AP HOME` v jeho ověřené provozní konfiguraci.

**Test úspěchu:**

- fungují internet, DNS a očekávané služby;
- správa z HOME do Rybníků je dostupná;
- privátní síť Rybníků se do HOME nedostane bez položky v allowlistu;
- hosté se nedostanou do privátní sítě, HOME ani managementu a nevidí se navzájem;
- na přijímacím rádiu ani jinde nezůstal skrytý DHCP, NAT nebo další firewall;
- NVR a zařízení „Stavba“ fungují stejně jako před změnou.

**Rollback:** odpojit nový hEX S, obnovit původní zapojení a konfiguraci přijímací jednotky i původního core podle fotografií a záloh z etapy 0. Před zásahem určit časový limit, po kterém se bez dalšího ladění vrací původní stav.

### 3. Odstranění NAT ostrovů

**Vstupní podmínka:** core je stabilní, každá větev má portovou mapu a seznam očekávaných klientů. Začít jedinou pilotní větví.

**Práce:** postupovat samostatně po větvích Obývák, Včelín, Hospoda a Dílna. SOHO routery převést do AP/bridge režimu, nahradit nebo odstranit. V jednom servisním kroku měnit pouze jednu větev.

**Test úspěchu:** všichni známí klienti pilotní větve dostanou adresu z centrálního DHCP, fungují očekávané služby a Wi-Fi a v dané větvi není další DHCP ani NAT.

**Rollback:** vrátit původní zařízení, konfiguraci a kabeláž pouze měněné větve. Dokud pilotní větev neprojde testy a není stabilní, nepokračovat na další.

### 4. L2 distribuce a Wi-Fi

**Vstupní podmínka:** známý počet portů, PoE rozpočet, stav optiky, změřené pokrytí a vybrané konkrétní skladové kusy.

**Práce:**

- Včelín provozovat pouze jako L2 distribuční bod;
- doplnit spravované switche podle skutečného počtu portů, optiky a PoE;
- nastavit identity, management IP, popisy portů, RSTP a zálohy konfigurací;
- nasadit soukromé a hostovské SSID;
- VLAN a CAPsMAN použít jen tehdy, pokud jsou potřebné pro bezpečné oddělení nebo prokazatelně zjednoduší správu.

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

- přidat do Mikr hEX S, rádiový přívod a klíčovou distribuci;
- nastavit souhrnný alarm lokality tak, aby výpadek upstreamu nevyvolal lavinu alarmů všech AP;
- nastavit exporty a pravidelné zálohy konfigurací;
- zapsat finální topologii, adresaci, portovou mapu a výsledky provozních testů do GitHubu.

**Test úspěchu:** kontrolovaný výpadek vhodného prvku vyvolá očekávaný alarm, záloha je dostupná a obnova je prakticky ověřená na náhradním nebo testovacím zařízení.

**Rollback:** chybné monitorovací pravidlo nebo zálohovací úlohu odstranit a obnovit předchozí konfiguraci; tato etapa nesmí měnit datovou cestu lokality.

## Otevřené přípravné úkoly

- [ ] Přidělit cílový LAN prefix Rybníků v rámci společného adresního plánu.
- [ ] Po inventuře sepsat jednotlivé nutné výjimky z privátní sítě Rybníků do HOME; bez doložené potřeby zůstane výchozí `deny`.
- [ ] Podle inventury doplnit konkrétní testovací checklist, časový limit a kabelový postup rollbacku pro etapu 2.
- [ ] Vybrat pilotní větev pro odstranění prvního NAT ostrova.
- [ ] V dokumentu Mikr navrhnout závislosti a souhrnný alarm lokality.
- [ ] V dokumentaci záloh MikroTiků doplnit a prakticky ověřit obnovu konfigurace Rybníků.

## Hlavní rizika

- neznámé statické IP a port-forwardy;
- výpadek NVR nebo zařízení „Stavba“;
- změna více částí v jednom zásahu;
- smíšené RouterOS a Wi-Fi generace;
- přepětí na venkovních metalických trasách;
- zbytečné VLAN, CAPsMAN nebo nový monitoring bez konkrétního přínosu.

Každá etapa musí mít zálohu konfigurace, testovací checklist a jasný rollback.
