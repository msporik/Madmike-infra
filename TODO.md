# TODO

> Tento soubor je automaticky generovaný přehled. Úkol upravuj nebo označ jako
> hotový v odkazovaném původním dokumentu; `TODO.md` se potom obnoví automaticky.

## HA-ValTom / Home-Assistant

### GoodWe a energetika

- [ ] [Zjistit přesný model GoodWe střídače, jeho lokální IP adresu, dostupný způsob komunikace a skutečné zdroje výroby, spotřeby, odběru a přetoku.](HA-ValTom/Home-Assistant/GoodWe-a-energie.md?plain=1#L101)
- [ ] [Zprovoznit nejprve čtecí integraci GoodWe, ověřit význam, jednotky a znaménka skutečných entit a vytvořit základní produkční FVE dashboard s přiměřenou historií.](HA-ValTom/Home-Assistant/GoodWe-a-energie.md?plain=1#L102)
- [ ] [Zmapovat typ, výkon, HDO, stykač, termostat a současné ruční ovládání bojleru; teprve potom navrhnout bezpečné automatické řízení.](HA-ValTom/Home-Assistant/GoodWe-a-energie.md?plain=1#L103)

### Nasazení a vzdálený přístup

- [ ] [Před fyzickým nasazením a při převzetí dokončit přejímací kontrolu HA ValTom.](HA-ValTom/Home-Assistant/Nasazeni-a-pristup.md?plain=1#L117)

## Honza / Home-Assistant

### Home Assistant – Honza

- [ ] [Ověřit a doplnit aktuální verze Home Assistant Core, OS a Supervisor a datum poslední bezpečné aktualizace.](Honza/Home-Assistant/README.md?plain=1#L113)
- [ ] [Ověřit fyzické umístění, napájení a možnost místního zásahu u HA Green.](Honza/Home-Assistant/README.md?plain=1#L114)
- [ ] [Provést aplikační inventuru podle první provozní kontroly a zaznamenat pouze odchylky od doloženého stavu.](Honza/Home-Assistant/README.md?plain=1#L115)

### NSPanel a topení

- [ ] [Ověřit model, umístění, napájení, síťovou identitu a stav konfigurace každého ze tří běžných NSPanelů.](Honza/Home-Assistant/NSPanel-a-topeni.md?plain=1#L102)
- [ ] [Ověřit a zdokumentovat běžící verze ESPHome, Blackymas blueprintu a TFT a bezpečné umístění obnovovacích YAML.](Honza/Home-Assistant/NSPanel-a-topeni.md?plain=1#L103)
- [ ] [Dokončit a prakticky otestovat místní dashboard každého skutečně nasazeného panelu bez rozšiřování na centrální dashboard domu.](Honza/Home-Assistant/NSPanel-a-topeni.md?plain=1#L104)
- [ ] [Zmapovat místnosti na jednotlivé okruhy rozdělovače.](Honza/Home-Assistant/NSPanel-a-topeni.md?plain=1#L105)
- [ ] [Vybrat a ověřit zdroj pokojové teploty pro každou plánovanou zónu.](Honza/Home-Assistant/NSPanel-a-topeni.md?plain=1#L106)
- [ ] [Navrhnout pohony, akční členy, elektrické schéma, ruční režim a fail-safe před zahájením řízení topení.](Honza/Home-Assistant/NSPanel-a-topeni.md?plain=1#L107)

### Zigbee a osvětlení

- [ ] [Dokončit a prakticky otestovat automatizaci pohybového čidla a světel na chodbě včetně ručního režimu a návratu do automatiky.](Honza/Home-Assistant/Zigbee-a-osvetleni.md?plain=1#L101)
- [ ] [Ověřit fyzickou montáž, přesný typ, elektrické zapojení, umístění a funkci Sonoff relé.](Honza/Home-Assistant/Zigbee-a-osvetleni.md?plain=1#L102)
- [ ] [Doplnit inventuru významných Zigbee zařízení, jejich modely, umístění, napájení a případné skupiny.](Honza/Home-Assistant/Zigbee-a-osvetleni.md?plain=1#L103)
- [ ] [Ověřit verzi Zigbee2MQTT, firmware a síťové umístění SLZB-06P10 a existenci použitelných obnovovacích podkladů.](Honza/Home-Assistant/Zigbee-a-osvetleni.md?plain=1#L104)
- [ ] [Prakticky prověřit chování osvětlení při výpadku Home Assistantu, MQTT, Zigbee2MQTT a koordinátoru.](Honza/Home-Assistant/Zigbee-a-osvetleni.md?plain=1#L105)

## Honza / Sit

### MikroTik a Wi-Fi

- [ ] [Živými read-only výpisy ověřit přesný model, RouterOS, firmware a provozní konfiguraci RB4011 a hAP ac3.](Honza/Sit/MikroTik-a-WiFi.md?plain=1#L120)
- [ ] [Doplnit WAN, propojovací porty, napájení a fyzické umístění obou aktivních zařízení.](Honza/Sit/MikroTik-a-WiFi.md?plain=1#L121)
- [ ] [Ověřit skutečnou roli RB4011 pro DHCP, DNS, NAT a firewall a skutečný Wi-Fi stack hAP ac3.](Honza/Sit/MikroTik-a-WiFi.md?plain=1#L122)
- [ ] [Porovnat aktivní zařízení s Mikr Managerem a kusovou evidencí v Airtable; skladový stav sám neurčuje nasazení v lokalitě.](Honza/Sit/MikroTik-a-WiFi.md?plain=1#L123)
- [ ] [Ověřit poslední použitelný `.backup` a `.rsc` obou zařízení a možnost místního zásahu.](Honza/Sit/MikroTik-a-WiFi.md?plain=1#L124)

## MadMike / Home-Assistant

### FVE SolaX

- [ ] [Ověřit a zdokumentovat přesný název a komunikační cestu používané SolaX integrace a klíčové entity pro diagnostiku, Energy dashboard a automatizace.](MadMike/Home-Assistant/FVE-SolaX.md?plain=1#L105)
- [ ] [Dotáhnout energetické řízení do plně automatického režimu a zdokumentovat skutečně řízené prvky, podmínky, ruční režim, bezpečný stav a návrat do automatiky.](MadMike/Home-Assistant/FVE-SolaX.md?plain=1#L106)
- [ ] [Realizovat malý pilot InfluxDB a Grafany pro domácí energetická data včetně stanovení retence a zálohování.](MadMike/Home-Assistant/FVE-SolaX.md?plain=1#L107)

### Home Assistant

- [ ] [Ověřit živý seznam aktivních integrací a vyřadit z evidence již nepoužívané položky.](MadMike/Home-Assistant/README.md?plain=1#L181)
- [ ] [Ověřit, zda Uptime Kuma hlídá dostupnost domácího Home Assistantu a zda upozornění směřují do schváleného notifikačního systému.](MadMike/Home-Assistant/README.md?plain=1#L182)
- [ ] [S využitím plošiny vyměnit připravené 2 kamery za Hikvision, ověřit jejich záznam na Hikvision NVR a dokončit migraci kamerového systému na Hikvision.](MadMike/Home-Assistant/README.md?plain=1#L183)

### Zigbee

- [ ] [Ověřit plánované nasazení SLZB-06M pro Thread/Matter a zvolit způsob OTBR: OTBR v Home Assistantu, nebo OTBR přímo na SLZB-06M.](MadMike/Home-Assistant/Zigbee.md?plain=1#L91)
- [ ] [Ověřit, zda je původní USB koordinátor skutečně použitelný jako nouzová záloha produkční Zigbee sítě.](MadMike/Home-Assistant/Zigbee.md?plain=1#L92)

## MadMike / Monitoring

### Mikr Manager

- [ ] [Ověřit současnou verzi, image, počet zařízení, licenci, interval grafů a retenci.](MadMike/Monitoring/Mikr.md?plain=1#L133)
- [ ] [Určit kritická zařízení a lokality.](MadMike/Monitoring/Mikr.md?plain=1#L134)
- [ ] [Ověřit současné alarmy, jejich prahy, zpoždění a recovery chování.](MadMike/Monitoring/Mikr.md?plain=1#L135)
- [ ] [Ověřit, že RSC exporty pravidelně vznikají a kde jsou persistentně uložené.](MadMike/Monitoring/Mikr.md?plain=1#L136)
- [ ] [Ověřit, které události už spolehlivěji pokrývá Uptime Kuma.](MadMike/Monitoring/Mikr.md?plain=1#L137)

### Monitoring

- [ ] [Ověřit současný stav VM510, Dockeru a všech provozovaných kontejnerů.](MadMike/Monitoring/README.md?plain=1#L106)

### Pulse

- [ ] [Zdokumentovat přesný postup aktualizace Pulse agentů na PVE Ryzen, PVE Dell a PBS.](MadMike/Monitoring/Pulse.md?plain=1#L226)
- [ ] [Ověřit současnou verzi Pulse serveru a všech tří agentů.](MadMike/Monitoring/Pulse.md?plain=1#L227)
- [ ] [Zjistit současnou konfiguraci notifikačních cílů a pravidel na PVE Ryzen, PVE Dell a PBS.](MadMike/Monitoring/Pulse.md?plain=1#L228)
- [ ] [Poslat vestavěnou testovací notifikaci ze všech tří systémů.](MadMike/Monitoring/Pulse.md?plain=1#L229)
- [ ] [Bez narušení produkčních záloh ověřit hlášení neúspěšného Backup jobu.](MadMike/Monitoring/Pulse.md?plain=1#L230)
- [ ] [Ověřit hlášení neúspěšného Verify, Prune a Garbage Collection jobu.](MadMike/Monitoring/Pulse.md?plain=1#L231)
- [ ] [Ověřit plánování ZFS scrubů a způsob hlášení chyby nebo příliš starého posledního běhu.](MadMike/Monitoring/Pulse.md?plain=1#L232)
- [ ] [Ověřit, že běžné úspěšné úlohy nevytvářejí notifikační šum.](MadMike/Monitoring/Pulse.md?plain=1#L233)

### Pushover notifikace

- [ ] [Vybrat produkční monitory Uptime Kumy, jednotlivě jim přiřadit `Pushover – Kuma` a ověřit, že nevznikají duplicitní zprávy.](MadMike/Monitoring/Pushover.md?plain=1#L108)
- [ ] [Připojit a samostatně otestovat nativní notifikace PVE/PBS.](MadMike/Monitoring/Pushover.md?plain=1#L109)
- [ ] [Připojit a samostatně otestovat vybrané alarmy Mikr Manageru.](MadMike/Monitoring/Pushover.md?plain=1#L110)
- [ ] [Pulse připojit pouze pro události nepokryté jiným zdrojem a samostatně otestovat alarm i recovery.](MadMike/Monitoring/Pushover.md?plain=1#L111)
- [ ] [Po pilotním provozu vyhodnotit četnost, priority, formát zpráv a potlačení duplicit.](MadMike/Monitoring/Pushover.md?plain=1#L112)

### Uptime Kuma

- [ ] [Ověřit současnou verzi, image a přesné startovací parametry kontejneru.](MadMike/Monitoring/Uptime-Kuma.md?plain=1#L160)
- [ ] [Porovnat živý seznam monitorů s historickým a schváleným rozsahem.](MadMike/Monitoring/Uptime-Kuma.md?plain=1#L161)
- [ ] [Ověřit typy kontrol, intervaly, retries, timeouty a skutečná zpoždění alarmů.](MadMike/Monitoring/Uptime-Kuma.md?plain=1#L162)
- [ ] [Vybrat produkční monitory, které mají používat `Pushover – Kuma`, přiřadit cíl jednotlivě a ověřit, že nevznikají duplicity.](MadMike/Monitoring/Uptime-Kuma.md?plain=1#L163)
- [ ] [Zdokumentovat samostatnou zálohu a obnovu konfigurace Kumy, pokud existuje.](MadMike/Monitoring/Uptime-Kuma.md?plain=1#L164)

## MadMike / Nextcloud

### Provoz a úložiště

- [ ] [Ověřit aktuální PVE konfiguraci VM401 a fyzický ZFS pool za storage ID `tank-nas-zfs` v PVE Ryzen.](MadMike/Nextcloud/Provoz-a-uloziste.md?plain=1#L192)
- [ ] [Ověřit živé verze operačního systému, Nextcloudu, PHP, Apache a MariaDB.](MadMike/Nextcloud/Provoz-a-uloziste.md?plain=1#L193)
- [ ] [Ověřit skutečnou cestu instalace, PHP handler, databázovou konfiguraci a cache bez zveřejnění tajných hodnot.](MadMike/Nextcloud/Provoz-a-uloziste.md?plain=1#L194)
- [ ] [Ověřit obsazení a volnou kapacitu systémového i datového disku.](MadMike/Nextcloud/Provoz-a-uloziste.md?plain=1#L195)
- [ ] [Ověřit trvalé připojení `/var/nc-data`, zařízení, filesystem a mount po restartu VM.](MadMike/Nextcloud/Provoz-a-uloziste.md?plain=1#L196)
- [ ] [Ověřit nastavení background jobs a cronu; chybějící doporučený způsob následně doplnit.](MadMike/Nextcloud/Provoz-a-uloziste.md?plain=1#L197)
- [ ] [Připravit, bezpečně otestovat a zapsat konkrétní aktualizační postup pro zjištěnou živou verzi.](MadMike/Nextcloud/Provoz-a-uloziste.md?plain=1#L198)
- [ ] [Ověřit v Uptime Kuma, zda je aktivní monitor webového endpointu Nextcloudu a zda jeho zpoždění odpovídá schválenému chování alarmů.](MadMike/Nextcloud/Provoz-a-uloziste.md?plain=1#L199)

### Přístup a uživatelé

- [ ] [Opravit přihlášení Katky a ověřit následnou synchronizaci.](MadMike/Nextcloud/Pristup-a-uzivatele.md?plain=1#L169)
- [ ] [Ověřit aktivní účty, administrátorskou roli a skutečný stav účtu `djlobo`.](MadMike/Nextcloud/Pristup-a-uzivatele.md?plain=1#L170)
- [ ] [Ověřit stav MFA a bezpečný recovery postup.](MadMike/Nextcloud/Pristup-a-uzivatele.md?plain=1#L171)
- [ ] [Ověřit používaná aplikační hesla a připojené klienty bez zápisu jejich tajných hodnot.](MadMike/Nextcloud/Pristup-a-uzivatele.md?plain=1#L172)
- [ ] [Ověřit současné veřejné odkazy a pravidla externího sdílení.](MadMike/Nextcloud/Pristup-a-uzivatele.md?plain=1#L173)
- [ ] [Popsat a ověřit úplnou publikační cestu `cloud.madmike.cz`, včetně DNS, NAT/firewallu a Apache VirtualHostu.](MadMike/Nextcloud/Pristup-a-uzivatele.md?plain=1#L174)
- [ ] [Ověřit platnost certifikátu Let's Encrypt, automatickou obnovu přes Certbot a prakticky provést bezpečný dry-run.](MadMike/Nextcloud/Pristup-a-uzivatele.md?plain=1#L175)
- [ ] [Později založit účty pro dvě děti podle schváleného rozšíření služby.](MadMike/Nextcloud/Pristup-a-uzivatele.md?plain=1#L176)

## MadMike / Premier

### Přístup a provoz

- [ ] [Zjistit zařízení a místa přístupu účetní a její požadavky na tisk, schránku a přenos souborů.](MadMike/Premier/Pristup-a-provoz.md?plain=1#L149)
- [ ] [Po ověření pracovního prostředí účetní nasadit a prakticky otestovat schválené krátkodobé omezení RDP na české IP rozsahy.](MadMike/Premier/Pristup-a-provoz.md?plain=1#L150)
- [ ] [Po výběru cílového přístupového řešení v projektu Přístupy ověřit s účetní celý běžný pracovní postup a teprve poté odstranit původní veřejné RDP.](MadMike/Premier/Pristup-a-provoz.md?plain=1#L151)
- [ ] [Ověřit verzi a edici Windows, aktivaci, stav aktualizací a podpory.](MadMike/Premier/Pristup-a-provoz.md?plain=1#L155)
- [ ] [Ověřit verzi PREMIERu, licenční stav bez klíče, obecné umístění dat a bezpečné umístění instalačních a licenčních podkladů.](MadMike/Premier/Pristup-a-provoz.md?plain=1#L156)
- [ ] [Stanovit pravidelný aktualizační postup a termín pro Windows a PREMIER včetně návratové cesty a přejímky.](MadMike/Premier/Pristup-a-provoz.md?plain=1#L157)
- [ ] [Ustálit jedno vstupní místo a stavy nezpracované, připravené, zadané a chybějící pro jednoduchý tok faktur před případnou automatizací importu.](MadMike/Premier/Pristup-a-provoz.md?plain=1#L158)
- [ ] [Porovnat živý stav a konfiguraci VM501 s dokumentací a případné změny zapsat do autoritativního dokumentu PVE Ryzen.](MadMike/Premier/Pristup-a-provoz.md?plain=1#L162)
- [ ] [Navrhnout a zavést podporovanou aplikační zálohu PREMIERu mimo VM501 včetně retence, offsite ochrany a testu obnovy jedné účetní jednotky.](MadMike/Premier/Pristup-a-provoz.md?plain=1#L163)
- [ ] [Stanovit požadované RPO, RTO a přijatelnou dobu odstávky PREMIERu.](MadMike/Premier/Pristup-a-provoz.md?plain=1#L164)
- [ ] [Prakticky ověřit aplikační DR postup včetně dočasného přístupu účetní a zajištění, že nikdy neběží dvě produkční kopie VM501.](MadMike/Premier/Pristup-a-provoz.md?plain=1#L165)

## MadMike / Pristupy

### Bitwarden

- [ ] [Nainstalovat Bitwarden na telefon a ověřit přihlášení, synchronizaci, odemykání a automatické vyplňování.](MadMike/Pristupy/Bitwarden.md?plain=1#L157)
- [ ] [Zapnout MFA a připravit nezávislý recovery podklad mimo telefon, počítač a samotný trezor; poté prakticky ověřit recovery postup.](MadMike/Pristupy/Bitwarden.md?plain=1#L158)
- [ ] [Přenést vybrané důležité účty a zkontrolovat jejich přesná URI a porovnávání podle hostitele; zejména GitHub, Microsoft, Home Assistant, RouterOS/WebFig a iDRAC.](MadMike/Pristupy/Bitwarden.md?plain=1#L159)
- [ ] [Po splnění podmínek pilotu rozhodnout o vypnutí starého ukládání hesel v Chromu.](MadMike/Pristupy/Bitwarden.md?plain=1#L160)

### Přístupy

- [ ] [Vybrat jednoduchou cílovou náhradu přímého veřejného RDP k PREMIERu podle skutečného způsobu práce účetní.](MadMike/Pristupy/README.md?plain=1#L141)
- [ ] [Definovat a prakticky ověřit minimální nouzový postup pro obnovu administrátorského přístupu po současné ztrátě notebooku a telefonu.](MadMike/Pristupy/README.md?plain=1#L142)
- [ ] [Vytvořit bezpečný přehled kritických identit po kategoriích, který bez uživatelských jmen a tajných hodnot eviduje odpovědnost, stav MFA, stav recovery a datum posledního ověření.](MadMike/Pristupy/README.md?plain=1#L143)

## MadMike / Servery

### Interní DNS, NPM a HTTPS

- [ ] [Ověřit současnou verzi NPM, stav všech proxy hostů a datum poslední úspěšné obnovy wildcard certifikátu.](MadMike/Servery/DNS-NPM-HTTPS.md?plain=1#L221)
- [ ] [Ověřit, že Cloudflare API token je uložený v Bitwardenu a případný nezašifrovaný TXT soubor byl odstraněn.](MadMike/Servery/DNS-NPM-HTTPS.md?plain=1#L222)

### PVE Dell

- [ ] [Najít skutečný soubor `create-vm.sh`, pravděpodobně na PVE Dell nebo v umístění, ze kterého byl při vytvoření VM400 spuštěn.](MadMike/Servery/PVE-Dell.md?plain=1#L140)
- [ ] [Ověřit přesný obsah a verzi skriptu.](MadMike/Servery/PVE-Dell.md?plain=1#L141)
- [ ] [Zdokumentovat jeho cestu, vlastníka a oprávnění.](MadMike/Servery/PVE-Dell.md?plain=1#L142)
- [ ] [Zdokumentovat způsob spuštění a všechny vstupní parametry.](MadMike/Servery/PVE-Dell.md?plain=1#L143)
- [ ] [Ověřit, které hodnoty jsou pevně zadané a které se předávají jako argumenty nebo interaktivní vstup.](MadMike/Servery/PVE-Dell.md?plain=1#L144)
- [ ] [Ověřit, zda je skript bezpečně použitelný také na PVE Ryzen.](MadMike/Servery/PVE-Dell.md?plain=1#L145)
- [ ] [Po nalezení uložit ověřený skript nebo jeho autoritativní kopii na vhodné místo a doplnit reprodukovatelný postup vytvoření nové Debian VM.](MadMike/Servery/PVE-Dell.md?plain=1#L146)
- [ ] [Ověřit současný obsah a další potřebnost VM400 před jakýmkoliv odstraněním nebo novým použitím VMID `400`.](MadMike/Servery/PVE-Dell.md?plain=1#L147)
- [ ] [Zjistit původ a účel Dell / VM400.](MadMike/Servery/PVE-Dell.md?plain=1#L262)
- [ ] [Ověřit aktuální verzi a konfiguraci PVE Dell, VM200, storage a sítě proti živému systému.](MadMike/Servery/PVE-Dell.md?plain=1#L263)
- [ ] [Připravit a schválit bezpečný migrační plán z dnešních dvou mirrorů na jeden pool ze čtyř 8TB disků, včetně cílové topologie, zálohy, obnovy a rollbacku.](MadMike/Servery/PVE-Dell.md?plain=1#L264)

### PVE Ryzen

- [ ] [Ověřit aktuální PVE konfiguraci VM401 živými výpisy `pvesm` a `qm config 401`, včetně prostředků, disků a fyzického ZFS poolu za storage ID `tank-nas-zfs`.](MadMike/Servery/PVE-Ryzen.md?plain=1#L200)
- [ ] [Ověřit současné rozdělení a obsazení systémového NVMe.](MadMike/Servery/PVE-Ryzen.md?plain=1#L201)
- [ ] [Ověřit přesný model základní desky A520, současný zdroj a zapojení napájení před instalací M4-ATX.](MadMike/Servery/PVE-Ryzen.md?plain=1#L202)
- [ ] [Po návratu z dovolené objednat standardní Mini-Box M4-ATX 6–30 V / 250 W a potřebné kabely.](MadMike/Servery/PVE-Ryzen.md?plain=1#L203)
- [ ] [Před instalací M4-ATX ověřit práh baterie DRS a připravit zapojení AC OK/AC FAIL → IGNITION → POWER SW.](MadMike/Servery/PVE-Ryzen.md?plain=1#L204)
- [ ] [Po instalaci nastavit prodlevy a prakticky otestovat celý cyklus výpadek → korektní shutdown → bezpečný hard-off → návrat sítě → automatický start.](MadMike/Servery/PVE-Ryzen.md?plain=1#L205)

### VM510 – Docker infrastruktura

- [ ] [Pořídit úplnou sanitizovanou inventuru NPM, Pulse a Mikru: běžící image/verze, restart policy, sítě, porty, volumes, bind mounty a umístění `.env` bez jejich obsahu.](MadMike/Servery/VM510-Docker.md?plain=1#L178)
- [ ] [Ověřit a zdokumentovat persistentní data NPM včetně databáze, proxy hostů, certifikátů a bezpečného způsobu obnovy Cloudflare DNS challenge.](MadMike/Servery/VM510-Docker.md?plain=1#L179)
- [ ] [Ověřit, že Pulse stále používá `pulse_data` a Mikr `/opt/mikr/data` a `/opt/mikr/exports`.](MadMike/Servery/VM510-Docker.md?plain=1#L180)

### WireGuard

- [ ] [Vypsat na RB5009 všechny aktivní WG peery, jejich WG adresy, `allowed-address` a routy.](MadMike/Servery/WireGuard.md?plain=1#L181)
- [ ] [Ověřit, zda kromě čtyř známých propojení neexistuje další aktivní WireGuard tunel.](MadMike/Servery/WireGuard.md?plain=1#L182)
- [ ] [Ověřit přesnou WG adresu klienta notebooku a peeru HOME ↔ Richard.](MadMike/Servery/WireGuard.md?plain=1#L183)
- [ ] [Ověřit, zda historická WG adresa `10.200.0.10` stále patří aktivnímu peeru RD Švecovi.](MadMike/Servery/WireGuard.md?plain=1#L184)
- [ ] [Ověřit a případně odstranit zbytky starého IPsec na HOME, u Honzy a u RD Švecových až po potvrzení, že na nich nic nezávisí.](MadMike/Servery/WireGuard.md?plain=1#L185)
- [ ] [Při kontrole starého IPsec určit původ rozsahu `192.168.30.0/24`.](MadMike/Servery/WireGuard.md?plain=1#L186)

## MadMike / Sit

### Adresní plán

- [ ] [Vypsat současné LAN, VLAN, routované a transitní rozsahy všech spravovaných lokalit; provozní WG inventuru převzít z dokumentu WireGuard.](MadMike/Sit/Adresni-plan.md?plain=1#L232)
- [ ] [Jednoznačně přiřadit číselný identifikátor každé lokalitě s respektováním blokací `0`, `8` a `89`.](MadMike/Sit/Adresni-plan.md?plain=1#L233)
- [ ] [Navrhnout jednotný slovník funkčních segmentů; číslo segmentu automaticky neztotožňovat s VLAN ID.](MadMike/Sit/Adresni-plan.md?plain=1#L234)
- [ ] [Navrhnout vnitřní členění `10.255.0.0/16` pro VPN, transit a virtuální adresy.](MadMike/Sit/Adresni-plan.md?plain=1#L235)
- [ ] [Provést kontrolu kolizí s používanými VPN, kontejnery a běžnými vzdálenými sítěmi.](MadMike/Sit/Adresni-plan.md?plain=1#L236)
- [ ] [Zařadit dnešní `10.89.1.0/24` a `10.200.0.0/24` do budoucího migračního plánu VPN vrstvy.](MadMike/Sit/Adresni-plan.md?plain=1#L237)
- [ ] [Teprve potom připravit migrační pořadí; žádnou fungující lokalitu nepřečíslovávat jen kvůli estetice.](MadMike/Sit/Adresni-plan.md?plain=1#L238)

### MikroTik

- [ ] [Ověřit aktivní uplinky a portovou mapu RB5009, CRS326 a CRS112 proti živé konfiguraci.](MadMike/Sit/MikroTik.md?plain=1#L213)
- [ ] [Ověřit aktuální seznam domácích AP a jejich role přímo v CAPsMAN.](MadMike/Sit/MikroTik.md?plain=1#L214)
- [ ] [Doplnit VLAN a další domácí síťové role pouze tehdy, pokud jsou skutečně nasazené.](MadMike/Sit/MikroTik.md?plain=1#L215)

## MadMike / Zalohy

### PBS a disaster recovery

- [ ] [Ověřit plánování a poslední běh scrubů na `tank-pbs` a `tank-nas`.](MadMike/Zalohy/PBS-DR.md?plain=1#L301)
- [ ] [Ověřit SMART a teploty čtyř SAS disků a systémového SSD proti živému stavu.](MadMike/Zalohy/PBS-DR.md?plain=1#L302)
- [ ] [Ověřit persistentní Docker data a mounty VM510 a provést testovací restore.](MadMike/Zalohy/PBS-DR.md?plain=1#L303)
- [ ] [Prakticky ověřit start PVE Dell, VM200 a datastore po úplném výpadku napájení.](MadMike/Zalohy/PBS-DR.md?plain=1#L304)
- [ ] [Stanovit rozumnou četnost opakovaných testů obnovy.](MadMike/Zalohy/PBS-DR.md?plain=1#L305)
- [ ] [Stanovit společné RPO, RTO, pořadí obnovy a maximální přijatelné stáří backupu.](MadMike/Zalohy/PBS-DR.md?plain=1#L306)
- [ ] [Stanovit minimální bezpečnou rezervu datastore a hranici kapacitního alarmu.](MadMike/Zalohy/PBS-DR.md?plain=1#L307)
- [ ] [Určit původ nejasných/orphaned backup groups a samostatně ověřit účel Dell / VM400 jako odlišného objektu.](MadMike/Zalohy/PBS-DR.md?plain=1#L308)
- [ ] [Zdokumentovat bezpečné umístění recovery materiálů hostitelů bez zveřejnění tajných údajů.](MadMike/Zalohy/PBS-DR.md?plain=1#L309)
- [ ] [Rozhodnout o klientském šifrování PBS a při jeho použití bezpečně uložit recovery klíč.](MadMike/Zalohy/PBS-DR.md?plain=1#L310)
- [ ] [Určit odpovědnost a dostupnost místního zásahu u Richarda.](MadMike/Zalohy/PBS-DR.md?plain=1#L311)

### Zálohy Home Assistantu

- [ ] [Ověřit živé nastavení backupu, poslední úspěch a retenci u všech tří produkčních instancí.](MadMike/Zalohy/Home-Assistant.md?plain=1#L147)
- [ ] [Stanovit hranici stáří HA backupu vyžadující upozornění a odpovědnost za reakci.](MadMike/Zalohy/Home-Assistant.md?plain=1#L148)
- [ ] [Zprovoznit a ověřit prostor `ha-backup`, oddělená app hesla a složky jednotlivých lokalit.](MadMike/Zalohy/Home-Assistant.md?plain=1#L149)
- [ ] [Ověřit, že Nextcloud kopie jsou skutečně součástí PBS zálohy VM401.](MadMike/Zalohy/Home-Assistant.md?plain=1#L150)
- [ ] [Provést a zdokumentovat praktický restore HA Vernířovice.](MadMike/Zalohy/Home-Assistant.md?plain=1#L151)
- [ ] [Provést a zdokumentovat praktický restore HA Honza.](MadMike/Zalohy/Home-Assistant.md?plain=1#L152)
- [ ] [Po instalaci HA ValTom nastavit pravidelné produkční zálohování a provést restore test.](MadMike/Zalohy/Home-Assistant.md?plain=1#L153)
- [ ] [Při příštím opakování domácí obnovy doplnit datum, použitý backup, hardware a ověřené funkce.](MadMike/Zalohy/Home-Assistant.md?plain=1#L154)
- [ ] [Doplnit odpovědnosti a možnost místního zásahu pro jednotlivé lokality.](MadMike/Zalohy/Home-Assistant.md?plain=1#L155)

### Zálohy MikroTiků

- [ ] [Ověřit scope 22 zařízení, skutečný rozvrh a poslední úspěšné exporty.](MadMike/Zalohy/MikroTik.md?plain=1#L170)
- [ ] [Určit prioritní zařízení, vlastníky lokalit a možnost místního zásahu.](MadMike/Zalohy/MikroTik.md?plain=1#L171)
- [ ] [Ověřit retenci, hranici stáří a přesné persistentní umístění exportů v Mikr Manageru.](MadMike/Zalohy/MikroTik.md?plain=1#L172)
- [ ] [Ověřit, zda jsou exporty součástí PBS zálohy VM510.](MadMike/Zalohy/MikroTik.md?plain=1#L173)
- [ ] [Zavést binární `.backup` pro důležitá zařízení a checkpoint před i po zásadní změně.](MadMike/Zalohy/MikroTik.md?plain=1#L174)
- [ ] [Zprovoznit chráněnou druhou kopii přes Nextcloud a PBS.](MadMike/Zalohy/MikroTik.md?plain=1#L175)
- [ ] [Prověřit zacházení s citlivými údaji v používané verzi RouterOS a Mikr Manageru.](MadMike/Zalohy/MikroTik.md?plain=1#L176)
- [ ] [Prakticky otestovat obnovu `.backup` a `.rsc` na náhradním nebo testovacím MikroTiku.](MadMike/Zalohy/MikroTik.md?plain=1#L177)
- [ ] [Zapsat pro prioritní zařízení datum posledního použitelného checkpointu a restore testu.](MadMike/Zalohy/MikroTik.md?plain=1#L178)

## Rybniky-Amerika

### Hardware

- [ ] [Udělat úplný seznam aktivních routerů, switchů, AP a jejich napájení.](Rybniky-Amerika/Hardware.md?plain=1#L143)
- [ ] [V Airtable určit a rezervovat konkrétní hEX S (2025) a vhodná AP až podle inventury.](Rybniky-Amerika/Hardware.md?plain=1#L144)
- [ ] [Ověřit přesné modely, stav a kompatibilitu skladových AP uvažovaných pro nasazení.](Rybniky-Amerika/Hardware.md?plain=1#L145)
- [ ] [Ověřit dostupné switche, SFP moduly, typ optiky, PoE zdroje, přepěťové ochrany a uzemnění.](Rybniky-Amerika/Hardware.md?plain=1#L146)
- [ ] [Před návrhem sloupu ověřit přesné schopnosti konkrétního mANTBoxu nebo jiného rádia.](Rybniky-Amerika/Hardware.md?plain=1#L147)

### Plán rekonstrukce

- [ ] [Přidělit cílový LAN prefix Rybníků v rámci společného adresního plánu.](Rybniky-Amerika/Plan-rekonstrukce.md?plain=1#L210)
- [ ] [Po inventuře sepsat jednotlivé nutné výjimky z privátní sítě Rybníků do HOME; bez doložené potřeby zůstane výchozí `deny`.](Rybniky-Amerika/Plan-rekonstrukce.md?plain=1#L211)
- [ ] [Podle inventury doplnit konkrétní testovací checklist, časový limit a kabelový postup rollbacku pro etapu 2.](Rybniky-Amerika/Plan-rekonstrukce.md?plain=1#L212)
- [ ] [Vybrat pilotní větev pro odstranění prvního NAT ostrova.](Rybniky-Amerika/Plan-rekonstrukce.md?plain=1#L213)
- [ ] [Vybrat způsob centrální správy AP a ověřit kompatibilitu konkrétních modelů.](Rybniky-Amerika/Plan-rekonstrukce.md?plain=1#L214)
- [ ] [V dokumentu Mikr navrhnout závislosti a souhrnný alarm lokality.](Rybniky-Amerika/Plan-rekonstrukce.md?plain=1#L215)
- [ ] [V dokumentaci záloh MikroTiků doplnit a prakticky ověřit obnovu konfigurace Rybníků.](Rybniky-Amerika/Plan-rekonstrukce.md?plain=1#L216)

### Topologie

- [ ] [Ověřit přesný model, RouterOS, konfiguraci a ostatní klienty sektoru `AP HOME`.](Rybniky-Amerika/Topologie.md?plain=1#L155)
- [ ] [Ověřit přesný model, RouterOS a režim přijímací jednotky.](Rybniky-Amerika/Topologie.md?plain=1#L156)
- [ ] [Změřit aktuální rádiové parametry, stabilitu a reálnou propustnost přívodu.](Rybniky-Amerika/Topologie.md?plain=1#L157)
- [ ] [Určit zařízení, které dnes routuje a poskytuje DHCP, NAT a firewall.](Rybniky-Amerika/Topologie.md?plain=1#L158)
- [ ] [Zmapovat všechny další DHCP servery, NATy, aktivní rozsahy, statické IP a port-forwardy.](Rybniky-Amerika/Topologie.md?plain=1#L159)
- [ ] [Zmapovat zařízení, porty a kabely v Obýváku, Včelíně, Hospodě a Dílně.](Rybniky-Amerika/Topologie.md?plain=1#L160)
- [ ] [Ověřit stav, typ a zakončení optiky ke sloupu.](Rybniky-Amerika/Topologie.md?plain=1#L161)
- [ ] [Ověřit NVR, zařízení „Stavba“ a další klienty citlivé na změnu adresace.](Rybniky-Amerika/Topologie.md?plain=1#L162)
- [ ] [Ověřit současnou management cestu, možnost místního zásahu a skutečné zařazení lokality v Mikru.](Rybniky-Amerika/Topologie.md?plain=1#L163)

## Vernirovice / BESS-a-FVE

### Technologie FVE, BESS a tepelné infrastruktury

- [ ] [S dodavatelem vyřešit komunikaci baterie–střídač větší sestavy a doložit skutečné nabíjení, vybíjení, alarmy a bezpečný lokální režim.](Vernirovice/BESS-a-FVE/Technologie.md?plain=1#L173)
- [ ] [Opsat typové štítky obou měničů a bateriových systémů a uzavřít rozpory v modelech, výkonech a kapacitách.](Vernirovice/BESS-a-FVE/Technologie.md?plain=1#L174)
- [ ] [Ověřit současný instalovaný výkon FVE panelů.](Vernirovice/BESS-a-FVE/Technologie.md?plain=1#L175)
- [ ] [Získat jednopólové schéma nebo vytvořit ověřený provozní nákres včetně jištění jednotlivých zařízení a zálohovaných okruhů.](Vernirovice/BESS-a-FVE/Technologie.md?plain=1#L176)
- [ ] [Ověřit model, zapojení, znaménka a kalibraci hlavního Shelly a smartmeterů obou měničů.](Vernirovice/BESS-a-FVE/Technologie.md?plain=1#L177)
- [ ] [Ověřit, kde a jak je při souběhu obou měničů rychle vynucován společný exportní limit 50 kW.](Vernirovice/BESS-a-FVE/Technologie.md?plain=1#L178)
- [ ] [Ověřit současný stav, měření, ruční ovládání a fyzickou řiditelnost tepelné a wellness infrastruktury.](Vernirovice/BESS-a-FVE/Technologie.md?plain=1#L179)
- [ ] [Zapsat komunikační rozhraní a adresy zařízení bez tajných údajů a teprve poté připravit read-only RS485 pilot.](Vernirovice/BESS-a-FVE/Technologie.md?plain=1#L180)

### Řízení energie

- [ ] [Zdokumentovat přesný cenový vstup, současnou automatizaci, její blokaci, log rozhodnutí a potvrzení povelu.](Vernirovice/BESS-a-FVE/Rizeni-energie.md?plain=1#L226)
- [ ] [Prakticky ověřit návrat do `Zero Export To CT`, hraniční SOC, chyby vstupů, odmítnutý povel, ztrátu komunikace a restart Home Assistantu.](Vernirovice/BESS-a-FVE/Rizeni-energie.md?plain=1#L227)
- [ ] [Stanovit a otestovat bezpečný ruční režim, fail-safe stav a návrat do automatiky pro obě sestavy.](Vernirovice/BESS-a-FVE/Rizeni-energie.md?plain=1#L228)
- [ ] [Před koordinací obou baterií prokázat bezpečné vynucení společného exportního limitu 50 kW nezávisle na pomalé nadřazené optimalizaci.](Vernirovice/BESS-a-FVE/Rizeni-energie.md?plain=1#L229)
- [ ] [Po vyřešení problému dodavatelem read-only způsobem ověřit rozhraní, limity a skutečné chování větší sestavy.](Vernirovice/BESS-a-FVE/Rizeni-energie.md?plain=1#L230)
- [ ] [Ověřit backup/ostrovní zapojení a navrhnout, otestovat a zdokumentovat režim Maximální záloha.](Vernirovice/BESS-a-FVE/Rizeni-energie.md?plain=1#L231)
- [ ] [Po uzavření výběrového řízení zapsat skutečný nákupní a výkupní produkt a teprve poté připravit spotové řízení.](Vernirovice/BESS-a-FVE/Rizeni-energie.md?plain=1#L232)
- [ ] [Ověřit měření, ruční požadavky a komfortní podmínky tepelných a wellness zátěží.](Vernirovice/BESS-a-FVE/Rizeni-energie.md?plain=1#L233)
- [ ] [Zavést měsíční ekonomické vyhodnocení a ověřovat čistý přínos jednotlivých strategií.](Vernirovice/BESS-a-FVE/Rizeni-energie.md?plain=1#L234)

## Vernirovice / Home-Assistant

### Hardware a migrace

- [ ] [Ověřit a doplnit verze Home Assistant OS, Core a Supervisoru a skutečné parametry produkčního Raspberry Pi 5.](Vernirovice/Home-Assistant/Hardware-a-migrace.md?plain=1#L164)
- [ ] [Ověřit obsah zálohy a ochranu dat add-onů InfluxDB, Grafana a MQTT.](Vernirovice/Home-Assistant/Hardware-a-migrace.md?plain=1#L165)
- [ ] [Ověřit Qotom, připravit na něm Home Assistant OS a zdokumentovat síťové, úložné a bootovací parametry.](Vernirovice/Home-Assistant/Hardware-a-migrace.md?plain=1#L166)
- [ ] [Doplnit konkrétní předmigrační kontrolní seznam současných funkcí, údržbovou dobu a funkční kritéria rollbacku.](Vernirovice/Home-Assistant/Hardware-a-migrace.md?plain=1#L167)
- [ ] [Po úspěšné migraci provést a zdokumentovat přejímací test podle tohoto dokumentu.](Vernirovice/Home-Assistant/Hardware-a-migrace.md?plain=1#L168)

### Služby a integrace

- [ ] [Ověřit živý seznam aktivních integrací, add-onů, jejich verze a provozní vlastníky.](Vernirovice/Home-Assistant/Sluzby-a-integrace.md?plain=1#L199)
- [ ] [Ověřit konfiguraci, retenci, velikost databází, hlavní Grafana dashboardy a obnovitelnost dat InfluxDB/Grafany.](Vernirovice/Home-Assistant/Sluzby-a-integrace.md?plain=1#L200)
- [ ] [Ověřit účel, klienty, autentizaci a zálohování MQTT brokeru bez uložení tajných údajů do dokumentace.](Vernirovice/Home-Assistant/Sluzby-a-integrace.md?plain=1#L201)
- [ ] [Ověřit přesný stav klíčových entit a ovládání původní i větší bateriové sestavy.](Vernirovice/Home-Assistant/Sluzby-a-integrace.md?plain=1#L202)
- [ ] [Ověřit `IOTVL`, současný lokální a vzdálený přístup a zapojení instance do společného monitoringu.](Vernirovice/Home-Assistant/Sluzby-a-integrace.md?plain=1#L203)
- [ ] [Před zavedením RS485/Modbus připravit samostatný read-only test, přejímací kritéria a rollback.](Vernirovice/Home-Assistant/Sluzby-a-integrace.md?plain=1#L204)
- [ ] [Zapsat pouze stabilní entity skutečně důležité pro automatizace, řízení a diagnostiku.](Vernirovice/Home-Assistant/Sluzby-a-integrace.md?plain=1#L205)
