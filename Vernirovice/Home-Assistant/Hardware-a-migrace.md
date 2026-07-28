# Hardware a migrace

## Současný stav

- Produkční Home Assistant běží na Raspberry Pi 5.
- Migrace zatím nebyla provedena.

## Připravený cílový hardware

| Součást | Stav | Známý údaj |
|---|---|---|
| zařízení | připraveno | fanless Qotom s Intel N100 |
| operační paměť | potvrzeno | 16 GB DDR5 |
| systémový disk | potvrzeno | Micron NVMe 512 GB |
| průmyslová komunikace | zamýšleno | lokální RS485/Modbus |

Qotom má převzít roli hlavního lokálního uzlu pro Home Assistant a energetické automatizace.

## Požadavky na migraci

- před migrací vytvořit ověřenou zálohu současného Home Assistantu;
- zachovat Raspberry Pi jako dočasnou návratovou variantu;
- po obnově ověřit integrace, automatizace, databázi historie a připojení k měničům;
- migraci nepovažovat za dokončenou, dokud neproběhne praktický provozní test.

## Otevřené úkoly

1. Zvolit konkrétní způsob instalace Home Assistantu na Qotom.
2. Zjistit, zda všechny potřebné RS485 porty a převodníky jsou fyzicky připravené.
3. Připravit kontrolní seznam migrace a návratu.
4. Určit způsob zálohování Qotomu a obnovy na náhradní hardware.
