# Budoucí produkční serverová platforma

## Schválený směr

Upgrade domácího [PVE Ryzen](PVE-Ryzen.md) je plánovaný nenásilně, bez pevného termínu a podle vhodné aktuální nabídky.

- zůstává se na platformě AMD AM4;
- preferovaný procesor a současný sweet spot je Ryzen 7 5700G;
- cílem je základní deska s čipsetem B550;
- ideální deska má čtyři DIMM sloty pro DDR4 a integrovanou 2,5GbE síť;
- konkrétní model desky ani okamžik nákupu zatím nejsou vybrané.

Současný Ryzen 3 4300G provozované služby zvládá, takže není důvod kupovat nevhodný kompromis jen kvůli rychlosti. Zároveň už B550 a Ryzen 7 5700G nejsou pouhou průzkumnou variantou, ale schváleným cílovým směrem.

M4-ATX je samostatné zlepšení napájení současného serveru. Jeho objednání a následný test jsou vedené v [PVE-Ryzen.md](PVE-Ryzen.md), nikoliv jako podmínka výměny celé platformy.

## Důvod této volby

- AM4 umožní dál využít stávající DDR4 a drží náklady i složitost nízko.
- Ryzen 7 5700G nabízí výraznou rezervu proti současnému 4300G a současně integrovanou grafiku.
- B550 je běžná, dobře dostupná a opravitelná platforma bez závislosti na speciálním serverovém hardwaru.
- Čtyři DIMM sloty umožní rozšířit paměť bez okamžité výměny všech modulů.
- Integrované 2,5GbE omezí potřebu zabírat další PCIe slot síťovou kartou.

## Požadavky na konkrétní nabídku

Před nákupem se u konkrétní desky a sestavy ověří:

1. podpora Ryzen 7 5700G včetně potřebné verze BIOSu;
2. čtyři fyzické DIMM sloty a kompatibilita se stávající DDR4;
3. model integrovaného 2,5GbE řadiče a jeho bezproblémová podpora v Proxmoxu;
4. počet M.2, SATA a použitelných PCIe slotů po osazení;
5. IOMMU a další vlastnosti potřebné pro současné VM;
6. rozměry desky, chlazení, spotřeba a kompatibilita se skříní a napájením;
7. stav, záruka a celková cena nabídky.

Tento seznam je kontrolou při konkrétní nákupní příležitosti, nikoliv sadou trvale otevřených položek v centrálním `TODO.md`.

## Co není podmínkou

- ECC není pro tuto roli povinné.
- IPMI ani jiné plnohodnotné vzdálené řízení není priorita.
- Staré vícesocketové Xeony, hlučné rackové servery a energeticky náročné platformy nejsou běžnou cestou upgradu jen proto, že jsou levné.
- Drahé nebo obtížně dostupné speciální paměti nemají být zbytečnou podmínkou.
- Samostatná grafická karta nebo AI akcelerátor se pořídí až pro konkrétní využití.

## Výhled zátěže

Nová platforma musí bezpečně zvládnout současné produkční role:

- Nextcloud;
- Windows VM s účetním systémem PREMIER;
- VM510 s NPM a monitoringem;
- další současné podpůrné služby Proxmoxu.

Současně má ponechat rozumnou rezervu pro:

- další menší VM nebo kontejnery;
- případné n8n;
- menší lokální AI;
- další službu, která přinese konkrétní užitek.

Nejde o požadavek provozovat všechny tyto úlohy okamžitě. Jsou to směry, které nemá cílová platforma předem zablokovat.

## Historické a opuštěné směry

Dříve posuzované platformy Supermicro a Xeon patřily převážně ke starší koncepci PBS/DR uzlu. Nejsou cílovým nástupcem PVE Ryzen.

Intel/B660, starší serverové sestavy a jednotlivé jiné bazarové nabídky zůstávají historií průzkumu trhu. Současný schválený směr je AM4, B550 a preferovaně Ryzen 7 5700G.
