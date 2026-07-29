# Zálohy MikroTiků

> Poslední doložený stav Mikr Manageru: **2026-07-28**.

## Aktuální stav

- Mikr Manager má povolený export konfigurací ve formátu `.rsc`.
- V Mikr Manageru je vedeno 22 zařízení.
- Poslední doložená cesta exportů je `/opt/mikr/data/exports/<site>/`.
- Není živě ověřená frekvence exportů, poslední úspěšný běh, retence ani druhá kopie.
- Není ověřeno, které exporty jsou skutečně obsažené v persistentních datech a PBS záloze VM510.
- Praktická obnovitelnost uložených exportů zatím nebyla ověřena.

Devadesátidenní retence grafů v Mikr Manageru je retence monitorovacích metrik, nikoli retence záloh konfigurace.

Monitoring a provoz Mikr Manageru jsou popsány v [Monitoring / Mikr](../Monitoring/Mikr.md). Obecná evidence zařízení patří do projektu [Síť](../Sit/MikroTik.md).

## Schválený cílový stav

U důležitých zařízení uchovávat dvě rozdílné formy:

- binární `.backup` pro rychlou obnovu na stejném nebo odpovídajícím modelu a vhodné verzi RouterOS;
- čitelný `.rsc` export pro kontrolu, dokumentaci a přenositelnější obnovu.

Zálohy mají vznikat pravidelně a také jako označený checkpoint po zásadní změně konfigurace. Samotná existence souboru bez kontroly jeho stáří, rozsahu a použitelnosti není dokončená záloha.

Schválený řetězec druhé kopie:

```text
MikroTik
→ Mikr Manager
→ chráněný prostor v Nextcloudu
→ PBS záloha Nextcloudu
```

Případná současná ochrana uvnitř zálohy VM510 je užitečná další vrstva, ale nesmí se považovat za prokázanou, dokud nebudou ověřeny persistentní Docker mounty a testovací restore VM510.

## Bezpečnost a použitelnost

- Exporty a binární backupy se ukládají pouze do chráněného prostoru.
- Je nutné ověřit, jak daná verze RouterOS zachází s citlivými údaji v exportu.
- Obsah `.rsc` ani `.backup` souborů nepatří do GitHubu.
- Binární backup se nepovažuje za univerzálně přenositelný mezi různými modely.
- Textový export se před obnovou kontroluje kvůli názvům rozhraní, MAC adresám, certifikátům, balíčkům a verzím RouterOS.

## Minimální test obnovy

1. Vybrat důležité zařízení a odpovídající náhradní nebo testovací MikroTik.
2. Zaznamenat model, verzi RouterOS, datum backupu a zdroj souboru.
3. Ověřit binární obnovu, pokud je náhradní hardware kompatibilní.
4. Samostatně projít obnovu z `.rsc` a zaznamenat nutné ruční úpravy.
5. Ověřit start, management přístup, základní routing, VLAN nebo bridge a bezpečnostní pravidla bez připojení testovacího zařízení do produkce.
6. Výsledek zapsat bez zveřejnění konfigurace a tajných údajů.

## Otevřené úkoly

- [ ] Ověřit scope 22 zařízení, skutečný rozvrh a poslední úspěšné exporty.
- [ ] Ověřit retenci a přesné persistentní umístění exportů v Mikr Manageru.
- [ ] Ověřit, zda jsou exporty součástí PBS zálohy VM510.
- [ ] Zavést binární `.backup` pro důležitá zařízení a checkpoint po zásadní změně.
- [ ] Zprovoznit chráněnou druhou kopii přes Nextcloud a PBS.
- [ ] Prověřit zacházení s citlivými údaji v používané verzi RouterOS.
- [ ] Prakticky otestovat obnovu na náhradním nebo testovacím MikroTiku.
