# MikroTik

## Účel

Obecná evidence MikroTik infrastruktury, fyzických rolí zařízení a rezerv. Monitoring, grafy a alerty Mikr Manageru jsou popsány samostatně v [Monitoring / Mikr](../Monitoring/Mikr.md).

## HOME – aktivní infrastruktura

| Role | Zařízení | Poznámka |
|---|---|---|
| hlavní router | RB5009UPr | Nahradil RB4011 |
| hlavní switch | CRS326-24G-2S+RM | Propojení s RB5009 přes 10G DAC |
| PoE switch | CRS112-8P-4S | Propojení s CRS326 přes 1G DAC; napájí mimo jiné kamery |
| AP patro | cAP XL | Správa přes CAPsMAN |
| AP obývák | hAP ac3 | Správa přes CAPsMAN |
| AP domek | hAP ac | Správa přes CAPsMAN |

## Známé další lokality

### Vernířovice

Známá zařízení:

- CRS224;
- RB2011;
- wAP;
- mANTBOX;
- cAP ac;
- 3× cAP mini.

### Panelák

- RB1100AHx4; dlouhodobě stabilní provoz.

Podrobný a aktuální seznam zařízení v ostatních lokalitách je potřeba ověřit proti živému Mikr Manageru a konfiguracím routerů.

## Rezervní zařízení

- RB4011 po výměně hlavního domácího routeru;
- 2× RB5009UG+S+IN;
- 2× CRS326-24G-2S+RM.

Rezervní zařízení nejsou součástí aktivní topologie, dokud nejsou skutečně nasazená.

## Související dokumentace

- [Adresní plán](Adresni-plan.md)
- [Serverový WireGuard](../Servery/WireGuard.md)
- [Interní DNS, NPM a HTTPS](../Servery/DNS-NPM-HTTPS.md)
- [Mikr Manager](../Monitoring/Mikr.md)

## Otevřené kontroly

1. Porovnat inventuru se všemi 22 zařízeními vedenými v Mikr Manageru.
2. Doplnit přesné role a lokality zařízení, která nejsou v tomto dokumentu uvedena.
3. Ověřit aktivní uplinky, CAPsMAN role a rezervní kusy proti živému stavu.
4. Zapsat síťové IP adresy až po ověření přímo v konfiguraci.
