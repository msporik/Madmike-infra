# Hardware

## Doložené zařízení

| Role | Zařízení | Stav / poznámka |
|---|---|---|
| hlavní PtP spoj | MikroTik Sextant / LHG | přesné přiřazení obou konců ověřit |
| starší Sextant | RB711G-5HnD / Sextant G | RouterOS `6.49.19`, 32 MB RAM; stabilní, nepřevádět bez důvodu na ROS 7 |
| místní core | historicky RB450G nebo hEX S | současné aktivní zařízení a konfiguraci ověřit |
| lokální distribuce | různé switche a SOHO routery | úplná inventura chybí; více NATů je pravděpodobně stále možné |

## Kandidáti pro rekonstrukci

Následující zařízení byla v červencových podkladech vyhodnocena jako vhodná ze skladových zásob. Před alokací je nutné znovu ověřit jejich dostupnost.

| Role | Preferovaný kandidát | Podmínka nasazení |
|---|---|---|
| pragmatický core | hEX S | rychlá konsolidace současné menší sítě |
| cílový core | RB5009UG+S+IN | systematická rekonstrukce celé lokality |
| centrální switch | CRS326-24G-2S+RM | jen pokud se využije počet portů, centrální rozvod nebo optika |
| Včelín / optická distribuce | CRS112-8G-4S-IN nebo CRS112-8P-4S-IN | podle PoE a optických potřeb |
| vnitřní Wi-Fi | cAP ax / cAP ax XL | počet určit podle reálného pokrytí |
| méně důležitá Wi-Fi | cAP ac | starší nebo dočasná varianta |
| venkovní Wi-Fi | wAP | přesný model a pásmo ověřit |
| sloupový PoE bod | PowerBox Pro | ověřit PoE rozpočet, zdroj, ochranu a krabici |
| nový bezdrátový spoj | Wireless Wire nebo samostatné CPE | až po zaměření trasy a potvrzení přímé viditelnosti |

## Překonané nebo nevhodné cílové varianty

RB2011, RB3011, RB951/RB951Ui, RB751, RouterBOARD 750UP, hAP ac lite a RB450G nemají být základem nové cílové sítě. Mohou zůstat jako dočasný mezikrok, servisní kus nebo nouzová náhrada.

SXT Lite5 nebyl vyhodnocen jako smysluplný upgrade stávajícího Sextantu.

## Otevřené kontroly

1. Udělat úplný seznam aktivních routerů, switchů, AP a jejich napájení.
2. Porovnat zařízení s živou evidencí v Mikr Manageru a skladovou evidencí.
3. Ověřit dostupné SFP moduly, typ optiky, PoE zdroje a přepěťové ochrany.
4. Nealokovat RB5009, CRS ani AP pouze podle starého seznamu zásob.
5. Před návrhem sloupu ověřit přesné schopnosti konkrétního mANTBoxu nebo jiného rádia.
