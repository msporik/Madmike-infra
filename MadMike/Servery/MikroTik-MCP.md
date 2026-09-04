# MikroTik MCP

> Stav prakticky ověřen **2026-09-04**. Dokument popisuje aktuální produkční způsob zpřístupnění MikroTik MCP pro AI klienty; hesla, tokeny a další tajné hodnoty zde nejsou uvedené.

## Účel

VM511 poskytuje read-only MCP vrstvu nad MikroTik RouterOS tak, aby ChatGPT a další MCP klienti mohli bezpečně číst stav routerů bez ručního kopírování výpisů.

První prakticky ověřené zařízení je hlavní domácí RB5009.

## Aktuální architektura

```text
ChatGPT / další vzdálený MCP klient
→ HTTPS mikrotik-mcp.mikehub.cz
→ Cloudflare Tunnel mikrotik-mcp
→ cloudflared na VM511
→ http://localhost:8000/mcp
→ @usex/mikrotik-mcp 5.5.0 [READ-ONLY]
→ SSH mcp-read@192.168.89.1:7405
→ RB5009
```

VM511:

- VMID: `511` na PVE Ryzen;
- hostname: `mikrotik-mcp`;
- IP: `192.168.89.36`;
- Debian: `13.6`;
- Bun: `1.3.14`;
- MCP: `@usex/mikrotik-mcp` `5.5.0`;
- HTTP MCP endpoint lokálně: `http://0.0.0.0:8000/mcp`;
- veřejný hostname: `https://mikrotik-mcp.mikehub.cz/mcp`;
- transport: `streamable-http`.

## Read-only ochrana

Ochrana je záměrně dvouvrstvá.

### 1. MCP server

Produkční služba se spouští s parametrem:

```text
--read-only
```

Při ověření server hlásil:

```text
385 tools, 39 prompts, 7 app views (streamable-http) [READ-ONLY]
```

Za správnou kontrolu read-only režimu se považuje startovní hláška serveru s `[READ-ONLY]`. Příkaz `mikrotik-mcp tools` vypisuje katalog dostupných nástrojů balíčku včetně WRITE a DESTRUCTIVE položek a sám o sobě neprokazuje, které nástroje jsou registrované v běžící read-only session.

### 2. RouterOS účet

Na hlavním RB5009 existuje účet `mcp-read` ve skupině stejného názvu. Ověřená policy skupiny je pouze:

```text
ssh,read
```

Ostatní relevantní práva včetně `write`, `reboot`, `policy`, `password`, `sniff`, `sensitive`, `api` a `rest-api` jsou zakázaná. Přístup uživatele je omezený na VM511.

Tato vrstva musí zůstat read-only i kdyby se někdy změnila konfigurace MCP serveru.

## Připojení k hlavnímu RB5009

Ověřená cílová konfigurace:

```text
host: 192.168.89.1
username: mcp-read
SSH port: 7405
```

Autentizace používá uživatelské jméno a heslo, nikoliv SSH klíč. Heslo není v tomto repozitáři.

Přímé SSH přihlášení z VM511 i `mikrotik-mcp auth-check` byly ověřené. První end-to-end test z ChatGPT přes veřejný MCP konektor úspěšně vrátil system identity hlavního routeru:

```text
Na Zabrani 26, Sporik
```

## systemd služba

MCP běží trvale jako:

```text
/etc/systemd/system/mikrotik-mcp.service
```

Použitá binárka:

```text
/home/madmike/.bun/bin/mikrotik-mcp
```

Služba používá:

```text
serve --transport streamable-http --mcp-port 8000 --mcp-allowed-hosts mikrotik-mcp.mikehub.cz --read-only
```

Připojovací hodnoty jsou načítané z:

```text
/etc/mikrotik-mcp.env
```

Soubor obsahuje `MIKROTIK_HOST`, `MIKROTIK_USERNAME`, `MIKROTIK_PORT` a `MIKROTIK_PASSWORD`, vlastní ho `root:root` a má práva `0600`. Jeho obsah se do GitHubu nekopíruje.

Ověřený stav služby:

```text
Loaded: loaded; enabled
Active: active (running)
transport=streamable-http
[READ-ONLY]
```

Běžná kontrola:

```bash
sudo systemctl status mikrotik-mcp --no-pager -l
curl http://127.0.0.1:8000/health
```

Health endpoint má vrátit:

```text
OK
```

## Cloudflare Tunnel

Pro veřejný přístup AI klientů byl vytvořen samostatný Cloudflare Tunnel `mikrotik-mcp` s konektorem `cloudflared` přímo na VM511.

Publikovaná route:

```text
mikrotik-mcp.mikehub.cz
→ HTTP
→ localhost:8000
```

Cloudflare ukončuje veřejné HTTPS; mezi `cloudflared` a lokálním MCP serverem je HTTP. Na routeru se kvůli tomuto endpointu neotevírá veřejný port a cesta není závislá na Home Assistantu ani NPM.

Interní wildcard DNS `*.mikehub.cz → 192.168.89.35` může z domácí LAN stejný hostname směrovat na NPM. Lokální `curl https://mikrotik-mcp.mikehub.cz/...` proto nemusí testovat Cloudflare Tunnel; pro ověření veřejné cesty je nutné použít skutečně externího klienta nebo veřejný MCP handshake.

## ChatGPT

V ChatGPT byl vytvořen vlastní konektor:

```text
MikroTik MCP
```

URL serveru:

```text
https://mikrotik-mcp.mikehub.cz/mcp
```

Při nasazení byla zvolena volba bez aplikační autentizace. End-to-end čtení z RB5009 bylo prakticky ověřené.

- [ ] Posoudit a doplnit vhodnou autentizační vrstvu veřejného MCP endpointu, která bude kompatibilní s používanými MCP klienty. Read-only na MCP i RouterOS snižuje dopad, ale veřejný endpoint bez aplikační autentizace není cílový dlouhodobý bezpečnostní stav.

## Přidávání dalších routerů

Více routerů má být řešeno podporovanou multi-device konfigurací MCP, nikoliv samostatnou VM nebo novým veřejným endpointem pro každý router.

Před přidáním dalšího zařízení musí být na RouterOS vytvořen samostatný read-only účet nebo ekvivalentně omezený přístup. Tajné hodnoty patří mimo repozitář.

- [ ] Navrhnout a prakticky ověřit jednotný multi-device config pro další MikroTik routery bez oslabení read-only ochrany.

## Poučení z nasazení

Během prvního nasazení vzniklo několik slepých odboček. Tyto body jsou důležité pro další práci:

1. **Nezaměňovat interní HTTPS za veřejnou dostupnost.** `*.mikehub.cz` je v domácí síti split-horizonově směrované na NPM. Úspěšný lokální `curl` přes HTTPS proto neprokazuje, že se k endpointu dostane ChatGPT z internetu.
2. **Před návrhem ingressu nejprve číst existující dokumentaci.** U MadMike jsou běžné administrační služby přes NPM interní; veřejné výjimky jsou řešené samostatně. Nasazení se zbytečně stočilo k NPM a Home Assistantu, než byl z dokumentace dohledán funkční vzor Cloudflare Tunnel přímo u cílové služby.
3. **Home Assistant není tranzitní vrstva pro MikroTik MCP.** Existující HA tunnel byl užitečný jako vzor, ale MikroTik MCP má vlastní tunnel a vlastní konektor na VM511.
4. **NPM zůstává interní reverse proxy.** Vytvořený proxy host `mikrotik-mcp.mikehub.cz → 192.168.89.36:8000` může být užitečný pro interní HTTPS, ale není součástí veřejné cesty ChatGPT → MCP.
5. **`mikrotik-mcp tools` není test read-only režimu.** Správný důkaz je start serveru s `[READ-ONLY]` a omezeným počtem registrovaných nástrojů.
6. **Single-device provoz nepřekombinovat konfigurákem.** Pro první RB5009 se ověřila jednoduchá kombinace `MIKROTIK_*` proměnných + `--read-only`; pokusy s neověřeným `config.json` vedly k chybnému defaultu `127.0.0.1:22` a zbytečnému ladění.
7. **Trvalou službu vytvořit až po ověření transportu.** Ruční test `streamable-http` + `/health` nejprve potvrdil funkci, teprve potom vznikla systemd služba.
8. **Při dalším zásahu nepokračovat metodou pokus–grep–pokus.** Nejprve použít autoritativní dokumentaci projektu a dokumentaci konkrétní verze MCP; teprve potom dávat příkaz k provedení.

## Provozní kontrola po restartu VM511

1. Ověřit službu:

```bash
sudo systemctl status mikrotik-mcp --no-pager -l
```

2. Ověřit lokální health:

```bash
curl http://127.0.0.1:8000/health
```

3. V Cloudflare ověřit tunnel `mikrotik-mcp` jako `Healthy`.
4. Z AI klienta provést neškodný read test, například system identity.
5. Při problému nejprve oddělit vrstvy: MCP služba → SSH k routeru → cloudflared → veřejný MCP klient.
