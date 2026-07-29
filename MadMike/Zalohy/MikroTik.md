# Zálohy MikroTiků

## Aktuální stav

- Mikr Manager má povolený export konfigurací ve formátu RSC.
- V Mikr Manageru je vedeno 22 zařízení.
- Praktická obnovitelnost uložených exportů zatím nebyla ověřena.

Monitoring a provoz Mikr Manageru jsou popsány v [Monitoring / Mikr](../Monitoring/Mikr.md). Obecná evidence zařízení patří do projektu [Síť](../Sit/MikroTik.md).

## Požadovaný výsledek

Pro důležitá zařízení má být k dispozici aktuální čitelný export konfigurace, který lze použít při obnově nebo výměně zařízení. Samotná existence souboru bez kontroly jeho obsahu není považovaná za dokončenou zálohu.

## Úkoly k ověření

- [ ] Ověřit, která zařízení se skutečně exportují a jak často.
- [ ] Zkontrolovat retenci a umístění exportů.
- [ ] Ověřit, zda exporty neobsahují tajné hodnoty, které nemají být ukládány mimo chráněné úložiště.
- [ ] Prakticky projít postup obnovy na náhradním nebo testovacím MikroTiku.
- [ ] Rozhodnout, zda mají být exporty dále kopírované do PBS nebo jiného offsite úložiště.
