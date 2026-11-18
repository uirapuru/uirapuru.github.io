#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generuje statyczne strony serwisu z treści w dane.py.

Uruchomienie:  python3 narzedzia/generuj.py
Wynik:         pliki HTML w katalogu repozytorium.
"""

import html
import re
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dane import MARKA, EMAIL, GITHUB, HERO, WTYCZKI, EBOOKI, KURSY  # noqa: E402

EBOOKI = [b for b in EBOOKI if not b.get("ukryty")]

KORZEN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Etykiety interfejsu w obu językach.
E = {
    "pl": {
        "kod": "pl",
        "start": "Strona główna",
        "wtyczki": "Wtyczki",
        "urzadzenia": "Urządzenia",
        "aplikacje": "Aplikacje",
        "urzadzenia_wstep": "Własne oprogramowanie na reTerminal Sticky, mały komputer z ekranem "
                            "e-papierowym, który mocuje się na broni albo na oporządzeniu.",
        "aplikacje_wstep": "Samodzielne aplikacje na Androida. Nie potrzebują ATAK-a.",
        "ebooki": "Ebooki",
        "kursy": "Kursy",
        "kursy_wstep": "Kursy wideo, które prowadzę na strzelecwyborowy.pl.",
        "do_kursu": "Przejdź do kursu",
        "kontakt": "Kontakt",
        "prywatnosc": "Prywatność",
        "drugi_jezyk": "English",
        "wtyczki_wstep": "Wtyczki do ATAK-a. Każda powstała, bo czegoś brakowało mnie "
                         "samemu.",
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
        "film": "Film",
        "wsparcie": "Wsparcie",
        "wsparcie_link": "Wsparcie, zgłaszanie błędów i częste pytania",
        "zdjecia": "Zdjęcia",
        "polityka_apki": "Polityka prywatności aplikacji",
        "repo": "Kod źródłowy",
        "sklep": "Pobierz z Google Play",
        "wroc": "Wróć na stronę główną",
        "prawa_naglowek": "Prawa autorskie",
        "stopka_zastrzezenie": "Strona nie jest powiązana z TAK Product Center ani z żadną "
                               "instytucją publiczną.",
        "narzedzia_naglowek": "Narzędzia w przeglądarce",
        "narzedzia_wstep": "Rzeczy, które działają bez instalowania czegokolwiek.",
        "serwisy_naglowek": "Serwisy",
        "serwisy_wstep": "Strony, które prowadzę.",
    },
    "en": {
        "kod": "en",
        "start": "Home",
        "wtyczki": "Plugins",
        "urzadzenia": "Devices",
        "aplikacje": "Apps",
        "urzadzenia_wstep": "My own firmware for the reTerminal Sticky, a small computer with an "
                            "e-paper screen that mounts on a rifle or on the kit.",
        "aplikacje_wstep": "Standalone Android apps. They do not need ATAK.",
        "ebooki": "Books",
        "kursy": "Courses",
        "kursy_wstep": "Video courses I run on strzelecwyborowy.pl.",
        "do_kursu": "Go to the course",
        "kontakt": "Contact",
        "prywatnosc": "Privacy",
        "drugi_jezyk": "Polski",
        "wtyczki_wstep": "ATAK plugins. Each exists because something was missing for me "
                         "first.",
        "ebooki_wstep": "Free PDF downloads. Some I wrote, some I translated.",
        "wiecej": "Read more",
        "pobierz": "Download PDF",
        "pobierz_maly": "Light version",
        "stron": "pages",
        "email_etykieta": "Email",
        "telefon_etykieta": "Phone",
        "telefon_bez_js": "number shown once JavaScript is enabled",
        "zrzuty": "Screenshots",
        "film": "Video",
        "wsparcie": "Support",
        "wsparcie_link": "Support, bug reports and FAQ",
        "zdjecia": "Photos",
        "polityka_apki": "App privacy policy",
        "repo": "Source code",
        "sklep": "Get it on Google Play",
        "wroc": "Back to the home page",
        "prawa_naglowek": "Copyright",
        "stopka_zastrzezenie": "This site is not affiliated with TAK Product Center or any "
                               "public institution.",
        "narzedzia_naglowek": "Browser tools",
        "narzedzia_wstep": "Things that work without installing anything.",
        "serwisy_naglowek": "Sites",
        "serwisy_wstep": "Sites I run.",
    },
}

KOLEJNOSC_SEKCJI = ["urzadzenia", "serwisy", "aplikacje", "wtyczki", "kursy", "ebooki",
                    "narzedzia"]

SEKCJA = {"urzadzenie": "urzadzenia", "aplikacja": "aplikacje", "wtyczka": "wtyczki"}

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
        "pl": ("Animacja toru pocisku", "Poglądowa animacja lotu pocisku: jak kąt lufy, prędkość "
                                        "i stan powietrza zmieniają tor. Nie służy do liczenia nastaw."),
        "en": ("Bullet trajectory animation", "An illustrative animation of a bullet in flight: how "
                                              "barrel angle, velocity and air change the path. Not for "
                                              "computing corrections."),
    },
]

SERWISY = [
    {
        "url": "https://strzelecwyborowy.pl/",
        "pl": ("strzelecwyborowy.pl", "Kursy wideo po polsku. „12 strzałów”: strzelanie z karabinu "
                                      "na duże odległości w 12 etapach, od naboju i zerowania po "
                                      "wiatr i pracę strzelca z obserwatorem; każdy etap ma filmy "
                                      "z lektorem, wykład, test i zadanie z tarczą do druku. "
                                      "„Kurs ATAK”: 49 filmów od instalacji ATAK-CIV, przez mapy "
                                      "offline i MGRS, po łączenie telefonów przez serwer. Pierwszy "
                                      "etap każdego kursu jest za darmo."),
        "en": ("strzelecwyborowy.pl", "Video courses in Polish. „12 strzałów” teaches long-range "
                                      "rifle shooting in 12 stages, from the cartridge and zeroing "
                                      "to wind and shooter–spotter work; every stage has narrated "
                                      "videos, a lecture, a test and a task with a printable "
                                      "target. „Kurs ATAK” has 49 videos, from installing ATAK-CIV "
                                      "through offline maps and MGRS to linking phones through a "
                                      "server. The first stage of each course is free."),
    },
    {
        "url": "https://sharpshooteracademy.com/",
        "pl": ("sharpshooteracademy.com", "12 Shots, angielskie wydanie kursu „12 strzałów” o strzelaniu "
                                          "z karabinu na duże odległości. Ma angielskiego lektora "
                                          "i jednostki imperialne obok metrycznych. Pierwszy etap "
                                          "jest za darmo."),
        "en": ("sharpshooteracademy.com", "12 Shots, the English edition of the long-range rifle "
                                          "course, with English narration and imperial units shown "
                                          "alongside metric. The first stage is free."),
    },
    {
        "url": "https://atakplugins.eu/",
        "pl": ("atakplugins.eu", "Katalog wtyczek, aplikacji i klientów TAK ze zrzutami "
                                 "ekranu i odnośnikami do pobrania. Wtyczki, które ładują się "
                                 "na ATAK-CIV 5.8, mają odznakę „Zweryfikowano”."),
        "en": ("atakplugins.eu", "A catalogue of TAK plugins, apps and clients with "
                                 "screenshots and download links. Plugins that load on "
                                 "ATAK-CIV 5.8 carry a „Verified” badge."),
    },
    {
        "url": "https://taklab.eu/",
        "pl": ("taklab.eu", "Własny serwer TAK na ćwiczenie, kurs albo akcję, postawiony "
                            "w chmurze w pięć minut. Z mapą CloudTAK, czatem i łącznością "
                            "głosową."),
        "en": ("taklab.eu", "Your own TAK server for an exercise, a course or an operation, "
                            "up in the cloud in five minutes. With a CloudTAK map, chat and "
                            "voice."),
    },
]


MIESIACE = {
    "pl": ["stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca", "lipca",
           "sierpnia", "września", "października", "listopada", "grudnia"],
    "en": ["January", "February", "March", "April", "May", "June", "July", "August",
           "September", "October", "November", "December"],
}


def wersja_i_data(w, jezyk):
    """Napis „Wersja 1.0.1 · 18 października 2026” albo pusty, gdy brak danych."""
    if not w.get("wersja"):
        return ""
    r, m, d = (int(x) for x in w["data"].split("-"))
    etykieta = "Wersja" if jezyk == "pl" else "Version"
    return f"{etykieta} {w['wersja']} · {d} {MIESIACE[jezyk][m - 1]} {r}"


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
<link rel="stylesheet" href="{r('styl.css')}?v=5">
<link rel="icon" href="{r('favicon.svg')}" type="image/svg+xml">

<header class="pasek">
  <div class="szeroko">
    <a class="marka" href="{r(sciezka(jezyk, 'index.html'))}">{u(MARKA)}</a>
    <nav>
      <a href="{r(sciezka(jezyk, 'index.html'))}#urzadzenia">{u(e['urzadzenia'])}</a>
      <a href="{r(sciezka(jezyk, 'index.html'))}#serwisy">{u(e['serwisy_naglowek'])}</a>
      <a href="{r(sciezka(jezyk, 'index.html'))}#aplikacje">{u(e['aplikacje'])}</a>
      <a href="{r(sciezka(jezyk, 'index.html'))}#wtyczki">{u(e['wtyczki'])}</a>
      <a href="{r(sciezka(jezyk, 'index.html'))}#kursy">{u(e['kursy'])}</a>
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
    if rodzaj == "pytania":
        return "".join(f"<h3>{u(q)}</h3><p>{u(a)}</p>" for q, a in tresc[1])
    raise ValueError(f"nieznany rodzaj bloku: {rodzaj}")


def sekcje_html(sekcje, r=None):
    czesci = []
    for tytul, tresci in sekcje:
        czesci.append(f"<h2>{u(tytul)}</h2>")
        for t in tresci:
            if isinstance(t, tuple) and t[0] == "odnosnik":
                czesci.append(f'<p><a href="{u(r(t[2]))}">{u(t[1])}</a></p>')
            else:
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

    # urządzenia, aplikacje, wtyczki
    for rodzaj, klucz, tlo in (("urzadzenie", "urzadzenia", ""),
                               ("aplikacja", "aplikacje", ' class="przemienna"'),
                               ("wtyczka", "wtyczki", "")):
        karty = []
        for w in WTYCZKI:
            if w["rodzaj"] != rodzaj:
                continue
            d = w[jezyk]
            ikona = (f'<img class="ikona" src="{r("media/wtyczki/" + w["ikona"])}" alt="">'
                     if w["ikona"] else "")
            if w.get("miniatura"):
                ikona = (f'<img class="miniatura" src="{r("media/wtyczki/" + w["miniatura"])}" '
                         f'alt="" loading="lazy">' + ikona)
            karty.append(f"""    <a class="karta karta-wtyczka" href="{r(sciezka(jezyk, kat_wtyczki, w['slug'] + '.html'))}">
      {ikona}
      <span class="stan">{u(d['stan'])}</span>
      <h3>{u(d['nazwa'])}</h3>
      <p class="wersja">{u(wersja_i_data(w, jezyk))}</p>
      <p class="podtytul">{u(d['podtytul'])}</p>
      <p>{u(d['skrot'])}</p>
      <span class="wiecej">{u(e['wiecej'])} →</span>
    </a>""")
        czesci.append(f"""
<section id="{klucz}"{tlo}>
  <div class="szeroko">
    <h2>{u(e[klucz])}</h2>
    <p class="wstep">{u(e[klucz + '_wstep'])}</p>
    <div class="siatka pary">
{chr(10).join(karty)}
    </div>
  </div>
</section>
""")

    # kursy
    karty = []
    for k in KURSY:
        tytul, opis = k[jezyk]
        karty.append(f"""    <a class="karta" href="{u(k['url'])}">
      <h3>{u(tytul)}</h3>
      <p>{u(opis)}</p>
      <span class="wiecej">{u(e['do_kursu'])} →</span>
    </a>""")
    czesci.append(f"""
<section id="kursy" class="przemienna">
  <div class="szeroko">
    <h2>{u(e['kursy'])}</h2>
    <p class="wstep">{u(e['kursy_wstep'])}</p>
    <div class="siatka">
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
<section id="ebooki">
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
<section id="narzedzia" class="przemienna">
  <div class="szeroko">
    <h2>{u(e['narzedzia_naglowek'])}</h2>
    <p class="wstep">{u(e['narzedzia_wstep'])}</p>
    <div class="siatka">
{chr(10).join(karty)}
    </div>
  </div>
</section>
""")

    # serwisy
    karty = []
    for n in SERWISY:
        tytul, opis = n[jezyk]
        karty.append(f"""    <a class="karta" href="{u(n['url'])}">
      <h3>{u(tytul)}</h3>
      <p>{u(opis)}</p>
      <span class="wiecej">{u(e['wiecej'])} →</span>
    </a>""")
    czesci.append(f"""
<section id="serwisy">
  <div class="szeroko">
    <h2>{u(e['serwisy_naglowek'])}</h2>
    <p class="wstep">{u(e['serwisy_wstep'])}</p>
    <div class="siatka">
{chr(10).join(karty)}
    </div>
  </div>
</section>
""")

    # Kolejność sekcji i naprzemienne tło ustalane w jednym miejscu.
    sekcje = {re.search(r'<section id="([a-z]+)"', c).group(1): c
              for c in czesci if '<section id="' in c}
    reszta = [c for c in czesci if '<section id="' not in c]
    for i, klucz in enumerate(KOLEJNOSC_SEKCJI):
        c = re.sub(r'<section id="([a-z]+)"[^>]*>', r'<section id="\1">', sekcje[klucz], count=1)
        if i % 2:
            c = c.replace(f'<section id="{klucz}">', f'<section id="{klucz}" class="przemienna">', 1)
        reszta.append(c)
    reszta.append(stopka(jezyk, glebokosc))
    return "".join(reszta)


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
                           [(e[SEKCJA[w["rodzaj"]]],
                             sciezka(jezyk, "index.html") + "#" + SEKCJA[w["rodzaj"]]),
                            (d["nazwa"], None)]))

    ikona = (f'<p><img class="ikona-duza" src="{r("media/wtyczki/" + w["ikona"])}" alt=""></p>'
             if w["ikona"] else "")

    zrzuty = ""
    if w["zrzuty"]:
        obrazy = "".join(
            f'<img src="{r("media/wtyczki/" + z)}" alt="" loading="lazy">' for z in w["zrzuty"]
        )
        naglowek_zrzutow = e["zdjecia"] if w.get("film") else e["zrzuty"]
        zrzuty = f'<h2>{u(naglowek_zrzutow)}</h2><div class="zrzuty">{obrazy}</div>'
    if w.get("film"):
        f = w["film"]
        zrzuty = (f'<h2>{u(e["film"])}</h2>'
                  f'<video class="film" controls muted playsinline preload="none" '
                  f'poster="{r("media/wtyczki/" + f["plakat"])}">'
                  f'<source src="{r("media/wtyczki/" + f["plik"])}" type="video/mp4"></video>'
                  + zrzuty)

    linki = []
    if d.get("wsparcie"):
        linki.append(f'<a href="{w["slug"]}-{"wsparcie" if jezyk == "pl" else "support"}.html">'
                     f'{u(e["wsparcie_link"])}</a>')
    if w["repo"]:
        linki.append(f'<a href="{u(w["repo"])}">{u(e["repo"])}</a>')
    if d["polityka"]:
        linki.append(f'<a href="{u(d["polityka"])}">{u(e["polityka_apki"])}</a>')
    linki_html = f'<p>{" · ".join(linki)}</p>' if linki else ""
    sklep = (f'\n  <p><a class="pobierz" href="{u(w["sklep"])}">{u(e["sklep"])}</a></p>'
             if w.get("sklep") else "")

    czesci.append(f"""
<article class="wasko">
  {ikona}
  <span class="stan">{u(d['stan'])}</span>
  <h1>{u(d['nazwa'])}</h1>
  <p class="wersja">{u(wersja_i_data(w, jezyk))}</p>
  <p class="podtytul">{u(d['podtytul'])}</p>
  <p>{u(d['skrot'])}</p>{sklep}
{sekcje_html(d['sekcje'])}
{zrzuty}
{linki_html}
  <p><a href="{r(sciezka(jezyk, 'index.html'))}">← {u(e['wroc'])}</a></p>
</article>
""")
    czesci.append(stopka(jezyk, glebokosc))
    return "".join(czesci)


def strona_wsparcia(w, jezyk):
    e = E[jezyk]
    d = w[jezyk]
    kat = 'wtyczki' if jezyk == 'pl' else 'plugins'
    plik = f"{w['slug']}-{'wsparcie' if jezyk == 'pl' else 'support'}.html"
    glebokosc = 1 if jezyk == "pl" else 2
    r = lambda p: wzgledny(glebokosc, p)  # noqa: E731
    druga = (f"en/plugins/{w['slug']}-support.html" if jezyk == "pl"
             else f"wtyczki/{w['slug']}-wsparcie.html")
    tytul = f"{d['nazwa']} — {e['wsparcie']}"
    czesci = [naglowek(jezyk, glebokosc, f"{tytul} — {MARKA}", d["wsparcie"]["wstep"], druga)]
    czesci.append(okruszek(jezyk, glebokosc,
                           [(e[SEKCJA[w["rodzaj"]]],
                             sciezka(jezyk, "index.html") + "#" + SEKCJA[w["rodzaj"]]),
                            (d["nazwa"], sciezka(jezyk, kat, w["slug"] + ".html")),
                            (e["wsparcie"], None)]))
    czesci.append(f"""
<article class="wasko">
  <h1>{u(tytul)}</h1>
  <p class="podtytul">{u(d['wsparcie']['wstep'])}</p>
{sekcje_html(d['wsparcie']['sekcje'], r)}
  <p><a href="{w['slug']}.html">← {u(d['nazwa'])}</a></p>
</article>
""")
    czesci.append(stopka(jezyk, glebokosc))
    return "".join(czesci), f"{'' if jezyk == 'pl' else 'en/'}{kat}/{plik}"


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
                         ("SniperTAK — polityka prywatności (po angielsku)",
                          "sniperTAK/privacy-policy.html"),
                         ("SniperKIT — polityka prywatności (po angielsku)",
                          "sniperkit/privacy-policy.html"),
                         ("PrintPlugin — polityka prywatności (po angielsku)",
                          "printplugin/privacy-policy.html"),
                         ("Sarneg — polityka prywatności (po angielsku)",
                          "sarneg/privacy-policy.html"),
                         ("StarlinkTAK — polityka prywatności (po angielsku)",
                          "starlinktak/privacy-policy.html"),
                         ("Modern UI — polityka prywatności (po angielsku)",
                          "modernui/privacy-policy.html"),
                         ("Ułan — polityka prywatności",
                          "ulan/polityka-prywatnosci.html")])]),
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
                          "sniperTAK/privacy-policy.html"),
                         ("SniperKIT — privacy policy",
                          "sniperkit/privacy-policy.html"),
                         ("PrintPlugin — privacy policy",
                          "printplugin/privacy-policy.html"),
                         ("Sarneg — privacy policy",
                          "sarneg/privacy-policy.html"),
                         ("StarlinkTAK — privacy policy",
                          "starlinktak/privacy-policy.html"),
                         ("Modern UI — privacy policy",
                          "modernui/privacy-policy.html"),
                         ("Ułan — privacy policy (Polish)",
                          "ulan/polityka-prywatnosci.html")])]),
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
            if w[jezyk].get("wsparcie"):
                tresc, plik = strona_wsparcia(w, jezyk)
                zapisz(plik, tresc)
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
