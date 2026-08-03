# Hardware

> Poslední doložený stav a schválená rozhodnutí: **2026-07-29**. Nejde o potvrzení současného živého stavu ani o kusovou skladovou kartu.

## Autorita a práce s evidencí

Tento dokument eviduje role zařízení specifické pro Rybníky, doložené modely a podmínky výběru. Aktuální počet kusů, MAC adresy, fyzický stav a rezervace zůstávají výhradně v Airtable.

Před nasazením se vždy ověří, že konkrétní kus:

- je stále skladem a není rezervovaný jinému projektu;
- odpovídá přesnému modelu a potřebné revizi;
- má ověřené napájení, porty a příslušenství;
- projde základním testem a má připravený backup původního stavu;
- je v Airtable označený jako přidělený až po skutečné rezervaci.

## Naposledy doložené zařízení

| Role | Zařízení | Stav / poznámka |
|---|---|---|
| vysílací strana přívodu | kvalitnější 5GHz sektor `AP HOME` | aktivní náhrada původní jednotky; sdílený sektorový/PtMP provoz, přesný model a konfiguraci ověřit |
| přijímací strana přívodu | stávající přijímací jednotka | zůstala beze změny; přesný model a režim ověřit |
| historicky doložený Sextant | RB711G-5HnD / Sextant G | RouterOS `6.49.19`, 32 MB RAM; dnešní roli potvrdit a stabilní kus nepřevádět bez důvodu na ROS 7 |
| místní core | historicky RB450G nebo starší hEX S | současné aktivní zařízení a konfiguraci ověřit |
| lokální distribuce | různé switche a SOHO routery | úplná inventura chybí; další DHCP a NAT jsou možné |

Přesné aktivní kusy a jejich stav: **Vyžaduje ověření v živém systému.**

## Schválené cílové role

| Role | Řešení | Stav / podmínka |
|---|---|---|
| místní router | hEX S (2025) | schválený jediný core; lokální DHCP, směrování a firewall |
| přijímací rádio | stávající vhodné rádio | pouze bridge/CPE; přesný model ověřit |
| vnitřní distribuce | spravované L2 prvky podle skutečné potřeby | Včelín a další mezilehlé body bez DHCP a NAT |
| soukromá Wi-Fi | samostatná kabelově připojená AP | modely a počet určit podle pokrytí a dostupného HW |
| hostovská Wi-Fi | druhé SSID na vhodných AP | oddělit od privátní sítě, HOME i správy; zajistit izolaci klientů |
| sloup a mobilhome | zatím neurčeno | rozhodnout až po ověření optiky, trasy, napájení a potřebné kapacity |

RB5009 ani CRS326 nejsou podmínkou cílového návrhu. Použijí se jen tehdy, pokud se později objeví konkrétní potřeba, která odůvodní změnu schválené jednoduché architektury.

## Doložení skladoví kandidáti

Airtable v posledním dostupném záznamu obsahuje více kandidátů:

- `hEX S`, model `RB760iGS`;
- `cAP ax`, model `cAPGi-5HaxD2HaxD`.

Konkrétní kus pro Rybníky dosud není v publikovaných podkladech jednoznačně rezervovaný. MAC adresy a proměnlivý počet kusů se do GitHubu nekopírují.

Další historicky zvažované skladové typy zahrnují CRS112, PowerBox Pro, wAP, cAP ac a bezdrátové spoje. Jejich současná dostupnost a přesný model: **Vyžaduje ověření v živém systému.** Kontrola zahrne Airtable i fyzický sklad.

## Požadavky na router a distribuci

### hEX S

Před přípravou cílového kusu ověřit:

- přesný model, stav portů a SFP šachty;
- aktuální RouterOS, RouterBOARD firmware a podporované balíčky;
- potřebný výkon pro skutečnou propustnost, firewall a řízení hostovského provozu;
- možnost místního napájení a bezpečného servisního přístupu;
- kompatibilitu SFP modulu, pokud se SFP skutečně použije.

hEX S nemá provozovat Wi-Fi. Jeho role zůstává routing, DHCP, firewall, management a případné řízení segmentů.

### L2 distribuční prvky

Konkrétní switch se vybírá až podle inventury:

- počet a rychlost metalických portů;
- počet a typ optických uplinků;
- PoE standard, napětí, příkon a rezerva zdroje;
- potřeba přenášet privátní, hostovskou a management síť;
- fyzické prostředí, teplota, krytí a servisní přístup.

Distribuční switch nesmí bez výslovného rozhodnutí převzít DHCP, NAT nebo routing.

## Požadavky na AP a rádiové spoje

- AP budou samostatná a kabelově připojená; jejich počet se neurčuje podle počtu budov, ale podle změřeného pokrytí.
- Hlavním cílem je stabilní areálové pokrytí, zejména v 2,4 GHz; 5 GHz se použije podle reálného prostředí a potřeb klientů.
- Vhodná AP musí umět bezpečně vysílat privátní i hostovské SSID a přenést jejich oddělení do drátové sítě.
- Kompatibilita centrální správy se ověří podle konkrétních modelů a použitých RouterOS/WiFi balíčků.
- Bezdrátové repeatery ani mesh nejsou cílovou náhradou kabeláže.
- Samostatný PtP spoj se použije jen v místě, kde kabel nebo optika skutečně nejsou možné.
- Schopnosti mANTBoxu, wAP, Wireless Wire nebo jiného venkovního rádia se nesmí odvozovat pouze z obchodního názvu; ověřuje se přesné SKU, pásma, počet rádií, anténa, napájení a prostředí.

## Venkovní instalace

Před výběrem prvku pro sloup nebo mobilhome ověřit:

- stav, typ, zakončení a útlum případné optiky;
- přímou viditelnost, Fresnelovu zónu, vegetaci a požadovanou kapacitu;
- napájení, PoE rozpočet, uzemnění a přepěťovou ochranu;
- galvanické vazby venkovních metalických tras;
- krytí, kondenzaci, rozsah teplot a ochranu konektorů;
- fyzický přístup pro výměnu a možnost odpojit novou větev bez dopadu na základní síť.

Pro hlavní přívod HOME → Rybníky není v současném schváleném plánu přechod na 60 GHz. Stabilní přívod se nemění pouze kvůli stáří.

## Příprava a aktualizace zařízení

Obecný postup je v [MadMike / Síť / MikroTik](../MadMike/Sit/MikroTik.md#bezpečný-postup-změny) a [Zálohách MikroTiků](../MadMike/Zalohy/MikroTik.md#checkpoint-před-změnou). Pro Rybníky navíc platí:

1. konkrétní kus nejprve rezervovat v Airtable a zaznamenat jeho cílovou roli;
2. mimo produkci ověřit model, RouterOS, firmware, porty, PoE/SFP a resetovací postup;
3. před aktualizací vytvořit `.backup` a `.rsc` původního stavu;
4. neaktualizovat současně cílový core, přijímací rádio, distribuci a AP;
5. nový kus předkonfigurovat, pojmenovat a fyzicky označit;
6. připravit zálohu cílové konfigurace, kabelový plán a konkrétní rollback;
7. po nasazení provést přejímku podle [Topologie](Topologie.md#přejímka-po-běžné-změně);
8. až po úspěšné přejímce označit kus v Airtable jako nasazený a vytvořit nový známý funkční checkpoint.

Starý Sextant s 32 MB RAM se bez jasného přínosu nepřevádí na RouterOS 7. Aktualizace sdíleného sektoru `AP HOME` vyžaduje navíc posouzení dopadu na ostatní připojení.

## Výměna porouchaného zařízení

1. Nejdřív vyloučit poruchu napájení, kabelu, PoE, SFP nebo nadřazeného uplinku.
2. Z [Topologie](Topologie.md) určit roli a závislosti zařízení.
3. V Airtable vybrat odpovídající náhradní kus a ověřit jeho skutečnou dostupnost.
4. Dohledat poslední použitelný `.backup` a `.rsc`; jejich obsah nepatří do GitHubu.
5. Náhradní kus připravit mimo produkci a zabránit vzniku duplicitní IP, DHCP nebo routy.
6. Připojovat navazující větve postupně a po každém kroku ověřit skutečnou službu.
7. Po obnově provést úplnou provozní kontrolu, vytvořit nový checkpoint a aktualizovat GitHub i Airtable.

## Handover minimum

Přebírající správce musí před výběrem nebo výměnou znát:

- skutečnou roli a umístění zařízení;
- fyzický uplink, napájení, PoE/SFP a navazující klienty;
- management cestu a možnost místního zásahu;
- verzi RouterOS/firmware a kompatibilitu náhradního kusu;
- poslední použitelnou zálohu a podmínky rollbacku;
- aktuální rezervaci kusu v Airtable;
- přejímací test odpovídající měněné roli.

## Otevřené kontroly

> Následující body **vyžadují ověření v živém systému**. Podle povahy se kontroluje také Airtable a fyzický sklad.

- [ ] Udělat úplný seznam aktivních routerů, switchů, AP a jejich napájení.
- [ ] V Airtable určit a rezervovat konkrétní hEX S (2025) a vhodná AP až podle inventury.
- [ ] Ověřit přesné modely, stav a kompatibilitu skladových AP uvažovaných pro nasazení.
- [ ] Ověřit dostupné switche, SFP moduly, typ optiky, PoE zdroje, přepěťové ochrany a uzemnění.
- [ ] Před návrhem sloupu ověřit přesné schopnosti konkrétního mANTBoxu nebo jiného rádia.
