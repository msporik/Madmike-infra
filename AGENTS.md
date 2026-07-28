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

## Bezpečnost a rozsah práce

- Do repozitáře neukládej hesla, tokeny, privátní klíče ani neupravené výpisy obsahující tajné hodnoty.
- Úprava dokumentace sama o sobě neopravňuje ke změnám v infrastruktuře.
- Nemaž ani nepřepisuj nesouvisející uživatelské změny.
- Neoznačuj VM, zálohu nebo jiný objekt jako nepotřebný bez ověření jeho role.

## Výstup práce

Po úpravě stručně uveď:

- které soubory se změnily;
- co bylo konsolidováno;
- které nejasnosti nebo ověřovací úkoly zůstaly otevřené.
