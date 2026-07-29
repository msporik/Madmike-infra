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

### Honza

Potvrzená zařízení:

- RB4011 jako hlavní router a CAPsMAN;
- cAP ac jako AP v patře;
- hAP ac3 jako AP v přízemí.

Místní LAN je `192.168.10.0/24` a brána `192.168.10.1`. Podrobná evidence je v [Honza / Síť / MikroTik a Wi-Fi](../../Honza/Sit/MikroTik-a-WiFi.md).

### Rybníky – Amerika

Doložené podklady potvrzují 5GHz PtP spoj z HOME dlouhý přibližně 500–600 m. Na jednom z konců pracuje starší Sextant G / RB711G-5HnD s RouterOS `6.49.19` a 32 MB RAM; přesné modely obou konců i současný core je nutné ověřit.

Místní síť obsahuje větve Obývák, Včelín, Hospoda a Dílna. Úplná aktivní inventura zatím chybí. Podrobná evidence a plán rekonstrukce jsou v [Rybníky – Amerika / Síť](../../Rybniky-Amerika/Sit/README.md).

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
- [Síť lokality Honza](../../Honza/Sit/README.md)
- [Síť lokality Rybníky – Amerika](../../Rybniky-Amerika/Sit/README.md)

## Otevřené kontroly

- [ ] Porovnat inventuru se všemi 22 zařízeními vedenými v Mikr Manageru.
- [ ] Doplnit přesné role a lokality zařízení, která nejsou v tomto dokumentu uvedena.
- [ ] Ověřit aktivní uplinky, CAPsMAN role a rezervní kusy proti živému stavu.
- [ ] Zapsat další síťové IP adresy až po ověření přímo v konfiguraci.
- [ ] Provést fyzickou a konfigurační inventuru Rybníků „Amerika“.
