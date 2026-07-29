# Pravidla práce s repozitářem

Tento soubor platí pro celý repozitář.

## Struktura dokumentace

- První úroveň je **kapitola** – hlavní spravovaný celek nebo lokalita.
- Druhá úroveň je **projekt** – dlouhodobá oblast uvnitř kapitoly.
- `README.md` projektu je autoritativní přehled projektu.
- Podrobnější témata projektu jsou samostatné Markdown soubory přímo v adresáři projektu.
- Vlastní podadresář vznikne až tehdy, když se z tématu skutečně stane samostatný projekt.
- Prázdné adresáře pro možné budoucí oblasti se předem nezakládají.

Příklad: `MadMike/Monitoring/Mikr.md`.

## Přesnost a stav informací

- Nevymýšlej chybějící technické údaje a nedoplňuj je odhadem.
- Jasně rozlišuj:
  - ověřený aktuální stav;
  - schválený návrh nebo plán;
  - otevřený úkol k ověření;
  - užitečnou historii.
- Před změnou projdi relevantní současnou dokumentaci a dostupný živý stav.
- Pokud je údaj nejasný, ponech ho jako úkol k ověření nebo se zeptej.
- Piš česky, pokud uživatel výslovně nepožádá jinak.

## Jeden živý zdroj pravdy

- Aktualizuj existující autoritativní dokument místo vytváření nové datované kopie.
- Historii změn uchovává Git; checkpointy a staré exporty nejsou paralelní aktuální dokumentace.
- Stejnou informaci bez důvodu neduplikuj do více souborů. Umísti ji do přirozeného hlavního dokumentu a z ostatních míst na ni odkaž.
- Dokumentace má být stručná a provozně užitečná, ne podrobný technický deník.

## Otevřené úkoly

- Otevřený úkol zapisuj v jeho autoritativním dokumentu jako Markdown checkbox `- [ ]`.
- Splněný úkol označ v původním dokumentu jako `- [x]`; z centrálního přehledu pak zmizí.
- Kořenový `TODO.md` je automaticky generovaný rozcestník a ručně se neupravuje.
- Každá položka v `TODO.md` odkazuje na původní řádek, který je jediným zdrojem pravdy.
- Běžné opakované provozní checklisty neoznačuj jako otevřené úkoly, pokud nejde o konkrétní nedokončenou práci.

## Bezpečnost a rozsah práce

- Repozitář je soukromý a je určený jako interní zdroj pravdy.
- Je povoleno evidovat interní IP adresy, hostname, DNS a NPM směrování, routy, názvy tunelů a další provozně potřebnou topologii.
- Do repozitáře nikdy neukládej hesla, tokeny, privátní klíče, preshared keys, recovery kódy ani neupravené výpisy obsahující tajné hodnoty.
- Při vkládání konfigurace nejdřív odstraň všechny tajné hodnoty; nestačí spoléhat na to, že repozitář je soukromý.
- Pokud by se viditelnost repozitáře změnila na veřejnou, před dalším zápisem znovu posuď celý bezpečnostní rozsah dokumentace.
- Úprava dokumentace sama o sobě neopravňuje ke změnám v infrastruktuře.
- Nemaž ani nepřepisuj nesouvisející uživatelské změny.
- Neoznačuj VM, zálohu nebo jiný objekt jako nepotřebný bez ověření jeho role.

## Výstup práce

Po úpravě stručně uveď:

- které soubory se změnily;
- co bylo konsolidováno;
- které nejasnosti nebo ověřovací úkoly zůstaly otevřené.
