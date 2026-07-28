# MadMike Infrastructure

Živá technická dokumentace infrastruktury MadMike.

## Struktura

Dokumentace používá jednoduchou hierarchii:

```text
kapitola/
└── projekt/
    ├── README.md
    └── jednotlivá témata projektu.md
```

- **Kapitola** je hlavní spravovaný celek nebo lokalita.
- **Projekt** je dlouhodobá oblast uvnitř kapitoly.
- `README.md` projektu je společný a autoritativní přehled.
- Jednotlivá témata projektu jsou soubory přímo v jeho adresáři.

Příklad: `MadMike/Monitoring/Mikr.md`.

## Obsah

- [MadMike](MadMike/README.md) – provozovaná infrastruktura a jednotlivé projekty.
- [Vernířovice](Vernirovice/README.md) – místní Home Assistant, BESS, FVE a řízení energie.

## Zásady

- Dokumentace popisuje aktuální stav, rozhodnutí a navazující kroky.
- Historické checkpointy se do repozitáře nekopírují jako paralelní aktuální dokumentace.
- Nová kapitola nebo projekt vznikne až ve chvíli, kdy se skutečně začne řešit.
- Hesla, tokeny a jiné tajné hodnoty do repozitáře nepatří.
- Podrobná pravidla pro práci s dokumentací jsou v [AGENTS.md](AGENTS.md).
