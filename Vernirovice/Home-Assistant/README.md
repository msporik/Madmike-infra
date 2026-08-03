# Home Assistant – Vernířovice

## Účel

Lokální řídicí a integrační vrstva pro FVE, baterie, energetické automatizace a další technologie ve Vernířovicích. Preferovaný směr je spolehlivé místní řízení s omezenou závislostí na cloudu.

## Poslední doložený provozní stav

- Produkční Home Assistant běží na Raspberry Pi 5.
- InfluxDB, Grafana a MQTT broker běží jako add-ony stejné instalace Home Assistant OS na Raspberry Pi 5.
- Home Assistant získává data z Deye zařízení přes integraci Solarman. Žádná lokální RS485/Modbus komunikace dnes není funkční.
- Automatizace vybíjení baterie během dvou nejdražších hodin funguje; její logika je popsána v [Řízení energie](../BESS-a-FVE/Rizeni-energie.md).
- Home Assistant Cloud byl pro tuto instanci potvrzen 21. 7. 2026.

## Schválený cílový stav

- Přesunout Home Assistant z Raspberry Pi 5 na připravený Qotom N100.
- Na Qotomu provozovat Home Assistant OS přímo na hardware.
- Zachovat Raspberry Pi 5 jako dočasnou návratovou variantu, dokud nebude migrace prakticky ověřená.
- Lokální RS485/Modbus zavádět až jako samostatně připravenou a otestovanou změnu tam, kde bude spolehlivější a lépe kontrolovatelná než současný Solarman.

## Hranice projektu

- Technologie měničů, baterií, exportní limit, bezpečnostní limity a algoritmus řízení jsou autoritativně vedené v [BESS a FVE](../BESS-a-FVE/README.md).
- Společná strategie záloh, retence, druhé kopie a restore testy jsou v [Zálohách Home Assistantu](../../MadMike/Zalohy/Home-Assistant.md).
- Síťová topologie, DHCP, VLAN a adresní plán patří do [MadMike / Síť](../../MadMike/Sit/README.md).
- Centrální dohled a notifikace patří do [MadMike / Monitoring](../../MadMike/Monitoring/README.md).
- Účty, MFA a recovery patří do [MadMike / Přístupy](../../MadMike/Pristupy/README.md).

## Podrobnosti

- [Hardware a migrace](Hardware-a-migrace.md)
- [Služby a integrace](Sluzby-a-integrace.md)
- [BESS a FVE](../BESS-a-FVE/README.md)
- [Společná strategie záloh Home Assistantu](../../MadMike/Zalohy/Home-Assistant.md)

## Navazující práce

Otevřené kroky jsou vedené jen v příslušných autoritativních dokumentech:

- backup, retence a praktický restore v [Zálohách Home Assistantu](../../MadMike/Zalohy/Home-Assistant.md);
- příprava, provedení a přejímka migrace v [Hardware a migrace](Hardware-a-migrace.md);
- lokální a vzdálený přístup, integrace a společný monitoring ve [Službách a integracích](Sluzby-a-integrace.md).
