#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generuje statyczne strony serwisu z treści w dane.py.

Uruchomienie:  python3 narzedzia/generuj.py
Wynik:         pliki HTML w katalogu repozytorium.
"""

import html
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dane import MARKA, EMAIL, GITHUB, HERO, WTYCZKI, EBOOKI  # noqa: E402

KORZEN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Etykiety interfejsu w obu językach.
E = {
    "pl": {
        "kod": "pl",
        "start": "Strona główna",
        "wtyczki": "Wtyczki",
        "ebooki": "Ebooki",
        "kontakt": "Kontakt",
        "prywatnosc": "Prywatność",
        "drugi_jezyk": "English",
        "wtyczki_wstep": "Wtyczki i aplikacje, które napisałem do ekosystemu TAK. "
                         "Każda powstała, bo czegoś w ATAK-u brakowało mnie samemu.",
        "ebooki_wstep": "Książki do pobrania za darmo, w formacie PDF. "
                        "Część napisałem, część przetłumaczyłem.",
        "wiecej": "Czytaj dalej",
        "pobierz": "Pobierz PDF",
        "pobierz_maly": "Wersja lekka",
        "stron": "stron",
        "email_etykieta": "E-mail",
        "telefon_etykieta": "Telefon",
        "telefon_bez_js": "numer widoczny po włączeniu JavaScriptu",
        "zrzuty": "Zrzuty ekranu",
        "polityka_apki": "Polityka prywatności aplikacji",
        "repo": "Kod źródłowy",
        "wroc": "Wróć na stronę główną",
        "prawa_naglowek": "Prawa autorskie",
        "stopka_zastrzezenie": "Strona nie jest powiązana z TAK Product Center ani z żadną "
                               "instytucją publiczną.",
        "narzedzia_naglowek": "Narzędzia w przeglądarce",
        "narzedzia_wstep": "Rzeczy, które działają bez instalowania czegokolwiek.",
    },
    "en": {
        "kod": "en",
        "start": "Home",
        "wtyczki": "Plugins",
        "ebooki": "Books",
        "kontakt": "Contact",
        "prywatnosc": "Privacy",
        "drugi_jezyk": "Polski",
        "wtyczki_wstep": "Plugins and apps I wrote for the TAK ecosystem. Each exists because "
                         "something in ATAK was missing for me first.",
        "ebooki_wstep": "Free PDF downloads. Some I wrote, some I translated.",
        "wiecej": "Read more",
        "pobierz": "Download PDF",
        "pobierz_maly": "Light version",
        "stron": "pages",
        "email_etykieta": "Email",
        "telefon_etykieta": "Phone",
        "telefon_bez_js": "number shown once JavaScript is enabled",
        "zrzuty": "Screenshots",
        "polityka_apki": "App privacy policy",
        "repo": "Source code",
        "wroc": "Back to the home page",
        "prawa_naglowek": "Copyright",
        "stopka_zastrzezenie": "This site is not affiliated with TAK Product Center or any "
                               "public institution.",
        "narzedzia_naglowek": "Browser tools",
        "narzedzia_wstep": "Things that work without installing anything.",
    },
}

NARZEDZIA = [
    {
        "url": "kestrel/",
        "pl": ("Symulator Kestrela 5700", "Wiatromierz Kestrel w przeglądarce: te same menu "
                                          "i ten sam wyświetlacz, bez kupowania urządzenia."),
        "en": ("Kestrel 5700 simulator", "The Kestrel weather meter in a browser: the same "
                                         "menus and the same display, without buying one."),
    },
    {
        "url": "ballistics/",
        "pl": ("Kalkulator balistyczny", "Tor pocisku liczony w przeglądarce."),
        "en": ("Ballistic calculator", "Trajectory solved in the browser."),
    },
]


def u(t):
    return html.escape(str(t), quote=True)


def sciezka(jezyk, *czesci):
    if jezyk == "pl":
        return "/".join(czesci)
    return "/".join(("en",) + czesci)


def wzgledny(skad_glebokosc, do):
    """Adres do pliku `do` (licząc od korzenia) ze strony leżącej `glebokosc` katalogów w dół."""
    return "../" * skad_glebokosc + do


# --- składanie fragmentów --------------------------------------------------

def naglowek(jezyk, glebokosc, tytul, opis, druga_wersja, bez_indeksu=False):
    e = E[jezyk]
    r = lambda p: wzgledny(glebokosc, p)  # noqa: E731
    robots = '<meta name="robots" content="noindex, nofollow">\n' if bez_indeksu else ""
    return f"""<!doctype html>
<html lang="{e['kod']}">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{u(tytul)}</title>
<meta name="description" content="{u(opis)}">
{robots}
<link rel="stylesheet" href="{r('styl.css')}">
<link rel="icon" href="{r('favicon.svg')}" type="image/svg+xml">

<header class="pasek">
  <div class="szeroko">
    <a class="marka" href="{r(sciezka(jezyk, 'index.html'))}">{u(MARKA)}</a>
    <nav>
      <a href="{r(sciezka(jezyk, 'index.html'))}#wtyczki">{u(e['wtyczki'])}</a>
      <a href="{r(sciezka(jezyk, 'index.html'))}#ebooki">{u(e['ebooki'])}</a>
      <a href="{r(sciezka(jezyk, 'kontakt.html' if jezyk == 'pl' else 'contact.html'))}">{u(e['kontakt'])}</a>
    </nav>
    <span class="jezyk"><a href="{r(druga_wersja)}">{u(e['drugi_jezyk'])}</a></span>
  </div>
</header>
"""


def stopka(jezyk, glebokosc):
    e = E[jezyk]
    r = lambda p: wzgledny(glebokosc, p)  # noqa: E731
    kontakt = 'kontakt.html' if jezyk == 'pl' else 'contact.html'
    prywatnosc = 'prywatnosc.html' if jezyk == 'pl' else 'privacy.html'
    return f"""
<footer class="stopka">
  <div class="szeroko">
    <nav>
      <a href="{r(sciezka(jezyk, 'index.html'))}">{u(e['start'])}</a>
      <a href="{r(sciezka(jezyk, kontakt))}">{u(e['kontakt'])}</a>
      <a href="{r(sciezka(jezyk, prywatnosc))}">{u(e['prywatnosc'])}</a>
      <a href="{u(GITHUB)}">GitHub</a>
    </nav>
    <p>{u(MARKA)} · <a href="mailto:{u(EMAIL)}">{u(EMAIL)}</a> ·
       <span data-telefon>{u(e['telefon_bez_js'])}</span></p>
    <p>{u(e['stopka_zastrzezenie'])}</p>
  </div>
</footer>
<script src="{r('js/tel.js')}"></script>
</html>
"""


def blok(tresc):
    """Zamienia jeden element sekcji na HTML."""
    if isinstance(tresc, str):
        return f"<p>{u(tresc)}</p>"
    rodzaj = tresc[0]
    if rodzaj == "lista":
        punkty = "".join(f"<li>{u(p)}</li>" for p in tresc[1])
        return f"<ul>{punkty}</ul>"
    if rodzaj == "tabela":
        naglowki = "".join(f"<th>{u(h)}</th>" for h in tresc[1])
        wiersze = "".join(
            "<tr>" + "".join(f"<td>{u(k)}</td>" for k in w) + "</tr>" for w in tresc[2]
        )
        return f"<table><thead><tr>{naglowki}</tr></thead><tbody>{wiersze}</tbody></table>"
    raise ValueError(f"nieznany rodzaj bloku: {rodzaj}")


def sekcje_html(sekcje):
    czesci = []
    for tytul, tresci in sekcje:
        czesci.append(f"<h2>{u(tytul)}</h2>")
        for t in tresci:
            czesci.append(blok(t))
    return "\n".join(czesci)


def okruszek(jezyk, glebokosc, slady):
    e = E[jezyk]
    r = lambda p: wzgledny(glebokosc, p)  # noqa: E731
    linki = [f'<a href="{r(sciezka(jezyk, "index.html"))}">{u(e["start"])}</a>']
    for etykieta, cel in slady:
        if cel:
            linki.append(f'<a href="{r(cel)}">{u(etykieta)}</a>')
        else:
            linki.append(u(etykieta))
    return f'<div class="wasko okruszek">{" › ".join(linki)}</div>'


def drive_link(ident):
    return f"https://drive.google.com/file/d/{ident}/view"


# --- strona główna ---------------------------------------------------------

def strona_glowna(jezyk):
    e = E[jezyk]
    h = HERO[jezyk]
    kontakt = 'kontakt.html' if jezyk == 'pl' else 'contact.html'
    kat_wtyczki = 'wtyczki' if jezyk == 'pl' else 'plugins'
    kat_ebooki = 'ebooki' if jezyk == 'pl' else 'books'
    glebokosc = 0 if jezyk == "pl" else 1
    r = lambda p: wzgledny(glebokosc, p)  # noqa: E731
    druga = "en/index.html" if jezyk == "pl" else "index.html"

    czesci = [naglowek(jezyk, glebokosc, f"{MARKA} — {h['motto']}", h["motto"], druga)]

    czesci.append(f"""
<div class="hero">
  <div class="szeroko">
    <h1>{u(MARKA)}</h1>
    <p class="motto">{u(h['motto'])}</p>
    <blockquote>{u(h['cytat'])}<cite>— {u(h['cytat_autor'])}</cite></blockquote>
    <p class="robie">{u(h['robie'])}</p>
    <div class="kontakt-pasek">
      <span>{u(e['email_etykieta'])}: <a href="mailto:{u(EMAIL)}">{u(EMAIL)}</a></span>
      <span>{u(e['telefon_etykieta'])}: <span data-telefon>{u(e['telefon_bez_js'])}</span></span>
      <span><a href="{u(GITHUB)}">GitHub</a></span>
      <span><a href="{r(sciezka(jezyk, kontakt))}">{u(e['kontakt'])}</a></span>
    </div>
  </div>
</div>
""")

    # wtyczki
    karty = []
    for w in WTYCZKI:
        d = w[jezyk]
        ikona = (f'<img class="ikona" src="{r("media/wtyczki/" + w["ikona"])}" alt="">'
                 if w["ikona"] else "")
        karty.append(f"""    <a class="karta karta-wtyczka" href="{r(sciezka(jezyk, kat_wtyczki, w['slug'] + '.html'))}">
      {ikona}
      <span class="stan">{u(d['stan'])}</span>
      <h3>{u(d['nazwa'])}</h3>
      <p class="podtytul">{u(d['podtytul'])}</p>
      <p>{u(d['skrot'])}</p>
      <span class="wiecej">{u(e['wiecej'])} →</span>
    </a>""")
    czesci.append(f"""
<section id="wtyczki">
  <div class="szeroko">
    <h2>{u(e['wtyczki'])}</h2>
    <p class="wstep">{u(e['wtyczki_wstep'])}</p>
    <div class="siatka pary">
{chr(10).join(karty)}
    </div>
  </div>
</section>
""")

    # ebooki
    karty = []
    for b in EBOOKI:
        d = b[jezyk]
        rel = ' rel="nofollow"' if b.get("bez_indeksu") else ""
        karty.append(f"""    <a class="karta karta-ebook"{rel} href="{r(sciezka(jezyk, kat_ebooki, b['slug'] + '.html'))}">
      <img class="okladka" src="{r('media/okladki/' + b['okladka'])}" alt="" loading="lazy">
      <h3>{u(d['tytul'])}</h3>
      <p class="podtytul">{u(d['podtytul'])} · {b['strony']} {u(e['stron'])}</p>
      <p>{u(d['skrot'])}</p>
      <span class="wiecej">{u(e['wiecej'])} →</span>
    </a>""")
    czesci.append(f"""
<section id="ebooki" class="przemienna">
  <div class="szeroko">
    <h2>{u(e['ebooki'])}</h2>
    <p class="wstep">{u(e['ebooki_wstep'])}</p>
    <div class="siatka">
{chr(10).join(karty)}
    </div>
  </div>
</section>
""")

    # narzędzia
    karty = []
    for n in NARZEDZIA:
        tytul, opis = n[jezyk]
        karty.append(f"""    <a class="karta" href="{r(n['url'])}">
      <h3>{u(tytul)}</h3>
      <p>{u(opis)}</p>
      <span class="wiecej">{u(e['wiecej'])} →</span>
    </a>""")
    czesci.append(f"""
<section id="narzedzia">
  <div class="szeroko">
    <h2>{u(e['narzedzia_naglowek'])}</h2>
    <p class="wstep">{u(e['narzedzia_wstep'])}</p>
    <div class="siatka">
{chr(10).join(karty)}
    </div>
  </div>
</section>
""")

    czesci.append(stopka(jezyk, glebokosc))
    return "".join(czesci)


# --- podstrony -------------------------------------------------------------

def strona_wtyczki(w, jezyk):
    e = E[jezyk]
    d = w[jezyk]
    kat = 'wtyczki' if jezyk == 'pl' else 'plugins'
    glebokosc = 1 if jezyk == "pl" else 2
    r = lambda p: wzgledny(glebokosc, p)  # noqa: E731
    druga = (f"en/plugins/{w['slug']}.html" if jezyk == "pl"
             else f"wtyczki/{w['slug']}.html")

    czesci = [naglowek(jezyk, glebokosc, f"{d['nazwa']} — {MARKA}", d["skrot"], druga)]
    czesci.append(okruszek(jezyk, glebokosc,
                           [(e["wtyczki"], sciezka(jezyk, "index.html") + "#wtyczki"),
                            (d["nazwa"], None)]))

    ikona = (f'<p><img class="ikona-duza" src="{r("media/wtyczki/" + w["ikona"])}" alt=""></p>'
             if w["ikona"] else "")

    zrzuty = ""
    if w["zrzuty"]:
        obrazy = "".join(
            f'<img src="{r("media/wtyczki/" + z)}" alt="" loading="lazy">' for z in w["zrzuty"]
        )
        zrzuty = f'<h2>{u(e["zrzuty"])}</h2><div class="zrzuty">{obrazy}</div>'

    linki = []
    if w["repo"]:
        linki.append(f'<a href="{u(w["repo"])}">{u(e["repo"])}</a>')
    if d["polityka"]:
        linki.append(f'<a href="{u(d["polityka"])}">{u(e["polityka_apki"])}</a>')
    linki_html = f'<p>{" · ".join(linki)}</p>' if linki else ""

    czesci.append(f"""
<article class="wasko">
  {ikona}
  <span class="stan">{u(d['stan'])}</span>
  <h1>{u(d['nazwa'])}</h1>
  <p class="podtytul">{u(d['podtytul'])}</p>
  <p>{u(d['skrot'])}</p>
{sekcje_html(d['sekcje'])}
{zrzuty}
{linki_html}
  <p><a href="{r(sciezka(jezyk, 'index.html'))}">← {u(e['wroc'])}</a></p>
</article>
""")
    czesci.append(stopka(jezyk, glebokosc))
    return "".join(czesci)


def strona_ebooka(b, jezyk):
    e = E[jezyk]
    d = b[jezyk]
    glebokosc = 1 if jezyk == "pl" else 2
    r = lambda p: wzgledny(glebokosc, p)  # noqa: E731
    druga = (f"en/books/{b['slug']}.html" if jezyk == "pl" else f"ebooki/{b['slug']}.html")

    czesci = [naglowek(jezyk, glebokosc, f"{d['tytul']} — {MARKA}", d["skrot"], druga,
                       bez_indeksu=b.get("bez_indeksu", False))]
    czesci.append(okruszek(jezyk, glebokosc,
                           [(e["ebooki"], sciezka(jezyk, "index.html") + "#ebooki"),
                            (d["tytul"], None)]))

    przyciski = [f'<a class="pobierz" href="{drive_link(b["drive"])}">{u(e["pobierz"])}</a>']
    if b["drive_maly"]:
        przyciski.append(
            f'<a class="pobierz drugi" href="{drive_link(b["drive_maly"])}">{u(e["pobierz_maly"])}</a>'
        )

    czesci.append(f"""
<article class="wasko">
  <img class="okladka-duza" src="{r('media/okladki/' + b['okladka'])}" alt="">
  <h1>{u(d['tytul'])}</h1>
  <p class="podtytul">{u(d['podtytul'])} · {b['strony']} {u(e['stron'])} · PDF</p>
  <p>{u(d['skrot'])}</p>
  <p>{''.join(przyciski)}</p>
{sekcje_html(d['sekcje'])}
  <p><a href="{r(sciezka(jezyk, 'index.html'))}">← {u(e['wroc'])}</a></p>
</article>
""")
    czesci.append(stopka(jezyk, glebokosc))
    return "".join(czesci)


# --- kontakt i prywatność --------------------------------------------------

TRESC_KONTAKT = {
    "pl": [
        ("Jak się skontaktować",
         ["Najszybciej e-mailem. Na wiadomości odpowiadam w ciągu kilku dni.",
          "Telefon jest czynny w dni robocze."]),
        ("Współpraca",
         ["Piszę wtyczki do ATAK-a, stawiam serwery TAK i prowadzę szkolenia z ich obsługi. "
          "Jeżeli potrzebujesz jednej z tych rzeczy, napisz, co ma działać i w jakim terminie."]),
    ],
    "en": [
        ("How to get in touch",
         ["Email is fastest. I reply within a few days.",
          "The phone is answered on working days."]),
        ("Work",
         ["I write ATAK plugins, build TAK servers and run training on both. If you need one of "
          "those, write what has to work and by when."]),
    ],
}

TRESC_PRYWATNOSC = {
    "pl": [
        ("Co zbiera ta strona",
         ["Nic. Strona nie ma formularzy, liczników odwiedzin ani reklam. Nie zapisuje ciasteczek."]),
        ("Co zbiera serwer",
         ["Strona stoi na GitHub Pages. GitHub zapisuje adresy IP odwiedzających w swoich "
          "dziennikach serwera. Nie mam do nich dostępu. Zasady GitHuba opisuje "
          "<a href=\"https://docs.github.com/site-policy/privacy-policies/github-privacy-statement\">"
          "oświadczenie o prywatności GitHuba</a>."]),
        ("Pliki na Dysku Google",
         ["Przyciski pobierania prowadzą do plików na Dysku Google. Pobranie pliku odbywa się "
          "na warunkach Google i podlega jego polityce prywatności. Nie widzę, kto pobrał plik."]),
        ("Aplikacje",
         ["Aplikacje mają własne polityki prywatności, bo zbierają inne dane niż strona:",
          ("odnosniki", [("TakLab Hub — polityka prywatności", "taklab-hub/prywatnosc.html"),
                         ("TakLab Hub — usunięcie konta i danych",
                          "taklab-hub/usuwanie-konta.html"),
                         ("SniperTAK — polityka prywatności",
                          "sniperTAK/privacy-policy.html")])]),
        ("Kontakt w sprawie danych",
         [f"Pytania o dane kieruj na adres {EMAIL}. Odpowiadam w ciągu 30 dni."]),
    ],
    "en": [
        ("What this site collects",
         ["Nothing. There are no forms, no visitor counters and no adverts. The site sets no "
          "cookies."]),
        ("What the server collects",
         ["The site is hosted on GitHub Pages. GitHub records visitors' IP addresses in its "
          "server logs. I have no access to them. GitHub's terms are set out in the "
          "<a href=\"https://docs.github.com/site-policy/privacy-policies/github-privacy-statement\">"
          "GitHub Privacy Statement</a>."]),
        ("Files on Google Drive",
         ["The download buttons point to files on Google Drive. Downloading happens on Google's "
          "terms and under its privacy policy. I cannot see who downloaded a file."]),
        ("Apps",
         ["The apps have their own privacy policies, because they collect data the site does not:",
          ("odnosniki", [("TakLab Hub — privacy policy (Polish)", "taklab-hub/prywatnosc.html"),
                         ("TakLab Hub — account and data deletion (Polish)",
                          "taklab-hub/usuwanie-konta.html"),
                         ("SniperTAK — privacy policy",
                          "sniperTAK/privacy-policy.html")])]),
        ("Data enquiries",
         [f"Send data enquiries to {EMAIL}. I reply within 30 days."]),
    ],
}


def strona_prosta(jezyk, tytul, wstep, sekcje, plik, druga, kontaktowa=False):
    e = E[jezyk]
    glebokosc = 0 if jezyk == "pl" else 1
    r = lambda p: wzgledny(glebokosc, p)  # noqa: E731

    czesci = [naglowek(jezyk, glebokosc, f"{tytul} — {MARKA}", wstep, druga)]
    czesci.append(okruszek(jezyk, glebokosc, [(tytul, None)]))

    dane_kontaktowe = ""
    if kontaktowa:
        dane_kontaktowe = f"""
  <table>
    <tr><th>{u(e['email_etykieta'])}</th><td><a href="mailto:{u(EMAIL)}">{u(EMAIL)}</a></td></tr>
    <tr><th>{u(e['telefon_etykieta'])}</th><td><span data-telefon>{u(e['telefon_bez_js'])}</span></td></tr>
    <tr><th>GitHub</th><td><a href="{u(GITHUB)}">{u(GITHUB)}</a></td></tr>
  </table>
"""

    czesci.append(f"""
<article class="wasko">
  <h1>{u(tytul)}</h1>
  <p class="podtytul">{u(wstep)}</p>
{dane_kontaktowe}
{sekcje_html_surowe(sekcje, r)}
  <p><a href="{r(sciezka(jezyk, 'index.html'))}">← {u(e['wroc'])}</a></p>
</article>
""")
    czesci.append(stopka(jezyk, glebokosc))
    zapisz(plik, "".join(czesci))


def sekcje_html_surowe(sekcje, r):
    """Jak sekcje_html, ale dopuszcza odnośniki wpisane w treść.

    `r` przelicza adres liczony od korzenia na adres względny wobec strony.
    """
    czesci = []
    for tytul, tresci in sekcje:
        czesci.append(f"<h2>{html.escape(tytul)}</h2>")
        for t in tresci:
            if isinstance(t, str):
                czesci.append(f"<p>{t}</p>")
            elif t[0] == "odnosniki":
                punkty = "".join(
                    f'<li><a href="{u(r(cel))}">{u(etykieta)}</a></li>' for etykieta, cel in t[1]
                )
                czesci.append(f"<ul>{punkty}</ul>")
            else:
                czesci.append(blok(t))
    return "\n".join(czesci)


# --- zapis -----------------------------------------------------------------

def zapisz(wzgledna, tresc):
    sciezka_pliku = os.path.join(KORZEN, wzgledna)
    os.makedirs(os.path.dirname(sciezka_pliku), exist_ok=True)
    with open(sciezka_pliku, "w", encoding="utf-8") as f:
        f.write(tresc)
    print(f"  {wzgledna}")


def main():
    print("Generuję strony:")
    for jezyk in ("pl", "en"):
        kat_wtyczki = "wtyczki" if jezyk == "pl" else "plugins"
        kat_ebooki = "ebooki" if jezyk == "pl" else "books"
        przedrostek = "" if jezyk == "pl" else "en/"

        zapisz(f"{przedrostek}index.html", strona_glowna(jezyk))

        for w in WTYCZKI:
            zapisz(f"{przedrostek}{kat_wtyczki}/{w['slug']}.html", strona_wtyczki(w, jezyk))
        for b in EBOOKI:
            zapisz(f"{przedrostek}{kat_ebooki}/{b['slug']}.html", strona_ebooka(b, jezyk))

        if jezyk == "pl":
            strona_prosta("pl", "Kontakt", "Jak się ze mną skontaktować.",
                          TRESC_KONTAKT["pl"], "kontakt.html", "en/contact.html",
                          kontaktowa=True)
            strona_prosta("pl", "Polityka prywatności",
                          "Co ta strona zbiera i czego nie zbiera.",
                          TRESC_PRYWATNOSC["pl"], "prywatnosc.html", "en/privacy.html")
        else:
            strona_prosta("en", "Contact", "How to reach me.",
                          TRESC_KONTAKT["en"], "en/contact.html", "kontakt.html",
                          kontaktowa=True)
            strona_prosta("en", "Privacy policy",
                          "What this site collects and what it does not.",
                          TRESC_PRYWATNOSC["en"], "en/privacy.html", "prywatnosc.html")

    print("Gotowe.")


if __name__ == "__main__":
    main()
