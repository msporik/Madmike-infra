# Přístup a uživatelé

## Webový přístup

Produkční Nextcloud je dostupný na:

`https://cloud.madmike.cz`

Podle potvrzení správce z 29. 7. 2026 je služba publikovaná přímo na VM401 přes Apache, nikoli přes interní Nginx Proxy Manager.

Poslední doložený stav potvrzuje HTTPS certifikát Let's Encrypt spravovaný pomocí Certbotu na VM401. **Vyžaduje ověření v živém systému.** Přesný název certifikátu, Apache VirtualHost, současná platnost, automatická obnova, veřejné DNS a pravidla NAT/firewallu.

## Publikační cesta

Poslední doložený princip:

```text
internet
→ veřejné DNS cloud.madmike.cz
→ hraniční NAT/firewall
→ VM401 / Apache / HTTPS
→ Nextcloud
```

Konkrétní veřejná IP, port-forward pravidla a firewallová politika se nesmějí odhadovat. Po živém ověření se doplní jejich bezpečný popis bez tajných hodnot. Společná zásada je, že veřejně dostupný Nextcloud je vědomá výjimka; administrační služby infrastruktury veřejné být nemají.

## Bezpečná diagnostika přístupu

### Služba není dostupná z internetu

1. Zjistit, zda problém nastává i z jiné internetové přípojky, nikoli jen z domácí LAN.
2. Ověřit DNS záznam `cloud.madmike.cz` a porovnat jej s očekávanou veřejnou cestou.
3. Ověřit dosažitelnost VM401 a Apache z interní sítě.
4. Ověřit stav Nextcloudu podle [Provozu a úložiště](Provoz-a-uloziste.md).
5. Pokud interní služba funguje, zkontrolovat NAT/firewall a veřejné HTTPS.
6. Neměnit současně DNS, NAT, Apache i certifikát; nejprve určit vrstvu poruchy.

Selhání přístupu z domácí LAN při funkčním přístupu z mobilních dat může být problém hairpin NAT nebo interního DNS, nikoli výpadek Nextcloudu.

### Kontrola Apache a HTTPS na VM401

```bash
systemctl status apache2 --no-pager
apache2ctl -S
sudo certbot certificates
systemctl list-timers --all | grep -i certbot
```

Názvy balíčků a timeru se mohou podle živého systému lišit. Výstupy se před sdílením kontrolují, protože konfigurace může obsahovat interní údaje.

Bezpečný test obnovy certifikátu se provádí pouze podporovaným příkazem Certbotu pro nainstalovanou verzi, typicky:

```bash
sudo certbot renew --dry-run
```

Před testem se ověří současná konfigurace a způsob řešení ACME challenge. Certifikát se ručně nemaže ani nevydává znovu jen kvůli diagnostice.

### HTTPS funguje, ale Nextcloud hlásí nedůvěryhodnou doménu nebo chybný protokol

Nejdříve se ověří živá konfigurace Apache, Nextcloudu a skutečná cesta požadavku. `trusted_domains`, `overwriteprotocol` ani proxy parametry se nemění podle odhadu. NPM není součástí současné cesty a nemá se do ní přidávat pouze jako pokus o opravu.

## Současní a plánovaní uživatelé

| Uživatel | Provozní stav |
|---|---|
| `madmike` | ukládání a synchronizace vlastních souborů fungují |
| `katka` | účet, webové přihlášení, data a desktopová synchronizace ověřeny 31. 8. 2026 |
| `djlobo` | vyřazen ze současného používání; technická existence a stav účtu nejsou živě ověřené |
| dvě děti | účty jsou plán, nikoli současný stav |

Tento přehled popisuje používání potvrzené správcem. Neprokazuje aktuální technickou existenci všech účtů ani jejich oprávnění.

Účetní Nextcloud nepoužívá a služba není součástí předávání dat pro PREMIER.

## Katka – dokončení desktopového přístupu 31. 8. 2026

Ověřeno na produkční VM401:

- účet `katka` existuje a její obnovená data jsou dostupná;
- administrátorsky bylo nastaveno nové heslo; původní heslo nebylo zjišťováno ani ukládáno;
- po několika neúspěšných pokusech se aktivovala standardní brute-force ochrana Nextcloudu; blokace byla po identifikaci zdrojové IP bezpečně resetována pomocí `occ`;
- webové přihlášení uživatele `katka` s novým heslem bylo následně úspěšně ověřeno;
- na Katčině notebooku zůstala původní instalace Nextcloud Desktop klienta i původní synchronizační složka; notebook nebyl přeinstalován;
- klient požadoval pouze nové heslo, účet ani synchronizační vztah nebyly odpojovány ani vytvářeny znovu;
- po zadání nového hesla klient navázal na `cloud.madmike.cz` a provedl synchronizaci přibližně 9,5 GB / 2688 souborů;
- synchronizace skončila stavem **„Vše synchronizováno!“** bez zjištěného hromadného mazání nebo konfliktů;
- následná kontrola potvrdila funkční data a přístup.

Stav:

```text
Katka / webový přístup       OK
Katka / desktopový klient    OK
Katka / synchronizace dat    OK
```

Důležité provozní poučení: Nextcloud Desktop používá obousměrnou synchronizaci. Při budoucí reinstalaci notebooku nebo novém párování klienta se nesmí bez kontroly připojit prázdná či jinak změněná lokální složka k produkčnímu účtu. Před takovým zásahem se ověří stav serverových dat a existující záloha.

## Správa účtů

Preferovaným běžným místem pro kontrolu účtů je administrační rozhraní Nextcloudu. Konzolové zásahy přes `occ` se provádějí z ověřeného instalačního adresáře a pod webovým uživatelem; heslo se nezadává do historie shellu ani dokumentace.

Před změnou účtu se ověří:

- přesný identifikátor účtu;
- zda je účet aktivní nebo zakázaný;
- jeho skupiny, kvóty a případná administrátorská role;
- vlastnictví dat a sdílení;
- připojené klienty, aplikační hesla a stav MFA;
- dopad změny na synchronizovaná zařízení.

Účet se nemaže jen proto, že se aktuálně nepoužívá. Nejprve se rozhodne o jeho datech, sdíleních a případném předání vlastnictví.

## Ověření účtu `djlobo`

1. Ověřit technickou existenci, stav a skupiny účtu.
2. Ověřit vlastněná data, sdílení a připojené klienty.
3. Potvrdit se správcem, zda má být účet pouze zakázaný, nebo později odstraněný.
4. Před odstraněním rozhodnout o předání či uchování dat a zneplatnit přístupy.
5. V dokumentaci uvést jen výsledek a datum ověření, nikoli tajné hodnoty nebo seznam soukromých souborů.

Dokud tato kontrola neproběhne, nelze tvrdit, že účet nemá aktivní přístup.

## MFA a recovery

**Vyžaduje ověření v živém systému.** Není doložené, zda je MFA vynucené nebo zapnuté u administrátora či běžných účtů a zda existuje ověřený recovery postup.

Před vynucením MFA:

1. identifikovat administrátorské účty;
2. zvolit podporovaný faktor pro živou verzi;
3. bezpečně uložit recovery kódy mimo GitHub;
4. ověřit nouzový přístup bez snížení zabezpečení celé služby;
5. zavádět MFA po jednotlivých účtech a vždy dokončit praktický test přihlášení.

Recovery kódy, TOTP seed ani bezpečnostní klíče se do repozitáře, chatu ani běžných poznámek nekopírují. Společné zásady jsou v projektu [Přístupy](../Pristupy/README.md).

## Aplikační hesla a klienti

**Vyžaduje ověření v živém systému.** Neexistuje kompletní inventura desktopových a mobilních klientů, jejich poslední aktivity ani aplikačních hesel.

Při kontrole se eviduje pouze:

- vlastník a účel klienta;
- typ zařízení;
- zda je stále používaný;
- datum kontroly nebo poslední smysluplné aktivity;
- zda bylo staré aplikační heslo zneplatněno.

Samotná tajná hodnota se nezapisuje. Při ztrátě zařízení se zneplatní příslušná relace nebo aplikační heslo, nikoli bezdůvodně všechny ostatní přístupy.

### Otevřené téma – mobilní Nextcloud v rodině

Desktopový přístup Katky je od 31. 8. 2026 ověřený. Samostatně zůstává otevřené dokončení mobilních klientů:

- [ ] Katka – ověřit / zprovoznit Nextcloud aplikaci v mobilu;
- [ ] dítě 1 – rozhodnout o účtu a následně nastavit mobilní Nextcloud;
- [ ] dítě 2 – rozhodnout o účtu a následně nastavit mobilní Nextcloud.

Před nasazením u dětí nejprve rozhodnout, zda budou mít vlastní Nextcloud účty, jaká data mají mít dostupná a zda se má používat automatické nahrávání fotografií. Hesla ani aplikační tokeny se do dokumentace neukládají.

## Sdílení a veřejné odkazy

**Vyžaduje ověření v živém systému.** Veřejné odkazy, externí sdílení a jejich expirace nejsou inventarizované.

Při kontrole se ověří:

- vlastník a účel sdílení;
- příjemce nebo veřejný charakter odkazu;
- oprávnění ke čtení či zápisu;
- heslo a expirace, pokud je daná verze podporuje a použití to vyžaduje;
- zda sdílení stále odpovídá provozní potřebě.

Do dokumentace se nevkládají samotné veřejné odkazy, hesla ani názvy citlivých souborů.

## Bezpečnostní hranice

- Hesla, recovery kódy, aplikační hesla, tokeny ani obsah soukromých dat se do repozitáře neukládají.
- Veřejná cesta má vést pouze k zamýšlené HTTPS službě; administrační rozhraní hostitele, databáze a SSH se tímto způsobem nepublikují.
- Změny účtů, MFA a sdílení se dělají po ověření dopadu na uživatele a synchronizovaná zařízení.
- Přímý veřejný přístup je dokumentovaná výjimka Nextcloudu, nikoli vzor pro ostatní služby.

## Otevřené kontroly

> Následující body **vyžadují ověření v živém systému**.

- [x] Opravit přihlášení Katky a ověřit následnou desktopovou synchronizaci (31. 8. 2026).
- [ ] Dokončit mobilní Nextcloud pro Katku.
- [ ] Rozhodnout a následně zprovoznit Nextcloud účty / mobilní klienty pro dvě děti.
- [ ] Ověřit aktivní účty, administrátorskou roli a skutečný stav účtu `djlobo`.
- [ ] Ověřit stav MFA a bezpečný recovery postup.
- [ ] Ověřit používaná aplikační hesla a připojené klienty bez zápisu jejich tajných hodnot.
- [ ] Ověřit současné veřejné odkazy a pravidla externího sdílení.
- [ ] Popsat a ověřit úplnou publikační cestu `cloud.madmike.cz`, včetně DNS, NAT/firewallu a Apache VirtualHostu.
- [ ] Ověřit platnost certifikátu Let's Encrypt, automatickou obnovu přes Certbot a prakticky provést bezpečný dry-run.
