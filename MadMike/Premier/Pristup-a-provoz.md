# Přístup a provoz

## Současný vzdálený přístup

- VM501 používá standardní Windows RDP.
- RDP je podle posledního potvrzeného stavu publikované přímo do internetu přes MikroTik.
- Přesné aktuální pravidlo dst-nat, cílová IP, zdrojová omezení a stav firewallu je nutné ověřit na živém RB5009.
- Přístup musí zůstat jednoduchý pro externí účetní; změna nesmí bez náhrady zablokovat běžnou práci.

Přihlašovací údaje, hesla a RDP konfigurace obsahující tajné hodnoty se do repozitáře nezapisují. Společné zásady jsou v projektu [Přístupy](../Pristupy/README.md).

## Schválený směr zabezpečení

### Krátkodobý kompromis

Ponechat používání běžného klienta RDP, ale omezit příchozí spojení na české IP rozsahy. Jde pouze o omezení rizika, ne o plnohodnotnou náhradu bezpečného vzdáleného přístupu.

Před nasazením je potřeba ověřit, odkud se účetní skutečně připojuje a zda omezení neznemožní legitimní přístup.

### Cílový stav

Odstranit přímé veřejné RDP a zachovat jednoduchý způsob přihlášení. Zvažované varianty jsou:

- RD Gateway;
- přístup přes VPN.

Konečná varianta zatím nebyla vybrána. Realizace musí vycházet z praktického způsobu práce účetní, ne jen z technické elegance.

## Základní provozní kontrola

Po spuštění nebo obnově VM ověřit:

1. VM501 běží na zamýšleném hostiteli.
2. Má správnou interní IP a síťovou konektivitu.
3. RDP funguje pouze zamýšlenou cestou.
4. PREMIER se spustí.
5. Účetní data jsou dostupná.
6. Aplikační záloha PREMIERu probíhá, pokud je nakonfigurovaná.
7. Licence a aktivace zůstaly funkční.

Obnova z PBS je doložena v [PBS a disaster recovery](../Zalohy/PBS-DR.md). Přesný postup dočasného přepnutí přístupu při DR ještě není sepsaný.

## Otevřené úkoly

- zjistit, kdo VM vzdáleně používá a jakým postupem;
- ověřit současné NAT a firewall pravidlo;
- ověřit, zda už existuje omezení zdrojových IP;
- rozhodnout mezi RD Gateway a VPN;
- zjistit umístění účetních dat a aplikačních záloh bez ukládání samotných dat do repozitáře;
- doplnit odpovědnost za aktualizace Windows a PREMIERu;
- sepsat stručný postup pro start, kontrolu a dočasný DR provoz.
