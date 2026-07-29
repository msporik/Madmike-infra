# MadMike Infrastructure

Živá technická dokumentace infrastruktury MadMike.

## Struktura

Dokumentace používá co nejjednodušší potřebnou hierarchii:

```text
kapitola/
├── README.md
├── jednotlivá témata kapitoly.md
└── projekt/
    ├── README.md
    └── jednotlivá témata projektu.md
```

- **Kapitola** je hlavní spravovaný celek nebo lokalita.
- Pokud kapitola obsahuje jediný ucelený projekt, jeho přehled a témata mohou být přímo v kořeni kapitoly.
- Samostatný adresář **projektu** vznikne, když kapitola obsahuje více dlouhodobě oddělených oblastí.
- `README.md` je společný a autoritativní přehled příslušné kapitoly nebo projektu.
- Jednotlivá témata jsou Markdown soubory přímo vedle příslušného `README.md`.

Příklady: `Rybniky-Amerika/Topologie.md` a `MadMike/Monitoring/Mikr.md`.

## Obsah

- [Otevřené úkoly](TODO.md) – automaticky generovaný přehled s odkazy na původní dokumenty.
- [MadMike](MadMike/README.md) – provozovaná infrastruktura a jednotlivé projekty.
- [Vernířovice](Vernirovice/README.md) – místní Home Assistant, BESS, FVE a řízení energie.
- [Honza](Honza/README.md) – místní Home Assistant, chytrá domácnost a síť.
- [HA ValTom](HA-ValTom/README.md) – připravený HA Green pro Tomáše Valentu, vzdálený přístup a budoucí GoodWe energetika.
- [Rybníky – Amerika](Rybniky-Amerika/README.md) – místní síť a její postupná konsolidace.

## Zásady

- Dokumentace popisuje aktuální stav, rozhodnutí a navazující kroky.
- Historické checkpointy se do repozitáře nekopírují jako paralelní aktuální dokumentace.
- Nová kapitola nebo projekt vznikne až ve chvíli, kdy se skutečně začne řešit.
- Hesla, tokeny a jiné tajné hodnoty do repozitáře nepatří.
- Podrobná pravidla pro práci s dokumentací jsou v [AGENTS.md](AGENTS.md).
