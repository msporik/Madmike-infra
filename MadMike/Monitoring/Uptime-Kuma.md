# Uptime Kuma

## Role

Uptime Kuma hlídá dostupnost služeb a oznamuje jejich následný návrat do provozu. Nemá suplovat detailní stav Proxmoxu, PBS nebo MikroTiků.

## Poslední doložený stav k 2026-07-28

- Služba běžela na monitorovací VM510.
- Webové rozhraní bylo dostupné na `https://kuma.mikehub.cz`.
- HTTPS přístup vedl přes Nginx Proxy Manager.
- Přesná verze a živý seznam monitorů nebyly při konsolidaci ověřeny.
- Konečný seznam monitorů nebyl uzavřený.

DNS, Nginx Proxy Manager, HTTPS a WireGuard jsou popsány v projektu [Servery](../Servery/DNS-NPM-HTTPS.md).

## Schválené chování

- Kuma hlídá dostupnost klíčových služeb, nikoliv každý technický detail.
- Výchozí zpoždění alarmu má být přibližně 5 minut, aby krátký výpadek nevytvářel zbytečný hluk.
- Podle významu a běžného chování konkrétní služby lze zpoždění nastavit individuálně.
- Po trvající nedostupnosti se odešle stav `DOWN`.
- Po obnovení stejné služby se odešle odpovídající `UP` / recovery zpráva.
- Historický seznam monitorů se nepovažuje za současný stav, dokud nebude porovnán s živou konfigurací.

## Zamýšlené pokrytí

- klíčová webová rozhraní a služby publikované přes Nginx Proxy Manager;
- důležité služby dosažitelné přes WireGuard;
- delší nedostupnost služby;
- následné obnovení služby.

Konkrétní monitory a jejich časové podmínky se zapíší až po praktickém nastavení a ověření.

## Navazující práce

- [ ] Aktualizovat Uptime Kuma na aktuální stabilní verzi.
- [ ] Projít existující monitory proti živé konfiguraci.
- [ ] Stanovit seznam kritických a doplňkových služeb.
- [ ] Nastavit přibližně pětiminutové výchozí zpoždění a individuální výjimky.

Připojení vybraných alarmů a návratů do normálu je vedené v [Telegram notifikacích](Telegram.md).
