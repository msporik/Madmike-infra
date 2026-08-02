# Hikvision

Domácí dveřní interkom a jeho napojení na Home Assistant.

## Aktuální stav

- **Zařízení:** Hikvision DS-KB8113-IME1(B).
- Hovor funguje.
- Vyzvánění funguje.
- Propojení přes Jablotron PG funguje, takže zvonění pracuje stejně jako dříve.
- Interkom je nasazený a jeho základní integrace je považovaná za dokončenou.

Poslední doložené stavy volání v integraci byly `idle`, `ring` a `onCall`. Home Assistant je může využívat jako stavovou informaci; funkce samotného zvonění není na Home Assistantu závislá.

## Uzavřená historie

Dříve řešená ozvěna a další drobné nedokonalosti nejsou vedené jako otevřený úkol. Znovu se budou řešit pouze tehdy, pokud budou mít skutečný provozní dopad.

## Hranice dokumentu

Tento dokument popisuje interkom. Stav kamer, NVR a plánovaná migrace kamerového systému na Hikvision jsou shrnuté pouze v [hlavním dokumentu projektu](README.md), protože záznam kamer není funkcí Home Assistantu.
