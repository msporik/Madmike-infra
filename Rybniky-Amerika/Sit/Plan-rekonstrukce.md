# Plán rekonstrukce

## Cíl

Přestavět existující funkční, ale nesourodou síť po etapách tak, aby měla jasný core, lokální DHCP, jeden NAT, spravované L2 body a samostatná AP. Rekonstrukce nesmí sama o sobě ohrozit nezdokumentované služby.

## Rozhodovací pravidlo pro core

```text
rychlá konsolidace současného stavu = hEX S
cílová rekonstrukce celé lokality = RB5009
```

CRS326 má smysl jen při skutečném využití většího počtu portů, centrálního rozvodu nebo optiky.

## Etapy

### 0. Inventura a zálohy

- získat exporty aktivních MikroTiků;
- zaznamenat modely, identity, IP, MAC, RouterOS a napájení;
- zmapovat porty, kabely, optiku, AP, DHCP, NAT a statické klienty;
- vytvořit aktuální topologii a portový plán;
- ověřit NVR a zařízení „Stavba“.

### 1. Oddělení PtP rádia od routingu

- připravit nový core mimo produkci;
- převést DHCP, NAT a firewall na core;
- ověřit WAN parametry, internet, DNS a přístup z HOME;
- přijímací rádio ponechat pouze jako bridge/CPE.

### 2. Odstranění NAT ostrovů

Postupovat samostatně po větvích: Obývák, Včelín, Hospoda a Dílna. SOHO routery převést do AP/bridge režimu, nahradit nebo odstranit. U každé větve zachovat možnost rychlého návratu.

### 3. Spravovaná L2 distribuce

- Včelín provozovat pouze jako L2 bod;
- doplnit spravované switche podle skutečného počtu portů a PoE;
- nastavit identity, management IP, popisy portů, RSTP a zálohy konfigurací.

### 4. Wi-Fi

- zaměřit reálné pokrytí;
- určit počet AP;
- nasadit cAP ax/ax XL tam, kde dávají dlouhodobý smysl;
- sjednotit SSID;
- CAPsMAN zvolit až po ověření kompatibility RouterOS 6/7 a starého/nového Wi-Fi balíku.

### 5. Sloup

Až po stabilizaci základní sítě ověřit optiku, napájení, uzemnění, přepěťovou ochranu a PoE rozpočet. Potom rozhodnout mezi PowerBox Pro se samostatnými rádii a jiným venkovním řešením.

### 6. Mobilhome

Zaměřit trasu, přímou viditelnost, Fresnelovu zónu, vegetaci a požadovanou kapacitu. Teprve potom rozhodnout mezi 5 a 60 GHz.

### 7. Správa a monitoring

- přidat potvrzená zařízení do Mikr;
- nastavit exporty a pravidelné zálohy konfigurací;
- ověřit obnovitelnost záloh;
- další topologický monitoring řešit jen tehdy, pokud Mikr nepokryje skutečnou potřebu.

## Otevřená rozhodnutí

- [ ] hEX S, nebo RB5009 jako core.
- [ ] Zda je CRS326 přiměřený skutečné topologii.
- [ ] Který CRS112 a kde má zajišťovat PoE.
- [ ] Kolik AP je reálně potřeba.
- [ ] Zda zavést CAPsMAN.
- [ ] Zda existuje konkrétní důvod pro VLAN.
- [ ] Stav optiky a řešení sloupu.
- [ ] 5GHz, nebo 60GHz uplink k mobilhome.
- [ ] Zda HOME potřebuje přímý přístup do celé LAN Rybníků bez dalšího NAT.

## Hlavní rizika

- neznámé statické IP a port-forwardy;
- výpadek NVR nebo zařízení „Stavba“;
- změna více částí v jednom zásahu;
- smíšené RouterOS a Wi-Fi generace;
- přepětí na venkovních metalických trasách;
- zbytečné VLAN, CAPsMAN nebo nový monitoring bez konkrétního přínosu.

Každá etapa musí mít zálohu konfigurace, testovací checklist a jasný rollback.
