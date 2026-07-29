# Síť – Honza

## Ověřený stav k 2026-07-28

- místní LAN: `192.168.10.0/24`;
- výchozí brána: `192.168.10.1`;
- hlavní router: MikroTik RB4011, označovaný jako `RB4011Honza`;
- router zajišťuje také CAPsMAN;
- propojení HOME ↔ Honza přes WireGuard funguje;
- vzdálený WinBox přes WireGuard byl prakticky ověřený.

## Témata projektu

- [MikroTik a Wi-Fi](MikroTik-a-WiFi.md)
- Přesné parametry site-to-site tunelu jsou vedené v [MadMike / Servery / WireGuard](../../MadMike/Servery/WireGuard.md).

## Otevřené kontroly

- [ ] Ověřit aktuální RouterOS, konfiguraci bridge a CAPsMAN.
- [ ] Porovnat evidenci zařízení s živým Mikr Managerem.
- [ ] Ověřit, zda byly z routeru úplně odstraněné zbytky starého IPsec.
- [ ] Doplnit případné další subnety nebo VLAN až podle živé konfigurace.
