# Budoucí produkční serverová platforma

## Schválený směr

Upgrade domácího [PVE Ryzen](PVE-Ryzen.md) je plánovaný nenásilně, bez pevného termínu a podle vhodné aktuální nabídky.

- zůstává se na platformě AMD AM4;
- preferovaný procesor a současný sweet spot je Ryzen 7 5700G;
- cílem je základní deska s čipsetem B550;
- ideální deska má čtyři DIMM sloty pro DDR4 a integrovanou 2,5GbE síť;
- konkrétní model desky ani okamžik nákupu zatím nejsou vybrané.

Současný Ryzen 3 4300G provozované služby zvládá, takže není důvod kupovat nevhodný kompromis jen kvůli rychlosti. B550 a Ryzen 7 5700G už nejsou průzkumná varianta, ale schválený cílový směr.

Po upgradu má současná platforma A520 + Ryzen 3 4300G zůstat jako vypnutá náhradní a experimentální platforma. Nemusí být trvale zapnutá ani předem plně osazená.

M4-ATX je samostatné zlepšení napájení současného serveru. Jeho objednání, zapojení a výpadkový test jsou vedené v [PVE-Ryzen.md](PVE-Ryzen.md), nikoliv jako podmínka výměny celé platformy.

## Důvod této volby

- AM4 umožní dál využít stávající DDR4 a drží náklady i složitost nízko.
- Ryzen 7 5700G nabízí výraznou rezervu proti současnému 4300G a integrovanou grafiku.
- B550 je běžná, dostupná a opravitelná platforma bez závislosti na speciálním serverovém hardwaru.
- Čtyři DIMM sloty umožní rozšířit paměť bez okamžité výměny všech modulů.
- Integrované 2,5GbE omezí potřebu zabírat další PCIe slot síťovou kartou.

## Požadavky na konkrétní nabídku

Před nákupem se u konkrétní desky a sestavy ověří:

1. podpora Ryzen 7 5700G včetně potřebné verze BIOSu;
2. čtyři fyzické DIMM sloty a kompatibilita se stávající DDR4;
3. model integrovaného 2,5GbE řadiče a jeho podpora v používané verzi Proxmoxu;
4. počet M.2, SATA a použitelných PCIe slotů po osazení;
5. IOMMU a další vlastnosti potřebné pro současné VM;
6. rozměry desky, chlazení, spotřeba a kompatibilita se skříní a M4-ATX;
7. stav, záruka a celková cena nabídky.

Tento seznam je kontrolou při konkrétní nákupní příležitosti, nikoliv sadou trvale otevřených položek v centrálním `TODO.md`.

## Co není podmínkou

- ECC není pro tuto roli povinné.
- IPMI ani jiné plnohodnotné vzdálené řízení není priorita.
- Staré vícesocketové Xeony, hlučné rackové servery a energeticky náročné platformy nejsou běžnou cestou upgradu jen proto, že jsou levné.
- Drahé nebo obtížně dostupné speciální paměti nemají být zbytečnou podmínkou.
- Samostatná grafická karta nebo AI akcelerátor se pořídí až pro konkrétní využití.
- 10Gb síť není současný požadavek; cílovou rychlostí serveru je 2,5 Gb/s.

## Výhled zátěže

Nová platforma musí bezpečně zvládnout současné produkční role:

- Nextcloud;
- Windows VM s účetním systémem PREMIER;
- VM510 s NPM a monitoringem;
- další současné podpůrné služby Proxmoxu.

Současně má ponechat rozumnou rezervu pro další menší VM nebo kontejnery a případnou službu s konkrétním užitkem. N8n nebo menší lokální AI jsou pouze možné budoucí zátěže, nikoliv důvod k okamžitému předimenzování.

## Migrační runbook

### Příprava

1. Zaznamenat živou verzi PVE, síťová rozhraní, storage a konfigurace všech produkčních VM.
2. Ověřit poslední úspěšné PBS backupy VM401, VM501 a VM510 a dostupnost offsite PBS.
3. Provést základní kontrolu obou ZFS poolů, SMART a systémového NVMe.
4. Zaznamenat zapojení disků, SATA portů, napájení a síťového kabelu.
5. Ověřit BIOS cílové desky a připravit podporovaný CPU ještě před demontáží funkční platformy.
6. Stanovit časové kritérium pro rollback a ponechat původní A520 + 4300G ve stavu umožňujícím návrat.

### Provedení

1. Korektně odstavit produkční VM a hostitele.
2. Neměnit současně rozložení ZFS, identitu VM ani adresaci; cílem je výměna platformy, ne několik migrací v jednom zásahu.
3. Připojit systémový NVMe a datové disky podle zaznamenaného zapojení.
4. V BIOSu ověřit boot, virtualizaci, IOMMU, chování po návratu napájení a rozpoznání všech zařízení.
5. Spustit PVE a nejprve ověřit síť, storage a ZFS bez startu všech VM.
6. Produkční VM spouštět jednotlivě a po každé ověřit její základní i aplikační funkci.

### Přejímka

- PVE je dostupný nouzově přes interní IP i běžně přes `pveryzen.mikehub.cz`.
- Oba ZFS pooly jsou `ONLINE` bez nových read/write/checksum chyb.
- VM401, VM501 a VM510 odpovídají doloženým konfiguracím a prošly aplikační kontrolou ve svých projektech.
- QEMU Guest Agent odpovídá tam, kde je nasazený.
- NPM, interní HTTPS a monitoring fungují.
- Síť běží požadovanou rychlostí a nejsou zjevné chyby linky.
- Teploty, spotřeba a stabilita jsou přijatelné.
- Po stabilizaci proběhne nový PBS backup a kontrola jeho výsledku.

### Rollback

Pokud nový host nespolehlivě bootuje, nevidí některý disk, ZFS není v očekávaném stavu nebo selže zásadní produkční funkce, další změny se zastaví. Původní disky se nemění ani neinicializují. Podle předem stanoveného plánu se vrátí původní A520 + 4300G nebo se použije obnova z PBS.

## Historické a opuštěné směry

Dříve posuzované platformy Supermicro a Xeon patřily převážně ke starší koncepci PBS/DR uzlu. Nejsou cílovým nástupcem PVE Ryzen.

Intel/B660, starší serverové sestavy a jednotlivé jiné bazarové nabídky zůstávají historií průzkumu trhu. Současný schválený směr je AM4, B550 a preferovaně Ryzen 7 5700G.
