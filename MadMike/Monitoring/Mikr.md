# Mikr Manager

> Poslední doložený provozní stav: **2026-07-28**. Nejde o potvrzení současného živého stavu.

## Účel a role

Mikr Manager poskytuje přehled stavu MikroTik zařízení a lokalit, historii provozních hodnot a výběr alarmů, které skutečně vyžadují pozornost.

Není autoritativní dokumentací síťové topologie ani úplným zálohovacím systémem:

- inventura, topologie a RouterOS patří do [dokumentace MikroTik sítě](../Sit/MikroTik.md);
- exporty konfigurací, retence a test obnovy patří do [záloh MikroTiků](../Zalohy/MikroTik.md);
- Docker nasazení, porty a sítě jsou v [VM510 – Docker infrastruktura](../Servery/VM510-Docker.md).

Běžný přístup: `https://mikr.mikehub.cz`

## Poslední doložený stav

K 2026-07-28:

- evidováno 22 zařízení;
- licence pro 50 zařízení;
- interval grafů 5 minut;
- retence historie 90 dní;
- export konfigurací RSC byl povolený;
- kontejner byl připojený do aplikační sítě i do `npm_default`;
- přístup přes interní HTTPS fungoval.

Povolený RSC export sám o sobě nepotvrzuje, že exporty pravidelně vznikají nebo že z nich lze zařízení obnovit.

## Rozsah sledování

Mikr je vhodný pro sledování:

- dostupnosti zařízení;
- uptime a restartu zařízení;
- CPU a RAM;
- zaplnění úložiště;
- teploty, pokud ji zařízení poskytuje;
- stavu nebo vytížení vybraných kritických linek;
- napětí pouze tam, kde má praktický provozní význam;
- výpadku významného routeru nebo celé lokality.

Konkrétní prahy a zpoždění se považují za platné až po jejich nastavení a praktickém ověření. Alarmy se nezapínají bez rozmyslu na všech zařízeních; běžné provozní změny, krátké výkyvy a nekritická zařízení nemají vytvářet notifikační šum.

## Interpretace nedostupnosti

Nedostupnost zařízení v Mikru nemusí znamenat poruchu samotného Mikr Manageru.

| Stav | První kontrola |
|---|---|
| Jedno zařízení je nedostupné | napájení, RouterOS, síťová cesta a konkrétní zařízení |
| Více zařízení jedné lokality je nedostupných | hlavní router, WAN, WireGuard nebo napájení lokality |
| Všechna zařízení chybějí | Mikr kontejner, VM510 a síťové propojení |
| Mikr i Kuma hlásí stejnou lokalitu | určit jednu hlavní událost a neposílat duplicity |

Podle samotného alarmu se automaticky nemění konfigurace MikroTiku.

## Provozní kontrola

Na VM510 přejít do Compose projektu Mikr uvedeného v [VM510 – Docker infrastruktura](../Servery/VM510-Docker.md) a spustit:

```bash
sudo docker compose config --quiet
sudo docker compose ps
sudo docker compose logs --tail=100
```

V aplikaci ověřit:

1. přihlášení přes `https://mikr.mikehub.cz`;
2. načtení seznamu zařízení;
3. dostupnost očekávaných lokalit;
4. aktuální grafy;
5. licenční stav;
6. stav exportů konfigurací.

## Restart služby

V Compose projektu Mikr:

```bash
sudo docker compose restart
sudo docker compose ps
sudo docker compose logs --tail=100
```

Po restartu provést [provozní kontrolu](#provozní-kontrola). Nestačí ověřit pouze web; musí se načíst zařízení a nová provozní data.

Při problému jedné aplikace se bezdůvodně nerestartuje celá VM510 ani ostatní kontejnery.

## Aktualizace

Před aktualizací:

1. ověřit použitelnou zálohu VM510;
2. zaznamenat běžící image a verzi aplikace;
3. zkontrolovat dostupnost zařízení a poslední grafy;
4. ověřit, že případný problém lokality nebyl přítomný už před aktualizací.

V Compose projektu Mikr:

```bash
sudo docker compose config --quiet
sudo docker compose pull
sudo docker compose up -d
sudo docker compose ps
sudo docker compose logs --tail=100
```

Po aktualizaci provést [provozní kontrolu](#provozní-kontrola). Při chybě se jako první pokus o opravu nemažou persistentní data ani exporty konfigurací.

## Obnova služby

Pokud Mikr nefunguje, jednotlivé MikroTiky se dál spravují přímo přes RouterOS. Výpadek Mikru proto neznamená automaticky výpadek sítě.

Obnova kontejneru a VM510 se řídí dokumenty:

- [VM510 – Docker infrastruktura](../Servery/VM510-Docker.md);
- [PBS a disaster recovery](../Zalohy/PBS-DR.md).

Po obnově provést [provozní kontrolu](#provozní-kontrola) a navíc ověřit:

- komunikaci s několika zařízeními z různých lokalit;
- pokračování grafů;
- existenci exportů konfigurací;
- aktivní alarmy a jejich notifikační cíle.

## Otevřené úkoly

> Následující body vyžadují ověření v živém systému.

- [ ] Ověřit současnou verzi, image, počet zařízení, licenci, interval grafů a retenci.
- [ ] Určit kritická zařízení a lokality.
- [ ] Ověřit současné alarmy, jejich prahy, zpoždění a recovery chování.
- [ ] Ověřit, že RSC exporty pravidelně vznikají a kde jsou persistentně uložené.
- [ ] Ověřit, které události už spolehlivěji pokrývá Uptime Kuma.

Praktická obnova konfigurace na náhradním MikroTiku je vedena výhradně v [zálohách MikroTiků](../Zalohy/MikroTik.md). Připojení neduplicitních alarmů patří do [Pushover notifikací](Pushover.md).
