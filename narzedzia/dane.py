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
        "pl": {
            "nazwa": "SniperTAK",
            "podtytul": "Wtyczka ATAK-CIV",
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
                ("Znany błąd",
                 ["Podczas przenoszenia silnika balistycznego na komputer wyszło, że całkowanie "
                  "toru pocisku jest ucięte po czterech sekundach lotu. Powyżej mniej więcej "
                  "1600 metrów wyliczona elewacja zaczyna maleć zamiast rosnąć. Na dystansach "
                  "poniżej tej granicy wynik jest poprawny."]),
            ],
            "polityka": "https://uirapuru.github.io/sniperTAK/privacy-policy.html",
        },
        "en": {
            "nazwa": "SniperTAK",
            "podtytul": "ATAK-CIV plugin",
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
                ("Known defect",
                 ["Porting the ballistic engine to the desktop revealed that trajectory "
                  "integration is cut off after four seconds of flight. Beyond roughly 1600 "
                  "metres the computed elevation starts falling instead of rising. Below that "
                  "range the result is correct."]),
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
            "podtytul": "Wtyczka ATAK-CIV 5.8",
            "stan": "Działa",
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
                  "zostawia białą."]),
            ],
            "polityka": None,
        },
        "en": {
            "nazwa": "PrintPlugin",
            "podtytul": "ATAK-CIV 5.8 plugin",
            "stan": "Working",
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
                  "leaves the rest of the area white."]),
            ],
            "polityka": None,
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
