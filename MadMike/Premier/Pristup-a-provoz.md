# Přístup a provoz

> Současný uživatelský stav byl potvrzen **2026-07-29**. Přesná pravidla na RB5009, verze aplikací a konfigurace VM501 nebyly při auditu ověřeny proti živému prostředí.

## Uživatelé a provozní požadavky

PREMIER používají pouze správce infrastruktury a externí účetní. Správce zadává přijaté faktury, PREMIER AI/OCR z nich automaticky čte údaje a účetní je následně účtuje.

Účetní se nyní úspěšně připojuje z internetu. Přístup musí zůstat jednoduchý, ale zatím není zjištěné:

- zda používá jedno spravované zařízení, nebo více zařízení;
- z jakých míst a sítí se připojuje;
- zda potřebuje místní tiskárnu;
- zda používá schránku mezi místním a vzdáleným počítačem;
- zda potřebuje přenos souborů přes RDP.

Tyto požadavky je nutné zjistit před změnou přístupového řešení.

## Vzdálený přístup

### Potvrzený současný stav

- VM501 používá standardní Windows RDP.
- RDP je publikované přímo do internetu přes MikroTik.
- Vzdálený přístup účetní nyní funguje.
- Omezení příchozího RDP pouze na české IP rozsahy není nasazené.
- Přesné živé pravidlo dst-nat, cílová IP, zdrojová omezení a související firewallová pravidla nejsou ověřená.

Přihlašovací údaje, hesla a konfigurace obsahující tajné hodnoty se do repozitáře nezapisují. Společné bezpečnostní zásady jsou v projektu [Přístupy](../Pristupy/README.md), konkrétní NAT a firewall patří do projektu [Síť](../Sit/MikroTik.md).

### Schválený krátkodobý krok

Ponechat běžného RDP klienta, ale omezit příchozí spojení na české IP rozsahy. Jde o dočasné snížení rizika, nikoli o cílovou náhradu bezpečného vzdáleného přístupu.

Omezení lze nasadit až po zjištění skutečných míst připojení účetní. Po změně se musí přístup prakticky otestovat z jejího běžného prostředí.

### Cílový stav

Odstranit přímé veřejné RDP a zachovat jednoduchý způsob přihlášení. Zvažované varianty jsou RD Gateway a VPN. Konečná varianta zatím nebyla vybrána a musí vycházet ze skutečného způsobu práce účetní.

Ověření současného pravidla a výběr cílového bezpečnostního modelu jsou evidované v projektu [Přístupy](../Pristupy/README.md) a zde se jako samostatné checkboxy neduplikují.

## Odpovědnost za správu

- Windows i PREMIER má aktualizovat správce infrastruktury.
- Licenci a licenční podklady drží správce.
- Přesná verze a edice Windows, aktivace, stav podpory a aktualizací nejsou ověřené.
- Přesná verze PREMIERu, licenční stav bez klíče, umístění dat a instalačních médií nejsou ověřené.
- Pravidelný termín a přesný postup aktualizací zatím nejsou stanovené.

Před plánovanou aktualizací nebo restartem musí být potvrzené, že v PREMIERu nikdo nepracuje.

## Běžná provozní kontrola

Po startu, restartu, aktualizaci nebo obnově ověřit:

1. Běží pouze zamýšlená kopie VM501 na správném hostiteli.
2. VM má očekávanou síťovou konektivitu a QEMU Guest Agent odpovídá.
3. RDP funguje pouze zamýšlenou cestou.
4. PREMIER se spustí a účetní data jsou dostupná.
5. AI/OCR funguje.
6. Licence a aktivace zůstaly funkční.
7. Poslední PBS backup skončil úspěšně.
8. Po zavedení aplikační zálohy skončil úspěšně i její poslední běh.
9. Po změně přístupu nebo aplikace se účetní připojí a dokončí běžný pracovní krok.

## Aktualizace a restart

1. Domluvit dobu, kdy v PREMIERu nikdo nepracuje, a aplikaci korektně ukončit.
2. Ověřit poslední úspěšný PBS backup; po zavedení aplikační zálohy ověřit i ji.
3. Zaznamenat výchozí verze bez licenčních klíčů a dalších tajných hodnot.
4. Provést plánovanou aktualizaci Windows nebo PREMIERu podle pokynů výrobce.
5. Po restartu projít běžnou provozní kontrolu.
6. Zaznamenat datum, rozsah a výsledek změny.

## Zálohy a obnova

VM501 je chráněná PBS zálohou celé VM. Vlastní aplikační záloha PREMIERu mimo PBS k 2026-07-29 neexistuje.

Cílem aplikační zálohy je umožnit rychlejší a přesnější obnovu PREMIERu nebo jedné účetní jednotky bez obnovy celé Windows VM. Před zavedením je nutné určit podporovaný způsob zálohy, cílové úložiště, retenci a ochranu před ztrátou samotné VM. Následně se musí prakticky ověřit obnova jedné testovací nebo bezpečně zvolené účetní jednotky.

Při DR platí:

1. Dell / VM501 vznikla historicky importem; tento krok není PBS restore.
2. Obnova VM501 z PBS zpět na Ryzen byla prakticky ověřena.
3. Před startem obnovené kopie musí být původní VM501 vypnutá nebo bezpečně izolovaná.
4. V jednu chvíli smí být produkčně aktivní pouze jedna kopie VM501.
5. Přístup účetní se přesměruje až po kontrole Windows, sítě, RDP, PREMIERu, dat, AI/OCR a licence.
6. Po návratu z dočasného DR provozu se jednoznačně určí autoritativní kopie, druhá se zastaví a pořídí se nový ověřený backup.

Podrobnosti PBS a obecný pořadník obnovy jsou v [PBS a disaster recovery](../Zalohy/PBS-DR.md).

## Otevřené úkoly

- [ ] Zjistit zařízení a místa přístupu účetní a její požadavky na tisk, schránku a přenos souborů.
- [ ] Porovnat živý stav a konfiguraci VM501 s dokumentací a případné změny zapsat do autoritativního dokumentu PVE Ryzen.
- [ ] Ověřit verzi a edici Windows, aktivaci, stav aktualizací a podpory.
- [ ] Ověřit verzi PREMIERu, licenční stav bez klíče, obecné umístění dat a bezpečné umístění instalačních médií.
- [ ] Po ověření pracovního prostředí účetní nasadit a prakticky otestovat schválené krátkodobé omezení RDP na české IP rozsahy.
- [ ] Navrhnout a zavést podporovanou aplikační zálohu PREMIERu mimo VM501 včetně retence a testu obnovy jedné účetní jednotky.
- [ ] Stanovit pravidelný aktualizační postup a termín pro Windows a PREMIER.
- [ ] Po výběru cílového přístupového řešení v projektu Přístupy ověřit s účetní celý běžný pracovní postup.
- [ ] Prakticky ověřit stručný DR postup se zajištěním, že nikdy neběží dvě produkční kopie VM501.
