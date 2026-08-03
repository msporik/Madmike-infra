# Hikvision

Domácí dveřní interkom a jeho napojení na Home Assistant.

## Aktuální stav

- **Zařízení:** Hikvision DS-KB8113-IME1(B).
- Hovor funguje.
- Vyzvánění funguje.
- Propojení přes Jablotron PG funguje, takže zvonění pracuje stejně jako dříve.
- Interkom je nasazený a jeho základní integrace je považovaná za dokončenou.

Poslední doložené stavy volání v integraci byly `idle`, `ring` a `onCall`. Home Assistant je může využívat jako stavovou informaci; funkce samotného zvonění není na Home Assistantu závislá.

## Poslední doložené technické údaje

K 2026-07-14 byly v projektových podkladech uvedené:

| Parametr | Hodnota |
|---|---|
| Lokální IP | `192.168.89.45` |
| Firmware | `V2.2.60 build 231204` |
| Stavy volání | `idle`, `ring`, `onCall` |

Současná IP a firmware nejsou potvrzené. **Vyžaduje ověření v živém systému.** Skutečná produkční entity ID stavů volání nejsou v dostupných autoritativních zdrojích uvedená a nesmějí být domyšlená z dřívějších návrhů.

## Provozní princip

```text
Hikvision interkom
→ lokální hovor a vyzvánění
→ stav volání pro Home Assistant
→ Jablotron PG pro domácí gong
```

Home Assistant rozšiřuje stavovou informaci a ovládá vazbu na domácí automatizaci. Nesmí být jedinou podmínkou základního zvonění ani hovoru. Hovor se nepřijímá automaticky.

## Provozní kontrola

Při přejímce ověřit v tomto pořadí:

1. fyzické tlačítko a místní vyzvánění;
2. navázání hovoru a obousměrné audio;
3. stav `idle → ring → onCall → idle` v používané integraci;
4. krátké a správně ukončené sepnutí Jablotron PG;
5. návrat do klidového stavu;
6. případný náhled nebo reakci panelu, pokud je používána.

## Diagnostický runbook

| Projev | Postup |
|---|---|
| Nefunguje hovor ani lokální vyzvánění | Řešit napájení, síť a konfiguraci interkomu. Home Assistant není první místo diagnostiky. |
| Lokální interkom funguje, ale HA nevidí stav | Ověřit dostupnost zařízení, použitou integraci a její logy. Neměnit funkční lokální zvonění. |
| HA vidí `ring`, ale gong nezazvoní | Ověřit stav integrace Jablotronu, PG výstup a automatizaci. Zabránit trvalému sepnutí PG. |
| Gong se spouští opakovaně | Ověřit změny stavů a ochranu proti opakovanému triggeru během jednoho zazvonění. |
| Ozvěna nebo horší audio | Řešit pouze při skutečném provozním dopadu. Zaznamenat výchozí hodnoty a měnit vždy jediný audio parametr nebo jedinou část řetězce. |

Po zásahu se vždy znovu ověří celý řetězec od fyzického tlačítka po lokální gong a hovor.

## Aktualizace a změny

Před změnou firmware interkomu, integrace nebo automatizace:

1. zaznamenat současnou verzi a funkční výchozí stav;
2. ověřit použitelnou zálohu Home Assistantu;
3. bezpečně uložit export nastavení interkomu mimo GitHub, pokud jej zařízení podporuje;
4. měnit pouze jednu vrstvu;
5. provést úplnou provozní kontrolu;
6. při zhoršení obnovit výchozí nastavení nebo verzi podle připraveného návratového postupu.

Hesla, exporty s tajnými hodnotami ani přístupové tokeny do repozitáře nepatří.

## Uzavřená historie

Dříve řešená ozvěna a další drobné nedokonalosti nejsou vedené jako otevřený úkol. Znovu se budou řešit pouze tehdy, pokud budou mít skutečný provozní dopad.

Dřívější návrhy konkrétních entity ID nebyly potvrzené jako produkční a nejsou zdrojem pravdy.

## Hranice dokumentu

Tento dokument popisuje interkom a jeho vazbu na Home Assistant a Jablotron. Stav kamer, NVR a plánovaná migrace kamerového systému na Hikvision jsou shrnuté pouze v [hlavním dokumentu projektu](README.md), protože záznam kamer není funkcí Home Assistantu.
