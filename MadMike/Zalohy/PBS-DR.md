# PBS a disaster recovery

## Aktuální architektura

- Produkční virtuální stroje běží převážně na PVE Ryzen.
- Offsite DR host je PVE Dell.
- Proxmox Backup Server běží na Dellu jako **Dell / VM200**.
- PBS používá datastore `backup`.
- Datová vrstva PBS je vedena na ZFS poolu `tank-pbs` se 4× 8TB SAS disky.
- Propojení lokalit je řešené přes WireGuard.

Podrobnosti fyzických hostů jsou v projektu [Servery](../Servery/README.md). Síťové propojení je popsáno v [WireGuardu](../Servery/WireGuard.md).

## Ověřené testy obnovy

### Nextcloud

- Produkční zdroj: Ryzen / VM401.
- Testovací obnova: Dell / VM402.
- Obnova z PBS byla úspěšná.
- Po spuštění fungovaly Apache, MariaDB, Nextcloud i přístup k datům.

### Windows a PREMIER

- Produkční zdroj: Ryzen / VM501.
- Testovací obnova: Dell / VM501.
- Obnova Windows VM s účetním systémem PREMIER byla úspěšná.

Dell / VM401 je starší migrační test Nextcloudu, nikoli PBS DR obnova. Dell / VM400 má zatím neověřený účel.

## Co zatím není ověřené

- aktuální seznam zálohovaných hostů a VM;
- rozvrhy a retence jednotlivých backup jobů;
- stav a rozvrh Verify;
- pravidla Prune a Garbage Collection;
- pravidelnost budoucích testů obnovy;
- úplnost nativních notifikací PVE a PBS.

Tyto údaje se doplní až po kontrole živé konfigurace.
