# Technologie FVE a BESS

## Potvrzené komponenty

| Systém | Aktuálně známý údaj | Stav údaje |
|---|---|---|
| původní měnič | Deye 50 kW | potvrzeno |
| původní baterie | přibližně 50 kWh | orientačně potvrzeno |
| nová baterie | 215 kWh | kapacita potvrzena |
| nový měnič | Deye; přesný model a výkon neověřen | ověřit |
| hlavní jištění | 3×80 A | evidovaný současný stav |
| limit exportu | 50 kW | potvrzený současný stav |

Starší poznámky uvádějí pro nový měnič rozdílné hodnoty a označení. Dokud nebude přečtený štítek nebo ověřená dokumentace zařízení, nesmí se žádná z variant vydávat za aktuální skutečnost.

## Provozní princip

- Měniče a bateriové systémy musí samostatně dodržovat své ochrany a základní bezpečné limity.
- Home Assistant může měnit provozní režimy a požadované hodnoty, ale nemá být jedinou bezpečnostní vrstvou.
- Exportní řízení se má opírat o měření v hlavním předávacím místě a respektovat společný limit lokality.

## Otevřené ověření

- [ ] Opsat typové štítky obou měničů a bateriových systémů.
- [ ] Získat jednopólové schéma nebo vytvořit ověřený provozní nákres.
- [ ] Ověřit místo a zdroj hlavního měření výkonu.
- [ ] Zapsat komunikační rozhraní a adresy zařízení bez hesel a klíčů.
- [ ] Ověřit chování obou systémů při ztrátě komunikace s Home Assistantem.
