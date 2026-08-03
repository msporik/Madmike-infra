# Síť – Honza

> Poslední uživatelem potvrzený stav: **2026-08-02**. Verze RouterOS, portová mapa a další údaje označené k ověření vyžadují kontrolu v živém systému.

## Účel a hranice

Tento projekt je provozní přehled Honzovy místní sítě. Podrobný stav routeru, Wi-Fi, provozní kontrola a diagnostika jsou v dokumentu [MikroTik a Wi-Fi](MikroTik-a-WiFi.md).

Parametry site-to-site tunelu, společný adresní plán, monitoring a zálohování mají vlastní autoritativní dokumenty a zde se neduplikují.

## Potvrzená topologie

```text
Internet
  │
RB4011Honza (192.168.10.1)
  │
hAP ac3 (jediné Wi-Fi AP)
  │
LAN 192.168.10.0/24
```

- RB4011 je hlavní router a výchozí brána;
- za RB4011 je jediné Wi-Fi AP `hAP ac3`;
- hAP ac3 je spravovaný samostatně a CAPsMAN se nepoužívá;
- všechna zařízení jsou v jedné LAN;
- nejsou aktivní VLAN, hostovská Wi-Fi ani samostatná IoT síť;
- `cAP ac` ani L009 nejsou součástí současné topologie.

Přesné porty, způsob napájení, fyzické umístění a živé role DHCP, DNS, NAT a firewallu: **Vyžaduje ověření v živém systému.**

## Závislosti a dopad výpadku

| Výpadek | Očekávaný dopad podle doložené role |
|---|---|
| Internet / WAN | místní LAN může fungovat, ale nejsou dostupné internetové služby a vzdálený WireGuard |
| RB4011 | výpadek routingu, internetu a pravděpodobně i DHCP; přesný rozsah služeb vyžaduje živé ověření |
| hAP ac3 | výpadek místní Wi-Fi; funkce kabelové LAN závisí na skutečné fyzické topologii |
| WireGuard HOME ↔ Honza | místní síť a HA mohou dál fungovat, ale vzdálená správa z HOME není dostupná |
| Mikr Manager | ztratí se dohled; síť samotná má fungovat dál |

## První provozní kontrola

1. Ověřit napájení a fyzický link RB4011 a hAP ac3.
2. Z místní LAN ověřit přidělení adresy v `192.168.10.0/24`, bránu `192.168.10.1` a internet přes IP i DNS jméno.
3. Ověřit správu RB4011 a hAP ac3 z důvěryhodné místní sítě.
4. Ověřit Home Assistant na poslední potvrzené adrese `192.168.10.22`.
5. Z HOME odděleně otestovat WireGuard handshake, router↔router a skutečný přístup do vzdálené LAN podle [WireGuard runbooku](../../MadMike/Servery/WireGuard.md#běžná-provozní-kontrola).
6. Porovnat stav s Mikr Managerem; živá konfigurace je rozhodující.

## Bezpečná změna

- U vzdálené změny zachovat místní nebo jinou nezávislou návratovou cestu.
- Před změnou ověřit použitelný `.backup` i `.rsc` podle [Záloh MikroTiků](../../MadMike/Zalohy/MikroTik.md).
- Neměnit současně WAN, bridge, adresaci, DHCP, firewall a WireGuard.
- Aktivní síť se nesegmentuje ani nepřečíslovává pouze kvůli sjednocení s budoucím adresním plánem.
- Po změně se testuje místní klient, internet, Home Assistant, Wi-Fi i vzdálený přístup; samotné otevření WinBoxu není úplná přejímka.

## Handover minimum

Před samostatnou správou musí být živě ověřené:

- fyzické umístění, napájení, WAN a propojovací porty obou zařízení;
- identita, model a verze RouterOS a RouterBOARD firmware;
- aktivní bridge, adresace, DHCP, DNS, NAT a firewall;
- Wi-Fi názvy, pásma, zabezpečení a správcovská cesta bez zapisování hesel;
- místní přístup při výpadku WireGuardu;
- poslední použitelný backup a export obou zařízení;
- vazba na Mikr Manager a osoba schopná místního zásahu.

## Související dokumentace

- [MikroTik a Wi-Fi](MikroTik-a-WiFi.md)
- [MadMike / Síť / Adresní plán](../../MadMike/Sit/Adresni-plan.md)
- [MadMike / Servery / WireGuard](../../MadMike/Servery/WireGuard.md)
- [MadMike / Monitoring / Mikr Manager](../../MadMike/Monitoring/Mikr.md)
- [MadMike / Zálohy / MikroTiky](../../MadMike/Zalohy/MikroTik.md)
- [Honza / Home Assistant](../Home-Assistant/README.md)

