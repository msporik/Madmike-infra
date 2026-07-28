# Síť

## Účel

Projekt popisuje samotnou síť MadMike: současné a plánované IP rozsahy, obecnou evidenci MikroTiků, fyzické síťové role a budoucí sjednocování lokalit.

Serverové přístupové služby zůstávají v projektu [Servery](../Servery/README.md):

- interní DNS, Nginx Proxy Manager a HTTPS;
- WireGuard propojení používaná pro přístup k serverům.

Mikr Manager jako monitorovací nástroj zůstává v projektu [Monitoring](../Monitoring/Mikr.md).

## Dokumenty

- [Adresní plán](Adresni-plan.md) – současné známé rozsahy a předběžný návrh sjednocení.
- [MikroTik](MikroTik.md) – role aktivních a rezervních MikroTik zařízení.

## Zásady

- Současný stav a budoucí adresní plán se nesmí směšovat.
- Nová IP adresa se neoznačí jako přidělená, dokud není ověřena v živé konfiguraci.
- Přesné interní IP adresy a směrování mohou být v tomto soukromém repozitáři evidované.
- Hesla, tokeny, privátní klíče a preshared keys do repozitáře nepatří.
