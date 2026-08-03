# TODO

> Tento soubor je automaticky generovaný přehled. Úkol upravuj nebo označ jako
> hotový v odkazovaném původním dokumentu; `TODO.md` se potom obnoví automaticky.

## HA-ValTom / Home-Assistant

### GoodWe a energetika

- [ ] [Zjistit přesný model GoodWe střídače, jeho lokální IP adresu, dostupný způsob komunikace a skutečné zdroje výroby, spotřeby, odběru a přetoku.](HA-ValTom/Home-Assistant/GoodWe-a-energie.md?plain=1#L32)
- [ ] [Zprovoznit nejprve čtecí integraci GoodWe, ověřit význam, jednotky a znaménka skutečných entit a vytvořit základní produkční FVE dashboard s přiměřenou historií.](HA-ValTom/Home-Assistant/GoodWe-a-energie.md?plain=1#L33)
- [ ] [Zmapovat typ, výkon, HDO, stykač, termostat a současné ruční ovládání bojleru; teprve potom navrhnout bezpečné automatické řízení.](HA-ValTom/Home-Assistant/GoodWe-a-energie.md?plain=1#L34)

### Nasazení a vzdálený přístup

- [ ] [Před fyzickým nasazením a při převzetí dokončit přejímací kontrolu HA ValTom.](HA-ValTom/Home-Assistant/Nasazeni-a-pristup.md?plain=1#L38)

## Honza / Home-Assistant

### Home Assistant – Honza

- [ ] [Ověřit a doplnit aktuální verze Home Assistant Core, OS a Supervisor.](Honza/Home-Assistant/README.md?plain=1#L50)

### NSPanel a topení

- [ ] [Ověřit a dokončit konfiguraci každého ze tří běžných NSPanelů.](Honza/Home-Assistant/NSPanel-a-topeni.md?plain=1#L50)
- [ ] [Zmapovat místnosti na jednotlivé okruhy rozdělovače.](Honza/Home-Assistant/NSPanel-a-topeni.md?plain=1#L51)
- [ ] [Vybrat a ověřit zdroj pokojové teploty pro každou plánovanou zónu.](Honza/Home-Assistant/NSPanel-a-topeni.md?plain=1#L52)
- [ ] [Navrhnout pohony, akční členy, ruční režim a fail-safe před zahájením řízení topení.](Honza/Home-Assistant/NSPanel-a-topeni.md?plain=1#L53)

### Zigbee a osvětlení

- [ ] [Dokončit a prakticky otestovat automatizaci pohybového čidla a světel na chodbě.](Honza/Home-Assistant/Zigbee-a-osvetleni.md?plain=1#L42)
- [ ] [Ověřit fyzickou montáž, typ, umístění a funkci Sonoff relé.](Honza/Home-Assistant/Zigbee-a-osvetleni.md?plain=1#L43)
- [ ] [Doplnit přesnou inventuru významných Zigbee zařízení, jejich umístění a případné skupiny.](Honza/Home-Assistant/Zigbee-a-osvetleni.md?plain=1#L44)
- [ ] [Prakticky prověřit chování osvětlení při výpadku Home Assistantu, MQTT, Zigbee2MQTT a koordinátoru.](Honza/Home-Assistant/Zigbee-a-osvetleni.md?plain=1#L45)

## Honza / Sit

### MikroTik a Wi-Fi

- [ ] [Živými read-only výpisy ověřit verzi RouterOS a provozní konfiguraci RB4011 a hAP ac3.](Honza/Sit/MikroTik-a-WiFi.md?plain=1#L29)
- [ ] [Doplnit přesné porty, napájení a fyzické umístění obou aktivních zařízení.](Honza/Sit/MikroTik-a-WiFi.md?plain=1#L30)
- [ ] [Porovnat RB4011 a hAP ac3 s Mikr Managerem a hardwarovou evidencí.](Honza/Sit/MikroTik-a-WiFi.md?plain=1#L31)

## MadMike / Home-Assistant

### FVE SolaX

- [ ] [Ověřit a zdokumentovat přesný název a komunikační cestu používané SolaX integrace a klíčové entity pro diagnostiku, Energy dashboard a automatizace.](MadMike/Home-Assistant/FVE-SolaX.md?plain=1#L105)
- [ ] [Dotáhnout energetické řízení do plně automatického režimu a zdokumentovat skutečně řízené prvky, podmínky, ruční režim, bezpečný stav a návrat do automatiky.](MadMike/Home-Assistant/FVE-SolaX.md?plain=1#L106)
- [ ] [Realizovat malý pilot InfluxDB a Grafany pro domácí energetická data včetně stanovení retence a zálohování.](MadMike/Home-Assistant/FVE-SolaX.md?plain=1#L107)

### Home Assistant

- [ ] [Ověřit živý seznam aktivních integrací a vyřadit z evidence již nepoužívané položky.](MadMike/Home-Assistant/README.md?plain=1#L160)
- [ ] [Ověřit a zdokumentovat aktuálně používanou vzdálenou přístupovou cestu k domácímu Home Assistantu.](MadMike/Home-Assistant/README.md?plain=1#L161)
- [ ] [Ověřit, zda Uptime Kuma hlídá dostupnost domácího Home Assistantu a zda upozornění směřují do schváleného notifikačního systému.](MadMike/Home-Assistant/README.md?plain=1#L162)
- [ ] [S využitím plošiny vyměnit připravené 2 kamery za Hikvision, ověřit jejich záznam na Hikvision NVR a dokončit migraci kamerového systému na Hikvision.](MadMike/Home-Assistant/README.md?plain=1#L163)

### Zigbee

- [ ] [Zjistit přesný model druhého zařízení SMLIGHT/SLZB určeného pro Matter/Thread a ověřit jeho zamýšlenou roli a stav OTBR.](MadMike/Home-Assistant/Zigbee.md?plain=1#L91)
- [ ] [Ověřit, zda je původní USB koordinátor skutečně použitelný jako nouzová záloha produkční Zigbee sítě.](MadMike/Home-Assistant/Zigbee.md?plain=1#L92)

## MadMike / Monitoring

### Mikr Manager

- [ ] [Ověřit současnou verzi, image, počet zařízení, licenci, interval grafů a retenci.](MadMike/Monitoring/Mikr.md?plain=1#L133)
- [ ] [Určit kritická zařízení a lokality.](MadMike/Monitoring/Mikr.md?plain=1#L134)
- [ ] [Ověřit současné alarmy, jejich prahy, zpoždění a recovery chování.](MadMike/Monitoring/Mikr.md?plain=1#L135)
- [ ] [Ověřit, že RSC exporty pravidelně vznikají a kde jsou persistentně uložené.](MadMike/Monitoring/Mikr.md?plain=1#L136)
- [ ] [Ověřit, které události už spolehlivěji pokrývá Uptime Kuma.](MadMike/Monitoring/Mikr.md?plain=1#L137)

### Monitoring

- [ ] [Ověřit současný stav VM510, Dockeru a všech provozovaných kontejnerů.](MadMike/Monitoring/README.md?plain=1#L102)
- [ ] [Ověřit, že je VM510 stále zahrnuta v automatickém PBS backup jobu.](MadMike/Monitoring/README.md?plain=1#L103)

### Pulse

- [ ] [Zdokumentovat přesný postup aktualizace Pulse agentů na PVE Ryzen, PVE Dell a PBS.](MadMike/Monitoring/Pulse.md?plain=1#L226)
- [ ] [Ověřit současnou verzi Pulse serveru a všech tří agentů.](MadMike/Monitoring/Pulse.md?plain=1#L227)
- [ ] [Zjistit současnou konfiguraci notifikačních cílů a pravidel na PVE Ryzen, PVE Dell a PBS.](MadMike/Monitoring/Pulse.md?plain=1#L228)
- [ ] [Poslat vestavěnou testovací notifikaci ze všech tří systémů.](MadMike/Monitoring/Pulse.md?plain=1#L229)
- [ ] [Bez narušení produkčních záloh ověřit hlášení neúspěšného Backup jobu.](MadMike/Monitoring/Pulse.md?plain=1#L230)
- [ ] [Ověřit hlášení neúspěšného Verify, Prune a Garbage Collection jobu.](MadMike/Monitoring/Pulse.md?plain=1#L231)
- [ ] [Ověřit plánování ZFS scrubů a způsob hlášení chyby nebo příliš starého posledního běhu.](MadMike/Monitoring/Pulse.md?plain=1#L232)
- [ ] [Ověřit, že běžné úspěšné úlohy nevytvářejí notifikační šum.](MadMike/Monitoring/Pulse.md?plain=1#L233)

### Telegram notifikace

- [ ] [Ověřit, zda již existuje soukromá skupina `MadMike – infrastruktura`; pokud ne, vytvořit ji.](MadMike/Monitoring/Telegram.md?plain=1#L99)
- [ ] [Ověřit existenci a vlastníka společného bota; pokud neexistuje, vytvořit ho.](MadMike/Monitoring/Telegram.md?plain=1#L100)
- [ ] [Ověřit administrátory skupiny, bezpečné umístění tokenu a systémy, které ho používají.](MadMike/Monitoring/Telegram.md?plain=1#L101)
- [ ] [Odeslat testovací zprávu.](MadMike/Monitoring/Telegram.md?plain=1#L102)
- [ ] [Připojit Uptime Kumu a prakticky otestovat skutečný `DOWN` i odpovídající recovery.](MadMike/Monitoring/Telegram.md?plain=1#L103)
- [ ] [Připojit otestované nativní notifikace PVE/PBS.](MadMike/Monitoring/Telegram.md?plain=1#L104)
- [ ] [Připojit vybrané alarmy Mikr Manageru.](MadMike/Monitoring/Telegram.md?plain=1#L105)
- [ ] [Pulse připojit pouze pro události nepokryté jiným zdrojem.](MadMike/Monitoring/Telegram.md?plain=1#L106)
- [ ] [Po pilotním provozu ověřit potlačení duplicit a opakovaných zpráv a upravit četnost.](MadMike/Monitoring/Telegram.md?plain=1#L107)

### Uptime Kuma

- [ ] [Ověřit současnou verzi, image a přesné startovací parametry kontejneru.](MadMike/Monitoring/Uptime-Kuma.md?plain=1#L144)
- [ ] [Porovnat živý seznam monitorů s historickým a schváleným rozsahem.](MadMike/Monitoring/Uptime-Kuma.md?plain=1#L145)
- [ ] [Ověřit typy kontrol, intervaly, retries, timeouty a skutečná zpoždění alarmů.](MadMike/Monitoring/Uptime-Kuma.md?plain=1#L146)
- [ ] [Ověřit současné notifikační cíle.](MadMike/Monitoring/Uptime-Kuma.md?plain=1#L147)
- [ ] [Prakticky otestovat jeden alarm `DOWN` a následnou recovery zprávu.](MadMike/Monitoring/Uptime-Kuma.md?plain=1#L148)
- [ ] [Zdokumentovat samostatnou zálohu a obnovu konfigurace Kumy, pokud existuje.](MadMike/Monitoring/Uptime-Kuma.md?plain=1#L149)

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

- [ ] [Vybrat jednoduchou cílovou náhradu přímého veřejného RDP k PREMIERu podle skutečného způsobu práce účetní.](MadMike/Pristupy/README.md?plain=1#L131)
- [ ] [Definovat a prakticky ověřit minimální nouzový postup pro obnovu administrátorského přístupu po současné ztrátě notebooku a telefonu.](MadMike/Pristupy/README.md?plain=1#L132)
- [ ] [Vytvořit bezpečný přehled kritických identit po kategoriích, který bez uživatelských jmen a tajných hodnot eviduje odpovědnost, stav MFA, stav recovery a datum posledního ověření.](MadMike/Pristupy/README.md?plain=1#L133)

## MadMike / Servery

### Interní DNS, NPM a HTTPS

- [ ] [Ověřit současnou verzi NPM, stav všech proxy hostů a datum poslední úspěšné obnovy wildcard certifikátu.](MadMike/Servery/DNS-NPM-HTTPS.md?plain=1#L212)
- [ ] [Ověřit, že Cloudflare API token je uložený v Bitwardenu a případný nezašifrovaný TXT soubor byl odstraněn.](MadMike/Servery/DNS-NPM-HTTPS.md?plain=1#L213)

### PVE Dell

- [ ] [Zjistit původ a účel Dell / VM400.](MadMike/Servery/PVE-Dell.md?plain=1#L218)
- [ ] [Ověřit aktuální verzi a konfiguraci PVE Dell, VM200, storage a sítě proti živému systému.](MadMike/Servery/PVE-Dell.md?plain=1#L219)
- [ ] [Připravit a schválit bezpečný migrační plán z dnešních dvou mirrorů na jeden pool ze čtyř 8TB disků, včetně cílové topologie, zálohy, obnovy a rollbacku.](MadMike/Servery/PVE-Dell.md?plain=1#L220)

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

- [ ] [Ověřit živý výběr objektů backup jobu a odstranit případnou neexistující položku CT100.](MadMike/Zalohy/PBS-DR.md?plain=1#L283)
- [ ] [Ověřit poslední úspěšné běhy Backup, Verify, Prune a Garbage Collection.](MadMike/Zalohy/PBS-DR.md?plain=1#L284)
- [ ] [Ověřit aktuální obsazení datastore `backup`.](MadMike/Zalohy/PBS-DR.md?plain=1#L285)
- [ ] [Ověřit plánování a poslední běh scrubů na `tank-pbs` a `tank-nas`.](MadMike/Zalohy/PBS-DR.md?plain=1#L286)
- [ ] [Ověřit SMART a teploty čtyř SAS disků a systémového SSD proti živému stavu.](MadMike/Zalohy/PBS-DR.md?plain=1#L287)
- [ ] [Ověřit persistentní Docker data a mounty VM510 a provést testovací restore.](MadMike/Zalohy/PBS-DR.md?plain=1#L288)
- [ ] [Prakticky ověřit start PVE Dell, VM200 a datastore po úplném výpadku napájení.](MadMike/Zalohy/PBS-DR.md?plain=1#L289)
- [ ] [Stanovit rozumnou četnost opakovaných testů obnovy.](MadMike/Zalohy/PBS-DR.md?plain=1#L290)
- [ ] [Stanovit společné RPO, RTO, pořadí obnovy a hranici stáří záloh vyžadující zásah.](MadMike/Zalohy/PBS-DR.md?plain=1#L291)
- [ ] [Určit původ nejasných/orphaned backup groups a samostatně ověřit účel Dell / VM400 jako odlišného objektu.](MadMike/Zalohy/PBS-DR.md?plain=1#L292)
- [ ] [Zdokumentovat bezpečné umístění recovery materiálů hostitelů bez zveřejnění tajných údajů.](MadMike/Zalohy/PBS-DR.md?plain=1#L293)
- [ ] [Rozhodnout o klientském šifrování PBS a při jeho použití bezpečně uložit recovery klíč.](MadMike/Zalohy/PBS-DR.md?plain=1#L294)
- [ ] [Určit odpovědnost a dostupnost místního zásahu u Richarda.](MadMike/Zalohy/PBS-DR.md?plain=1#L295)

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

- [ ] [Udělat úplný seznam aktivních routerů, switchů, AP a jejich napájení.](Rybniky-Amerika/Hardware.md?plain=1#L41)
- [ ] [V Airtable určit a rezervovat konkrétní hEX S (2025) a vhodná AP až podle inventury.](Rybniky-Amerika/Hardware.md?plain=1#L42)
- [ ] [Ověřit přesné modely a stav skladových AP uvažovaných pro nasazení.](Rybniky-Amerika/Hardware.md?plain=1#L43)
- [ ] [Ověřit dostupné SFP moduly, typ optiky, PoE zdroje, přepěťové ochrany a uzemnění.](Rybniky-Amerika/Hardware.md?plain=1#L44)
- [ ] [Před návrhem sloupu ověřit přesné schopnosti konkrétního mANTBoxu nebo jiného rádia.](Rybniky-Amerika/Hardware.md?plain=1#L45)

### Plán rekonstrukce

- [ ] [Přidělit cílový LAN prefix Rybníků v rámci společného adresního plánu.](Rybniky-Amerika/Plan-rekonstrukce.md?plain=1#L127)
- [ ] [Po inventuře sepsat jednotlivé nutné výjimky z privátní sítě Rybníků do HOME; bez doložené potřeby zůstane výchozí `deny`.](Rybniky-Amerika/Plan-rekonstrukce.md?plain=1#L128)
- [ ] [Podle inventury doplnit konkrétní testovací checklist, časový limit a kabelový postup rollbacku pro etapu 2.](Rybniky-Amerika/Plan-rekonstrukce.md?plain=1#L129)
- [ ] [Vybrat pilotní větev pro odstranění prvního NAT ostrova.](Rybniky-Amerika/Plan-rekonstrukce.md?plain=1#L130)
- [ ] [V dokumentu Mikr navrhnout závislosti a souhrnný alarm lokality.](Rybniky-Amerika/Plan-rekonstrukce.md?plain=1#L131)
- [ ] [V dokumentaci záloh MikroTiků doplnit a prakticky ověřit obnovu konfigurace Rybníků.](Rybniky-Amerika/Plan-rekonstrukce.md?plain=1#L132)

### Topologie

- [ ] [Ověřit přesný model, RouterOS a konfiguraci sektoru `AP HOME`.](Rybniky-Amerika/Topologie.md?plain=1#L68)
- [ ] [Ověřit přesný model, RouterOS a režim přijímací jednotky.](Rybniky-Amerika/Topologie.md?plain=1#L69)
- [ ] [Změřit aktuální rádiové parametry, stabilitu a reálnou propustnost přívodu.](Rybniky-Amerika/Topologie.md?plain=1#L70)
- [ ] [Určit zařízení, které dnes routuje a poskytuje DHCP, NAT a firewall.](Rybniky-Amerika/Topologie.md?plain=1#L71)
- [ ] [Zmapovat všechny další DHCP servery, NATy, aktivní rozsahy, statické IP a port-forwardy.](Rybniky-Amerika/Topologie.md?plain=1#L72)
- [ ] [Zmapovat zařízení, porty a kabely v Obýváku, Včelíně, Hospodě a Dílně.](Rybniky-Amerika/Topologie.md?plain=1#L73)
- [ ] [Ověřit stav, typ a zakončení optiky ke sloupu.](Rybniky-Amerika/Topologie.md?plain=1#L74)
- [ ] [Ověřit NVR, zařízení „Stavba“ a další klienty citlivé na změnu adresace.](Rybniky-Amerika/Topologie.md?plain=1#L75)

## Vernirovice / BESS-a-FVE

### Technologie FVE, BESS a tepelné infrastruktury

- [ ] [S dodavatelem vyřešit komunikaci baterie–střídač větší sestavy a potvrdit skutečné nabíjení, vybíjení a bezpečný lokální režim.](Vernirovice/BESS-a-FVE/Technologie.md?plain=1#L69)
- [ ] [Opsat typové štítky obou měničů a bateriových systémů a uzavřít rozpory v modelech, výkonech a kapacitách.](Vernirovice/BESS-a-FVE/Technologie.md?plain=1#L70)
- [ ] [Ověřit současný instalovaný výkon FVE panelů.](Vernirovice/BESS-a-FVE/Technologie.md?plain=1#L71)
- [ ] [Získat jednopólové schéma nebo vytvořit ověřený provozní nákres včetně jištění jednotlivých zařízení.](Vernirovice/BESS-a-FVE/Technologie.md?plain=1#L72)
- [ ] [Ověřit přesný model hlavního Shelly, znaménka měření, smartmetery obou měničů a jejich skutečnou vazbu na regulaci.](Vernirovice/BESS-a-FVE/Technologie.md?plain=1#L73)
- [ ] [Ověřit, kde a jak je při souběhu obou měničů vynucován společný exportní limit 50 kW.](Vernirovice/BESS-a-FVE/Technologie.md?plain=1#L74)
- [ ] [Ověřit současný stav, měření a fyzickou řiditelnost tepelné a wellness infrastruktury.](Vernirovice/BESS-a-FVE/Technologie.md?plain=1#L75)
- [ ] [Zapsat komunikační rozhraní a adresy zařízení bez hesel a klíčů a teprve poté připravit read-only RS485 pilot.](Vernirovice/BESS-a-FVE/Technologie.md?plain=1#L76)

### Řízení energie

- [ ] [Zdokumentovat přesný cenový vstup, současnou automatizaci a vazbu jejích entit na původní sestavu.](Vernirovice/BESS-a-FVE/Rizeni-energie.md?plain=1#L73)
- [ ] [Prakticky ověřit návrat do `Zero Export To CT`, hraniční SOC, chybějící cenová data, odmítnutý povel, ztrátu komunikace a restart Home Assistantu.](Vernirovice/BESS-a-FVE/Rizeni-energie.md?plain=1#L74)
- [ ] [Stanovit a otestovat bezpečný ruční režim, fail-safe stav a návrat do automatiky pro obě sestavy.](Vernirovice/BESS-a-FVE/Rizeni-energie.md?plain=1#L75)
- [ ] [Před koordinací obou baterií prokázat bezpečné vynucení společného exportního limitu 50 kW nezávisle na pomalé nadřazené optimalizaci.](Vernirovice/BESS-a-FVE/Rizeni-energie.md?plain=1#L76)
- [ ] [Po vyřešení problému dodavatelem read-only způsobem ověřit rozhraní, limity a skutečné chování větší sestavy.](Vernirovice/BESS-a-FVE/Rizeni-energie.md?plain=1#L77)
- [ ] [Navrhnout, otestovat a zdokumentovat ručně aktivovatelný režim Maximální záloha.](Vernirovice/BESS-a-FVE/Rizeni-energie.md?plain=1#L78)
- [ ] [Po uzavření výběrového řízení zapsat skutečný nákupní a výkupní produkt a teprve poté připravit spotové řízení.](Vernirovice/BESS-a-FVE/Rizeni-energie.md?plain=1#L79)
- [ ] [Zavést měsíční ekonomické vyhodnocení a ověřovat čistý přínos jednotlivých strategií.](Vernirovice/BESS-a-FVE/Rizeni-energie.md?plain=1#L80)

## Vernirovice / Home-Assistant

### Hardware a migrace

- [ ] [Ověřit verzi Home Assistant OS, Core a Supervisor na současném Raspberry Pi 5.](Vernirovice/Home-Assistant/Hardware-a-migrace.md?plain=1#L82)
- [ ] [Ověřit obsah zálohy a ochranu dat add-onů InfluxDB, Grafana a MQTT.](Vernirovice/Home-Assistant/Hardware-a-migrace.md?plain=1#L83)
- [ ] [Připravit Qotom s Home Assistant OS a ověřit jeho síťové a úložné parametry.](Vernirovice/Home-Assistant/Hardware-a-migrace.md?plain=1#L84)
- [ ] [Doplnit konkrétní předmigrační kontrolní seznam současných funkcí.](Vernirovice/Home-Assistant/Hardware-a-migrace.md?plain=1#L85)
- [ ] [Stanovit konkrétní časové a funkční kritérium pro rollback.](Vernirovice/Home-Assistant/Hardware-a-migrace.md?plain=1#L86)
- [ ] [Po úspěšné migraci provést a zdokumentovat přejímací test podle tohoto dokumentu.](Vernirovice/Home-Assistant/Hardware-a-migrace.md?plain=1#L87)

### Služby a integrace

- [ ] [Ověřit živý seznam aktivních integrací, add-onů a jejich aktuální verze.](Vernirovice/Home-Assistant/Sluzby-a-integrace.md?plain=1#L71)
- [ ] [Ověřit konfiguraci, retenci, velikost databází a zálohování InfluxDB.](Vernirovice/Home-Assistant/Sluzby-a-integrace.md?plain=1#L72)
- [ ] [Ověřit hlavní Grafana dashboardy, zdroje dat a jejich obnovitelnost.](Vernirovice/Home-Assistant/Sluzby-a-integrace.md?plain=1#L73)
- [ ] [Ověřit účel, klienty, autentizaci a zálohování MQTT brokeru bez uložení tajných údajů do dokumentace.](Vernirovice/Home-Assistant/Sluzby-a-integrace.md?plain=1#L74)
- [ ] [Ověřit přesný stav entit a ovládání původní i větší bateriové sestavy.](Vernirovice/Home-Assistant/Sluzby-a-integrace.md?plain=1#L75)
- [ ] [Ověřit, zda je `IOTVL` stále samostatná aktivní síť a jaký používá rozsah.](Vernirovice/Home-Assistant/Sluzby-a-integrace.md?plain=1#L76)
- [ ] [Ověřit současný způsob lokálního a vzdáleného přístupu včetně Home Assistant Cloud.](Vernirovice/Home-Assistant/Sluzby-a-integrace.md?plain=1#L77)
- [ ] [Zapojit dostupnost instance do společného monitoringu a schváleného notifikačního systému.](Vernirovice/Home-Assistant/Sluzby-a-integrace.md?plain=1#L78)
- [ ] [Před případným zavedením RS485/Modbus připravit samostatný read-only test, přejímací kritéria a rollback.](Vernirovice/Home-Assistant/Sluzby-a-integrace.md?plain=1#L79)
- [ ] [Zdokumentovat pouze entity skutečně důležité pro automatizace, řízení a diagnostiku.](Vernirovice/Home-Assistant/Sluzby-a-integrace.md?plain=1#L80)
