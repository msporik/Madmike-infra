# Adresní plán

## Stav dokumentu

Dokument odděluje současné potvrzené rozsahy od předběžného cílového návrhu. Návrhová část není migrační příkaz ani potvrzení, že navržené rozsahy už jsou nasazené.

## Současné potvrzené rozsahy

| Účel / lokalita | Rozsah | Stav |
|---|---|---|
| HOME | `192.168.89.0/24` | aktivní |
| Honza | `192.168.10.0/24` | aktivní; brána `192.168.10.1` |
| PBS / Richard | `192.168.100.0/24` | aktivní |
| notebookový WireGuard | `10.89.1.0/24` | aktivní; RB5009 má `10.89.1.1/24` |
| site-to-site WireGuard HOME ↔ Honza | `10.200.0.0/24` | aktivní; HOME `10.200.0.1`, Honza `10.200.0.3` |

Rozsahy dalších lokalit se doplní až po kontrole živých routerů.

## Cílový princip

Navržený formát adresy:

```text
10.LOKALITA.SEGMENT.HOST
```

Význam:

- `LOKALITA` určuje spravované místo;
- `SEGMENT` určuje funkční síť nebo VLAN v dané lokalitě;
- `HOST` je konkrétní zařízení;
- hlavní domácí lokalita má jako pracovní návrh `10.10.x.x`;
- pro domácí a těsně související sítě je předběžně vyhrazený prostor lokalit `10.0` až `10.31`.

Konkrétní číslování segmentů a migrace zatím nejsou schválené.

## Site-to-site WireGuard síť

Pro společnou WG tranzitní síť se používá nebo navrhuje tento rozsah:

| Lokalita / peer | WG adresa | Stav |
|---|---|---|
| HOME | `10.200.0.1` | aktivní pro propojení s Honzou |
| PBS / Richard | `10.200.0.2` | předběžný návrh; ověřit živou konfiguraci |
| Honza | `10.200.0.3` | aktivní |
| Vernířovice | `10.200.0.4` | předběžný návrh |
| RD Švecovi | `10.200.0.10` | předběžný návrh |

Pouze adresy HOME a Honza jsou v této tabulce potvrzené živým fungujícím propojením. Ostatní řádky jsou návrh, dokud je nepotvrdí konfigurace routerů.

## Známá kolizní rizika

Před přidělením rozsahů je nutné zohlednit zejména:

- Kubernetes service rozsahy kolem `10.96.0.0/12`;
- Flannel a podobné overlay sítě kolem `10.244.0.0/16`;
- časté OpenVPN použití `10.8.0.0/16`;
- firemní VPN využívající velkou část `10.0.0.0/8`;
- běžné hotelové a veřejné Wi-Fi sítě jako `10.0.0.0/24`, `10.1.0.0/24`, `10.10.0.0/24`, `10.20.0.0/24`, `10.50.0.0/24` nebo `10.100.0.0/24`.

Riziko kolize nelze úplně odstranit. Cílem je zvolit konzistentní a provozně zvládnutelný kompromis.

## Další postup

1. Vypsat současné LAN, VLAN a WG rozsahy všech spravovaných lokalit.
2. Jednoznačně přiřadit číselný identifikátor každé lokalitě.
3. Navrhnout společné číslování segmentů.
4. Provést kontrolu kolizí s používanými VPN, kontejnery a běžnými vzdálenými sítěmi.
5. Teprve potom připravit migrační pořadí; žádnou fungující lokalitu nepřečíslovávat jen kvůli estetice.
