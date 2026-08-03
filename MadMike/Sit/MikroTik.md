# MikroTik

## Účel

Dokument popisuje:

- domácí síťovou infrastrukturu HOME postavenou na MikroTiku;
- obecnější zásady a provozní postupy použitelné napříč spravovanými MikroTiky.

Není centrální evidencí všech zařízení ani skladovou kartou. Aktivní infrastruktura ostatních lokalit patří do jejich vlastních kapitol a detailní kusová HW evidence zůstává v Airtable.

## HOME – naposledy evidovaná aktivní infrastruktura

| Role | Zařízení | Vazba |
|---|---|---|
| hlavní router | RB5009UPr | Nahradil RB4011; centrální směrování a správa domácí sítě |
| hlavní switch | CRS326-24G-2S+RM | Propojení s RB5009 přes 10G DAC |
| PoE switch | CRS112-8P-4S | Propojení s CRS326 přes 1G DAC; napájí mimo jiné kamerovou větev |
| AP patro | cAP XL | Správa přes CAPsMAN |
| AP obývák | hAP ac3 | Správa přes CAPsMAN |
| AP domek | hAP ac | Správa přes CAPsMAN |

Tabulka zachycuje poslední konsolidovaný stav. Přesná portová mapa, aktivní VLAN a napájení jednotlivých klientů se doplní pouze podle živé konfigurace a fyzického ověření.

## Provozní role a dopady výpadku

| Prvek | Typický dopad poruchy podle evidované role |
|---|---|
| RB5009 | domácí routing, internet, interní DNS, centrální WireGuard a správa CAPsMAN |
| CRS326 | výpadek hlavní drátové distribuční vrstvy a navazujících větví |
| CRS112 | výpadek připojených PoE zařízení a kamerové větve |
| jedno AP | místní zhoršení nebo ztráta Wi-Fi; drátová síť a ostatní AP mohou dál fungovat |
| CAPsMAN na RB5009 | dopad na centrální správu AP; skutečné chování již připojených AP je nutné posoudit podle živé konfigurace |

Při souběžném výpadku více zařízení se nejprve ověřuje napájení a nejbližší společný uplink. Výpadek Mikr Manageru sám o sobě síť nevyřadí; Mikr je dohled, nikoli řídicí prvek.

## Přístup a bezpečnost

- Správa se provádí pouze z důvěryhodné LAN, přes existující WireGuard nebo místně.
- Veřejný WinBox, WebFig nebo SSH se nezapíná jako nouzový workaround.
- Přihlašovací údaje, klíče, certifikáty a neupravené exporty nepatří do GitHubu ani do chatu.
- Před sdílením výstupu se odstraní veřejné adresy, klíče, sériová čísla a další zbytečně citlivé hodnoty.
- Safe Mode chrání pouze před částí chyb v aktuální konfigurační relaci; nenahrazuje zálohu, místní přístup ani plán návratu.

Autoritativní model přístupů je v projektu [Přístupy](../Pristupy/README.md). Konkrétní WireGuard peery a routy patří do [Servery / WireGuard](../Servery/WireGuard.md).

## Read-only inventura

Před prvním zásahem se stav pouze přečte. Rozsah se přizpůsobí zařízení; ne každý switch nebo AP má všechny uvedené vrstvy.

```routeros
/system identity print
/system resource print
/system package print
/system routerboard print
/interface print detail
/interface bridge print detail
/interface bridge port print detail
/interface vlan print detail
/ip address print detail
/ip route print detail
/ip dhcp-server print detail
/ip dhcp-server network print detail
/ip dhcp-server lease print detail
/ip dns print
/ip firewall filter print
/ip firewall nat print
/caps-man manager print
/caps-man remote-cap print
/caps-man registration-table print
/log print
```

Na RB5009 se navíc podle autoritativního dokumentu [WireGuard](../Servery/WireGuard.md) ověří rozhraní, peery, routy a firewallová vazba. Výpisy mohou obsahovat citlivé údaje; do dokumentace se z nich přenáší pouze ověřený výsledný stav.

Při inventuře se zaznamená:

- identita, model, RouterOS a firmware;
- role zařízení a fyzické umístění;
- management IP a důvěryhodná přístupová cesta;
- bridge, VLAN, porty, uplinky a PoE vazby;
- DHCP, DNS, routy, NAT a firewall pouze tam, kde je zařízení skutečně provozuje;
- CAPsMAN role a registrace AP;
- návaznost na WireGuard, monitoring a zálohy;
- datum a způsob ověření.

## Běžná provozní kontrola HOME

1. Ověřit dostupnost RB5009 z důvěryhodné správcovské sítě.
2. Zkontrolovat uptime, CPU, RAM, storage, teplotu a systémový log.
3. Ověřit stav uplinku RB5009 ↔ CRS326 a CRS326 ↔ CRS112, včetně rychlosti a chyb rozhraní.
4. Ověřit dostupnost switchů a stav očekávaných PoE větví.
5. V CAPsMAN ověřit očekávaná AP a registrované klienty; chybějící AP řešit od napájení a uplinku.
6. Ověřit přidělování DHCP, interní DNS a přístup k několika skutečným službám.
7. Pokud incident zasahuje vzdálené lokality nebo offsite servery, pokračovat v [kontrole WireGuardu](../Servery/WireGuard.md#běžná-provozní-kontrola).
8. Porovnat výsledek s Mikr Managerem, ale živou konfiguraci považovat za rozhodující.

## Bezpečný postup změny

1. Vymezit jediný cíl změny, dotčená zařízení, služby a lokality.
2. Ověřit živý výchozí stav a dostupnost místního nebo nezávislého návratového přístupu.
3. Podle [Záloh MikroTiků](../Zalohy/MikroTik.md) ověřit použitelný export nebo backup a vytvořit označený checkpoint před zásadní změnou.
4. Zaznamenat přesný rollback; u vzdáleného routeru se nespoléhat na stejnou cestu, kterou změna může přerušit.
5. Kde je to vhodné, použít Safe Mode a měnit jednu logickou vrstvu po jednotlivých ověřitelných krocích.
6. Po každém kroku ověřit management přístup a příslušnou datovou cestu.
7. Po dokončení provést přejímací kontrolu včetně skutečných klientů a závislých služeb.
8. Aktualizovat autoritativní dokumentaci; tajné hodnoty ani neupravený export nezapisovat.

Změny firewallu se dělají s ohledem na pořadí pravidel. Změny bridge, VLAN, management IP, routingu a WireGuardu mohou okamžitě odříznout vzdálenou správu a vyžadují zvlášť jasný návratový postup.

## Aktualizace RouterOS a firmware

Aktualizace není běžný diagnostický pokus. Provádí se plánovaně a po jednom provozním celku.

Před aktualizací:

- ověřit model, architekturu, současnou verzi RouterOS, balíčky a firmware RouterBOARD;
- prostudovat změny cílové verze a kompatibilitu používaných funkcí;
- ověřit zálohu, export, místní přístup, napájení a návratovou variantu;
- zaznamenat výchozí stav uplinků, routingu, DHCP, Wi-Fi a WireGuardu;
- neaktualizovat současně hlavní router, navazující switche a všechna AP.

Bezpečné čtecí příkazy:

```routeros
/system package update check-for-updates
/system package print
/system routerboard print
```

Samotné stažení, instalace a případný upgrade RouterBOARD firmware se provedou až po výběru cílové verze. Po každém restartu se ověří:

1. verze a úplné naběhnutí zařízení;
2. management přístup;
3. fyzické linky, bridge a VLAN;
4. DHCP, DNS, routing, NAT a firewall;
5. CAPsMAN a AP, pokud se zařízení této vrstvy účastní;
6. WireGuard a skutečné vzdálené služby;
7. Mikr, logy a další následující provozní cyklus.

Pouhý návrat staršího konfiguračního souboru nemusí vrátit RouterOS nebo firmware. Postup návratu musí odpovídat konkrétnímu typu aktualizace.

## Diagnostika

| Projev | Pravděpodobná oblast | První kontrola |
|---|---|---|
| Nedostupná celá HOME | napájení, WAN, RB5009 nebo hlavní uplink | místní kontrola RB5009, napájení a link stavu |
| Internet nejde, interní síť funguje | WAN, default route, DNS nebo NAT | WAN linka, route, DNS test přes IP i jméno, NAT |
| Interní IP funguje, hostname ne | DNS | pokračovat v [DNS, NPM a HTTPS](../Servery/DNS-NPM-HTTPS.md) |
| Část drátové sítě nefunguje | konkrétní port, uplink, bridge, VLAN nebo PoE | rozhraní a log od klienta směrem ke společnému switchi |
| Jedno AP chybí | PoE, kabel, uplink nebo CAPsMAN spojení | napájení AP, link, remote CAP a log |
| Všechna AP chybí | RB5009/CAPsMAN nebo společná síťová větev | CAPsMAN manager, bridge, adresace a log |
| DHCP klient nezíská adresu | bridge/VLAN, DHCP server, pool nebo fyzická cesta | lease, pool, bridge port a správný segment |
| Vzdálená lokalita nejde, HOME funguje | WireGuard, WAN vzdálené lokality nebo routing | [WireGuard runbook](../Servery/WireGuard.md#diagnostika) |
| Mikr hlásí výpadek, služba funguje | monitoring nebo cesta z VM510 | [Monitoring / Mikr](../Monitoring/Mikr.md#interpretace-nedostupnosti) |
| Problém vznikl po změně | poslední změna a její závislosti | zastavit další zásahy, porovnat výchozí stav a použít připravený rollback |

Při diagnostice se nemění současně DNS, firewall, routing a fyzická topologie. Nejdřív se určí nejnižší nefunkční vrstva a zachová se výchozí stav i logy.

## Rollback a obnova zařízení

Pokud změna nesplní přejímací test nebo hrozí ztráta správy, vrátí se připraveným postupem. Nouzová improvizace nemá přednost před známou funkční konfigurací.

Při poruše nebo výměně:

1. určit roli zařízení a ověřit, zda jeho výpadek nezakrývá poruchu napájení, kabelu nebo nadřazeného prvku;
2. dohledat vhodný `.backup` a `.rsc` podle [Záloh MikroTiků](../Zalohy/MikroTik.md);
3. připravit náhradní zařízení mimo produkční síť a zkontrolovat model, RouterOS, balíčky a názvy rozhraní;
4. binární backup používat jen na kompatibilním hardwaru; textový export před importem zkontrolovat;
5. ručně vyřešit MAC adresy, certifikáty, klíče, názvy rozhraní a jiné nepřenositelné části;
6. před připojením do produkce ověřit management, bridge/VLAN, routing a firewall bez vzniku duplicitní IP nebo DHCP serveru;
7. připojovat navazující větve postupně a po každé provést dílčí test;
8. po obnově provést úplnou provozní kontrolu a aktualizovat dokumentaci.

Obsah backupů a exportů zůstává mimo GitHub. Tento dokument definuje provozní postup; umístění, retenci a test obnovitelnosti vlastní projekt Zálohy.

## Obecné zásady

- MikroTik zůstává preferovanou platformou pro routery, switche a spravovanou Wi-Fi tam, kde řeší konkrétní provozní potřebu.
- Kritická změna se připraví se zálohou konfigurace, testem a možností návratu.
- Stabilní zařízení se neupgraduje nebo nemění jen kvůli sjednocení verze či modelu.
- CAPsMAN se používá tam, kde zjednodušuje správu více AP; není povinným cílem každé malé lokality.
- VLAN, další router, nový tunel ani další monitorovací vrstva se nepřidávají bez konkrétního přínosu.
- Mikr Manager sleduje dostupnost a stav zařízení, ale neurčuje topologii ani sklad.
- IP adresace se vede v [adresním plánu](Adresni-plan.md), provozní WireGuard v [Servery / WireGuard](../Servery/WireGuard.md) a zálohy RouterOS v [Zálohy / MikroTik](../Zalohy/MikroTik.md).

## Handover minimum

Před samostatnou správou HOME musí být známé:

- fyzické umístění RB5009, CRS326, CRS112 a všech AP;
- WAN, uplinky, management porty, napájení a PoE vazby;
- aktivní bridge, VLAN, DHCP, DNS, routy, firewall, NAT a CAPsMAN role;
- dostupná místní správa při výpadku WireGuardu nebo management IP;
- poslední použitelný backup a export kritických zařízení;
- postup ověření HOME, vzdálených lokalit a závislých serverových služeb.

Neověřené body se nepovažují za implicitní standardní konfiguraci.

## Související dokumentace

- [Adresní plán](Adresni-plan.md)
- [Serverový WireGuard](../Servery/WireGuard.md)
- [Interní DNS, NPM a HTTPS](../Servery/DNS-NPM-HTTPS.md)
- [Mikr Manager](../Monitoring/Mikr.md)
- [Zálohy MikroTiků](../Zalohy/MikroTik.md)
- [Přístupy](../Pristupy/README.md)

## Otevřené kontroly HOME

> Následující body **vyžadují ověření v živém systému**.

- [ ] Ověřit aktivní uplinky a portovou mapu RB5009, CRS326 a CRS112 proti živé konfiguraci.
- [ ] Ověřit aktuální seznam domácích AP a jejich role přímo v CAPsMAN.
- [ ] Doplnit VLAN a další domácí síťové role pouze tehdy, pokud jsou skutečně nasazené.
