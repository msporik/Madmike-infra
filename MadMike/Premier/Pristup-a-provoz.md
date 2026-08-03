# Přístup a provoz

> Současný uživatelský stav byl potvrzen **2026-07-29**. Přesná pravidla na RB5009, verze aplikací a živá konfigurace VM501 nebyly při tomto zpracování ověřeny proti provoznímu prostředí.

## Provozní role

| Role | Odpovědnost |
|---|---|
| Správce infrastruktury | VM501, Windows, PREMIER, licence, aktualizace, koordinace odstávky, aplikační přejímka po obnově |
| Externí účetní | běžné účtování a praktická přejímka vzdáleného pracovního postupu |

PREMIER používají pouze tyto dvě role. Kontakty, hesla, licenční klíče a další autentizační materiály se do GitHubu nezapisují.

## Požadavky na práci účetní

Účetní se nyní úspěšně připojuje z internetu. Přístup musí zůstat jednoduchý. Před jeho změnou je nutné zjistit:

- zda používá jedno spravované zařízení, nebo více zařízení;
- z jakých míst a sítí se připojuje;
- zda potřebuje místní tiskárnu;
- zda používá schránku mezi místním a vzdáleným počítačem;
- zda potřebuje přenos souborů přes RDP.

Dokud tyto potřeby nejsou ověřené, nelze bezpečně uzavřít návrh cílového přístupu ani původní cestu odstranit.

## Vzdálený přístup

### Potvrzený současný stav

- VM501 používá standardní Windows RDP.
- RDP je publikované přímo do internetu přes MikroTik.
- Vzdálený přístup účetní nyní funguje.
- Omezení příchozího RDP pouze na české IP rozsahy není nasazené.

**Vyžaduje ověření v živém systému:** přesné pravidlo dst-nat, cílová IP, veřejný port, zdrojová omezení a související firewallová pravidla.

Přihlašovací údaje ani neupravené výpisy obsahující tajné hodnoty se do repozitáře nezapisují. Společné bezpečnostní zásady jsou v projektu [Přístupy](../Pristupy/README.md); konkrétní NAT a firewall patří do projektu [Síť](../Sit/MikroTik.md).

### Schválený krátkodobý krok

Ponechat běžného RDP klienta, ale omezit příchozí spojení na české IP rozsahy. Jde o dočasné snížení rizika, nikoli o cílovou náhradu bezpečného vzdáleného přístupu.

Omezení lze nasadit až po zjištění skutečných míst připojení účetní. Po změně se musí přístup prakticky otestovat z jejího běžného prostředí a musí být připravený návrat k předchozímu funkčnímu pravidlu.

### Cílový stav

Odstranit přímé veřejné RDP a zachovat jednoduchý způsob přihlášení. Zvažované varianty jsou RD Gateway a VPN. Konečná varianta zatím nebyla vybrána a musí vycházet ze skutečného způsobu práce účetní.

Výběr cílového bezpečnostního modelu je evidovaný v projektu [Přístupy](../Pristupy/README.md). Tento dokument popisuje aplikační dopady a praktický test, nikoli duplicitní síťovou konfiguraci.

## Běžný start a kontrola služby

1. Ověřit, že na Ryzenu ani na DR hostu neběží jiná produkční kopie VM501.
2. Spustit zamýšlenou VM501 standardním způsobem v Proxmoxu.
3. Vyčkat na start Windows a ověřit stav VM, očekávanou síťovou konektivitu a odpověď QEMU Guest Agentu.
4. Ověřit RDP nejprve z důvěryhodné správcovské cesty a podle potřeby také z běžného prostředí účetní.
5. Spustit PREMIER a ověřit, že jsou dostupná očekávaná účetní data, aniž by se jejich obsah zapisoval do dokumentace.
6. Ověřit AI/OCR na běžném bezpečně zvoleném pracovním kroku.
7. Ověřit licenci a aktivaci bez zobrazení nebo ukládání klíče.
8. Zkontrolovat poslední výsledek PBS backupu; po zavedení aplikační zálohy také její poslední běh.

Kontrola je dokončená až po ověření aplikace. Samotný běh VM, ping nebo dostupné RDP nejsou dostatečným důkazem funkčního účetního systému.

## Korektní odstavení a restart

1. Potvrdit se správcem a účetní, že v PREMIERu nikdo nepracuje.
2. Korektně ukončit PREMIER a rozpracovanou práci.
3. Ověřit poslední použitelný PBS backup; před rizikovější změnou pořídit backup podle pravidel projektu Zálohy.
4. Windows vypnout nebo restartovat standardním způsobem. Vynucené zastavení VM použít pouze při incidentu, kdy běžné ukončení nefunguje.
5. Po startu projít celý běžný kontrolní postup.

## Plánovaná aktualizace

1. Domluvit dobu, kdy v PREMIERu nikdo nepracuje.
2. Ověřit poslední úspěšný PBS backup a po budoucím zavedení i aplikační zálohu.
3. Zaznamenat výchozí verze Windows a PREMIERu bez licenčních a osobních údajů.
4. Připravit návratovou cestu a určit, co je důvodem k rollbacku.
5. Aktualizovat Windows nebo PREMIER podle podporovaného postupu výrobce; obě významné změny nespojovat bez konkrétního důvodu do jednoho nevratného zásahu.
6. Po restartu projít běžnou provozní kontrolu včetně AI/OCR a licence.
7. Nechat účetní ověřit běžný pracovní krok, pokud změna mohla ovlivnit její práci.
8. Zaznamenat datum, rozsah, původní a výslednou verzi a výsledek kontroly.

Pravidelný termín aktualizací a přesný postup dosud nejsou stanovené. **Vyžaduje ověření v živém systému** také aktuální podpora Windows a instalované verze PREMIERu.

## Diagnostika běžných problémů

| Projev | První kontrola | Další postup |
|---|---|---|
| VM501 neběží | stav PVE Ryzen, VM501 a storage | postupovat podle projektu Servery; před startem vyloučit běžící DR kopii |
| Windows nenabootují | konzole VM, stav disku a poslední změna | neprovádět současně změnu virtuálního hardwaru; rozhodnout mezi rollbackem a obnovou |
| RDP nefunguje, VM odpovídá | Guest Agent, IP VM, Windows síť a RDP služba | oddělit problém Windows od MikroTik NAT/firewall; ověřit interní a externí cestu zvlášť |
| RDP funguje interně, ne z internetu | doložená cílová IP a živé NAT/firewall pravidlo | řešit v projektech Síť a Přístupy; nezveřejňovat RDP na další port jako náhodný workaround |
| PREMIER se nespustí | poslední změna, stav Windows, volné místo a systémová hlášení | neměnit ani neobnovovat účetní data bez určení příčiny a použitelného backupu |
| Data nejsou dostupná | zda běží správná VM a správná kopie prostředí | zastavit další zápisy, nevytvářet druhou autoritativní kopii a určit rozsah incidentu |
| AI/OCR nefunguje | zda zbytek PREMIERu funguje a zda jde o izolovanou funkci | zaznamenat chybu bez dokladu a osobních údajů; ověřit licenční, síťovou nebo poskytovatelskou závislost podle podpory PREMIERu |
| Licence nebo aktivace po obnově selže | zda byla obnovena očekávaná VM a nezměnil se její hardware | použít bezpečně uložené licenční podklady a podporovaný postup; klíč nevkládat do GitHubu ani chatu |
| Poslední backup selhal | čas a chyba posledního PBS jobu | řešit v projektu Zálohy; do vyřešení nepovažovat VM za řádně chráněnou |

Při incidentu se nejprve chrání současná data a určuje autoritativní kopie. Opakované restarty, změny diskového řadiče, souběžné spuštění kopie nebo nahodilé opravy databáze mohou stav zhoršit.

## Zálohy

VM501 je chráněná PBS zálohou celé VM. Vlastní aplikační záloha PREMIERu mimo PBS k 2026-07-29 neexistuje.

Cílem aplikační zálohy je umožnit rychlejší a přesnější obnovu PREMIERu nebo jedné účetní jednotky bez obnovy celé Windows VM. Před zavedením je nutné určit:

- výrobcem podporovaný způsob zálohy a obnovy;
- obecné umístění zdrojových dat bez zveřejnění účetního obsahu;
- cílové úložiště a retenci;
- způsob, jak zálohu chránit mimo samotnou VM501;
- odpovědnost za kontrolu výsledku;
- bezpečný test obnovy jedné testovací nebo vhodně zvolené účetní jednotky.

Podrobnosti PBS, retence, Verify, Prune, Garbage Collection a obecný DR pořadník jsou pouze v [PBS a disaster recovery](../Zalohy/PBS-DR.md).

## Aplikační DR postup

Tento postup navazuje na obnovu VM podle projektu Zálohy a popisuje pouze přejímku PREMIERu.

1. Potvrdit cíl obnovy, poslední použitelný snapshot a očekávaný rozsah ztracených změn.
2. Zajistit, že původní VM501 je vypnutá nebo bezpečně izolovaná.
3. Obnovit VM501 podle autoritativního PBS postupu. Během havarijní obnovy neměnit diskový řadič, síťový adaptér ani jiný historicky funkční virtuální hardware.
4. Před připojením do produkční sítě vyloučit kolizi IP, VMID a souběžnou produkční kopii.
5. Ověřit start Windows, Guest Agent, síť a RDP správcovskou cestou.
6. Spustit PREMIER a ověřit dostupnost očekávaných dat, AI/OCR, licenci a aktivaci.
7. Připravit dočasnou přístupovou cestu účetní podle skutečného cílového hostitele; přesná síťová změna patří do projektů Síť a Přístupy.
8. Nechat účetní prakticky ověřit přihlášení a běžný pracovní krok včetně tisku nebo přenosu souborů, pokud je používá.
9. Teprve po přejímce označit kopii jako produkční a přesměrovat provoz.
10. Po stabilizaci vytvořit nový backup, zkontrolovat jeho výsledek a zaznamenat datum, použitý snapshot, autoritativní kopii a výsledek přejímky.

Po návratu z dočasného DR provozu se znovu jednoznačně určí autoritativní kopie, druhá se zastaví a pořídí se nový ověřený backup. V jednu chvíli smí být produkčně aktivní pouze jedna VM501.

## Dokladový tok a automatizace

Současnou používanou automatizací je pouze PREMIER AI/OCR. API ani automatický import faktur nejsou nasazené.

Nejprve se má ustálit jednoduchý ruční tok dokumentů:

- jedno vstupní místo pro nezpracované faktury;
- jednoznačné rozlišení připravených, zadaných a chybějících dokladů;
- jasné předání mezi správcem a účetní.

Teprve po praktickém ověření tohoto toku lze samostatně posoudit automatizaci importu. Starší ukázky nebo nápady kolem PREMIER API nejsou provozní konfigurací ani schváleným nasazením.

## Otevřené úkoly

### Přístup a pracovní prostředí

- [ ] Zjistit zařízení a místa přístupu účetní a její požadavky na tisk, schránku a přenos souborů.
- [ ] Po ověření pracovního prostředí účetní nasadit a prakticky otestovat schválené krátkodobé omezení RDP na české IP rozsahy.
- [ ] Po výběru cílového přístupového řešení v projektu Přístupy ověřit s účetní celý běžný pracovní postup a teprve poté odstranit původní veřejné RDP.

### Aplikace a Windows

- [ ] Ověřit verzi a edici Windows, aktivaci, stav aktualizací a podpory.
- [ ] Ověřit verzi PREMIERu, licenční stav bez klíče, obecné umístění dat a bezpečné umístění instalačních a licenčních podkladů.
- [ ] Stanovit pravidelný aktualizační postup a termín pro Windows a PREMIER včetně návratové cesty a přejímky.
- [ ] Ustálit jedno vstupní místo a stavy nezpracované, připravené, zadané a chybějící pro jednoduchý tok faktur před případnou automatizací importu.

### Zálohy a obnova

- [ ] Porovnat živý stav a konfiguraci VM501 s dokumentací a případné změny zapsat do autoritativního dokumentu PVE Ryzen.
- [ ] Navrhnout a zavést podporovanou aplikační zálohu PREMIERu mimo VM501 včetně retence, offsite ochrany a testu obnovy jedné účetní jednotky.
- [ ] Stanovit požadované RPO, RTO a přijatelnou dobu odstávky PREMIERu.
- [ ] Prakticky ověřit aplikační DR postup včetně dočasného přístupu účetní a zajištění, že nikdy neběží dvě produkční kopie VM501.
