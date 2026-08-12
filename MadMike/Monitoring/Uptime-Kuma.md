# Uptime Kuma

> Poslední souhrnný provozní stav: **2026-07-28**. Notifikační cesta Uptime Kuma → Pushover byla dílčím živým testem ověřena **2026-08-12**.

## Účel a role

Uptime Kuma hlídá dostupnost důležitých služeb a oznamuje jejich následný návrat do provozu.

Nemá suplovat:

- detailní stav PVE a PBS;
- ZFS, SMART a zálohovací úlohy;
- metriky a správu MikroTiků;
- aplikační diagnostiku cílových služeb.

Docker nasazení, port, kontejner a persistentní data jsou autoritativně vedené v [VM510 – Docker infrastruktura](../Servery/VM510-Docker.md). HTTPS směrování je v [Interní DNS, NPM a HTTPS](../Servery/DNS-NPM-HTTPS.md).

Běžný přístup: `https://kuma.mikehub.cz`

Nouzový přímý test z interní sítě: `http://192.168.89.35:3001`

## Poslední doložený stav

K 2026-07-28:

- Uptime Kuma běžela na VM510;
- používala samostatný Docker kontejner, nikoliv Compose projekt;
- kontejner se jmenoval `uptime-kuma`;
- aplikační data byla uložená v Docker volume `uptime-kuma`;
- přístup přes interní HTTPS fungoval;
- přesná verze a živý seznam monitorů nebyly ověřeny;
- původně navržené Telegram notifikace nebyly realizovány a tento návrh byl následně opuštěn.

## Ověřená notifikační cesta

Dne 2026-08-12 byla prakticky ověřena cesta `Uptime Kuma → Pushover → Samsung S22`:

- v Kumě vznikl notifikační cíl `Pushover – Kuma`;
- vestavěné tlačítko **Test** úspěšně doručilo zprávu do telefonu;
- dočasný Push monitor bezpečně vyvolal skutečný stav `DOWN` a následný `UP` bez zastavení produkční služby;
- dorazila právě jedna notifikace `DOWN` a jedna odpovídající notifikace `UP`;
- dočasný monitor byl po testu odstraněn;
- notifikační cíl není nastavený jako výchozí pro všechny existující monitory;
- zatím není přiřazený žádnému produkčnímu monitoru.

User Key a Application Token jsou uložené v Bitwardenu a jejich hodnoty se nezapisují do GitHubu ani chatu. Původní Application Token zachycený při nastavování na screenshotu byl resetován; platný token zůstává pouze v Bitwardenu.

Tento test potvrzuje funkci doručovací cesty, nikoliv současný živý seznam produkčních monitorů ani jejich provozní parametry.

## Schválené chování monitorů

- Sledují se klíčové služby, nikoliv každý technický port.
- Krátké zakolísání se může uložit do historie, ale nemá okamžitě vytvářet alarm.
- Výchozí zpoždění alarmu má být přibližně pět minut.
- Podle významu a běžného chování služby lze zpoždění upravit individuálně.
- Po trvající nedostupnosti se odešle `DOWN`.
- Po obnovení stejné služby se odešle odpovídající `UP` nebo recovery zpráva.
- U jednotlivých MikroTiků a lokalit se bezdůvodně neduplikuje Mikr Manager.

Schválený minimální rozsah zahrnuje:

- PVE Ryzen;
- VM510;
- Pulse;
- PBS;
- Nextcloud.

Doplňkově lze sledovat Mikr Manager, Nginx Proxy Manager a další interně publikované služby, pokud monitor přinese jasnou provozní hodnotu.

## Historický výchozí seznam

Při původním nasazení byly doloženy tyto monitory:

| Původní monitor | Adresa |
|---|---|
| PVE Ryzen | `192.168.89.32` |
| Nextcloud VM401 | `192.168.89.33` |
| Windows VM501 | `192.168.89.34` |
| PBS DR | `192.168.100.12` |

Tento seznam je historický výchozí bod, nikoliv tvrzení o současné konfiguraci.

U Windows VM501 bylo doporučeno použít TCP kontrolu portu `3389` místo ICMP, protože Windows Firewall neodpovídal na ping.

## Provozní kontrola

Na VM510:

```bash
sudo docker ps --filter name=uptime-kuma
sudo docker logs --tail=100 uptime-kuma
```

Při potřebě podrobnější kontroly:

```bash
sudo docker inspect uptime-kuma
```

Výstup `docker inspect` může obsahovat neveřejnou konfiguraci a nekopíruje se neupravený do GitHubu ani chatu.

Interpretace:

- pokud funguje přímý port, ale ne `https://kuma.mikehub.cz`, pokračovat podle dokumentu [DNS, NPM a HTTPS](../Servery/DNS-NPM-HTTPS.md);
- pokud nefunguje ani port `3001`, zkontrolovat kontejner, Docker a VM510;
- pokud Kuma funguje, ale jeden monitor hlásí `DOWN`, ověřit cílovou službu z pohledu VM510;
- pokud je nedostupná celá vzdálená lokalita, ověřit nejdříve WAN, WireGuard, napájení a hlavní router.

## Restart služby

```bash
sudo docker restart uptime-kuma
sudo docker ps --filter name=uptime-kuma
sudo docker logs --tail=100 uptime-kuma
```

Po restartu ověřit:

1. přihlášení do webového rozhraní;
2. načtení monitorů;
3. zachování jejich historie;
4. stav vybraných dostupných služeb;
5. funkci notifikačních cílů, pokud jsou nastavené.

## Ochrana dat a aktualizace

Před změnou image, odstraněním kontejneru nebo případnou migrací na Compose se ověří:

- použitelná záloha VM510;
- skutečné připojení persistentního volume;
- současný image a startovací parametry;
- návratový postup.

Nepoužívají se příkazy:

```text
docker rm -v
docker volume rm uptime-kuma
```

Hromadné čištění nepoužívaných volumes se neprovádí bez předchozí identifikace jejich obsahu.

Před odstraněním starého kontejneru musí být potvrzeno, že nový kontejner používá stejné persistentní úložiště. Uptime Kuma se nemigruje na Compose pouze kvůli sjednocení vzhledu nasazení.

## Obnova služby

Pokud Kuma nefunguje, dostupnost infrastruktury se dočasně ověřuje přímo v jednotlivých systémech. Její výpadek nemění stav sledovaných služeb.

Obnova kontejneru a celé VM510 se řídí:

- [VM510 – Docker infrastruktura](../Servery/VM510-Docker.md);
- [PBS a disaster recovery](../Zalohy/PBS-DR.md).

Po obnově se kontroluje nejen start webu, ale také monitory, historie, notifikační cíle a praktický test `DOWN` i recovery.

## Otevřené úkoly

> Následující body vyžadují ověření v živém systému.

- [ ] Ověřit současnou verzi, image a přesné startovací parametry kontejneru.
- [ ] Porovnat živý seznam monitorů s historickým a schváleným rozsahem.
- [ ] Ověřit typy kontrol, intervaly, retries, timeouty a skutečná zpoždění alarmů.
- [ ] Vybrat produkční monitory, které mají používat `Pushover – Kuma`, přiřadit cíl jednotlivě a ověřit, že nevznikají duplicity.
- [ ] Zdokumentovat samostatnou zálohu a obnovu konfigurace Kumy, pokud existuje.

Směrování vybraných alarmů a recovery zpráv patří do [Pushover notifikací](Pushover.md).
