# Síť – Honza

## Účel a hranice

Tento projekt je provozní přehled Honzovy místní sítě. Podrobný stav routeru, Wi-Fi a otevřené síťové kontroly jsou v dokumentu [MikroTik a Wi-Fi](MikroTik-a-WiFi.md).

Parametry site-to-site tunelu, společný adresní plán, monitoring a zálohování mají vlastní autoritativní dokumenty a zde se neduplikují.

## Stav potvrzený k 2026-08-02

- internet je přivedený do MikroTiku RB4011 označovaného jako `RB4011Honza`;
- RB4011 je hlavní router a výchozí brána `192.168.10.1`;
- za RB4011 je jediné Wi-Fi AP `hAP ac3`;
- hAP ac3 je spravovaný samostatně a CAPsMAN se nepoužívá;
- místní síť je `192.168.10.0/24`;
- všechna zařízení jsou v jedné LAN; nejsou aktivní VLAN, hostovská Wi-Fi ani samostatná IoT síť;
- cAP ac ani L009 nejsou součástí současné topologie.

## Poslední doložená vzdálená vazba

Propojení HOME ↔ Honza přes WireGuard a vzdálený WinBox byly prakticky ověřené v květnu 2026. Přesné parametry tunelu a související úkoly jsou vedené v autoritativním dokumentu [MadMike / Servery / WireGuard](../../MadMike/Servery/WireGuard.md).

## Související dokumentace

- [MikroTik a Wi-Fi](MikroTik-a-WiFi.md)
- [MadMike / Síť / Adresní plán](../../MadMike/Sit/Adresni-plan.md)
- [MadMike / Monitoring / Mikr Manager](../../MadMike/Monitoring/Mikr.md)
- [MadMike / Zálohy / MikroTiky](../../MadMike/Zalohy/MikroTik.md)
- [Honza / Home Assistant](../Home-Assistant/README.md)
