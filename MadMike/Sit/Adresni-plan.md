# Adresní plán

## Stav dokumentu

Dokument odděluje tři vrstvy:

- současné doložené rozsahy;
- historické nebo dosud živě neověřené údaje;
- předběžný cílový plán interních IPv4 adres.

Cílový plán je pracovní architektonický rámec. Není migračním příkazem ani potvrzením, že navržené rozsahy už jsou nasazené.

Provozní konfigurace WireGuard peerů, `allowed-address` a rout patří výhradně do [Servery / WireGuard](../Servery/WireGuard.md). Tento dokument vede jen adresní principy a používané nebo rezervované prefixy.

## Autorita záznamu

Za přidělený nebo aktivní se rozsah považuje pouze tehdy, když je:

- ověřený v živé konfiguraci a zapsaný v tomto dokumentu; nebo
- výslovně schválený jako rezervace a označený odpovídajícím stavem.

Poznámka v chatu, starý export, záznam v Mikru ani samotná route nejsou bez ověření důkazem aktuálního účelu prefixu. Detailní lokální topologie zůstává v kapitole dané lokality; sem se přenáší potvrzený prefix, stav a jeho společný význam.

## Současné doložené rozsahy

| Účel / lokalita | Rozsah | Stav |
|---|---|---|
| HOME | `192.168.89.0/24` | aktivní podle poslední dokumentace |
| Honza | `192.168.10.0/24` | aktivní; brána `192.168.10.1` |
| PBS / Richard | `192.168.100.0/24` | aktivní |
| ŠÉF / RD Švecovi | `192.168.22.0/24` | příslušnost lokality potvrzena; živou konfiguraci ještě ověřit |

Rozsah `192.168.22.0/24` nepatří Rybníkům. Historické přiřazení Rybníkům bylo chybné.

## Současné legacy VPN prefixy

| Účel | Rozsah | Stav |
|---|---|---|
| notebookový WireGuard | `10.89.1.0/24` | aktivní; RB5009 má `10.89.1.1/24` |
| site-to-site WireGuard | `10.200.0.0/24` | používaná legacy VPN vrstva |

Tyto prefixy nejsou součástí cílového schématu `10.LOKALITA.SEGMENT.HOST` a nesmí se vykládat jako fyzické lokality 89 a 200. Konkrétní peer adresy se zde záměrně neevidují.

## Historické nebo neověřené údaje

| Lokalita / původ | Rozsah | Stav |
|---|---|---|
| neznámý historický původ | `192.168.30.0/24` | určit při kontrole starého IPsec a živých konfigurací |
| Vernířovice / `IOTVL` | zatím neurčený | doložená samostatná IoT síť; rozsah a současný provoz ověřit v kapitole Vernířovice |
| Rybníky – Amerika | zatím neurčený | skutečný současný i cílový LAN prefix dosud není v tomto plánu přidělený |

Podrobnosti jednotlivých lokalit se ověřují a zapisují v jejich vlastních kapitolách. Do tohoto přehledu se přenesou až potvrzené rozsahy.

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

## VPN, transit a virtuální adresy

Pro budoucí společnou VPN a transitní vrstvu je rezervovaný prostor:

```text
10.255.0.0/16
```

Jeho vnitřní členění zatím není rozhodnuté.

Pravidla:

- přes WireGuard se inzerují jen potřebné prefixy, nikoli automaticky celé `10.0.0.0/8`;
- přidělení `/16` lokalitě samo o sobě nevytváří firewallové oprávnění;
- firewall nemá automaticky povolit celý rezervovaný `/16` jen proto, že je směrovaný;
- VPN adresy, transitní sítě a případné virtuální adresy se mají dlouhodobě soustředit do `10.255.0.0/16`;
- provozní mapování peerů zůstává pouze v dokumentaci WireGuardu.

Notebookový `10.89.1.0/24` i site-to-site `10.200.0.0/24` zůstávají do migrace legacy výjimkami. Lokalita 89 je proto blokovaná a nesmí být přidělena.

## Známá kolizní a technologická rizika

- Přesná shoda domácího prefixu s hotelovou, kempovou, firemní nebo jinou cizí LAN může znemožnit přístup do stejného prefixu přes WireGuard.
- Stoprocentně bezkolizní volba v privátním IPv4 prostoru neexistuje.
- `10.96.0.0/12` je běžný výchozí Kubernetes Service CIDR; proto se celý blok `10.96.0.0/11` ponechává jako technologická rezerva.
- `10.244.0.0/16` používá ve výchozím nastavení Flannel; leží v dlouhodobé rezervě a fyzické lokalitě se nepřidělí.
- `10.8.0.0/16` je často používaný prostor OpenVPN.
- Firemní VPN routující celé `10.0.0.0/8` může s domácí sítí kolidovat bez ohledu na konkrétní volbu lokality.
- Běžné hotelové a veřejné Wi-Fi používají například `10.0.0.0/24`, `10.1.0.0/24`, `10.10.0.0/24`, `10.20.0.0/24`, `10.50.0.0/24` nebo `10.100.0.0/24`.

Cílem není odstranit každé možné riziko kolize, ale zvolit konzistentní a provozně zvládnutelný kompromis.

## Přidělení nového rozsahu

Nový prefix se nepřiděluje pouze podle volného čísla. Postup:

1. určit lokalitu, vlastníka infrastruktury, správce a skutečný účel sítě;
2. ověřit všechny současné LAN, VLAN, VPN, transitní, kontejnerové a routované prefixy, které se mohou setkat v jedné routingové doméně;
3. zkontrolovat pracovní rezervace a blokované lokality;
4. zvolit identifikátor lokality pouze v odpovídajícím bloku a skutečnou síť typicky jako `/24` uvnitř jejího `/16`;
5. segment přidělit až po schválení společného slovníku, nebo jej do té doby označit jako pracovní návrh;
6. určit gateway, DHCP rozsah, pevné adresy, potřebné routy a firewallovou roli bez automatického rozšíření důvěry na celý `/16`;
7. zapsat rezervaci do tohoto dokumentu dříve, než vznikne další nezávislá konfigurace stejného prefixu;
8. po nasazení provést přejímací test a změnit stav z plánovaného na aktivní pouze podle živého ověření.

Minimální záznam prefixu obsahuje:

- lokalitu a účel;
- prefix a gateway, jsou-li aktivní;
- stav `rezervovaný`, `plánovaný`, `aktivní`, `legacy` nebo `historický / neověřený`;
- vazbu na lokální autoritativní dokument;
- datum a způsob posledního ověření;
- potřebné routingové a VPN souvislosti bez klíčů a tajných hodnot.

## Migrační zásady

- Po schválení plánu už nemají vznikat nové náhodné rozsahy `192.168.x.0/24`.
- Nové lokality mají používat nový adresní plán.
- Existující funkční sítě se nepřečíslovávají pouze kvůli estetice.
- Migrace proběhne při přirozené příležitosti, například při výměně routeru, zavedení segmentace, větší rekonstrukci nebo skutečné kolizi.
- Před konkrétním nasazením se provede inventura všech současných LAN, VLAN, VPN, routovaných a transitních rozsahů.

## Runbook migrace prefixu

1. **Inventura:** vypsat routery, switche, VLAN, DHCP, DNS, statické adresy, firewall, NAT, routy, WireGuard, monitoring, proxy upstreamy a zařízení bez DHCP.
2. **Závislosti:** určit služby a vzdálené lokality, které starý prefix používají; zvlášť ověřit serverové, zálohovací a správcovské cesty.
3. **Návrh:** schválit nový prefix, gateway, DHCP rozsah, pevné adresy, přechodné routy a podmínky rollbacku. Návrh se stále neoznačuje jako aktivní stav.
4. **Příprava:** ověřit zálohy konfigurací, místní přístup, servisní okno a nezávislou komunikační cestu.
5. **Změna:** měnit po vrstvách; nezavádět současně další nesouvisející VLAN, firewallovou koncepci nebo upgrade RouterOS.
6. **Navazující konfigurace:** upravit DHCP, DNS, statické klienty, routy, firewall, NAT, WireGuard, monitoring a aplikační upstreamy podle jejich autoritativních dokumentů.
7. **Přejímka:** otestovat skutečné klienty a služby, nikoli pouze ping gateway.
8. **Dohled:** ponechat starý rozsah nebo návratovou konfiguraci jen po dobu schváleného přechodu a sledovat logy, DHCP, monitoring a zálohy.
9. **Dokončení:** staré routy a výjimky odstranit až po ověření, že je nic nepoužívá; GitHub aktualizovat na skutečný konečný stav.

### Přejímací test

Podle rozsahu migrace se ověří:

- klient získá správnou adresu, gateway a DNS;
- lokální komunikace odpovídá zamýšlené segmentaci;
- internet, DNS a NTP fungují;
- správa routeru, switchů, AP a serverů zůstala dostupná;
- WireGuard funguje od handshake až po skutečnou službu v cílové LAN;
- NPM, monitoring a zálohy používají správné adresy a routy;
- statická zařízení, tiskárny, kamery, IoT a další klienti bez běžného DHCP byly ověřeny;
- firewall nepovolil širší přístup jen kvůli novému rezervovanému `/16`;
- nevznikl duplicitní DHCP server, gateway ani IP adresa.

### Podmínky rollbacku

Návrat se provede zejména při ztrátě správy, nefunkčním DHCP nebo DNS, nedostupnosti kritické služby, nejasné routingové smyčce či kolizi nebo při neověřitelné bezpečnostní segmentaci. Rollback vrací předem zaznamenaný funkční stav; není pokračováním pokusných změn.

## Co zatím není rozhodnuto

- definitivní slovník funkčních segmentů;
- rozdělení IoT a kamer;
- umístění serverových služeb, hypervizorů, managementu, monitoringu a IPMI/iDRAC;
- vztah segmentů k VLANám;
- přesné vnitřní členění `10.255.0.0/16`;
- identifikátory lokalit kromě pracovní volby HOME;
- pořadí migrace stávajících lokalit;
- případný budoucí doplněk IPv6 ULA.

## Handover minimum

Přebírající správce musí před přidělením nebo migrací umět rozlišit:

- fyzickou lokalitu, funkční segment a VLAN ID;
- rezervovaný `/16`, aktivní `/24` a prefix skutečně inzerovaný do VPN;
- aktivní stav, pracovní návrh a historickou stopu;
- lokální adresaci, VPN adresaci a kontejnerové nebo technologické prefixy;
- autoritativní dokument adresace od provozní konfigurace WireGuardu a lokální topologie.

Neznámý původ prefixu se řeší živou inventurou. Neobsazené číslo bez dokončené kontroly se nepovažuje za volné.

## Další postup

- [ ] Vypsat současné LAN, VLAN, routované a transitní rozsahy všech spravovaných lokalit; provozní WG inventuru převzít z dokumentu WireGuard.
- [ ] Jednoznačně přiřadit číselný identifikátor každé lokalitě s respektováním blokací `0`, `8` a `89`.
- [ ] Navrhnout jednotný slovník funkčních segmentů; číslo segmentu automaticky neztotožňovat s VLAN ID.
- [ ] Navrhnout vnitřní členění `10.255.0.0/16` pro VPN, transit a virtuální adresy.
- [ ] Provést kontrolu kolizí s používanými VPN, kontejnery a běžnými vzdálenými sítěmi.
- [ ] Zařadit dnešní `10.89.1.0/24` a `10.200.0.0/24` do budoucího migračního plánu VPN vrstvy.
- [ ] Teprve potom připravit migrační pořadí; žádnou fungující lokalitu nepřečíslovávat jen kvůli estetice.
