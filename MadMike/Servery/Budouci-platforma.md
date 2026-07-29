# Budoucí produkční serverová platforma

## Stav rozhodnutí

Tento dokument zachycuje požadavky na případného nástupce domácího produkčního serveru [PVE Ryzen](PVE-Ryzen.md).

- Současný Ryzen zatím pro provozované služby dostačuje.
- Okamžitá výměna serveru není naplánovaná.
- Konkrétní základní deska, procesor ani termín nákupu nejsou vybrané.
- Offsite PBS a disaster recovery zůstávají samostatnou rolí serveru [PVE Dell](PVE-Dell.md).

## Kdy má upgrade smysl

Upgrade se zahájí až kvůli konkrétnímu a doloženému limitu, například:

- nedostatečné kapacitě CPU, RAM, úložiště nebo sítě pro skutečně provozované služby;
- chybějící možnosti rozšíření pro nový reálný workload;
- zhoršující se spolehlivosti nebo obtížné opravitelnosti současného hardwaru;
- ekonomicky výhodné obnově v okamžiku, kdy už současná platforma omezuje provoz.

Samotná dostupnost zajímavé desky, procesoru nebo levného serveru není důvodem k migraci. Před výběrem nové platformy se nejdřív změří skutečný limit současného Ryzenu.

## Preferovaný charakter platformy

Budoucí produkční server má být především praktický:

- běžný, úsporný a snadno opravitelný hardware;
- nízká spotřeba v klidu a rozumný výkon jednoho jádra;
- standardní a dobře dostupné paměti;
- dostatečná kapacita RAM a rozumná rezerva pro další VM nebo kontejnery;
- možnost rozšířit úložiště, síť nebo doplnit akcelerátor bez výměny celé platformy;
- preferovaná integrovaná síť alespoň 2,5 Gb/s, případně možnost snadného doplnění rychlejšího adaptéru;
- bezproblémový provoz Proxmox VE, ZFS a stávajících produkčních služeb.

Rozšiřitelnost, spotřeba a dostupnost náhradních dílů jsou důležitější než označení platformy jako serverové.

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
- monitorovací VM a související infrastrukturu;
- další současné podpůrné služby Proxmoxu.

Současně má ponechat rozumnou rezervu pro:

- další menší VM nebo kontejnery;
- případné n8n;
- menší lokální AI;
- další službu, která přinese konkrétní užitek.

Nejde o požadavek provozovat všechny tyto úlohy okamžitě. Jsou to pouze směry, které nemá budoucí platforma předem zablokovat.

## Historické a průzkumné varianty

Dříve posuzované serverové platformy Supermicro a Xeon patřily ke starší koncepci PBS/DR uzlu v paneláku. Nejsou aktuálně vybraným nástupcem PVE Ryzen.

Stejně tak jednotlivé nabídky desek B550, B660, procesorů a použitých serverů představují pouze průzkum trhu. Dokud nebude doložený konkrétní limit a schválená sestava, nesmí být žádný z těchto kandidátů vedený jako rozhodnuté řešení.

## Kontroly před budoucím výběrem

1. Změřit běžné a špičkové využití CPU, RAM, disků a sítě na PVE Ryzen.
2. Určit konkrétní workload, který změnu vyvolává.
3. Ověřit potřebný počet disků, PCIe slotů, M.2 pozic a síťových portů.
4. Stanovit potřebnou kapacitu RAM včetně rozumné rezervy.
5. Ověřit kompatibilitu vybrané platformy s Proxmox VE, ZFS a plánovanými akcelerátory.
6. Teprve potom porovnat konkrétní nové a použité sestavy podle ceny, spotřeby a opravitelnosti.
