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

1. Ověřit aktuální RouterOS, konfiguraci bridge a CAPsMAN.
2. Porovnat evidenci zařízení s živým Mikr Managerem.
3. Ověřit, zda byly z routeru úplně odstraněné zbytky starého IPsec.
4. Doplnit případné další subnety nebo VLAN až podle živé konfigurace.
