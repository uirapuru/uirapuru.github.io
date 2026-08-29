# uirapuru.github.io

Strona wizytówkowa: wtyczki do ATAK-a, ebooki do pobrania i narzędzia działające
w przeglądarce. Stoi na GitHub Pages pod adresem <https://uirapuru.github.io>.

## Jak to jest zbudowane

Strony HTML są generowane ze skryptu, a wynik leży w repozytorium. Nie ma tu Jekylla
ani żadnego innego kroku budowania po stronie GitHuba — plik `.nojekyll` to wyłącza.

| Ścieżka | Zawartość |
|---|---|
| `narzedzia/dane.py` | Cała treść strony: opisy wtyczek, ebooków, hero, polityki. Obie wersje językowe obok siebie |
| `narzedzia/generuj.py` | Szablony i generator. Zapisuje 24 pliki HTML |
| `styl.css` | Wspólny arkusz stylów. Tryb ciemny przez `prefers-color-scheme` |
| `js/tel.js` | Składa numer telefonu w przeglądarce, żeby nie leżał w kodzie strony |
| `media/okladki/` | Miniatury okładek, pierwsza strona każdego PDF-a |
| `media/wtyczki/` | Ikony i zrzuty ekranu wtyczek |
| `taklab-hub/` | Polityka prywatności i usuwanie konta dla aplikacji TakLab Hub |
| `sniperTAK/` | Polityka prywatności wtyczki SniperTAK |
| `kestrel/`, `ballistics/`, `calculator/`, `simulator/` | Narzędzia w przeglądarce, starsze niż ta strona |

## Zmiana treści

1. Popraw tekst w `narzedzia/dane.py`.
2. Uruchom generator:

   ```bash
   python3 narzedzia/generuj.py
   ```

3. Obejrzyj wynik lokalnie:

   ```bash
   python3 -m http.server 8123
   ```

4. Zatwierdź zmiany razem z wygenerowanymi plikami HTML.

Nie poprawiaj plików HTML ręcznie. Generator nadpisze każdą taką zmianę.

## Miniatury okładek

Okładki powstają z pierwszej strony PDF-a:

```bash
pdftoppm -png -r 60 -f 1 -l 1 -singlefile ksiazka.pdf okladka
```

Potem skalowanie do 480 pikseli szerokości i zapis jako JPEG.

## Pliki do pobrania

Ebooki leżą na Dysku Google. W `dane.py` każdy ma pole `drive`
z identyfikatorem pliku; generator składa z niego adres pobrania.
