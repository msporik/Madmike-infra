# OpenProject

> Stav prakticky ověřen **2026-09-14**. Dokument popisuje aktuální pilotní nasazení OpenProjectu, veřejný přístup přes Cloudflare Tunnel a napojení ChatGPT přes MCP. Hesla, API tokeny a další tajné hodnoty zde nejsou uvedené.

## Účel

OpenProject slouží jako pilotní nadřazená vrstva projektového řízení pro ověření práce s Ganttem, závislostmi a AI integrací. Praktický pilot probíhá na projektu **BESS GuZu**.

Nasazení je záměrně jednoduché: OpenProject Community běží v Docker Compose na samostatné Debian VM a vzdálený přístup je řešen přes Cloudflare Tunnel bez veřejného port-forwardingu na MikroTiku.

## VM a základní parametry

OpenProject běží na PVE Ryzen:

- VMID: `612`;
- hostname: `openproject`;
- IP: `192.168.89.37`;
- OS: Debian 13;
- CPU: 2 vCPU;
- RAM: 4 GB;
- disk: 60 GB;
- Docker: `29.8.0`;
- Docker Compose: `v5.5.1`;
- OpenProject Compose repo: `opf/openproject-docker-compose`;
- branch: `stable/17`;
- pracovní adresář: `~/openproject`.

Lokální OpenProject běží na:

```text
http://192.168.89.37:8080
```

## Aktuální architektura

```text
Internet
  ├─ https://openproject.mikehub.cz
  │    → Cloudflare Tunnel openproject-mcp
  │    → cloudflared na VM612
  │    → http://localhost:8080
  │    → OpenProject GUI/API
  │
  └─ https://openproject-mcp.mikehub.cz/mcp
       → Cloudflare Tunnel openproject-mcp
       → cloudflared na VM612
       → http://localhost:8090
       → OpenProject MCP
       → https://openproject.mikehub.cz
       → OpenProject API

LAN
  openproject.mikehub.cz
    → split DNS (*.mikehub.cz)
    → NPM 192.168.89.35
    → http://192.168.89.37:8080
    → OpenProject
```

Na MikroTiku kvůli OpenProjectu ani MCP není potřeba veřejný port-forward.

## Veřejný OpenProject

Veřejné GUI je dostupné na:

```text
https://openproject.mikehub.cz
```

Po zveřejnění přes veřejný hostname bylo nutné nastavit v `~/openproject/.env`:

```env
OPENPROJECT_HOST__NAME=openproject.mikehub.cz
OPENPROJECT_HTTPS=true
```

Po změně konfigurace se stack aplikuje přes:

```bash
sudo docker compose up -d
```

Bez správného `OPENPROJECT_HOST__NAME` OpenProject při přístupu přes jiný host vracel:

```text
Invalid host_name configuration
```

Při veřejném HTTPS s `OPENPROJECT_HTTPS=false` navíc GUI zobrazovalo upozornění na nesoulad HTTPS konfigurace.

## Cloudflare Tunnel

Pro OpenProject GUI i MCP se používá tunnel:

- název: `openproject-mcp`;
- tunnel ID: `7ebb6021-f568-4ba5-8cc4-8c0f60dd9e8f`;
- config: `/etc/cloudflared/config.yml`;
- `cloudflared` běží jako systemd služba přímo na VM612.

Aktuální ingress:

```yaml
tunnel: 7ebb6021-f568-4ba5-8cc4-8c0f60dd9e8f
credentials-file: /home/madmike/.cloudflared/7ebb6021-f568-4ba5-8cc4-8c0f60dd9e8f.json

ingress:
  - hostname: openproject-mcp.mikehub.cz
    service: http://localhost:8090

  - hostname: openproject.mikehub.cz
    service: http://localhost:8080

  - service: http_status:404
```

Ověření konfigurace:

```bash
sudo cloudflared tunnel ingress validate
```

Veřejná DNS route pro GUI byla přidána do stejného tunnelu:

```bash
cloudflared tunnel route dns openproject-mcp openproject.mikehub.cz
```

## Split DNS a NPM

V domácí síti je wildcard DNS:

```text
*.mikehub.cz → 192.168.89.35
```

To znamená, že interní klient nepoužívá pro `openproject.mikehub.cz` veřejnou Cloudflare cestu, ale skončí na Nginx Proxy Manageru.

Proto byl v NPM vytvořen Proxy Host:

- Domain: `openproject.mikehub.cz`;
- Scheme: `http`;
- Forward Hostname/IP: `192.168.89.37`;
- Forward Port: `8080`;
- wildcard certifikát: `*.mikehub.cz`;
- Force SSL: enabled;
- HTTP/2: enabled;
- Websockets Support: enabled;
- Block Common Exploits: enabled.

Ověřená interní cesta je tedy:

```text
openproject.mikehub.cz
→ 192.168.89.35 (NPM)
→ http://192.168.89.37:8080
→ OpenProject
```

Test bez autentizace:

```bash
curl -I https://openproject.mikehub.cz/api/v3
```

Správný výsledek je `HTTP 401`, protože API je dosažitelné, ale požadavek neobsahuje token.

## OpenProject MCP

Použitý MCP server:

```text
tmskln/spring-openproject-mcp-server:latest
```

Verze při ověření startovala jako:

```text
SpringOpenprojectMcpServerApplication v1.0.2-SNAPSHOT
```

MCP běží v Docker kontejneru:

```text
openproject-mcp
```

Lokální port mapping:

```text
8090 → 8080/tcp
```

Veřejný MCP endpoint:

```text
https://openproject-mcp.mikehub.cz/mcp
```

Transport:

```text
STREAMABLE
```

MCP ověřuje Bearer token vůči OpenProjectu; API token není uložený v této dokumentaci ani jako environment proměnná kontejneru.

## Aktuální spuštění MCP kontejneru

Kontejner je aktuálně vytvořen takto:

```bash
sudo docker run -d \
  --name openproject-mcp \
  -p 8090:8080 \
  -e OPENPROJECT_URL=https://openproject.mikehub.cz \
  -e SPRING_AI_MCP_SERVER_PROTOCOL=STREAMABLE \
  --tmpfs /tmp \
  docker.io/tmskln/spring-openproject-mcp-server:latest
```

Aktuální provozní parametry:

```text
OPENPROJECT_URL=https://openproject.mikehub.cz
SPRING_AI_MCP_SERVER_PROTOCOL=STREAMABLE
/tmp = tmpfs
restart policy = no
```

- [ ] Doplnit vhodnou restart policy pro `openproject-mcp`, pokud se pilot změní na trvalou službu.

## Proč MCP používá veřejný hostname OpenProjectu

Původně MCP používal:

```text
OPENPROJECT_URL=http://192.168.89.37:8080
```

Po nastavení:

```env
OPENPROJECT_HOST__NAME=openproject.mikehub.cz
OPENPROJECT_HTTPS=true
```

přestal OpenProject přímý API přístup přes interní IP akceptovat a vracel:

```text
HTTP/1.1 400 Bad Request
Invalid host_name configuration
```

Proto MCP nyní používá canonical URL:

```text
https://openproject.mikehub.cz
```

Protože se tento hostname z Docker kontejneru v LAN řeší přes split DNS na NPM, musel pro něj být vytvořen i interní NPM Proxy Host. Bez něj kontejner sice hostname přeložil na `192.168.89.35`, ale TLS skončilo chybou SNI.

Po doplnění NPM proxy vrací API přes hostname bez tokenu správné `HTTP 401` a MCP může token validovat vůči OpenProjectu.

## ChatGPT integrace

V ChatGPT je přidaný MCP konektor:

```text
mcpopenproject
```

Server URL:

```text
https://openproject-mcp.mikehub.cz/mcp
```

Autorizace používá Bearer OpenProject API token.

End-to-end stav byl **2026-09-14** prakticky ověřen. ChatGPT přes `mcpopenproject` úspěšně načetl projekty:

- `BESS GuZu` — ID `3`, aktivní, neveřejný;
- `Scrum project` — ID `2`, aktivní, veřejný;
- `Demo project` — ID `1`, aktivní, veřejný.

## Provozní kontrola

Stav OpenProject stacku:

```bash
cd ~/openproject
sudo docker compose ps
```

Stav MCP:

```bash
sudo docker ps --filter name=openproject-mcp
```

Log MCP:

```bash
sudo docker logs openproject-mcp --tail 100
```

Veřejný MCP endpoint bez tokenu:

```bash
curl -i https://openproject-mcp.mikehub.cz/mcp
```

Očekávaný výsledek bez autentizace:

```text
401 unauthorized
```

Stejně tak `401` z OpenProject API bez tokenu je očekávaný a znamená, že síťová a HTTPS cesta funguje.

## Poučení z nasazení

1. **Canonical hostname OpenProjectu je důležitý i pro MCP.** Po změně `OPENPROJECT_HOST__NAME` nelze automaticky dál používat API přes interní IP.
2. **Veřejný hostname má v LAN jinou cestu.** Kvůli split DNS jde `openproject.mikehub.cz` interně přes NPM, ne přes Cloudflare Tunnel.
3. **MCP a OpenProject GUI mají rozdílné veřejné hostname, ale sdílejí jeden Cloudflare Tunnel.** GUI jde na port `8080`, MCP na `8090`.
4. **`HTTP 401` bez tokenu je v tomto případě správný test.** Potvrzuje, že endpoint odpovídá a problém už není v DNS, TLS nebo routingu.
5. **Při změně hostname OpenProjectu testovat celý řetězec.** OpenProject GUI → interní API přes canonical hostname → MCP → veřejný MCP endpoint → ChatGPT.
6. **Tajné hodnoty nepatří do GitHubu.** API token ani Cloudflare credentials obsah tohoto dokumentu neuvádí; uvedená je pouze cesta ke credentials souboru.

## Aktuální stav

K datu **2026-09-14** je ověřeno:

- OpenProject GUI funguje interně i veřejně přes `https://openproject.mikehub.cz`;
- HTTPS konfigurace OpenProjectu odpovídá veřejnému provozu;
- split DNS + NPM cesta funguje;
- Cloudflare Tunnel pro GUI i MCP je funkční;
- MCP kontejner je `healthy`;
- MCP používá `OPENPROJECT_URL=https://openproject.mikehub.cz`;
- ChatGPT autorizace přes `mcpopenproject` funguje a projekty jsou čitelné.
