# Služby a integrace

## Aktuální služby

| Služba nebo integrace | Stav | Role |
|---|---|---|
| Home Assistant | v provozu | automatizace a integrační vrstva |
| InfluxDB | v provozu | dlouhodobá časová data |
| Grafana | v provozu | vizualizace a analýza dat |
| Solarman | v provozu | data a řízení Deye zařízení |

U Deye zařízení jsou historicky evidované přibližně dvě stovky entit na zařízení. Přesný současný počet není provozně důležitý a má se ověřovat pouze při řešení konkrétní integrace.

## Principy

- Home Assistant řídí nadřazenou logiku, ale základní ochrany a bezpečné limity musí zůstat v měničích a dalších koncových zařízeních.
- Pro důležité řízení se preferuje místní komunikace před závislostí na vzdáleném cloudu.
- Historická data mají sloužit k vyhodnocování výsledků řízení, ne jen k vytváření grafů.

## Otevřené úkoly

1. Zapsat skutečné umístění a způsob provozu InfluxDB a Grafany.
2. Ověřit jejich retenci, velikost databází a zálohování.
3. Po přechodu na RS485 porovnat stabilitu a možnosti řízení se současnou integrací.
4. Zdokumentovat pouze ty entity, které jsou skutečně důležité pro automatizace a diagnostiku.
