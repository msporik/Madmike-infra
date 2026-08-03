# Zálohy MikroTiků

> Poslední doložený stav Mikr Manageru: **2026-07-28**.

## Účel a hranice

Tento dokument je autoritativní pro vznik, retenci, bezpečné uložení a praktickou obnovitelnost konfigurací MikroTiků. Monitoring a provoz Mikr Manageru jsou v [Monitoring / Mikr](../Monitoring/Mikr.md); topologie a provozní role zařízení patří do jejich síťových projektů.

Export ani binární backup nejsou dokumentace topologie. Jsou to obnovovací materiály, které mohou obsahovat citlivé údaje a zůstávají mimo GitHub.

## Poslední doložený stav

- Mikr Manager má povolený export konfigurací ve formátu `.rsc`.
- V Mikr Manageru je vedeno 22 zařízení.
- Poslední doložená cesta exportů je `/opt/mikr/data/exports/<site>/`.
- Frekvence exportů, poslední úspěšný běh, retence a druhá kopie: **Vyžaduje ověření v živém systému.**
- Zahrnutí exportů do persistentních dat a PBS zálohy VM510: **Vyžaduje ověření v živém systému.**
- Praktická obnovitelnost uložených exportů není doložená a vyžaduje restore test.

Devadesátidenní retence grafů v Mikr Manageru je retence monitorovacích metrik, nikoli retence záloh konfigurace.

## Schválený cílový stav

U důležitých zařízení uchovávat dvě rozdílné formy:

- binární `.backup` pro rychlou obnovu na stejném nebo odpovídajícím modelu a vhodné verzi RouterOS;
- čitelný `.rsc` export pro kontrolu, dokumentaci a přenositelnější obnovu.

Zálohy mají vznikat pravidelně a také jako označený checkpoint před a po zásadní změně konfigurace. Samotná existence souboru bez kontroly jeho stáří, rozsahu a použitelnosti není dokončená záloha.

Schválený řetězec druhé kopie:

```text
MikroTik
→ Mikr Manager
→ chráněný prostor v Nextcloudu
→ PBS záloha Nextcloudu
```

Případná současná ochrana uvnitř zálohy VM510 je užitečná další vrstva, ale nesmí se považovat za prokázanou, dokud nebudou ověřeny persistentní Docker mounty a testovací restore VM510.

## Rozsah ochrany a priorita

Nejdřív se chrání zařízení, jejichž ztráta vyřadí celou lokalitu, správu nebo zásadní datovou cestu. Patří sem zejména hlavní routery, distribuční switche s unikátní konfigurací a zařízení držící WireGuard, DHCP, DNS, firewall, CAPsMAN nebo důležitý bezdrátový spoj.

Úplný živý seznam prioritních zařízení a vlastníků lokalit: **Vyžaduje ověření v živém systému.** Kusová a skladová evidence zůstává v Airtable; zde se vede pouze rozsah zálohování a důkaz obnovitelnosti.

## Bezpečnost a použitelnost

- Exporty a binární backupy se ukládají pouze do chráněného prostoru.
- Je nutné ověřit, jak používaná verze RouterOS a Mikr Manageru zachází s citlivými údaji v exportu.
- Obsah `.rsc` ani `.backup` souborů nepatří do GitHubu, chatu ani běžné přílohy bez ochrany.
- Binární backup se nepovažuje za univerzálně přenositelný mezi různými modely, architekturami nebo verzemi RouterOS.
- Textový export se před obnovou kontroluje kvůli názvům rozhraní, MAC adresám, certifikátům, balíčkům, verzím RouterOS, uživatelům a klíčům.
- Backup nebo export vytvořený po chybné změně nesmí bez označení nahradit poslední známou funkční kopii.
- Přístupové údaje, certifikáty a privátní klíče se obnovují ze svého bezpečného zdroje, ne z GitHubu.

## Evidence každého checkpointu

U důležité zálohy se uchovává alespoň:

- lokalita, identita a model zařízení;
- verze RouterOS a RouterBOARD firmware;
- datum a důvod vytvoření;
- zda jde o `.backup`, `.rsc`, nebo obě formy;
- zda vznikla před změnou, po přejímce změny, nebo automaticky;
- umístění primární a druhé kopie;
- výsledek posledního testu obnovy na kompatibilním hardware.

Do evidence se nepřenáší obsah konfigurace ani tajné hodnoty.

## Běžná provozní kontrola

1. V Mikr Manageru ověřit očekávaný počet spravovaných zařízení a která z nich mají aktuální export.
2. U prioritních zařízení porovnat čas posledního exportu s poslední zásadní změnou a současnou verzí RouterOS.
3. Ověřit, že export není prázdný nebo zjevně neúplný a že je přiřazený správné lokalitě a zařízení.
4. Zkontrolovat retenci tak, aby existovala poslední funkční kopie i označené checkpointy před významnými změnami.
5. Ověřit druhou kopii v chráněném prostoru Nextcloudu a následnou ochranu v PBS snapshotu VM401.
6. Ověřit persistence Mikru podle [VM510 – Docker infrastruktura](../Servery/VM510-Docker.md#persistentní-data-a-obnova).
7. Odchylku řešit jako chybu zálohovacího řetězce; samotná dostupnost zařízení v Mikru nepotvrzuje existenci použitelné zálohy.

Požadovaná frekvence exportu, retence a hranice stáří vyžadující upozornění: **Vyžaduje ověření v živém systému.**

## Checkpoint před změnou

Před zásadní změnou RouterOS, firmware, bridge, VLAN, IP, routingu, firewallu, CAPsMAN nebo WireGuardu:

1. Ověřit živou identitu, model, verzi, roli a dostupnost místního nebo nezávislého přístupu.
2. Zkontrolovat poslední známý funkční `.backup` a `.rsc` a jejich druhou kopii.
3. Vytvořit nový jednoznačně označený předzměnový checkpoint v obou formách, pokud je zařízení podporuje.
4. Připravit konkrétní rollback; vzdálená obnova se nesmí opírat o stejnou cestu, kterou může změna přerušit.
5. Po změně provést provozní přejímku podle autoritativního síťového dokumentu.
6. Teprve po přejímce vytvořit nový označený checkpoint funkčního stavu.

Obecný bezpečný postup změny a rollback jsou v [Síť / MikroTik](../Sit/MikroTik.md#bezpečný-postup-změny).

## Runbook obnovy zařízení

### Příprava

1. Určit skutečnou příčinu výpadku; nejdřív vyloučit napájení, kabel, PoE, nadřazený uplink a poruchu jiné vrstvy.
2. Z autoritativní síťové dokumentace určit roli zařízení a dopad jeho výpadku.
3. Vybrat správný `.backup` a `.rsc` podle identity, modelu, verze, data a posledního funkčního stavu.
4. Připravit kompatibilní náhradní nebo testovací MikroTik podle aktuální evidence v Airtable.
5. Zajistit místní přístup a izolované testovací prostředí; obnova nesmí vytvořit duplicitní IP, DHCP server, CAPsMAN nebo routu v produkci.

### Obnova z binárního `.backup`

1. Použít pouze kompatibilní hardware a vhodnou verzi RouterOS.
2. Obnovu provést mimo produkční síť a po restartu ověřit management přístup.
3. Zkontrolovat rozhraní, bridge, VLAN, IP, DHCP, routing, firewall a služby odpovídající roli zařízení.
4. Ručně vyřešit nepřenositelné nebo změněné části, zejména fyzická rozhraní, MAC adresy, certifikáty, klíče a identity.
5. Pokud kompatibilita není jistá, binární backup nezkoušet opakovaně naslepo; použít kontrolovaný postup z `.rsc`.

### Obnova z textového `.rsc`

1. Export před importem ručně zkontrolovat a odstranit nebo upravit části vázané na původní hardware či starou verzi.
2. Připravit zařízení v čistém a známém výchozím stavu podle konkrétního modelu.
3. Importovat po logických částech, pokud úplný import znemožňuje kontrolu chyb nebo může odříznout správu.
4. Po každé vrstvě ověřit management a odpovídající datovou cestu.
5. Certifikáty, privátní klíče a jiné tajné materiály doplnit pouze ze schváleného bezpečného umístění.

### Přejímka a nasazení

1. Ověřit verzi, identitu, čas, management a systémový log.
2. Podle role otestovat fyzické linky, PoE, bridge/VLAN, DHCP/DNS, routing, NAT, firewall, CAPsMAN a WireGuard.
3. Připojovat produkční větve postupně a po každém kroku ověřit skutečné klienty a závislé služby.
4. Zabránit souběžnému provozu původního a obnoveného routeru se stejnou adresou nebo DHCP rolí.
5. Po úspěšné přejímce vytvořit nový `.backup` a `.rsc`, ověřit druhou kopii a aktualizovat dokumentaci.

## Minimální test obnovy

1. Vybrat jedno prioritní zařízení a odpovídající náhradní nebo testovací MikroTik.
2. Zaznamenat model, verzi RouterOS, datum backupu a zdroj souboru.
3. Ověřit binární obnovu, pokud je náhradní hardware kompatibilní.
4. Samostatně projít obnovu z `.rsc` a zaznamenat nutné ruční úpravy.
5. Ověřit start, management přístup, základní routing, VLAN nebo bridge a bezpečnostní pravidla bez připojení testovacího zařízení do produkce.
6. Výsledek, dobu obnovy a nepřenositelné části zapsat bez zveřejnění konfigurace a tajných údajů.

Jeden úspěšný test neprokazuje obnovitelnost všech modelů. Výsledek se vztahuje pouze na doloženou kombinaci zařízení, RouterOS a použité zálohy.

## Diagnostika

| Projev | První kontrola | Bezpečný další krok |
|---|---|---|
| Mikr nemá nový export | dostupnost zařízení, autentizace, job a persistence | zachovat starší kopii; účet ani šifrovací klíč Mikru neměnit naslepo |
| Export je prázdný nebo neúplný | konkrétní soubor, verze RouterOS a metoda exportu | označit jej jako nepoužitelný a vytvořit nový až po ověření příčiny |
| Export obsahuje citlivé údaje | rozsah exportu a zabezpečení cíle | soubor nepřenášet do GitHubu; ověřit chráněné uložení a přístupová práva |
| Záloha existuje jen ve VM510 | bind mounty, PBS backup VM510 a druhá kopie | nepovažovat ji za offsite ochranu, dokud není prokázaný celý řetězec |
| Import `.rsc` hlásí chyby | první chybový řádek, model, verze a názvy rozhraní | zastavit navazující import, opravit konkrétní nepřenositelné části a znovu ověřit správu |
| Binární restore nenaběhne | kompatibilita modelu a RouterOS | zachovat zdrojový soubor; přejít na řízenou obnovu z `.rsc` |
| Po obnově zmizí vzdálená správa | IP, bridge/VLAN, firewall a WireGuard | použít místní přístup a připravený rollback; nezapínat veřejnou správu jako workaround |
| Po nasazení vznikne konflikt v síti | duplicitní IP, DHCP, CAPsMAN nebo routing | obnovené zařízení okamžitě izolovat a určit jedinou aktivní kopii |

## Handover a odpovědnosti

Před samostatnou obnovou musí být známé:

- autoritativní síťový dokument a role zařízení;
- fyzické umístění, napájení, uplink a místní přístup;
- poslední použitelný `.backup` a `.rsc` a jejich druhá kopie;
- kompatibilní náhradní hardware v Airtable;
- bezpečné umístění přístupových, certifikačních a klíčových materiálů;
- přejímací test konkrétní lokality a osoba oprávněná schválit nasazení.

Vlastníci jednotlivých lokalit, možnost místního zásahu a schvalovací odpovědnosti: **Vyžaduje ověření v živém systému.**

## Otevřené úkoly

- [ ] Ověřit scope 22 zařízení, skutečný rozvrh a poslední úspěšné exporty.
- [ ] Určit prioritní zařízení, vlastníky lokalit a možnost místního zásahu.
- [ ] Ověřit retenci, hranici stáří a přesné persistentní umístění exportů v Mikr Manageru.
- [ ] Ověřit, zda jsou exporty součástí PBS zálohy VM510.
- [ ] Zavést binární `.backup` pro důležitá zařízení a checkpoint před i po zásadní změně.
- [ ] Zprovoznit chráněnou druhou kopii přes Nextcloud a PBS.
- [ ] Prověřit zacházení s citlivými údaji v používané verzi RouterOS a Mikr Manageru.
- [ ] Prakticky otestovat obnovu `.backup` a `.rsc` na náhradním nebo testovacím MikroTiku.
- [ ] Zapsat pro prioritní zařízení datum posledního použitelného checkpointu a restore testu.
