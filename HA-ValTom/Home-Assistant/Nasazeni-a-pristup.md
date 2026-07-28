# Nasazení a vzdálený přístup

## Současný stav

HA Green je připravený, ale ještě není v produkčním provozu u Tomáše. Nachází se u správce a čeká na fyzické nasazení a propojení s místními zařízeními.

Vzdálený přístup byl na připravené instalaci zprovozněný přes Cloudflare Tunnel:

- veřejný název: `valtom.mikehub.cz`;
- externí URL Home Assistantu: `https://valtom.mikehub.cz`;
- řešení nevyžaduje veřejnou IPv4 u Tomáše;
- `valtom.mikehub.cz` je v domácím interním DNS výjimka a nesměřuje na Nginx Proxy Manager.

Pro důvěru k reverzní proxy byla použita konfigurace Home Assistantu s `use_x_forwarded_for: true` a rozsahem `trusted_proxies: 172.30.33.0/24`. Cloudflare token ani jiné tajné hodnoty do repozitáře nepatří.

## Neověřený stav po budoucím přesunu

Po instalaci u Tomáše je nutné znovu ověřit:

1. lokální IP adresu HA Green a její rezervaci;
2. přístup k místním zařízením a GoodWe střídači;
3. funkčnost Cloudflare Tunnelu z nové sítě;
4. správné nastavení interní a externí URL;
5. spolehlivý start po výpadku napájení;
6. aktuálnost a obnovitelnost připravené zálohy.

## WireGuard a místní MikroTik

Instalace MikroTiku nebo WireGuardu u Tomáše byla pouze zvažovaná kvůli plnému servisnímu přístupu do místní sítě. Není doložené, že byla realizovaná. Rozhodnutí se má udělat až podle skutečné potřeby po nasazení HA Green.
