# MikroTik a Wi-Fi

## Ověřená infrastruktura

| Role | Zařízení | Stav / poznámka |
|---|---|---|
| hlavní router a CAPsMAN | MikroTik RB4011 | aktivní; označení `RB4011Honza` |
| AP patro | cAP ac | potvrzené nasazení |
| AP přízemí | hAP ac3 | potvrzené nasazení |

MikroTik L009UiGS-2HaxD-IN byl dříve pouze zvažovaný jako AP nebo switch. Nemá nahrazovat RB4011 v roli hlavního routeru; jeho skutečné nasazení je potřeba ověřit.

## Síťové vazby

- LAN: `192.168.10.0/24`;
- router / výchozí brána: `192.168.10.1`;
- site-to-site WireGuard zpřístupňuje domácí síť `192.168.89.0/24`;
- centrální parametry tunelu jsou v [MadMike / Servery / WireGuard](../../MadMike/Servery/WireGuard.md);
- monitoring MikroTiků je vedený v [MadMike / Monitoring / Mikr](../../MadMike/Monitoring/Mikr.md).

## Otevřené kontroly

- [ ] Ověřit aktuální seznam AP a jejich role přímo v CAPsMAN.
- [ ] Zjistit, zda je L009 skutečně nasazený.
- [ ] Ověřit uplinky, napájení AP a aktuální Wi-Fi konfiguraci.
- [ ] Ověřit automatické exporty konfigurace a praktickou obnovitelnost.
