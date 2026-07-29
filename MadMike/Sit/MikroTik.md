# MikroTik

## Účel

Dokument popisuje:

- domácí síťovou infrastrukturu HOME postavenou na MikroTiku;
- obecnější zásady a rozhodnutí použitelné napříč spravovanými MikroTiky.

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

## Obecné zásady

- MikroTik zůstává preferovanou platformou pro routery, switche a spravovanou Wi-Fi tam, kde řeší konkrétní provozní potřebu.
- Kritická změna se připraví se zálohou konfigurace, testem a možností návratu.
- Stabilní zařízení se neupgraduje nebo nemění jen kvůli sjednocení verze či modelu.
- CAPsMAN se používá tam, kde zjednodušuje správu více AP; není povinným cílem každé malé lokality.
- VLAN, další router, nový tunel ani další monitorovací vrstva se nepřidávají bez konkrétního přínosu.
- Mikr Manager sleduje dostupnost a stav zařízení, ale neurčuje topologii ani sklad.
- IP adresace se vede v [adresním plánu](Adresni-plan.md), provozní WireGuard v [Servery / WireGuard](../Servery/WireGuard.md) a zálohy RouterOS v [Zálohy / MikroTik](../Zalohy/MikroTik.md).

## Související dokumentace

- [Adresní plán](Adresni-plan.md)
- [Serverový WireGuard](../Servery/WireGuard.md)
- [Interní DNS, NPM a HTTPS](../Servery/DNS-NPM-HTTPS.md)
- [Mikr Manager](../Monitoring/Mikr.md)
- [Zálohy MikroTiků](../Zalohy/MikroTik.md)

## Otevřené kontroly HOME

- [ ] Ověřit aktivní uplinky a portovou mapu RB5009, CRS326 a CRS112 proti živé konfiguraci.
- [ ] Ověřit aktuální seznam domácích AP a jejich role přímo v CAPsMAN.
- [ ] Doplnit VLAN a další domácí síťové role pouze tehdy, pokud jsou skutečně nasazené.
