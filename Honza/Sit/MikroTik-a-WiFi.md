# MikroTik a Wi-Fi

## Současná topologie

`Internet → RB4011Honza → hAP ac3`

Stav zařízení potvrzený uživatelem k 2026-08-02:

| Zařízení | Role | Stav / poznámka |
|---|---|---|
| MikroTik RB4011 | hlavní router a výchozí brána `192.168.10.1` | aktivní; označení `RB4011Honza` |
| hAP ac3 | jediné Wi-Fi AP za RB4011 | aktivní; samostatná správa bez CAPsMANu |
| cAP ac | dříve uváděné další AP | není součástí současné topologie |
| L009UiGS-2HaxD-IN | dříve zvažované AP nebo switch | není nasazený; nenahrazuje RB4011 |

## Síť a správa

- LAN: `192.168.10.0/24`;
- router / výchozí brána: `192.168.10.1`;
- všechna zařízení jsou v jedné společné LAN;
- nejsou aktivní VLAN, hostovská Wi-Fi ani samostatná IoT síť;
- CAPsMAN se nepoužívá;
- přesné fyzické porty, napájení a umístění obou aktivních zařízení zatím nejsou zdokumentované.

Parametry propojení HOME ↔ Honza jsou vedené v [MadMike / Servery / WireGuard](../../MadMike/Servery/WireGuard.md). Monitoring MikroTiků je popsaný v [MadMike / Monitoring / Mikr Manager](../../MadMike/Monitoring/Mikr.md) a zálohování v [MadMike / Zálohy / MikroTiky](../../MadMike/Zalohy/MikroTik.md).

## Otevřené kontroly

- [ ] Živými read-only výpisy ověřit verzi RouterOS a provozní konfiguraci RB4011 a hAP ac3.
- [ ] Doplnit přesné porty, napájení a fyzické umístění obou aktivních zařízení.
- [ ] Porovnat RB4011 a hAP ac3 s Mikr Managerem a hardwarovou evidencí.
