# Uptime Kuma

## Role

Uptime Kuma hlídá dostupnost služeb a oznamuje jejich návrat do provozu. Nemá suplovat detailní stav Proxmoxu, PBS nebo MikroTiků.

## Ověřený stav k 2026-07-28

- Služba běží na monitorovací VM.
- Webové rozhraní je dostupné na `https://kuma.mikehub.cz`.
- Přístup vede přes Nginx Proxy Manager.
- Konečný seznam monitorů zatím není uzavřený.

## Zamýšlené pokrytí

- klíčová webová rozhraní a služby publikované přes Nginx Proxy Manager;
- důležité služby dosažitelné přes WireGuard;
- delší nedostupnost služby;
- následné obnovení služby.

Konkrétní monitory a časové podmínky se zapíší až po praktickém nastavení a ověření.

## Navazující práce

1. Aktualizovat Uptime Kuma na aktuální stabilní verzi.
2. Projít existující monitory.
3. Stanovit seznam kritických a doplňkových služeb.
4. Nastavit rozumné zpoždění, aby krátký výpadek nevytvářel zbytečný alarm.
5. Připojit vybrané alarmy a návraty do normálu do Telegramu.
