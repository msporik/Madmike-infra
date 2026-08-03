# Síť

## Účel

Projekt je autoritativním místem pro společnou síťovou koncepci MadMike:

- současné známé a budoucí IP rozsahy;
- domácí síťovou infrastrukturu HOME;
- obecnější rozhodnutí a provozní zásady platné pro MikroTik.

Podrobná topologie a zařízení ostatních lokalit patří do jejich vlastních kapitol. Tento projekt z nich nevytváří druhou centrální inventuru.

## Dokumenty

- [Adresní plán](Adresni-plan.md) – současné, historické nebo neověřené rozsahy, cílový rámec adresace a bezpečný postup přidělení nebo migrace.
- [MikroTik](MikroTik.md) – domácí síťová infrastruktura, provozní kontrola, změny, aktualizace, diagnostika a obnova.

## Rychlá orientace pro převzetí

Přebírající správce má před prvním zásahem:

1. projít známou infrastrukturu HOME v dokumentu [MikroTik](MikroTik.md);
2. rozlišit aktivní adresaci od cílového návrhu v [adresním plánu](Adresni-plan.md);
3. porovnat dokumentaci s živou konfigurací pouze čtecími příkazy;
4. případné rozdíly nejprve zaznamenat, ne automaticky „opravovat“;
5. před zapisující změnou ověřit přístupovou cestu, zálohu konfigurace, návratový postup a přejímací test.

Základní závislost HOME je:

```text
RB5009UPr
└── CRS326-24G-2S+RM
    ├── CRS112-8P-4S a navazující PoE větev
    └── domácí AP a další klienti
```

Přesné porty, aktivní VLAN a úplné napájecí vazby zatím nejsou živě ověřené. Při výpadku více služeb se proto nejprve kontroluje společná síťová cesta a napájení, až potom jednotlivé aplikace.

## Hranice vůči ostatním projektům

- Interní DNS, Nginx Proxy Manager, HTTPS a provozní dokumentace WireGuardu zůstávají v projektu [Servery](../Servery/README.md).
- Mikr Manager, jeho grafy a alerty zůstávají v projektu [Monitoring](../Monitoring/Mikr.md).
- Exporty konfigurací a postup obnovy RouterOS zůstávají v projektu [Zálohy](../Zalohy/MikroTik.md).
- Topologie, zařízení a lokální rozhodnutí jiné lokality se zapisují do kapitoly dané lokality.
- Detailní kusová evidence hardwaru a skladových zásob zůstává v Airtable. Postupně může zahrnout nejen MikroTik, ale také miniPC, disky, paměti a komponenty Home Assistantu.

## Autorita a stavy údajů

GitHub je autoritativní publikovaná dokumentace. Skutečný provozní stav se při změně nebo pochybnosti ověřuje v živé konfiguraci zařízení.

Při konsolidaci historických podkladů platí:

1. novější schválené rozhodnutí nebo checkpoint v Library;
2. není-li, schválený závěr v Airtable / Brainstorming;
3. starší pracovní exporty a poznámky pouze jako historický podklad.

Po zapsání ověřeného výsledku do GitHubu se GitHub stává jediným publikovaným zdrojem daného údaje. Detailní HW evidence v Airtable není zdrojem aktivní topologie. Mikr je zdrojem dostupnosti a monitoringu, ne autoritativním inventářem sítě.

Dokumenty rozlišují:

- **aktivní / potvrzené** – doložený současný provoz;
- **naposledy evidované** – poslední známý stav bez nového živého ověření;
- **plánované** – schválený budoucí stav, který ještě nemusí být nasazený;
- **historické / neověřené** – stopa vyžadující ověření nebo rozhodnutí.

## Bezpečná změna

Před změnou routeru, switche, Wi-Fi, VLAN, adresace, DHCP, DNS, firewallu nebo routingu musí být jasné:

- co je skutečný současný stav a odkud byl ověřen;
- které služby, lokality a správcovské cesty změna ovlivní;
- jaká použitelná záloha nebo export existuje;
- jak se správce dostane k zařízení při ztrátě vzdáleného přístupu;
- jaké konkrétní testy prokážou úspěch;
- podle jaké podmínky se provede návrat.

Nemění se současně více vrstev, pokud je nelze samostatně ověřit. Po zásahu nestačí stav rozhraní `running`; ověřuje se DHCP, DNS, routing, firewall, Wi-Fi, WireGuard a skutečná dostupnost závislých služeb podle rozsahu změny.

## Zásady

- Současný stav a budoucí plán se nesmí směšovat.
- Nová IP adresa se neoznačí jako přidělená, dokud není ověřena v živé konfiguraci nebo výslovně schválena jako rezervace.
- Přesné interní IP adresy a směrování mohou být v tomto soukromém repozitáři evidované.
- Hesla, tokeny, privátní klíče, preshared keys, sériová čísla a jiné tajné nebo zbytečně citlivé údaje do repozitáře nepatří.
- Úprava dokumentace neopravňuje k zásahu do živé infrastruktury.
- Nejasnost v topologii nebo návratové cestě je důvodem rizikovou změnu odložit, nikoli improvizovat.

## Handover minimum

Přebírající správce musí umět dohledat nebo živě ověřit:

- hlavní router, switche, AP a jejich vzájemné závislosti;
- současné LAN, VLAN, VPN a routované prefixy;
- cestu interního DNS, WireGuardu a správy zařízení;
- umístění záloh a exportů konfigurace mimo GitHub;
- způsob místního zásahu při ztrátě vzdáleného přístupu;
- otevřené ověřovací úkoly v obou detailních dokumentech.

Dokud některý z těchto bodů není známý, provádějí se jen neinvazivní kontroly nebo změny s prokazatelně omezeným dopadem.
