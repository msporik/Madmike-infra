# Služby a integrace

## Účel a hranice

Dokument popisuje služby, add-ony a integrační vazby produkční instance Home Assistantu ve Vernířovicích a jejich běžnou kontrolu a diagnostiku. Technologie měničů, baterií, limity lokality a algoritmus energetického řízení jsou autoritativně vedené v projektu [BESS a FVE](../BESS-a-FVE/README.md).

Úplný seznam entit, dynamická konfigurace, databáze a tajné hodnoty zůstávají v živém systému. Zde se evidují jen stabilní provozní role, závislosti a rozhraní důležitá pro převzetí správy.

## Poslední doložený provozní stav

> Stav byl konsolidován při auditu 2. 8. 2026. Živá konfigurace nebyla při auditu otevřena. Položka označená jako aktivní podle staršího podkladu musí být před rizikovou změnou potvrzena read-only kontrolou.

Produkční instance běží na Raspberry Pi 5 jako Home Assistant OS. Ve stejné instalaci jsou doložené tyto add-ony:

- InfluxDB – dlouhodobější časová data;
- Grafana – vizualizace a analýza dat;
- MQTT broker – lokální komunikační služba;
- Studio Code Server – správa konfigurace.

## Přehled služeb a integrací

| Služba nebo integrace | Poslední doložený stav | Provozní role | Hlavní závislost |
|---|---|---|---|
| Home Assistant | v provozu | automatizace a integrační vrstva | hostitel, síť, úložiště |
| InfluxDB | add-on HA OS | dlouhodobější časová data | hostitel, úložiště, zdroje dat |
| Grafana | add-on HA OS | vizualizace a analýza | InfluxDB nebo jiné nakonfigurované zdroje |
| MQTT broker | add-on HA OS | lokální komunikační vrstva | hostitel, síť, klientské konfigurace |
| Solarman | v provozu | data z Deye a vazba současné energetické automatizace | logger, síť, profil registrů |
| HACS | dříve doloženo jako aktivní | doplňkové integrace | GitHub/internet při instalaci a aktualizaci |
| Honeywell Total Connect Comfort | dříve doloženo jako aktivní | termostaty a topné zóny | cloudová služba a internet |
| Shelly | dříve doloženo jako aktivní | lokální měření a spínání | LAN/IoT síť a jednotlivá zařízení |
| Tasmota | dříve doloženo jako aktivní | lokální zařízení | zpravidla MQTT a LAN |
| Spotové ceny energií ČR | dříve doloženo jako aktivní | cenový vstup automatizací | externí data a správný čas |
| Studio Code Server | dříve doloženo jako aktivní add-on | správa konfigurace | Supervisor, úložiště |

Aktuální verze, přesné datové toky, retence, velikosti databází a skutečný seznam aktivních klientů nejsou autoritativně doloženy. **Vyžaduje ověření v živém systému.**

## Závislostní řetězce

### Energetická automatizace původní sestavy

1. externí cenový zdroj dodá aktuální cenová data;
2. Solarman poskytne SOC a stav původní Deye sestavy;
3. Home Assistant vyhodnotí podmínky automatizace;
4. integrační služba odešle požadavek na změnu režimu;
5. skutečný stav zařízení musí potvrdit, že byl povel přijat.

Přesná implementace posledního ověření a chování při chybě nejsou doloženy. Podrobnosti patří do [Řízení energie](../BESS-a-FVE/Rizeni-energie.md).

### Historie a vizualizace

1. integrace vytvoří entity a stavová data;
2. Home Assistant a InfluxDB ukládají data podle své konfigurace;
3. Grafana čte nakonfigurované zdroje;
4. dashboard je použitelný jen tehdy, pokud je čerstvý zdroj i databáze.

Běžící Grafana sama nepotvrzuje, že jsou data aktuální. Kontrolovat čas posledního bodu a porovnat jej se stavem entity v Home Assistantu.

### MQTT

MQTT broker je sdílená závislost zařízení a integrací, které MQTT skutečně používají. Jeho klienti, topic struktura, discovery, autentizace a zálohování nejsou doloženy. **Vyžaduje ověření v živém systému.**

## Solarman a Deye

- Současná komunikace Home Assistantu s Deye zařízeními probíhá přes Solarman.
- Žádná lokální RS485/Modbus komunikace není doložena jako funkční.
- Původní sestava je přes současnou integraci monitorována a řízena automatizací dvou nejdražších hodin.
- Větší sestava je v Home Assistantu přidána, ale problém komunikace baterie–střídač řeší dodavatel; existence entit nepotvrzuje plnou funkčnost.
- Historicky bylo evidováno přibližně dvě stě entit na zařízení. Tento počet není provozní údaj; dokumentovat se mají pouze entity použité v automatizacích, řízení a diagnostice.
- Historické podklady uvádějí profil `auto`. Správnost mapy, škál, znamének a všech významných hodnot je nutné ověřit proti skutečnému zařízení.

Při změně profilu, integrace nebo komunikační cesty porovnat minimálně PV výkon, síťový tok, výkon baterie, SOC, pracovní režim, exportní stav, energie, alarmy a teploty. Změnu profilu neprovádět jen kvůli počtu entit.

## InfluxDB a Grafana

InfluxDB a Grafana jsou doložené jako add-ony stejné instalace Home Assistant OS na Raspberry Pi 5. Z toho plyne, že výpadek hostitele nebo jeho úložiště může zasáhnout zároveň Home Assistant, historii i vizualizaci.

Při kontrole ověřit:

- oba add-ony běží bez opakovaných pádů;
- Grafana se připojí ke správnému zdroji;
- čas posledního bodu odpovídá současnému provozu;
- zapisují se pouze potřebná data;
- retence a velikost databáze odpovídají volnému místu;
- záloha skutečně chrání konfiguraci i potřebná data;
- existuje postup obnovy a byl prakticky ověřen.

Retence, velikost databáze, konkrétní buckets/databáze, hlavní dashboardy a rozsah zálohy nejsou doloženy. **Vyžaduje ověření v živém systému.**

## Síť, IoT a přístup

- IP adresy byly naposledy evidovány jako přidělované přes DHCP se statickými leases.
- Vedle běžné Wi-Fi byla evidována samostatná IoT síť `IOTVL` s vlastním rozsahem.
- Současný stav `IOTVL`, její rozsah, firewallová pravidla a vazba zařízení na ni nejsou potvrzeny. **Vyžaduje ověření v živém systému.**
- Zigbee byl v posledním souhrnném checkpointu pouze plánovaný a nesmí se označit jako aktivní bez živého ověření.
- Home Assistant Cloud byl potvrzen 21. 7. 2026. Současná lokální a vzdálená URL, role cloudového přístupu a případná záložní cesta nejsou doloženy.
- Obecná inventura MikroTiků zůstává v [MadMike / Síť / MikroTik](../../MadMike/Sit/MikroTik.md).

## Běžná provozní kontrola

### Home Assistant a Supervisor

- instance je dostupná lokálně;
- systémový čas je správný;
- Supervisor a Core nevykazují nevyřešenou chybu;
- volné místo je dostatečné;
- nejsou čekající opravy nebo opakované restarty add-onů.

### Datové služby

- InfluxDB přijímá nové body;
- hlavní Grafana dashboardy zobrazují čerstvá data;
- MQTT broker běží a očekávaní klienti jsou připojeni;
- databáze nebo protokoly nekontrolovaně nezaplňují úložiště.

### Integrace

- Solarman aktualizuje klíčové hodnoty v očekávaném intervalu;
- nejsou nové chyby mapy, autentizace nebo komunikace;
- cenový vstup obsahuje dnešní data a odpovídá správnému časovému pásmu;
- klíčová měření Shelly nejsou nedostupná;
- cloudové integrace nevykazují dlouhodobou chybu.

Přesné intervaly, prahy a seznam kritických entit musí vzniknout z živé inventury. **Vyžaduje ověření v živém systému.**

## Diagnostický runbook

### Entita je `unknown`, `unavailable` nebo se neaktualizuje

1. Určit, zda jde o jednu entitu, celé zařízení, integraci nebo síťovou vrstvu.
2. Porovnat čas poslední změny s jinými entitami stejného zařízení.
3. Ověřit dostupnost zařízení nebo loggeru bez změny konfigurace.
4. Zkontrolovat protokol pouze dotčené integrace a poslední známou funkční událost.
5. U Solarmanu porovnat klíčové hodnoty se stavem zařízení nebo jiným nezávislým měřením.
6. Neprovádět zápis ani změnu profilu, dokud není potvrzen správný model a mapa.
7. Po nápravě ověřit, že se obnovil datový tok a automatizace neprovedla opožděnou nežádoucí akci.

### Grafana zobrazuje stará nebo prázdná data

1. Ověřit aktuálnost zdrojové entity v Home Assistantu.
2. Ověřit běh a volné místo InfluxDB.
3. Ověřit, zda do databáze přibývají body.
4. Ověřit datový zdroj, časový rozsah a časové pásmo dashboardu.
5. Neprovádět purge ani změnu retence před zálohou a určením příčiny.

### MQTT zařízení zmizela

1. Ověřit běh brokeru a stav hostitele.
2. Ověřit síťovou dostupnost a čas posledního spojení klienta.
3. Rozlišit problém jednoho klienta od výpadku brokeru nebo IoT sítě.
4. Neměnit hromadně přihlašovací údaje, discovery ani topic strukturu během incidentu.
5. Po obnovení ověřit stav zařízení a možné opožděné příkazy.

### Cenová data chybí

1. Zabránit tomu, aby automatizace použila starou cenu jako dnešní vstup.
2. Ověřit datum, časové pásmo a platnost dat.
3. Ověřit stav poskytovatele a integrace.
4. Energetika musí přejít do určeného konzervativního režimu. Jeho přesné provedení není zdokumentováno. **Vyžaduje ověření v živém systému.**

### Home Assistant nebo integrace byla restartována během řízení

1. Neobnovovat předchozí výkonový stav jen podle posledního interního stavu HA.
2. Načíst skutečný režim měniče, exportní stav, SOC a dostupnost měření.
3. Ověřit platnost cenového okna a ručních zásahů.
4. Povolit automatiku až po splnění všech vstupních podmínek.

## Změny a aktualizace

Před aktualizací add-onu, HACS komponenty nebo integrace:

1. zaznamenat současnou verzi, stav a závislé automatizace;
2. přečíst poznámky k verzi a změny konfigurace nebo entit;
3. ověřit aktuální zálohu;
4. určit návratovou verzi nebo postup obnovy;
5. měnit pouze jednu logickou vrstvu;
6. po změně ověřit data, logy, závislé automatizace a dashboardy;
7. u integrační změny nejdřív potvrdit čtení, teprve potom případné zápisy.

Ruční aktualizace závislostí uvnitř spravovaného add-onu nebo HACS komponenty bez dokumentovaného důvodu není doporučený provozní postup.

## Monitoring a notifikace

Minimálně má být sledováno:

- dostupnost Home Assistantu;
- dostupnost produkčního hostitele;
- stáří poslední úspěšné zálohy;
- nedostupnost kritického datového toku Solarman;
- selhání cenového vstupu;
- dlouhodobě neaktualizující se hlavní měření;
- závažné alarmy měniče nebo baterie, pokud jsou spolehlivě dostupné;
- automatizace ponechaná v neočekávaném režimu.

Konkrétní monitory a notifikační cesty nebyly živě ověřeny. **Vyžaduje ověření v živém systému.** Společný model je v [MadMike / Monitoring](../../MadMike/Monitoring/README.md) a [Telegramu](../../MadMike/Monitoring/Telegram.md).

## Otevřené úkoly

- [ ] Ověřit živý seznam aktivních integrací, add-onů, jejich verze a provozní vlastníky.
- [ ] Ověřit konfiguraci, retenci, velikost databází, hlavní Grafana dashboardy a obnovitelnost dat InfluxDB/Grafany.
- [ ] Ověřit účel, klienty, autentizaci a zálohování MQTT brokeru bez uložení tajných údajů do dokumentace.
- [ ] Ověřit přesný stav klíčových entit a ovládání původní i větší bateriové sestavy.
- [ ] Ověřit `IOTVL`, současný lokální a vzdálený přístup a zapojení instance do společného monitoringu.
- [ ] Před zavedením RS485/Modbus připravit samostatný read-only test, přejímací kritéria a rollback.
- [ ] Zapsat pouze stabilní entity skutečně důležité pro automatizace, řízení a diagnostiku.
