# MikroTik a Wi-Fi

> Poslední uživatelem potvrzený stav: **2026-08-02**. Nejde o živý export RouterOS.

## Současná topologie a zařízení

`Internet → RB4011Honza → hAP ac3 → klienti LAN/Wi-Fi`

| Zařízení | Role | Stav / poznámka |
|---|---|---|
| MikroTik RB4011 | hlavní router a výchozí brána `192.168.10.1` | aktivní; označení `RB4011Honza` |
| hAP ac3 | jediné Wi-Fi AP za RB4011 | aktivní; samostatná správa bez CAPsMANu |
| cAP ac | dříve uváděné další AP | není součástí současné topologie |
| L009UiGS-2HaxD-IN | dříve zvažované AP nebo switch | není nasazený; nenahrazuje RB4011 |

LAN je `192.168.10.0/24`. Všechna zařízení jsou v jedné společné síti; nejsou aktivní VLAN, hostovská Wi-Fi ani samostatná IoT síť.

Parametry propojení HOME ↔ Honza jsou vedené v [MadMike / Servery / WireGuard](../../MadMike/Servery/WireGuard.md). Monitoring MikroTiků je popsaný v [MadMike / Monitoring / Mikr Manager](../../MadMike/Monitoring/Mikr.md) a zálohování v [MadMike / Zálohy / MikroTiky](../../MadMike/Zalohy/MikroTik.md).

## Přístup a bezpečnost

- Správa se provádí z důvěryhodné místní LAN, přes existující WireGuard nebo fyzicky na místě.
- Veřejný WinBox, WebFig nebo SSH se nezapíná jako náhradní přístup.
- Před vzdálenou změnou musí existovat místní nebo jiná nezávislá návratová cesta.
- Safe Mode je pomocný nástroj, ne náhrada zálohy a místního přístupu.
- Neupravené exporty, klíče, certifikáty, přístupové údaje a veřejné endpointy se neukládají do GitHubu ani chatu.

## Read-only inventura

Před prvním zásahem na obou zařízeních pouze přečíst stav. Dostupnost jednotlivých menu závisí na modelu, balíčcích a verzi RouterOS.

```routeros
/system identity print
/system resource print
/system package print
/system routerboard print
/interface print detail
/interface bridge print detail
/interface bridge port print detail
/ip address print detail
/ip route print detail
/ip dhcp-server print detail
/ip dhcp-server network print detail
/ip dhcp-server lease print detail
/ip dns print
/ip firewall filter print
/ip firewall nat print
/log print
```

Na hAP ac3 se podle skutečně instalovaného bezdrátového balíčku použije čtecí výpis `/interface wireless ...` nebo `/interface wifi ...`. Neověřenou konfiguraci jednoho stacku nelze přenášet do druhého odhadem.

Na RB4011 se parametry WireGuardu, routy a starý IPsec ověřují podle [WireGuard dokumentu](../../MadMike/Servery/WireGuard.md#bezpečná-inventura-na-rb5009); výstup se před sdílením sanitizuje.

Z inventury se do dokumentace přenese pouze výsledný stav:

- přesná identita, model, RouterOS a firmware;
- fyzické umístění, napájení, WAN, uplink a porty;
- skutečná role DHCP, DNS, NAT a firewallu;
- Wi-Fi pásma, SSID a zabezpečení bez hesel;
- management IP a místní přístupová cesta;
- datum ověření, stav záloh a monitoring.

## Běžná provozní kontrola

1. Ověřit dostupnost `192.168.10.1` z místní LAN.
2. Na RB4011 zkontrolovat uptime, CPU, RAM, storage, teplotu, systémový log a stav WAN/uplinku.
3. Ověřit, že klient získá adresu, bránu a DNS a dostane se na internet přes IP i jméno.
4. Ověřit dostupnost hAP ac3, jeho uplink a očekávané bezdrátové klienty.
5. Prakticky otestovat Wi-Fi v používaných částech domu; samotná registrace klienta neprokazuje použitelnou kvalitu spojení.
6. Ověřit místní Home Assistant na `192.168.10.22`.
7. Z HOME otestovat skutečný klient↔LAN provoz přes WireGuard, ne pouze handshake.
8. Porovnat výsledek s Mikr Managerem a posledním známým stavem před incidentem.

## Aktualizace RouterOS a firmware

Aktualizace není diagnostický pokus. Nejprve se ověří živá verze, balíčky, poznámky k cílové verzi, záloha, fyzický přístup a rollback.

Bezpečné čtecí příkazy:

```routeros
/system package update check-for-updates
/system package print
/system routerboard print
```

RB4011 a hAP ac3 se neaktualizují současně. Po každém zařízení se ověří management, WAN/uplink, DHCP/DNS, Wi-Fi, Home Assistant a WireGuard. Upgrade RouterBOARD firmware se považuje za samostatný krok a provede se jen po ověření kompatibility.

## Diagnostika

| Projev | První rozlišení | Bezpečný další krok |
|---|---|---|
| Nedostupná celá lokalita | napájení, WAN nebo RB4011 | místní kontrola napájení, link a systémového logu |
| Internet nejde, LAN funguje | WAN, default route, DNS nebo NAT | test přes IP a jméno, poté route, DNS a NAT |
| Klient nezíská adresu | uplink/bridge nebo DHCP | ověřit link, bridge port, DHCP server, pool a leases |
| Kabelová LAN funguje, Wi-Fi ne | napájení/uplink hAP ac3 nebo bezdrátová konfigurace | ověřit zařízení, link, příslušný Wi-Fi stack a log |
| Wi-Fi je dostupná, ale nestabilní | kanál, rušení, síla signálu nebo uplink | zaznamenat místo, pásmo a klienta; neměnit výkon a kanály naslepo |
| HA funguje místně, z HOME ne | WireGuard, route nebo firewall | pokračovat v [diagnostice WireGuardu](../../MadMike/Servery/WireGuard.md#diagnostika) |
| Handshake funguje, vzdálená LAN ne | route, `allowed-address`, firewall nebo starý IPsec | ověřit obě strany a sniffer; neregenerovat klíče jako první krok |
| Mikr hlásí výpadek, zařízení funguje | monitoring nebo cesta z VM510 | ověřit zařízení přímo a následně Mikr |
| Problém vznikl po změně | poslední změna | zastavit další změny a použít připravený rollback |

## Záloha, rollback a obnova

Před zásadní změnou vytvořit a bezpečně uložit označený `.backup` i `.rsc` podle [centrálního runbooku](../../MadMike/Zalohy/MikroTik.md#checkpoint-před-změnou). Po změně vznikne nový checkpoint až po úplné přejímce.

Při poruše zařízení:

1. vyloučit napájení, kabel a nadřazenou vrstvu;
2. určit přesnou roli a vybrat kompatibilní náhradní hardware podle aktuální evidence;
3. obnovovat nejprve mimo produkční síť, aby nevznikla duplicitní IP nebo DHCP server;
4. binární backup použít jen na kompatibilním modelu a verzi; `.rsc` před importem ručně zkontrolovat;
5. připojovat WAN, LAN a klientské větve postupně a po každém kroku testovat;
6. po přejímce vytvořit nový checkpoint a aktualizovat dokumentaci.

## Otevřené kontroly

> Následující body **vyžadují ověření v živém systému**.

- [ ] Živými read-only výpisy ověřit přesný model, RouterOS, firmware a provozní konfiguraci RB4011 a hAP ac3.
- [ ] Doplnit WAN, propojovací porty, napájení a fyzické umístění obou aktivních zařízení.
- [ ] Ověřit skutečnou roli RB4011 pro DHCP, DNS, NAT a firewall a skutečný Wi-Fi stack hAP ac3.
- [ ] Porovnat aktivní zařízení s Mikr Managerem a kusovou evidencí v Airtable; skladový stav sám neurčuje nasazení v lokalitě.
- [ ] Ověřit poslední použitelný `.backup` a `.rsc` obou zařízení a možnost místního zásahu.

