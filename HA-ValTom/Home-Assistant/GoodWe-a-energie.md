# GoodWe a energetika

## Cíl

První užitečnou funkcí HA ValTom má být přehled GoodWe FVE:

- aktuální výroba;
- spotřeba domu;
- odběr ze sítě a přetok do sítě;
- základní historické energetické údaje;
- jednoduchý a srozumitelný dashboard.

Pozdější rozšíření může řídit bojler podle výroby, přetoků nebo jiného schváleného energetického pravidla.

## Poslední doložený stav k 2026-08-03

Od předchozí přípravy nenastal posun. Přesný model GoodWe střídače, komunikační rozhraní a lokální IP adresa nejsou ověřené. Integrace GoodWe není zprovozněná, skutečné entity nejsou potvrzené a produkční dashboard neexistuje. Bojler není zmapovaný ani řízený Home Assistantem.

## Hranice řešení

- První fáze je pouze čtecí. Dokud nejsou ověřené hodnoty, neprovádějí se zápisové povely do střídače ani automatické řízení bojleru.
- Cloudflare Tunnel zpřístupňuje web Home Assistantu, ne celý lokální segment. Diagnostika GoodWe proto může vyžadovat místní zásah nebo později samostatně schválený servisní přístup do LAN.
- Přesný postup závisí na modelu střídače a jeho komunikačním modulu. Nepřebírá se konfigurace Deye, SolaX ani GoodWe z jiné lokality.
- Prvním kandidátem je oficiální lokálně dotazovaná integrace [GoodWe Inverter](https://www.home-assistant.io/integrations/goodwe/). Podporu konkrétního modelu a potřebné nastavení komunikačního modulu je nutné ověřit podle aktuální dokumentace a živého zařízení.

## Inventura před integrací

Před přidáním integrace zjistit a zapsat bez hesel a klíčů:

| Údaj | Skutečná hodnota | Jak ověřit |
|---|---|---|
| Přesný model střídače | **Vyžaduje ověření v živém systému.** | Typový štítek a oficiální rozhraní |
| Sériová řada a firmware | **Vyžaduje ověření v živém systému.** | Lokální nebo oficiální servisní aplikace |
| Komunikační modul | **Vyžaduje ověření v živém systému.** | Typový štítek, konfigurace modulu |
| Lokální IP a DHCP rezervace | **Vyžaduje ověření v živém systému.** | Router/DHCP a ověření z LAN |
| Měřicí prvky | **Vyžaduje ověření v živém systému.** | Elektrodokumentace a aplikace GoodWe |
| Dostupné lokální rozhraní | **Vyžaduje ověření v živém systému.** | Dokumentace modelu a read-only test |
| Význam směru toku | **Vyžaduje ověření v živém systému.** | Porovnání s elektroměrem/aplikací při známém stavu |

## Postup zprovoznění čtecí integrace

1. Dokončit síťovou část přejímky Green a ověřit stabilní lokální přístup k Home Assistantu.
2. Zjistit model, komunikační modul, IP a dostupnost GoodWe z téže sítě.
3. Ověřit, že lokální komunikace je pro daný model podporovaná a povolená. Neměnit firmware ani servisní nastavení bez důvodu a návratové cesty.
4. V Home Assistantu přidat oficiální integraci GoodWe podle aktuální dokumentace. Přístupové údaje neukládat do GitHubu.
5. Nechat integraci běžet bez řízení a zaznamenat skutečný seznam relevantních entit, jejich jednotky, dostupnost a interval změny.
6. Porovnat hodnoty ve stejný okamžik s oficiální aplikací GoodWe, lokálním displejem nebo důvěryhodným měřením.
7. Teprve po validaci přidat vybrané entity do dashboardu a případně do Energy dashboardu.
8. Po stabilním pilotu vytvořit full backup a zdokumentovat přesný model, komunikační cestu a pouze provozně důležité entity.

Výchozí interval dotazování se nemění bez důvodu. Pokud časté dotazování ovlivňuje jiný přístup nebo cloud GoodWe, nejprve potvrdit souvislost a potom použít podporované nastavení integrace.

## Validace energetických dat

| Veličina | Požadovaný význam | Ověření | Stav |
|---|---|---|---|
| Výroba FVE | Okamžitý výkon a kumulativní výroba | Porovnat při výrobě i večer; rozlišit W a kWh | Nerealizováno |
| Spotřeba domu | Okamžitý příkon a kumulativní spotřeba domu | Zapnout známou zátěž a ověřit odpovídající změnu | Nerealizováno |
| Odběr ze sítě | Tok a energie převzatá z distribuční sítě | Ověřit při spotřebě vyšší než výroba | Nerealizováno |
| Přetok do sítě | Tok a energie dodaná do distribuční sítě | Ověřit při výrobě vyšší než spotřeba | Nerealizováno |
| Dostupnost dat | Rozpoznání ztráty nebo zastarání komunikace | Odlišit platnou nulu od `unavailable` a staré hodnoty | Nerealizováno |

U každé použité entity zaznamenat:

- přesný `entity_id` a srozumitelný význam;
- jednotku a zda jde o výkon, okamžitou hodnotu nebo kumulativní energii;
- znaménko a směr toku;
- zdroj měření;
- typickou četnost aktualizace;
- chování při noci, výpadku střídače a ztrátě komunikace.

Odvozené template senzory nebo integrace výkonu na energii se vytvářejí až tehdy, když vhodná přímá entita opravdu chybí. Výpočet musí mít popsané vstupy, jednotky a chování po restartu.

## Minimální produkční dashboard

Dashboard má obsahovat jen ověřené hodnoty:

1. aktuální výrobu FVE;
2. spotřebu domu, pokud je skutečně měřená;
3. odběr a přetok se srozumitelným směrem;
4. dnešní výrobu a základní historii;
5. stav dostupnosti GoodWe a čas poslední smysluplné aktualizace;
6. stav bojleru až po jeho pozdějším bezpečném zapojení.

Přejímka dashboardu vyžaduje čitelnost na běžném zařízení, správné jednotky, shodu s referenčním měřením a viditelné rozlišení nuly, neznámé hodnoty a chyby komunikace.

## Diagnostika GoodWe

| Projev | První kontrola | Bezpečný další krok |
|---|---|---|
| Integrace zařízení nenajde | model, IP, stejná LAN a lokální rozhraní | Ověřit podporu konkrétní řady a nastavení komunikačního modulu podle oficiální dokumentace. |
| Zařízení odpovídá aplikaci, ale ne HA | protokol, firmware modulu a síťové omezení | Zachovat read-only režim, uložit chybu a porovnat s požadavky integrace. |
| Entity jsou `unavailable` | dosažitelnost IP, restart modulu, log integrace | Nezakládat automatizaci na poslední známé hodnotě; nejprve obnovit komunikaci. |
| Hodnoty se nemění | čas poslední aktualizace a polling | Porovnat se živou aplikací a ověřit, zda nejde o noc nebo legitimní nulu. |
| Odběr a přetok jsou obráceně | znaménko a instalace měření | Neopravovat jen kosmetikou v dashboardu; potvrdit fyzický význam a zdroj dat. |
| Denní součty nesedí | jednotky, reset cyklus a zdroj kumulativní entity | Porovnat celý uzavřený den a teprve potom volit odvozený senzor. |
| Po změně pollingu přestane fungovat cloud GoodWe | možný konflikt frekvence dotazování | Vrátit výchozí nastavení a řídit se doporučením oficiální integrace. |

## Otevřené kroky

- [ ] Zjistit přesný model GoodWe střídače, jeho lokální IP adresu, dostupný způsob komunikace a skutečné zdroje výroby, spotřeby, odběru a přetoku.
- [ ] Zprovoznit nejprve čtecí integraci GoodWe, ověřit význam, jednotky a znaménka skutečných entit a vytvořit základní produkční FVE dashboard s přiměřenou historií.
- [ ] Zmapovat typ, výkon, HDO, stykač, termostat a současné ruční ovládání bojleru; teprve potom navrhnout bezpečné automatické řízení.

## Bezpečnostní rámec řízení bojleru

- Home Assistant nesmí nahrazovat nezávislý termostat, havarijní tepelnou ochranu ani ostatní povinné elektrické ochrany.
- Spínací nebo regulační prvek musí být vhodný pro skutečný příkon a způsob zapojení bojleru a odborně nainstalovaný.
- Musí existovat srozumitelný ruční režim nezávislý na běhu automatizace.
- Při výpadku Home Assistantu, komunikace nebo potřebného měření musí systém přejít do předem určeného bezpečného stavu.
- Řízení musí mít zdokumentovaný práh, hysterezi, minimální dobu sepnutí a vypnutí, maximální dobu běhu a reakci na neplatná nebo zastaralá data.
- Návrat z ručního nebo poruchového režimu do automatiky musí být jednoznačný a předvídatelný.
- Zápisové řízení se nemá aktivovat, dokud nejsou ověřené energetické hodnoty, konkrétní hardware a schválená provozní logika.

Před produkčním spuštěním se automatizace otestuje nejprve bez skutečného spínání, potom pod dohledem a nakonec při výpadku HA, komunikace a měření. Výsledek a fail-safe stav se zapíší do tohoto dokumentu.
