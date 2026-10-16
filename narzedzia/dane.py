# -*- coding: utf-8 -*-
"""Treść strony. Jedno miejsce dla obu wersji językowych."""

MARKA = "Grzegorz Kaszuba"
EMAIL = "grzegorzkaszuba84@gmail.com"
GITHUB = "https://github.com/uirapuru"

HERO = {
    "pl": {
        "motto": "Rozkładam sprzęt i oprogramowanie na części, żeby dało się ich używać.",
        "cytat": "To nie problem jest problemem. Problemem jest twoje nastawienie do problemu.",
        "cytat_autor": "kapitan Jack Sparrow",
        "robie": (
            "Piszę wtyczki do ATAK-a — aplikacji, na której wojsko i służby prowadzą mapę "
            "sytuacyjną na telefonie. Stawiam serwery TAK, od Raspberry Pi po Kubernetes. "
            "Rozgryzam protokoły urządzeń, których producent nie opisał: wiatromierza Kestrel, "
            "radia Baofeng, dalmierza Leica. Z tego, czego się dowiem, robię ebooki po polsku, "
            "bo po polsku nikt tego nie napisał."
        ),
        "co_robie_naglowek": "Czym się zajmuję",
    },
    "en": {
        "motto": "I take hardware and software apart so they become usable.",
        "cytat": "The problem is not the problem. The problem is your attitude about the problem.",
        "cytat_autor": "Captain Jack Sparrow",
        "robie": (
            "I write plugins for ATAK — the app the military and emergency services use to run "
            "a situational map on a phone. I build TAK servers, from a Raspberry Pi to Kubernetes. "
            "I reverse-engineer device protocols their makers never documented: the Kestrel weather "
            "meter, Baofeng radios, Leica rangefinders. What I learn goes into books, written in "
            "Polish, because nobody had written them in Polish."
        ),
        "co_robie_naglowek": "What I do",
    },
}

# --- wtyczki ---------------------------------------------------------------

WTYCZKI = [
    {
        "slug": "taklab-hub",
        "ikona": "taklab-hub.png",
        "zrzuty": ["taklab-hub-1.jpg", "taklab-hub-2.jpg", "taklab-hub-3.jpg"],
        "repo": None,
        "pl": {
            "nazwa": "TakLab Hub",
            "podtytul": "Aplikacja na Androida",
            "stan": "Zgłoszona do Google Play",
            "skrot": (
                "Doprowadza telefon od stanu pustego do działającego klienta ATAK. Pobiera "
                "katalog, instaluje ATAK i wtyczki ze sprawdzeniem sumy kontrolnej, zakłada "
                "środowisko serwerowe."
            ),
            "sekcje": [
                ("Po co to jest",
                 ["Postawienie ATAK-a na telefonie wymaga dziś kilku kroków, których nikt "
                  "nowy nie zgadnie: trzeba znaleźć właściwą wersję aplikacji, dobrać wtyczki "
                  "do tej wersji, wgrać mapy i wczytać paczkę połączeniową z certyfikatem. "
                  "Każdy z tych kroków można wykonać źle.",
                  "TakLab Hub robi to za użytkownika. Instaluje pliki w odpowiedniej "
                  "kolejności, sprawdza je przed instalacją i przekazuje resztę do ATAK-a."]),
                ("Jak działa",
                 ["Aplikacja pobiera katalog plików z publicznego zasobnika. Katalog opisuje, "
                  "która wersja ATAK-a pasuje do której wtyczki i jaką sumę kontrolną ma każdy "
                  "plik.",
                  "Przed instalacją aplikacja liczy sumę SHA-256 pobranego pliku i porównuje "
                  "ją z katalogiem. Plik, który się nie zgadza, nie zostaje zainstalowany.",
                  "Pozycja „Mój serwer” zakłada środowisko szkoleniowe przez API TakLab, "
                  "dodaje operatorów, wydaje im paczki połączeniowe i pokazuje kod QR do "
                  "rejestracji."]),
                ("Stan prac",
                 ["Aplikacja działa na telefonie. Instalacja ATAK-a i wtyczek jest gotowa. "
                  "Obsługa środowisk serwerowych działa na atrapie API, bo samo API dopiero "
                  "powstaje. Mapy i VPN to na razie ekrany bez działania."]),
            ],
            "polityka": "https://uirapuru.github.io/taklab-hub/prywatnosc.html",
        },
        "en": {
            "nazwa": "TakLab Hub",
            "podtytul": "Android app",
            "stan": "Submitted to Google Play",
            "skrot": (
                "Takes a phone from empty to a working ATAK client. Fetches a catalogue, "
                "installs ATAK and its plugins with checksum verification, and provisions a "
                "server environment."
            ),
            "sekcje": [
                ("Why it exists",
                 ["Setting up ATAK on a phone takes several steps a newcomer cannot guess: "
                  "find the right version of the app, match plugins to that version, load maps, "
                  "and import a connection package with a certificate. Every one of those steps "
                  "can go wrong.",
                  "TakLab Hub does it for the user. It installs files in the right order, "
                  "verifies them first, and hands the rest to ATAK."]),
                ("How it works",
                 ["The app downloads a file catalogue from a public bucket. The catalogue "
                  "records which ATAK version each plugin matches and the checksum of every file.",
                  "Before installing, the app computes the SHA-256 of the downloaded file and "
                  "compares it against the catalogue. A file that does not match is not installed.",
                  "The „My server” screen provisions a training environment through the "
                  "TakLab API, adds operators, issues their connection packages, and shows a QR "
                  "code for enrolment."]),
                ("Status",
                 ["The app runs on a phone. Installing ATAK and plugins is finished. Server "
                  "environments run against a stub API, because the API itself is still being "
                  "built. Maps and VPN are screens without function for now."]),
            ],
            "polityka": "https://uirapuru.github.io/taklab-hub/prywatnosc.html",
        },
    },
    {
        "slug": "snipertak",
        "ikona": "snipertak.png",
        "zrzuty": ["snipertak-1.jpg", "snipertak-2.jpg", "snipertak-3.jpg"],
        "repo": "https://github.com/uirapuru/SniperTakPlugin",
        "sklep": "https://play.google.com/store/apps/details?id=com.snipertak.plugin",
        "pl": {
            "nazwa": "SniperTAK",
            "podtytul": "Wtyczka ATAK-CIV 5.5 i nowszych",
            "stan": "W Google Play",
            "skrot": (
                "Kalkulator balistyczny wbudowany w mapę ATAK-a. Liczy poprawkę na odległość "
                "i wiatr, uwzględnia gęstość wysokości, rysuje punkt obserwacyjny."
            ),
            "sekcje": [
                ("Po co to jest",
                 ["Strzelec na dystansie liczy poprawki w osobnym kalkulatorze, a położenie "
                  "celu ma na mapie w ATAK-u. Przepisywanie współrzędnych między jednym a drugim "
                  "zabiera czas i wprowadza błędy.",
                  "SniperTAK liczy poprawkę na tym samym ekranie, na którym leży cel. "
                  "Odległość i azymut bierze z mapy, nie z klawiatury."]),
                ("Co liczy",
                 ["Poprawkę pionową i poziomą dla wybranego naboju i lufy. Model uwzględnia "
                  "gęstość wysokości, czyli łączny wpływ temperatury, ciśnienia i wilgotności "
                  "na opór powietrza.",
                  "Gęstość wysokości jest modelem empirycznym, nie pełnym rozwiązaniem "
                  "atmosfery. Dane wejściowe są ograniczone do zakresu, w którym model był "
                  "sprawdzany: temperatura od −20 do 50 °C.",
                  "Wtyczka rysuje też punkt obserwacyjny na mapie i wysyła jego położenie do "
                  "pozostałych uczestników sieci."]),
                ("Skąd biorą się dane pogodowe",
                 ["Warunki można wpisać ręcznie albo pobrać z wiatromierza Kestrel. Protokół "
                  "Bluetooth Kestrela nie jest opisany publicznie, więc odtworzyłem go od zera, "
                  "nasłuchując transmisji. Opis protokołu jest częścią moich notatek "
                  "z rozkładania sprzętu na części."]),
            ],
            "polityka": "https://uirapuru.github.io/sniperTAK/privacy-policy.html",
        },
        "en": {
            "nazwa": "SniperTAK",
            "podtytul": "Plugin for ATAK-CIV 5.5 and newer",
            "stan": "On Google Play",
            "skrot": (
                "A ballistic calculator built into the ATAK map. It computes range and wind "
                "corrections, accounts for density altitude, and plots an observation post."
            ),
            "sekcje": [
                ("Why it exists",
                 ["A shooter computes corrections in one app and keeps the target on the ATAK "
                  "map in another. Copying coordinates between the two costs time and introduces "
                  "mistakes.",
                  "SniperTAK computes the correction on the same screen the target sits on. It "
                  "reads range and bearing from the map, not from the keyboard."]),
                ("What it computes",
                 ["Elevation and windage for the selected cartridge and barrel. The model "
                  "accounts for density altitude — the combined effect of temperature, pressure "
                  "and humidity on air resistance.",
                  "Density altitude is an empirical model, not a full atmospheric solver. Input "
                  "is clamped to the range it was validated against: temperature from −20 to "
                  "50 °C.",
                  "The plugin also plots an observation post on the map and shares its position "
                  "with the rest of the network."]),
                ("Where the weather data comes from",
                 ["Conditions can be typed in or read from a Kestrel weather meter. Kestrel's "
                  "Bluetooth protocol is not publicly documented, so I reconstructed it from "
                  "scratch by listening to the traffic."]),
            ],
            "polityka": "https://uirapuru.github.io/sniperTAK/privacy-policy.html",
        },
    },
    {
        "slug": "printplugin",
        "ikona": "printplugin.png",
        "zrzuty": ["printplugin-1.jpg", "printplugin-2.jpg", "printplugin-3.jpg"],
        "repo": None,
        "pl": {
            "nazwa": "PrintPlugin",
            "podtytul": "Wtyczka ATAK-CIV 5.5 i nowszych",
            "stan": "Test zamknięty w Google Play",
            "skrot": (
                "Zapisuje bieżący kadr mapy jako arkusze A4 w pliku PNG albo PDF. "
                "300 dpi, opcjonalna siatka MGRS, wybrana skala."
            ),
            "sekcje": [
                ("Po co to jest",
                 ["Bateria się kończy, telefon tonie albo w danym miejscu nie wolno wnosić "
                  "elektroniki. Papierowa mapa nie ma tych problemów.",
                  "Wtyczka drukuje dokładnie to, co widać na ekranie: podkład i obiekty mapy "
                  "w bieżącym kadrze. Interfejs ATAK-a nie trafia do pliku."]),
                ("Jak używać",
                 ["1. Naciśnij przycisk „Print” na pasku narzędzi ATAK.",
                  "2. Wybierz format, tło, siatkę i skalę.",
                  "3. Obejrzyj podgląd pełnoekranowy.",
                  "4. Naciśnij „Zapisz” i wskaż miejsce zapisu."]),
                ("Ustawienia",
                 [("tabela",
                   ["Opcja", "Wartości", "Domyślnie"],
                   [["Format", "PNG, PDF", "PNG"],
                    ["Tło", "kafelki mapy, białe tło", "kafelki mapy"],
                    ["Siatka MGRS", "włączona, wyłączona", "wyłączona"],
                    ["Skala", "dopasuj do kadru, 1:10 000, 1:25 000, 1:50 000, 1:100 000",
                     "dopasuj do kadru"]])]),
                ("Arkusz",
                 ["Wtyczka rysuje arkusz A4 w rozdzielczości 300 dpi, z marginesem 10 mm. "
                  "Obszar mapy zajmuje cały obszar druku poza dolnym paskiem stopki.",
                  "Mapa nie jest rozciągana. Zachowuje proporcje wycinka, a resztę obszaru "
                  "zostawia białą.",
                  "Przy skali stałej wtyczka pobiera kafelki mapy także spoza ekranu. Arkusze "
                  "na brzegu eksportu są pokryte mapą na całej powierzchni."]),
                ("Na czym działa",
                 ["Wtyczka zgłasza zgodność z ATAK 5.5, a ATAK ładuje ją też w wersjach 5.7 "
                  "i 5.8. Jedna paczka działa na wszystkich trzech."]),
            ],
            "polityka": "https://uirapuru.github.io/printplugin/privacy-policy.html",
        },
        "en": {
            "nazwa": "PrintPlugin",
            "podtytul": "Plugin for ATAK-CIV 5.5 and newer",
            "stan": "Closed testing on Google Play",
            "skrot": (
                "Saves the current map view as A4 sheets in a PNG or PDF file. 300 dpi, "
                "optional MGRS grid, selectable scale."
            ),
            "sekcje": [
                ("Why it exists",
                 ["Batteries run out, phones get wet, and some places do not allow electronics "
                  "at all. A paper map has none of those problems.",
                  "The plugin prints exactly what is on screen: the base layer and the map "
                  "objects in the current view. The ATAK interface is not included."]),
                ("How to use it",
                 ["1. Press the „Print” button on the ATAK toolbar.",
                  "2. Choose format, background, grid and scale.",
                  "3. Review the full-screen preview.",
                  "4. Press „Save” and pick a location."]),
                ("Settings",
                 [("tabela",
                   ["Option", "Values", "Default"],
                   [["Format", "PNG, PDF", "PNG"],
                    ["Background", "map tiles, white", "map tiles"],
                    ["MGRS grid", "on, off", "off"],
                    ["Scale", "fit to view, 1:10,000, 1:25,000, 1:50,000, 1:100,000",
                     "fit to view"]])]),
                ("The sheet",
                 ["The plugin renders an A4 sheet at 300 dpi with a 10 mm margin. The map area "
                  "fills the whole printable area except the footer strip.",
                  "The map is never stretched. It keeps the aspect ratio of the extract and "
                  "leaves the rest of the area white.",
                  "At a fixed scale the plugin fetches map tiles beyond the screen too. Sheets "
                  "at the edge of the export are covered by the map in full."]),
                ("What it runs on",
                 ["The plugin declares ATAK 5.5, and ATAK also loads it on 5.7 and 5.8. One "
                  "package runs on all three."]),
            ],
            "polityka": "https://uirapuru.github.io/printplugin/privacy-policy.html",
        },
    },
    {
        "slug": "simpleplugin",
        "ikona": "simpleplugin.png",
        "zrzuty": [],
        "repo": None,
        "pl": {
            "nazwa": "SimplePlugin",
            "podtytul": "Wtyczka ATAK-CIV 5.8",
            "stan": "Działa",
            "skrot": (
                "Ogranicza interfejs ATAK-a do narzędzi jednego z pięciu scenariuszy. "
                "Szósty przycisk cofa wszystkie zmiany."
            ),
            "sekcje": [
                ("Po co to jest",
                 ["ATAK ma kilkadziesiąt narzędzi. Ktoś, kto włącza go raz na miesiąc, używa "
                  "pięciu i szuka ich wśród reszty.",
                  "SimplePlugin zostawia na ekranie tylko te narzędzia, które pasują do "
                  "wybranego zajęcia: nawigacja, taktyka, monitoring, audio albo zestaw własny."]),
                ("Jak działa",
                 ["Wtyczka nie podmienia interfejsu ATAK-a. Steruje mechanizmami, które ATAK "
                  "już ma:",
                  ("lista",
                   ["zestawy widocznych narzędzi paska nawigacji (loadouty),",
                    "fabryka menu radialnego, która zawęża menu markera,",
                    "preferencje odpowiadające za czytelność mapy,",
                    "własny pasek z przyciskami rozmowy i czatu, pokazywany tylko "
                    "w scenariuszu audio."]),
                 "Domyślnego zestawu narzędzi ATAK-a wtyczka nigdy nie zapisuje ani nie usuwa. "
                 "Dlatego przywracanie sprowadza się do przełączenia się na niego i odtworzenia "
                 "preferencji z migawki zrobionej przed pierwszą zmianą."]),
                ("Czego się przy niej nauczyłem",
                 ["Sześć wad przeszło kompilację, testy jednostkowe i kontrolę pakietu, "
                  "a wyszło dopiero na uruchomionym ATAK-u. Między innymi: wpis komponentu "
                  "w pliku opisu wtyczki bywa ignorowany, lista ukrytych narzędzi nie odpowiada "
                  "slotom paska, a puste nazwy pozycji rozwalają menu radialne.",
                  "Wniosek jest prozaiczny i kosztowny: wtyczki do ATAK-a sprawdza się na "
                  "urządzeniu, nie w teście."]),
            ],
            "polityka": None,
        },
        "en": {
            "nazwa": "SimplePlugin",
            "podtytul": "ATAK-CIV 5.8 plugin",
            "stan": "Working",
            "skrot": (
                "Cuts the ATAK interface down to the tools of one of five scenarios. "
                "A sixth button undoes every change."
            ),
            "sekcje": [
                ("Why it exists",
                 ["ATAK ships dozens of tools. Someone who opens it once a month uses five of "
                  "them and hunts for those among the rest.",
                  "SimplePlugin leaves on screen only the tools that fit the chosen job: "
                  "navigation, tactics, monitoring, audio, or a custom set."]),
                ("How it works",
                 ["The plugin does not replace the ATAK interface. It drives mechanisms ATAK "
                  "already has:",
                  ("lista",
                   ["loadouts, the sets of visible toolbar tools,",
                    "the radial menu factory, which narrows a marker's menu,",
                    "the preferences that control map legibility,",
                    "its own toolbar with push-to-talk and chat buttons, shown only in the "
                    "audio scenario."]),
                  "The plugin never writes to or deletes ATAK's default loadout. Restoring is "
                  "therefore just switching back to it and replaying the preferences from a "
                  "snapshot taken before the first change."]),
                ("What it taught me",
                 ["Six defects passed compilation, unit tests and package checks, and only "
                  "surfaced on a running ATAK. Among them: the component entry in the plugin "
                  "descriptor can be ignored, the hidden-tools list does not map onto toolbar "
                  "slots, and empty item names break the radial menu.",
                  "The lesson is dull and expensive: ATAK plugins are verified on a device, "
                  "not in a test."]),
            ],
            "polityka": None,
        },
    },
    {
        "slug": "sarneg",
        "ikona": "sarneg.png",
        "zrzuty": [],
        "repo": None,
        "pl": {
            "nazwa": "Sarneg",
            "podtytul": "Wtyczka ATAK-CIV 5.8",
            "stan": "W Google Play",
            "skrot": (
                "Szyfruje liczby w wiadomości szyfrem SARNEG i zostawia resztę tekstu "
                "czytelną. Nic nie zapisuje na urządzeniu."
            ),
            "sekcje": [
                ("Po co to jest",
                 ["Pozycja, godzina, kurs i liczba ludzi to dane, które w wiadomości przez "
                  "radio albo czat niosą najwięcej. Reszta zdania zwykle nie zdradza nic, "
                  "czego przeciwnik już nie wie.",
                  "SARNEG chowa same liczby. Zdanie zostaje zrozumiałe dla odbiorcy i puste "
                  "dla kogoś, kto nie zna słowa klucza."]),
                ("Jak działa szyfr",
                 ["Słowo klucz to dziesięć różnych liter. Pozycja litery w słowie odpowiada "
                  "cyfrze: pierwsza to 0, ostatnia to 9. Przy słowie POLICJANTU tekst "
                  "„eta 1430\u201d wychodzi jako „eta OCIP\u201d.",
                  "Wielka litera w wyniku znaczy zaszyfrowaną cyfrę, mała znaczy tekst jawny. "
                  "Strefa MGRS zostaje jawna, bo to identyfikator miejsca, nie dana liczbowa.",
                  "To szyfr podstawieniowy, nie współczesna kryptografia. Chroni liczby przed "
                  "kimś, kto nie zna słowa klucza, przez czas jednej rozmowy."]),
                ("Co znika i kiedy",
                 ["Słowo klucz i treść żyją wyłącznie w pamięci. Nie ma pliku, nie ma wpisu "
                  "w ustawieniach ATAK-a, a dziennik notuje same nazwy zdarzeń.",
                  "Wynik kasuje odliczanie od 30 do 60 sekund, zależnie od długości tekstu. "
                  "Schowek systemowy wtyczka czyści osobno, 60 sekund po skopiowaniu. Okno "
                  "wyniku ma włączoną blokadę zrzutu ekranu."]),
                ("Czego się przy niej nauczyłem",
                 ["Przycisk „Wykonaj\u201d miał na XCoverze 5 czternaście pikseli wysokości "
                  "i leżał na krawędzi ekranu. Kompilacja, 103 testy i kontrola pakietu tego "
                  "nie widzą - wyszło dopiero przy zrzutach na telefonie."]),
            ],
            "polityka": "https://uirapuru.github.io/sarneg/privacy-policy.html",
        },
        "en": {
            "nazwa": "Sarneg",
            "podtytul": "ATAK-CIV 5.8 plugin",
            "stan": "On Google Play",
            "skrot": (
                "Encrypts the numbers in a message with the SARNEG cipher and leaves the rest "
                "of the text readable. It writes nothing to the device."
            ),
            "sekcje": [
                ("Why it exists",
                 ["A position, a time, a heading and a head count carry most of what a radio "
                  "or chat message is worth. The rest of the sentence usually gives away "
                  "nothing the other side does not already know.",
                  "SARNEG hides the numbers alone. The sentence stays readable for the "
                  "recipient and empty for anyone who does not know the key word."]),
                ("How the cipher works",
                 ["The key word is ten distinct letters. A letter's position stands for a "
                  "digit: the first is 0, the last is 9. With the key word POLICJANTU, "
                  "\u201ceta 1430\u201d comes out as \u201ceta OCIP\u201d.",
                  "A capital letter in the result means an encrypted digit; lowercase means "
                  "plain text. The MGRS zone stays in the clear, because it identifies a "
                  "place rather than being a number worth hiding.",
                  "This is a substitution cipher, not modern cryptography. It hides numbers "
                  "from someone who does not know the key word, for the length of one "
                  "conversation."]),
                ("What is cleared, and when",
                 ["The key word and the text live in memory only. There is no file, no entry "
                  "in the ATAK preferences, and the log records event names alone.",
                  "A countdown of 30 to 60 seconds wipes the result, depending on its length. "
                  "The plugin clears the system clipboard separately, 60 seconds after a copy. "
                  "The result window blocks screenshots."]),
                ("What it taught me",
                 ["On an XCover 5 the \u201cRun\u201d button was fourteen pixels tall and sat "
                  "on the edge of the screen. Compilation, 103 tests and the package checks "
                  "see none of that - it surfaced while taking screenshots on the phone."]),
            ],
            "polityka": "https://uirapuru.github.io/sarneg/privacy-policy.html",
        },
    },
    {
        "slug": "starlinktak",
        "ikona": "starlinktak.png",
        "zrzuty": [],
        "repo": None,
        "pl": {
            "nazwa": "StarlinkTAK",
            "podtytul": "Wtyczka ATAK-CIV 5.5 i nowszych",
            "stan": "Test zamknięty w Google Play",
            "skrot": (
                "Pomaga ustawić antenę Starlink w terenie. Pokazuje na mapie ATAK w 3D "
                "bieżący i zalecany kierunek anteny, przeszkody i satelity Starlink."
            ),
            "sekcje": [
                ("Po co to jest",
                 ["Antena Starlink podaje kierunek, w którym powinna patrzeć. W terenie trzeba "
                  "jeszcze wiedzieć, o ile stopni ją obrócić i pochylić oraz co zasłania niebo.",
                  "Wtyczka czyta antenę przez jej sieć Wi-Fi i rysuje oba kierunki jako wiązki "
                  "na mapie ATAK. Pod wykresem nieba podaje polecenie: o ile obrócić i o ile "
                  "pochylić antenę."]),
                ("Co jeszcze pokazuje",
                 ["Mapę przeszkód zapisaną przez antenę, satelity Starlink nad horyzontem, "
                  "w tym widoczne gołym okiem, oraz historię łącza z ostatnich 15 minut. "
                  "Pozycje satelitów wtyczka liczy z publicznych danych orbit CelesTrak."]),
                ("Satelita obsługujący to szacunek",
                 ["Antena nie podaje, z którym satelitą jest połączona. Wtyczka zgaduje go "
                  "z dwóch map przeszkód i zawsze oznacza wynik jako szacunek. Tryb „Szukaj "
                  "satelity\u201d co 15 sekund czyści mapę przeszkód anteny, więc przed "
                  "włączeniem ostrzega, że zebrana mapa zniknie."]),
                ("Czego się przy niej nauczyłem",
                 ["W stanie ustalonym mapa przeszkód anteny prawie się nie zmienia: w pomiarze "
                  "0 zmienionych komórek w 15 sekund i około 9 nowych na godzinę. Z samego "
                  "odczytu nie da się więc rozpoznać satelity. Stąd tryb, który mapę czyści."]),
            ],
            "polityka": "https://uirapuru.github.io/starlinktak/privacy-policy.html",
        },
        "en": {
            "nazwa": "StarlinkTAK",
            "podtytul": "Plugin for ATAK-CIV 5.5 and newer",
            "stan": "Closed testing on Google Play",
            "skrot": (
                "Helps you align a Starlink dish in the field. Shows the current and "
                "recommended dish direction in 3D on the ATAK map, with obstructions and "
                "Starlink satellites."
            ),
            "sekcje": [
                ("Why it exists",
                 ["A Starlink dish reports the direction it should point in. In the field you also "
                  "need to know how many degrees to rotate and tilt the dish, and what blocks "
                  "the sky.",
                  "The plugin reads the dish over its Wi-Fi network and draws both directions "
                  "as beams on the ATAK map. Below the sky chart it gives a command: how far "
                  "to rotate the dish and how far to tilt it."]),
                ("What else it shows",
                 ["The obstruction map recorded by the dish, Starlink satellites above the "
                  "horizon, including those visible to the naked eye, and the link history of "
                  "the last 15 minutes. Satellite positions come from public CelesTrak orbit "
                  "data."]),
                ("The serving satellite is an estimate",
                 ["The dish does not report which satellite it is connected to. The plugin "
                  "infers it from two obstruction maps and always labels the result as an "
                  "estimate. \u201cFind satellite\u201d mode clears the dish obstruction map "
                  "every 15 seconds, so the plugin warns you before it starts that the "
                  "collected map will be lost."]),
                ("What it taught me",
                 ["In steady state the dish obstruction map barely changes: the measurement "
                  "showed 0 changed cells in 15 seconds and about 9 new cells per hour. A plain "
                  "reading cannot identify the satellite. Hence the mode that clears the map."]),
            ],
            "polityka": "https://uirapuru.github.io/starlinktak/privacy-policy.html",
        },
    },
    {
        "slug": "modernui",
        "ikona": "modernui.png",
        "zrzuty": ["modernui-1.jpg", "modernui-2.jpg", "modernui-3.jpg"],
        "repo": None,
        "pl": {
            "nazwa": "Modern UI",
            "podtytul": "Wtyczka ATAK-CIV 5.5 i nowszych",
            "stan": "Test zamknięty w Google Play",
            "skrot": (
                "Chowa pasek narzędzi ATAK-a i układa najczęściej używane funkcje przy "
                "krawędziach ekranu, w zasięgu kciuka. Telefon w pionie, jedną ręką."
            ),
            "sekcje": [
                ("Po co to jest",
                 ["ATAK powstał na tablet trzymany poziomo. Na telefonie w pionie pasek "
                  "narzędzi zasłania mapę, a ikony leżą poza zasięgiem kciuka.",
                  "Modern UI chowa ten pasek i stawia dwie kolumny ikon w dolnej połowie "
                  "ekranu. Nie dodaje nowych funkcji. Każda ikona uruchamia to, co ATAK już "
                  "potrafi."]),
                ("Co widać na ekranie",
                 [("lista",
                   ["lewa kolumna: mapy, warstwy, postawienie punktu, pomiar odległości "
                    "i kierunku,",
                    "prawa kolumna: mapa 3D, obracanie mapy, kompas, własna pozycja, "
                    "powiększenie i pomniejszenie,",
                    "dolny rząd: czat, kontakty, menu „Więcej” i tryb „Tylko mapa”,",
                    "ramka stanów: godzina oraz stan serwera TAK, GPS i sieci komórkowej, "
                    "każdy w swoim kolorze."])]),
                ("Okna nad mapą",
                 ["Okna ATAK-a, na przykład kontakty albo menedżer nakładek, pływają nad "
                  "mapą. Da się je przesuwać, zmieniać ich rozmiar i chować do paska w rogu "
                  "ekranu. Mapa zostaje pod nimi w pełnym rozmiarze.",
                  "Położenie i rozmiar każdego okna wtyczka pamięta osobno dla pionu "
                  "i poziomu."]),
                ("Własny pasek i motywy",
                 ["W menu „Więcej” → „Dostosuj” wybierasz do sześciu narzędzi ATAK-a albo "
                  "innych wtyczek i ustawiasz ich kolejność. Motyw określa kolor przewodni, "
                  "tło i wielkość tekstu. Da się go zapisać do pliku i przenieść na inny "
                  "telefon."]),
                ("Czego się przy niej nauczyłem",
                 ["Obrót ekranu z wtyczki działa tylko przez intencję ATAK-a, nie przez "
                  "zapis ustawienia. Sam zapis zostawia okna po lewej stronie, a prawą "
                  "połowę ekranu szarą. Tę wadę pokazał telefon, nie emulator."]),
            ],
            "polityka": "https://uirapuru.github.io/modernui/privacy-policy.html",
        },
        "en": {
            "nazwa": "Modern UI",
            "podtytul": "Plugin for ATAK-CIV 5.5 and newer",
            "stan": "Closed testing on Google Play",
            "skrot": (
                "Hides the ATAK toolbar and lays the most used functions along the screen "
                "edges, within reach of a thumb. Phone in portrait, one hand."
            ),
            "sekcje": [
                ("Why it exists",
                 ["ATAK was designed for a tablet held in landscape. On a phone in portrait "
                  "the toolbar covers the map and the icons sit out of the thumb's reach.",
                  "Modern UI hides that toolbar and puts two columns of icons in the lower "
                  "half of the screen. It adds no features. Every icon runs something ATAK "
                  "already does."]),
                ("What is on screen",
                 [("lista",
                   ["left column: maps, layers, drop a point, measure distance and bearing,",
                    "right column: 3D map, map rotation, compass, own position, zoom in and "
                    "out,",
                    "bottom row: chat, contacts, the „More” menu and „Map only” mode,",
                    "status frame: the time plus TAK server, GPS and cellular status, each "
                    "in its own colour."])]),
                ("Windows above the map",
                 ["ATAK windows such as contacts or the overlay manager float above the map. "
                  "They can be moved, resized and collapsed into a strip in the screen "
                  "corner. The map stays at full size underneath.",
                  "The plugin remembers each window's position and size separately for "
                  "portrait and landscape."]),
                ("Custom toolbar and themes",
                 ["In „More” → „Customise” you pick up to six ATAK tools, or tools of other "
                  "plugins, and set their order. A theme sets the accent colour, the "
                  "background and the text size. It can be saved to a file and moved to "
                  "another phone."]),
                ("What it taught me",
                 ["Rotating the screen from a plugin works only through an ATAK intent, not "
                  "by writing the preference. The write alone leaves windows on the left "
                  "and the right half of the screen grey. The phone showed that defect, "
                  "the emulator did not."]),
            ],
            "polityka": "https://uirapuru.github.io/modernui/privacy-policy.html",
        },
    },
    {
        "slug": "mapfit",
        "ikona": "",
        "zrzuty": ["mapfit-1.jpg", "mapfit-2.jpg", "mapfit-3.jpg"],
        "repo": None,
        "pl": {
            "nazwa": "MapFit",
            "podtytul": "Wtyczka ATAK-CIV 5.8",
            "stan": "Działa",
            "skrot": (
                "Nakłada zdjęcie papierowej mapy na mapę ATAK-a. Wystarczą pary punktów "
                "albo jedno przecięcie siatki kilometrowej."
            ),
            "sekcje": [
                ("Po co to jest",
                 ["Papierowa mapa z odprawy, plan strzelnicy albo kserówka z siatką MGRS "
                  "zawierają dane, których nie ma w ATAK-u. Wbudowane narzędzie Rubber Sheet "
                  "pozwala nałożyć zdjęcie, ale obracanie i skalowanie palcem trwa długo "
                  "i wychodzi niedokładnie.",
                  "MapFit liczy położenie zdjęcia sam. Użytkownik wskazuje punkt na zdjęciu "
                  "i to samo miejsce na mapie. Od drugiej pary wtyczka pokazuje zdjęcie na "
                  "mapie, od trzeciej podaje błąd kontrolny w metrach dla każdej pary."]),
                ("Tryb siatki",
                 ["Gdy zdjęcie ma siatkę kilometrową, wtyczka wykrywa przecięcia linii sama, "
                  "bez sieci i bez uczenia maszynowego. Użytkownik stuka jedno przecięcie "
                  "i wpisuje jego dwucyfrowe opisy z brzegu mapy. Każde wykryte przecięcie "
                  "staje się parą punktów.",
                  "Zgiętą kartkę wtyczka dopasowuje kratka po kratce. Na planie poligonu "
                  "Wędrzyn, sfotografowanym telefonem, wykryła 143 przecięcia, a mediana "
                  "błędu na punktach kontrolnych wyniosła 20 m."]),
                ("Poprawka ręczna",
                 ["Uchwyty na mapie pozwalają przesunąć, obrócić i przeskalować zdjęcie po "
                  "dopasowaniu. Po zakończeniu zdjęcie zostaje w ATAK-u jako zwykła nakładka "
                  "Rubber Sheet."]),
                ("Czego się przy niej nauczyłem",
                 ["Pierwszy detektor siatki, dostrojony do dwóch zdjęć, po lekkim "
                  "przeskalowaniu zdjęcia dawał złą skalę bez żadnego ostrzeżenia. Pomógł "
                  "dopiero strażnik gęstości kratek i osobna próba na 92 zdjęciach."]),
            ],
            "polityka": None,
        },
        "en": {
            "nazwa": "MapFit",
            "podtytul": "ATAK-CIV 5.8 plugin",
            "stan": "Working",
            "skrot": (
                "Places a photo of a paper map on the ATAK map. Point pairs are enough, or "
                "a single intersection of the kilometre grid."
            ),
            "sekcje": [
                ("Why it exists",
                 ["A paper map from a briefing, a range plan or a photocopy with an MGRS "
                  "grid holds data that ATAK does not have. The built-in Rubber Sheet tool "
                  "can overlay a photo, but rotating and scaling it by hand takes long and "
                  "ends up imprecise.",
                  "MapFit computes where the photo lies. The user taps a point on the photo "
                  "and the same place on the map. From the second pair the plugin shows the "
                  "photo on the map; from the third it reports a control error in metres "
                  "for every pair."]),
                ("Grid mode",
                 ["When the photo has a kilometre grid, the plugin detects the line "
                  "intersections itself, offline and without machine learning. The user "
                  "taps one intersection and types its two-digit labels from the map "
                  "margin. Every detected intersection becomes a point pair.",
                  "A folded sheet is fitted cell by cell. On a plan of the Wędrzyn training "
                  "area, photographed with a phone, it found 143 intersections and the "
                  "median error at control points was 20 m."]),
                ("Manual adjustment",
                 ["Handles on the map move, rotate and scale the photo after the fit. When "
                  "the user finishes, the photo stays in ATAK as an ordinary Rubber Sheet "
                  "overlay."]),
                ("What it taught me",
                 ["The first grid detector, tuned on two photos, returned a wrong scale "
                  "without any warning once the photo was scaled slightly. A guard on cell "
                  "density and a separate trial on 92 photos fixed that."]),
            ],
            "polityka": None,
        },
    },
    {
        "slug": "sniperkit",
        "ikona": "sniperkit.png",
        "zrzuty": ["sniperkit-1.jpg", "sniperkit-2.jpg", "sniperkit-3.jpg"],
        "repo": None,
        "pl": {
            "nazwa": "SniperKIT",
            "podtytul": "Aplikacja na Androida",
            "stan": "Test zamknięty w Google Play",
            "skrot": (
                "Kalkulator balistyczny SniperTAK jako osobna aplikacja z własną mapą. "
                "Nie potrzebuje ATAK-a ani serwera TAK."
            ),
            "sekcje": [
                ("Po co to jest",
                 ["Nie każdy strzelec ma ATAK-a. Wersja wojskowa wymaga uprawnień, "
                  "a cywilna to osobna aplikacja, którą trzeba zainstalować i poznać.",
                  "SniperKIT liczy tym samym silnikiem co wtyczka SniperTAK, ale na własnej "
                  "mapie OpenStreetMap. Stuknięcie w mapę stawia cel. Odległość, azymut "
                  "i kąt strzału aplikacja czyta z mapy i z ukształtowania terenu."]),
                ("Co liczy",
                 [("lista",
                   ["poprawkę w pionie i w poziomie w tysięcznych, przeliczaną po każdej "
                    "zmianie,",
                    "czas lotu, prędkość i energię na celu, szansę trafienia, strefę "
                    "rażenia,",
                    "tabelę celów i kartę odległości dla punktu obserwacyjnego, z eksportem "
                    "do CSV,",
                    "tabele balistyczne co stały krok odległości,",
                    "WEZ, czyli szansę trafienia wyliczoną z niepewności danych "
                    "wejściowych."]),
                  "Nastawa liczy się tylko z kompletnego profilu broni. Puste pole nie "
                  "dostaje wartości domyślnej. Aplikacja pokazuje, której wartości brakuje."]),
                ("Wysyłka do klientów TAK",
                 ["Pozycję strzelca, punkt obserwacyjny i cele aplikacja wysyła jako "
                  "zdarzenia Cursor on Target, czyli w formacie, którego używają klienci "
                  "TAK. Zdarzenia idą multicastem w sieci lokalnej albo po TCP na wskazany "
                  "adres. Niewysłane czekają w telefonie, aż połączenie wróci."]),
                ("Jak powstała",
                 ["Ze 124 plików wtyczki SniperTAK tylko 8 dotykało biblioteki ATAK-a. "
                  "47 plików silnika przeszło do aplikacji bez zmian, razem z 470 testami. "
                  "Ciężar przenosin leżał w jednym pliku interfejsu, który miał 7724 "
                  "wiersze."]),
            ],
            "polityka": "https://uirapuru.github.io/sniperkit/privacy-policy.html",
        },
        "en": {
            "nazwa": "SniperKIT",
            "podtytul": "Android app",
            "stan": "Closed testing on Google Play",
            "skrot": (
                "The SniperTAK ballistic calculator as a standalone app with its own map. "
                "No ATAK and no TAK server needed."
            ),
            "sekcje": [
                ("Why it exists",
                 ["Not every shooter has ATAK. The military build needs clearance, and the "
                  "civilian one is a separate app to install and learn.",
                  "SniperKIT uses the same engine as the SniperTAK plugin, but on its own "
                  "OpenStreetMap map. A tap on the map places a target. The app reads range, "
                  "bearing and shot angle from the map and the terrain."]),
                ("What it computes",
                 [("lista",
                   ["elevation and windage in mils, recalculated after every change,",
                    "time of flight, velocity and energy at the target, hit probability, "
                    "danger space,",
                    "a target table and a range card for an observation post, with CSV "
                    "export,",
                    "ballistic tables at fixed distance steps,",
                    "WEZ, the hit probability derived from the uncertainty of your "
                    "inputs."]),
                  "The solution is computed only from a complete rifle profile. An empty "
                  "field gets no default value. The app tells you which value is missing."]),
                ("Sharing with TAK clients",
                 ["The app sends the shooter position, the observation post and targets as "
                  "Cursor on Target events, the format TAK clients use. Events go over "
                  "multicast on the local network or over TCP to an address you enter. "
                  "Unsent events wait on the phone until the connection returns."]),
                ("How it was made",
                 ["Of the 124 files in the SniperTAK plugin, only 8 touched the ATAK "
                  "library. 47 engine files moved into the app unchanged, together with "
                  "470 tests. The weight of the port sat in one interface file of 7,724 "
                  "lines."]),
            ],
            "polityka": "https://uirapuru.github.io/sniperkit/privacy-policy.html",
        },
    },
    {
        "slug": "ulan",
        "ikona": "ulan.png",
        "zrzuty": ["ulan-1.jpg", "ulan-2.jpg", "ulan-3.jpg"],
        "repo": None,
        "pl": {
            "nazwa": "Ułan",
            "podtytul": "Aplikacja na Androida",
            "stan": "Test zamknięty w Google Play",
            "skrot": (
                "Kalkulatory, filmy z lektorem i karty wiedzy do szkolenia indywidualnego "
                "żołnierza. Działa bez internetu i nie zbiera żadnych danych."
            ),
            "sekcje": [
                ("Po co to jest",
                 ["Żołnierz dostaje wiedzę w kilkunastu źródłach: instrukcje, prezentacje, "
                  "notatki z zajęć, filmy. W polu nie ma do nich dostępu, a telefon ma "
                  "zawsze.",
                  "Ułan zbiera tę wiedzę w jednej aplikacji, która działa bez sieci. Nie ma "
                  "konta, reklam ani analityki."]),
                ("Co zawiera",
                 [("lista",
                   ["strzelectwo: kalkulator balistyczny z profilami Grota, Beryla, Bora "
                    "i Sako TRG M10, przeliczniki MOA i tysięcznych, ćwiczenia bezstrzałowe, "
                    "dziennik strzelań,",
                    "nawigacja lądowa: współrzędne w stopniach, UTM i MGRS, azymut, "
                    "deklinacja, kompas, marsz na azymut,",
                    "rozpoznawanie sprzętu: 152 karty sprzętu rosyjskiego i 79 kart sprzętu "
                    "polskiego i NATO, quiz w dwóch trybach,",
                    "medycyna: TCCC z kartą MARCHE, pierwsza pomoc według wytycznych ERC "
                    "2025, 17 616 defibrylatorów AED z OpenStreetMap zapisanych "
                    "w aplikacji,",
                    "wiedza ogólnowojskowa: formularze meldunków SALUTE, SALT, GOTWA, LACE "
                    "i MIST, rozkaz bojowy, szyfr SARNEG, alfabet NATO,",
                    "14 filmów szkoleniowych z lektorem: azymut, Gwiazda Polarna, MGRS, "
                    "siatka mildot, opaska uciskowa, zasadzka liniowa i inne."])]),
                ("Czego jeszcze nie ma",
                 ["Karty przetrwania, TCCC i pierwszej pomocy nie przeszły przeglądu "
                  "instruktora. Każda ma o tym dopisek i nie zastępuje szkolenia. Cechy "
                  "rozpoznawcze sprzętu napisał model AI i czekają na sprawdzenie przez "
                  "człowieka, który ten sprzęt zna."]),
                ("Prywatność",
                 ["Aplikacja prosi o jedno uprawnienie: lokalizację, tylko na ekranie "
                  "wyszukiwania AED. Nie ma uprawnienia do internetu. Wszystko, co wpiszesz, "
                  "zostaje w telefonie i znika po przyciśnięciu „Usuń wszystkie dane”."]),
            ],
            "polityka": "https://uirapuru.github.io/ulan/polityka-prywatnosci.html",
        },
        "en": {
            "nazwa": "Ułan",
            "podtytul": "Android app",
            "stan": "Closed testing on Google Play",
            "skrot": (
                "Calculators, narrated videos and knowledge cards for the individual "
                "training of a soldier. Works offline and collects no data."
            ),
            "sekcje": [
                ("Why it exists",
                 ["A soldier gets knowledge from a dozen sources: manuals, slides, class "
                  "notes, videos. In the field none of them is at hand, but the phone "
                  "always is.",
                  "Ułan gathers that knowledge in one app that works without a network. "
                  "There is no account, no adverts and no analytics."]),
                ("What is inside",
                 [("lista",
                   ["shooting: a ballistic calculator with profiles for the Grot, Beryl, "
                    "Bor and Sako TRG M10, MOA and mil converters, dry-fire drills, "
                    "a shooting log,",
                    "land navigation: coordinates in degrees, UTM and MGRS, azimuth, "
                    "declination, compass, marching on a bearing,",
                    "equipment recognition: 152 cards of Russian equipment and 79 cards of "
                    "Polish and NATO equipment, a quiz in two modes,",
                    "medicine: TCCC with the MARCHE card, first aid under the ERC 2025 "
                    "guidelines, 17,616 AED defibrillators from OpenStreetMap stored in "
                    "the app,",
                    "general military knowledge: report forms SALUTE, SALT, GOTWA, LACE "
                    "and MIST, the combat order, the SARNEG cipher, the NATO alphabet,",
                    "14 narrated training videos: azimuth, Polaris, MGRS, the mil-dot "
                    "reticle, the tourniquet, the linear ambush and more."])]),
                ("What is not there yet",
                 ["The survival, TCCC and first-aid cards have not been reviewed by an "
                  "instructor. Each says so and none replaces training. The recognition "
                  "features of the equipment cards were written by an AI model and await "
                  "a check by someone who knows the equipment."]),
                ("Privacy",
                 ["The app asks for one permission: location, only on the AED search "
                  "screen. It has no internet permission. Everything you type stays on "
                  "the phone and goes away with „Delete all data”."]),
                ("Language",
                 ["The app is in Polish."]),
            ],
            "polityka": "https://uirapuru.github.io/ulan/polityka-prywatnosci.html",
        },
    },
]

# --- ebooki ----------------------------------------------------------------

EBOOKI = [
    {
        "slug": "poradnik-atak",
        "okladka": "atak-poradnik.jpg",
        "drive": "1wHZyoxdsE85kc6ldLgw3m0ZIDsmJD8iA",
        "drive_maly": None,
        "strony": 156,
        "wlasny": True,
        "pl": {
            "tytul": "Poradnik ATAK",
            "podtytul": "Ekosystem TAK od aplikacji po serwer",
            "skrot": ("Jak działa ATAK, po co komu serwer TAK i jak taki serwer postawić. "
                      "Po polsku, bo po polsku tego nie było."),
            "sekcje": [
                ("O czym jest",
                 ["ATAK to aplikacja mapowa, na której wojsko, straż i ratownicy prowadzą "
                  "wspólny obraz sytuacji. Dokumentacja jest po angielsku, rozproszona i pisana "
                  "dla osób, które już wiedzą.",
                  "Ten poradnik zaczyna od pytania, po co w ogóle ekosystem TAK, a kończy na "
                  "postawionym serwerze i podłączonych do niego telefonach."]),
                ("Co obejmuje",
                 [("lista",
                   ["aplikacje na urządzenia końcowe i różnice między nimi,",
                    "funkcje serwera TAK i to, kiedy serwer nie jest potrzebny,",
                    "porównanie dostępnych rozwiązań serwerowych,",
                    "certyfikaty, paczki połączeniowe i rejestrację urządzeń,",
                    "wtyczki: co robią i skąd je brać."])]),
                ("Dla kogo",
                 ["Dla osób, które chcą używać ATAK-a w grupie i nie mają obok nikogo, kto by "
                  "im to pokazał."]),
            ],
        },
        "en": {
            "tytul": "The ATAK Handbook",
            "podtytul": "The TAK ecosystem, from app to server",
            "skrot": ("How ATAK works, why anyone needs a TAK server, and how to stand one up. "
                      "Written in Polish, because nobody had."),
            "sekcje": [
                ("What it covers",
                 ["ATAK is a mapping app the military, fire services and rescue teams use to "
                  "share one picture of a situation. Its documentation is in English, scattered, "
                  "and written for people who already know.",
                  "The book starts with why the TAK ecosystem exists at all and ends with a "
                  "running server and phones connected to it."]),
                ("Contents",
                 [("lista",
                   ["end-user apps and how they differ,",
                    "what a TAK server does, and when you do not need one,",
                    "a comparison of the available server products,",
                    "certificates, connection packages and device enrolment,",
                    "plugins: what they do and where to get them."])]),
                ("Who it is for",
                 ["People who want to use ATAK as a group and have nobody around to show them."]),
                ("Language",
                 ["The book is written in Polish."]),
            ],
        },
    },
    {
        "slug": "vademecum-baofenga",
        "okladka": "vademecum-baofenga.jpg",
        "drive": "10rM6mkns8VptlVTlha4SP7fPnrVL7wDD",
        "drive_maly": None,
        "strony": 116,
        "wlasny": True,
        "pl": {
            "tytul": "Vademecum Baofenga",
            "podtytul": "Kompletny przewodnik po radiotelefonach Baofeng UV-5R",
            "skrot": ("Co wolno, czego nie wolno i jak w ogóle zaprogramować najtańsze radio "
                      "świata, żeby się na nim dogadać."),
            "sekcje": [
                ("O czym jest",
                 ["Baofeng UV-5R kosztuje tyle, co obiad, i dlatego trafia do kieszeni ludzi, "
                  "którzy nigdy wcześniej nie mieli radia. Instrukcja w pudełku jest tłumaczona "
                  "maszynowo i niczego nie wyjaśnia.",
                  "Ta książka wyjaśnia: jak radio działa, co znaczą pola w programatorze, jak "
                  "dobrać antenę i gdzie przebiega granica między pasmem, na którym wolno nadawać, "
                  "a takim, na którym nie wolno."]),
                ("Co obejmuje",
                 [("lista",
                   ["budowa i obsługa UV-5R krok po kroku,",
                    "programowanie kanałów, ręczne i przez komputer,",
                    "pasma PMR, CB i krótkofalarskie oraz przepisy, które ich dotyczą,",
                    "anteny: co daje wymiana i czego nie da,",
                    "zasięg w terenie i co go naprawdę ogranicza."])]),
                ("Dla kogo",
                 ["Dla turystów, ratowników, grup rekonstrukcyjnych i wszystkich, którzy kupili "
                  "Baofenga i utknęli na pierwszym menu."]),
            ],
        },
        "en": {
            "tytul": "The Baofeng Compendium",
            "podtytul": "A complete guide to Baofeng UV-5R radios",
            "skrot": ("What is allowed, what is not, and how to programme the cheapest radio in "
                      "the world so people can actually talk on it."),
            "sekcje": [
                ("What it covers",
                 ["A Baofeng UV-5R costs about as much as a meal, which is why it ends up in the "
                  "pockets of people who have never owned a radio. The manual in the box is "
                  "machine-translated and explains nothing.",
                  "This book explains how the radio works, what the fields in the programming "
                  "software mean, how to choose an antenna, and where the line runs between bands "
                  "you may transmit on and bands you may not."]),
                ("Contents",
                 [("lista",
                   ["the UV-5R, part by part, and how to operate it,",
                    "programming channels by hand and from a computer,",
                    "PMR, CB and amateur bands, and the rules that govern them,",
                    "antennas: what replacing one buys you and what it does not,",
                    "range in the field and what actually limits it."])]),
                ("Who it is for",
                 ["Hikers, rescue volunteers, reenactment groups, and anyone who bought a Baofeng "
                  "and got stuck on the first menu."]),
                ("Language",
                 ["The book is written in Polish."]),
            ],
        },
    },
    {
        "slug": "mindful-shooter",
        "okladka": "mindful-shooter.jpg",
        "drive": "1yetU7iRrjH2G0hg7gUOSk09OYedR6CMB",
        "drive_maly": "1FmmA3rsoAc9bMzwTBWeUx5xWH2s8cUQP",
        "strony": 52,
        "wlasny": True,
        "pl": {
            "tytul": "Mindful Shooter",
            "podtytul": "Uważność w strzelectwie sportowym",
            "skrot": ("Co dzieje się w głowie między decyzją a strzałem i dlaczego trening "
                      "uwagi poprawia wyniki bardziej niż kolejny tysiąc naboi."),
            "sekcje": [
                ("O czym jest",
                 ["Strzelectwo sportowe rozstrzyga się na poziomie uwagi, nie siły. Zawodnik, "
                  "który potrafi wrócić uwagą do przyrządów po nieudanym strzale, strzela lepszą "
                  "serię niż ten, który się na tym strzale zatrzymał.",
                  "Kompendium opisuje techniki uważności przełożone na konkretne czynności na "
                  "osi: oddech, rutynę przedstrzałową, pracę z myślami po błędzie."]),
                ("Skąd się wzięło",
                 ["Opracowanie powstało na podstawie kursu internetowego prowadzonego przez "
                  "psychologa sportu. Nie jest to podręcznik techniki strzeleckiej."]),
                ("Dla kogo",
                 ["Dla zawodników i instruktorów, którzy mają opanowaną technikę, a wyniki "
                  "wahają się z dnia na dzień."]),
            ],
        },
        "en": {
            "tytul": "Mindful Shooter",
            "podtytul": "Mindfulness in sport shooting",
            "skrot": ("What happens in your head between the decision and the shot, and why "
                      "training attention improves scores more than another thousand rounds."),
            "sekcje": [
                ("What it covers",
                 ["Sport shooting is decided by attention, not strength. A competitor who can "
                  "bring their attention back to the sights after a bad shot will shoot a better "
                  "string than one who stayed with that shot.",
                  "The book translates mindfulness techniques into concrete actions on the "
                  "line: breathing, the pre-shot routine, handling thoughts after a mistake."]),
                ("Where it came from",
                 ["It is based on an online course run by a sport psychologist. It is not a "
                  "manual of shooting technique."]),
                ("Who it is for",
                 ["Competitors and coaches whose technique is solid but whose scores swing from "
                  "day to day."]),
                ("Language",
                 ["The book is written in Polish."]),
            ],
        },
    },
    {
        "slug": "fry-the-brain",
        "bez_indeksu": True,   # tłumaczenie cudzej książki: poza wyszukiwarkami
        "okladka": "fry-the-brain.jpg",
        "drive": "1PXInsZeeQmz3xlg_ygsYcJuVEKZSjLvD",
        "drive_maly": "1xt_xj3wUqMaH3UzTKD-XOawiTHbBTrT5",
        "strony": 758,
        "wlasny": False,
        "autor": "John West",
        "pl": {
            "tytul": "Fry The Brain",
            "podtytul": "Sztuka snajperki miejskiej i jej rola we współczesnej wojnie partyzanckiej",
            "skrot": ("Tłumaczenie książki Johna Westa o snajperce miejskiej. 758 stron "
                      "o tym, że celem strzelca nie jest ciało, tylko psychika przeciwnika."),
            "sekcje": [
                ("O czym jest",
                 ["John West opisuje snajperkę miejską jako narzędzie oddziaływania "
                  "psychologicznego. Teza książki brzmi: pojedynczy strzelec zmienia zachowanie "
                  "całego pododdziału, i to jest jego rzeczywisty efekt, a nie liczba trafień.",
                  "Autor prowadzi wywód przez kampanie z Irlandii Północnej, Bałkanów, Iraku "
                  "i Czeczenii."]),
                ("Kto jest autorem",
                 ["Autorem jest John West. To tłumaczenie na polski, wykonane na własny użytek. "
                  "Prawa autorskie do treści należą do autora i wydawcy oryginału."]),
                ("Dwa pliki",
                 ["Wersja pełna zawiera ilustracje w wysokiej rozdzielczości i waży kilkaset "
                  "megabajtów. Wersja lekka ma ten sam tekst i mniejsze ilustracje."]),
            ],
        },
        "en": {
            "tytul": "Fry The Brain",
            "podtytul": "The art of urban sniping and its role in modern guerrilla warfare",
            "skrot": ("A Polish translation of John West's book on urban sniping. 758 pages "
                      "arguing that the target is the enemy's mind, not their body."),
            "sekcje": [
                ("What it covers",
                 ["John West treats urban sniping as an instrument of psychological effect. The "
                  "argument of the book is that a single shooter changes the behaviour of a whole "
                  "unit, and that this, not a hit count, is the real result.",
                  "The case studies run through Northern Ireland, the Balkans, Iraq and "
                  "Chechnya."]),
                ("Authorship",
                 ["The author is John West. This is a Polish translation made for private use. "
                  "Copyright in the text belongs to the author and the original publisher."]),
                ("Two files",
                 ["The full version carries high-resolution illustrations and runs to several "
                  "hundred megabytes. The light version has the same text with smaller images."]),
                ("Language",
                 ["The translation is in Polish."]),
            ],
        },
    },
    {
        "slug": "special-reconnaissance",
        "bez_indeksu": True,   # tłumaczenie cudzej książki: poza wyszukiwarkami
        "okladka": "sr-patrolling.jpg",
        "drive": "1H7XC9J93fvHwXxbi6_tBKi5Ha02SnW_P",
        "drive_maly": None,
        "strony": 508,
        "wlasny": False,
        "autor": None,
        "pl": {
            "tytul": "Rozpoznanie specjalne i patrolowanie małymi pododdziałami",
            "podtytul": "Special Reconnaissance and Advanced Small Unit Patrolling",
            "skrot": ("Tłumaczenie podręcznika patrolowania: przygotowanie misji, wykonanie, "
                      "zabezpieczenie, łączność i działania po powrocie. 508 stron."),
            "sekcje": [
                ("O czym jest",
                 ["Podręcznik prowadzi przez pełny cykl działania patrolu: przygotowanie przed "
                  "wyjściem, wykonanie zadania, zabezpieczenie działań, dowodzenie i łączność, "
                  "czynności po powrocie.",
                  "Osobne rozdziały obejmują wymagania wobec pojazdów oraz procedury działania "
                  "na wodzie."]),
                ("Skąd się wzięło",
                 ["To tłumaczenie na polski, wykonane na własny użytek. Prawa autorskie do "
                  "treści należą do autorów oryginału."]),
                ("Dla kogo",
                 ["Dla instruktorów i grup szkoleniowych, którym potrzebny jest wspólny "
                  "słownik i uporządkowany opis procedur po polsku."]),
            ],
        },
        "en": {
            "tytul": "Special Reconnaissance and Advanced Small Unit Patrolling",
            "podtytul": "Polish translation",
            "skrot": ("A translation of the patrolling manual: pre-mission work, execution, "
                      "support, command and communications, post-mission actions. 508 pages."),
            "sekcje": [
                ("What it covers",
                 ["The manual walks through a patrol's full cycle: preparation before departure, "
                  "execution, operational support, command and communications, and what happens "
                  "after the return.",
                  "Separate chapters cover vehicle requirements and water procedures."]),
                ("Where it came from",
                 ["This is a Polish translation made for private use. Copyright in the text "
                  "belongs to the original authors."]),
                ("Who it is for",
                 ["Instructors and training groups who need a shared vocabulary and an ordered "
                  "description of the procedures in Polish."]),
                ("Language",
                 ["The translation is in Polish."]),
            ],
        },
    },
]
