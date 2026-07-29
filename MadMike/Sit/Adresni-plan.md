# Adresní plán

## Stav dokumentu

Dokument spojuje dvě vrstvy:

- současné potvrzené nebo historicky doložené rozsahy;
- předběžný cílový plán interních IPv4 adres.

Cílový plán je pracovní architektonický rámec. Není migračním příkazem ani potvrzením, že navržené rozsahy už jsou nasazené.

Rozlišení stavů:

- **aktivní / potvrzené** – doložený současný provoz;
- **pracovní rezervace** – prostor vyhrazený pro budoucí použití, nikoli aktivní síť;
- **otevřené** – detail, který ještě nebyl rozhodnut nebo musí být ověřen.

## Současné potvrzené rozsahy

| Účel / lokalita | Rozsah | Stav |
|---|---|---|
| HOME | `192.168.89.0/24` | aktivní |
| Honza | `192.168.10.0/24` | aktivní; brána `192.168.10.1` |
| PBS / Richard | `192.168.100.0/24` | aktivní |
| notebookový WireGuard | `10.89.1.0/24` | aktivní; RB5009 má `10.89.1.1/24` |
| site-to-site WireGuard HOME ↔ Honza | `10.200.0.0/24` | aktivní; HOME `10.200.0.1`, Honza `10.200.0.3` |

Rozsahy dalších lokalit se doplní až po kontrole živých routerů.

## Známé historické nebo neověřené rozsahy

| Lokalita | Rozsah | Stav |
|---|---|---|
| Rybníky – Amerika | `192.168.22.0/24` | doložený ve starší konfiguraci hEX S; současný živý stav není potvrzený |

Podrobnosti k historické adresaci Rybníků jsou v [Rybníky – Amerika / Síť / Topologie](../../Rybniky-Amerika/Sit/Topologie.md). Tento rozsah se nesmí považovat za současně aktivní ani za schválený cílový rozsah bez kontroly živé konfigurace.

## Cílový princip

Dlouhodobý formát interní adresy:

```text
10.LOKALITA.SEGMENT.HOST
```

Význam:

- druhý oktet `LOKALITA` označuje spravované místo;
- každá lokalita dostane rezervovaný prostor `/16`;
- třetí oktet `SEGMENT` označuje funkční síť;
- skutečně provozované sítě budou typicky jednotlivé `/24`;
- číslo segmentu nemusí být VLAN ID;
- stejný segment by měl mít napříč lokalitami pokud možno stejný význam;
- konkrétní slovník segmentů je další vrstva návrhu a zatím není uzamčený.

Rezervovaný `/16`, skutečně provozované `/24` a prefixy inzerované do WireGuardu jsou tři odlišné věci. Rezervace `/16` sama o sobě neznamená, že se celý prostor směruje nebo povoluje firewallem.

## Hrubé rozdělení prostoru

| Rozsah | Zamýšlené použití | Stav |
|---|---|---|
| `10.0.0.0/11` | vlastní infrastruktura a master sítě | pracovní rezervace |
| `10.32.0.0/11` | rodinné lokality | pracovní rezervace |
| `10.64.0.0/11` | lokality kamarádů | pracovní rezervace |
| `10.96.0.0/11` | technologická rezerva; fyzickým lokalitám nepřidělovat | pracovní rezervace |
| `10.128.0.0/9` | dlouhodobá rezerva | pracovní rezervace |
| `10.255.0.0/16` | VPN, transit a virtuální adresy; vyňato z dlouhodobé rezervy | pracovní rezervace |

Členění na vlastní infrastrukturu, rodinu a kamarády je pouze organizační pomůcka. Neurčuje firewallovou důvěru ani automatická přístupová práva.

Lokalita se zařadí podle vlastnictví infrastruktury a odpovědnosti za její správu v okamžiku přidělení. Pozdější změna vztahu sama o sobě nezpůsobí přečíslování fungující sítě.

## Domov / hlavní master lokalita

Pro vlastní infrastrukturu je předběžně použitelný prostor:

```text
10.0.x.x až 10.31.x.x
```

Z tohoto prostoru jsou pracovně vyřazené:

```text
lokalita 0    velmi běžný začátek privátních sítí
lokalita 8    častý výchozí prostor OpenVPN
```

Pro domov je zvolená pracovní lokalita:

```text
lokalita 10
10.10.0.0/16   rezervovaný prostor domova
```

Volba `10.10.x.x` je přehledná a snadno zapamatovatelná. Není považovaná za bezkolizní rozsah.

Konkrétní sítě uvnitř `10.10.0.0/16` – například hlavní LAN, servery, management, IoT, kamery nebo hosté – zatím nejsou schválené. Určí je až společný slovník segmentů.

## WireGuard, transit a virtuální adresy

Pro budoucí společnou VPN a transitní vrstvu je rezervovaný prostor:

```text
10.255.0.0/16
```

Jeho vnitřní členění zatím není rozhodnuté.

Pravidla:

- přes WireGuard se inzerují jen potřebné prefixy, nikoli automaticky celé `10.0.0.0/8`;
- přidělení `/16` lokalitě samo o sobě nevytváří firewallové oprávnění;
- firewall nemá automaticky povolit celý rezervovaný `/16` jen proto, že je směrovaný;
- VPN adresy, transitní sítě a případné virtuální adresy se mají dlouhodobě soustředit do `10.255.0.0/16`.

### Současná site-to-site síť

Dnešní `10.200.0.0/24` je existující VPN vrstva. V cílovém schématu se nesmí vykládat jako fyzická lokalita 200.

| Lokalita / peer | WG adresa | Stav |
|---|---|---|
| HOME | `10.200.0.1` | aktivní pro propojení s Honzou |
| PBS / Richard | `10.200.0.2` | předběžný návrh; ověřit živou konfiguraci |
| Honza | `10.200.0.3` | aktivní |
| Vernířovice | `10.200.0.4` | předběžný návrh |
| RD Švecovi | `10.200.0.10` | předběžný návrh |

Pouze adresy HOME a Honza jsou v této tabulce potvrzené živým fungujícím propojením. Ostatní řádky zůstávají návrhem do ověření konfigurace routerů.

### Dočasná výjimka notebookového WireGuardu

Notebookový WireGuard dnes používá:

```text
10.89.1.0/24
```

V novém schématu by tento rozsah vypadal jako lokalita 89, segment 1. Do migrace VPN vrstvy proto platí:

```text
lokalita 89 je blokovaná a nesmí být přidělena
10.89.1.0/24 je dočasná legacy výjimka
```

Při zavádění nové VPN vrstvy se tento rozsah pravděpodobně přesune do `10.255.0.0/16`.

## Známá kolizní a technologická rizika

- Přesná shoda domácího prefixu s hotelovou, kempovou, firemní nebo jinou cizí LAN může znemožnit přístup do stejného prefixu přes WireGuard.
- Stoprocentně bezkolizní volba v privátním IPv4 prostoru neexistuje.
- `10.96.0.0/12` je běžný výchozí Kubernetes Service CIDR; proto se celý blok `10.96.0.0/11` ponechává jako technologická rezerva.
- `10.244.0.0/16` používá ve výchozím nastavení Flannel; leží v dlouhodobé rezervě a fyzické lokalitě se nepřidělí.
- `10.8.0.0/16` je často používaný prostor OpenVPN.
- Firemní VPN routující celé `10.0.0.0/8` může s domácí sítí kolidovat bez ohledu na konkrétní volbu lokality.
- Běžné hotelové a veřejné Wi-Fi používají například `10.0.0.0/24`, `10.1.0.0/24`, `10.10.0.0/24`, `10.20.0.0/24`, `10.50.0.0/24` nebo `10.100.0.0/24`.

Cílem není odstranit každé možné riziko kolize, ale zvolit konzistentní a provozně zvládnutelný kompromis.

## Migrační zásady

- Po schválení plánu už nemají vznikat nové náhodné rozsahy `192.168.x.0/24`.
- Nové lokality mají používat nový adresní plán.
- Existující funkční sítě se nepřečíslovávají pouze kvůli estetice.
- Migrace proběhne při přirozené příležitosti, například při výměně routeru, zavedení segmentace, větší rekonstrukci nebo skutečné kolizi.
- Před konkrétním nasazením se provede inventura všech současných LAN, VLAN, VPN, routovaných a transitních rozsahů.

## Co zatím není rozhodnuto

- definitivní slovník funkčních segmentů;
- rozdělení IoT a kamer;
- umístění serverových služeb, hypervizorů, managementu, monitoringu a IPMI/iDRAC;
- vztah segmentů k VLANám;
- přesné vnitřní členění `10.255.0.0/16`;
- pořadí migrace stávajících lokalit;
- případný budoucí doplněk IPv6 ULA.

## Další postup

- [ ] Vypsat současné LAN, VLAN, WG, routované a transitní rozsahy všech spravovaných lokalit.
- [ ] Jednoznačně přiřadit číselný identifikátor každé lokalitě s respektováním blokací `0`, `8` a `89`.
- [ ] Navrhnout jednotný slovník funkčních segmentů; číslo segmentu automaticky neztotožňovat s VLAN ID.
- [ ] Navrhnout vnitřní členění `10.255.0.0/16` pro VPN, transit a virtuální adresy.
- [ ] Provést kontrolu kolizí s používanými VPN, kontejnery a běžnými vzdálenými sítěmi.
- [ ] Zařadit dnešní `10.89.1.0/24` a `10.200.0.0/24` do budoucího migračního plánu VPN vrstvy.
- [ ] Teprve potom připravit migrační pořadí; žádnou fungující lokalitu nepřečíslovávat jen kvůli estetice.
