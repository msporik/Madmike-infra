# Plán rekonstrukce

## Cíl

Přestavět existující funkční, ale nesourodou síť po etapách na schválenou jednoduchou architekturu:

- přijímací rádio jako bridge/CPE;
- hEX S (2025) jako jediný router, DHCP server a firewall;
- přímé směrování k HOME přes stávající PtP bez WireGuardu;
- soukromá a oddělená hostovská Wi-Fi;
- spravovaná L2 distribuce bez dalších DHCP a NAT ostrovů.

Rekonstrukce nesmí sama o sobě ohrozit nezdokumentované služby. Starší varianty hEX S versus RB5009 a úvahy o povinném CRS326 jsou uzavřené; nejsou nadále rozhodovacími body.

## Etapy

### 0. Inventura a návratový plán

- získat exporty aktivních MikroTiků;
- zaznamenat modely, identity, IP, RouterOS, role a napájení;
- zmapovat porty, kabely, optiku, AP, DHCP, NAT, firewall a statické klienty;
- ověřit NVR, zařízení „Stavba“ a další klienty citlivé na změnu adresace;
- vytvořit aktuální topologii a portový plán;
- připravit zálohy, testovací checklist a konkrétní rollback.

### 1. Příprava hEX S (2025)

- ověřit dostupnost konkrétního kusu v HW evidenci;
- připravit konfiguraci mimo produkci;
- navrhnout místní LAN prefix podle společného adresního plánu;
- připravit lokální DHCP, DNS forwarding, firewall a management;
- připravit směrování mezi HOME a Rybníky bez WireGuardu;
- oddělit soukromou a hostovskou síť a zablokovat hostům přístup do privátní sítě, HOME a managementu.

### 2. Oddělení PtP rádia od routingu

- převést přijímací rádio do režimu bridge/CPE;
- zapojit připravený hEX S jako jediný core;
- ověřit WAN/upstream, internet, DNS a směrování mezi povolenými sítěmi HOME a Rybníků;
- ověřit, že nezůstal skrytý DHCP, NAT nebo firewall na rádiu;
- při problému použít připravený návratový postup.

### 3. Odstranění NAT ostrovů

Postupovat samostatně po větvích Obývák, Včelín, Hospoda a Dílna. SOHO routery převést do AP/bridge režimu, nahradit nebo odstranit. Každou větev měnit a otestovat zvlášť.

### 4. L2 distribuce a Wi-Fi

- Včelín provozovat pouze jako L2 distribuční bod;
- doplnit spravované switche podle skutečného počtu portů, optiky a PoE;
- nastavit identity, management IP, popisy portů, RSTP a zálohy konfigurací;
- zaměřit pokrytí a určit skutečný počet AP;
- nasadit soukromé a hostovské SSID;
- CAPsMAN nebo VLAN použít jen tehdy, pokud prokazatelně zjednoduší správu nebo bezpečné oddělení.

### 5. Sloup a mobilhome

Až po stabilizaci základní sítě ověřit:

- stav a zakončení optiky;
- napájení, uzemnění, přepěťovou ochranu a PoE rozpočet;
- trasu, přímou viditelnost, Fresnelovu zónu a vegetaci;
- požadovanou kapacitu.

Teprve potom vybrat venkovní distribuční prvek a 5GHz nebo 60GHz uplink k mobilhome.

### 6. Správa, monitoring a zálohy

- přidat potvrzená zařízení do Mikr;
- nastavit exporty a pravidelné zálohy konfigurací;
- ověřit obnovitelnost záloh;
- zapsat finální topologii, adresaci, portovou mapu a provozní testy do GitHubu.

## Otevřené kontroly

- [ ] Skutečná výchozí topologie, DHCP, NAT, firewall a port-forwardy.
- [ ] Přesný model a režim obou PtP rádií.
- [ ] Cílový LAN prefix Rybníků v rámci společného adresního plánu.
- [ ] Počet a umístění AP potřebných pro soukromou a hostovskou Wi-Fi.
- [ ] Stav optiky a technické řešení sloupu.
- [ ] 5GHz, nebo 60GHz uplink k mobilhome podle zaměření.
- [ ] Přesná směrovací a firewallová pravidla mezi HOME, privátní sítí Rybníků a hosty.

## Hlavní rizika

- neznámé statické IP a port-forwardy;
- výpadek NVR nebo zařízení „Stavba“;
- změna více částí v jednom zásahu;
- smíšené RouterOS a Wi-Fi generace;
- přepětí na venkovních metalických trasách;
- zbytečné VLAN, CAPsMAN nebo nový monitoring bez konkrétního přínosu.

Každá etapa musí mít zálohu konfigurace, testovací checklist a jasný rollback.
