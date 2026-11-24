"""
Builds the Darts Training website (English and Polish) into website/site/.

    python3 website/src/build.py

Edit the texts below and the templates next to this file, then rebuild. The generated HTML is
committed so any static host (GitLab Pages, Netlify, …) can serve website/site as it is.
"""
from pathlib import Path

SRC = Path(__file__).resolve().parent
SITE = SRC.parent / "site"

APP_STORE = "https://apps.apple.com/app/id6751161867"
GOOGLE_PLAY = "https://play.google.com/store/apps/details?id=org.jgc.darts.training"
# Shown on the privacy page and in the footer. Leave empty until a support address is chosen.
CONTACT_EMAIL = "jgcmobileapps@gmail.com"
UPDATED = {"en": "23 November 2026", "pl": "23 listopada 2026"}

TEXT = {
    "en": {
        "lang": "en",
        "root": "",
        "other_lang_href": "pl/",
        "other_lang": "PL",
        "title": "Darts Training: Practice Coach – see what your throwing arm does",
        "description": "Darts practice app with camera throw analysis, proven drills, your own training plans and clear stats. Free on iPhone and Android.",
        "nav_throw": "Throw analysis",
        "nav_features": "Features",
        "nav_pro": "Pro",
        "nav_faq": "FAQ",
        "badge": "NEW: THROW ANALYSIS",
        "h1": "Practise with a plan. <span class=\"lime\">See what your throwing arm does.</span>",
        "lead": "Darts Training gives you the drills good players use, watches your throwing arm with the camera, and tells you what to work on next.",
        "store_apple_small": "Download on the",
        "store_google_small": "Get it on",
        "free_note": "Free to download · Pro is a one-time purchase, no subscription",
        "tip": "Your elbow dropped on darts 7, 8, 9 – <b>about 9 cm lower</b> than at the start.",
        "fact_1": "Free to start",
        "fact_2": "No account needed",
        "fact_3": "Works offline",
        "fact_4": "iPhone and Android",
        "fact_5": "English and Polish",
        "throw_eyebrow": "Throw analysis",
        "throw_h2": "Your phone becomes your coach.",
        "throw_p": "Stand your phone up next to the oche and throw as usual. The camera follows your arm on every dart and checks what changed.",
        "check_elbow": "Elbow",
        "check_elbow_p": "Released at the same height every time?",
        "check_body": "Body",
        "check_body_p": "Did you lean or sway?",
        "check_follow": "Follow-through",
        "check_follow_p": "Did your arm finish towards the target?",
        "check_rhythm": "Rhythm",
        "check_rhythm_p": "The same tempo, or rushed?",
        "throw_p2": "After each session you get a consistency score and plain tips. Pin a throw that felt right as your reference and replay any dart against it – in slow motion, overlaid or side by side.",
        "private": "The picture is analysed on your phone and never recorded or uploaded. Try it free for 9 darts.",
        "features_eyebrow": "Everything you need to practise",
        "features_h2": "Train smarter, not just longer.",
        "drills_h3": "Five proven drills",
        "drill_1": "<b>Bob's 27</b> – the classic doubles test, from D1 to the bull",
        "drill_2": "<b>Round the World</b> – singles, doubles or trebles, in order or at random",
        "drill_3": "<b>Scoring</b> – 30 darts at T20 for an honest 3-dart average",
        "drill_4": "<b>Checkouts</b> – random finishes from 2 to 170",
        "drill_5": "<b>501</b> – a solo leg or a match against the computer",
        "drills_p": "Big buttons you can hit with darts in your hand, undo one tap away, and the screen stays on while you play.",
        "card_plan": "Your own training",
        "card_plan_p": "Chain drills into one session – “Bob's 27, then 30 darts at T20, then 15 checkouts” – and play it straight through.",
        "card_stats": "Stats that mean something",
        "card_stats_p": "3-dart average, checkout % by range, hit rate on every double and treble, personal bests and your practice streak.",
        "card_coach": "Knows what to practise",
        "card_coach_p": "If D16 lags behind your other doubles or your checkouts dipped this week, the home screen suggests the right drill.",
        "card_private": "Your data stays yours",
        "card_private_p": "No account, no sign-up. Everything is stored on your phone, and you can export a backup at any time.",
        "card_themes": "Light and dark",
        "card_themes_p": "Easy on the eyes in a bright club or a dark garage – the app follows your phone's theme.",
        "card_entry": "Quick to enter",
        "card_entry_p": "Log a whole visit at once, or every dart when you want the detail. Built to be used between throws.",
        "pro_eyebrow": "Free and Pro",
        "pro_h2": "Pay once, keep it forever.",
        "free_h3": "Free",
        "free_price": "€0",
        "free_1": "All five drills and 501",
        "free_2": "Stats for the last 30 days",
        "free_3": "Up to 3 custom trainings",
        "free_4": "Throw analysis: 9 free darts",
        "free_5": "Ads",
        "pro_h3": "Pro",
        "pro_price": "One-time purchase · no subscription",
        "pro_1": "Throw analysis for every session, with history and replay",
        "pro_2": "Full stats history",
        "pro_3": "Unlimited custom trainings",
        "pro_4": "Coach suggestions from all your history",
        "pro_5": "No ads",
        "faq_h2": "Questions",
        "q1": "Does the app record video of me?",
        "a1": "No. Throw analysis looks at the camera picture on your phone, finds your arm and body, and throws the picture away straight after. Only the measurements of each dart are kept, on your phone.",
        "q2": "Where do I put the phone?",
        "a2": "Upright, side-on to the throwing line, about 2–3 metres away and roughly at elbow height, so your whole body is in the picture. The front camera lets you watch yourself while you throw.",
        "q3": "Which phones does it work on?",
        "a3": "iPhone and Android phones and tablets. Throw analysis works best on recent phones, which can check more frames per second.",
        "q4": "Is it really free?",
        "a4": "Yes – all drills, stats for the last 30 days, three custom trainings and 9 darts of throw analysis are free. Pro unlocks the rest with a single purchase.",
        "q5": "Do I need an account?",
        "a5": "No. There is no sign-up and nothing is stored on a server. You can export a backup of your sessions whenever you like.",
        "q6": "Which languages are available?",
        "a6": "English and Polish. The app follows your phone's language.",
        "cta_h2": "Ready to throw?",
        "cta_p": "Download Darts Training and see what your throwing arm really does.",
        "privacy": "Privacy policy",
        "contact": "Contact",
        "rights": "Darts Training",
    },
    "pl": {
        "lang": "pl",
        "root": "../",
        "other_lang_href": "../",
        "other_lang": "EN",
        "title": "Darts Training: Practice Coach – zobacz, co robi Twoja ręka",
        "description": "Aplikacja do treningu darta z analizą rzutu kamerą, sprawdzonymi ćwiczeniami, własnymi planami i czytelnymi statystykami. Za darmo na iPhone'a i Androida.",
        "nav_throw": "Analiza rzutu",
        "nav_features": "Funkcje",
        "nav_pro": "Pro",
        "nav_faq": "Pytania",
        "badge": "NOWOŚĆ: ANALIZA RZUTU",
        "h1": "Trenuj z planem. <span class=\"lime\">Zobacz, co robi Twoja ręka.</span>",
        "lead": "Darts Training daje Ci ćwiczenia, z których korzystają dobrzy gracze, obserwuje kamerą Twoją rękę rzucającą i podpowiada, nad czym pracować.",
        "store_apple_small": "Pobierz z",
        "store_google_small": "Pobierz z",
        "free_note": "Pobieranie za darmo · Pro to jednorazowy zakup, bez abonamentu",
        "tip": "Łokieć opadł przy lotkach 7, 8, 9 – <b>około 9 cm niżej</b> niż na początku.",
        "fact_1": "Za darmo na start",
        "fact_2": "Bez zakładania konta",
        "fact_3": "Działa offline",
        "fact_4": "iPhone i Android",
        "fact_5": "Polski i angielski",
        "throw_eyebrow": "Analiza rzutu",
        "throw_h2": "Telefon staje się Twoim trenerem.",
        "throw_p": "Postaw telefon obok linii rzutu i rzucaj jak zwykle. Kamera śledzi Twoją rękę przy każdej lotce i sprawdza, co się zmieniło.",
        "check_elbow": "Łokieć",
        "check_elbow_p": "Czy wypuszczasz lotkę zawsze na tej samej wysokości?",
        "check_body": "Sylwetka",
        "check_body_p": "Czy się pochylasz albo kołyszesz?",
        "check_follow": "Prowadzenie",
        "check_follow_p": "Czy ręka kończy ruch w stronę celu?",
        "check_rhythm": "Rytm",
        "check_rhythm_p": "To samo tempo czy pośpiech?",
        "throw_p2": "Po każdej sesji dostajesz wynik powtarzalności i proste wskazówki. Ustaw dobry rzut jako wzorzec i porównuj z nim każdą lotkę – w zwolnionym tempie, nałożone albo obok siebie.",
        "private": "Obraz jest analizowany na telefonie i nigdy nie jest nagrywany ani wysyłany. Wypróbuj za darmo na 9 lotkach.",
        "features_eyebrow": "Wszystko do treningu",
        "features_h2": "Trenuj mądrzej, nie tylko dłużej.",
        "drills_h3": "Pięć sprawdzonych ćwiczeń",
        "drill_1": "<b>Bob's 27</b> – klasyczny test doubli, od D1 do bulla",
        "drill_2": "<b>Dookoła tarczy</b> – single, double lub treble, po kolei albo losowo",
        "drill_3": "<b>Punktowanie</b> – 30 rzutek w T20 i uczciwa średnia z 3 rzutek",
        "drill_4": "<b>Kończenia</b> – losowe checkouty od 2 do 170",
        "drill_5": "<b>501</b> – samodzielny leg albo mecz z komputerem",
        "drills_p": "Duże przyciski, które trafisz z rzutkami w dłoni, cofnięcie pod ręką i ekran, który nie gaśnie podczas gry.",
        "card_plan": "Własny trening",
        "card_plan_p": "Połącz ćwiczenia w jedną sesję – „Bob's 27, potem 30 rzutek w T20, potem 15 checkoutów” – i graj od początku do końca.",
        "card_stats": "Statystyki, które coś mówią",
        "card_stats_p": "Średnia z 3 rzutek, checkouty według zakresu, skuteczność na każdym doublu i treblu, rekordy i seria treningów.",
        "card_coach": "Wie, co ćwiczyć",
        "card_coach_p": "Gdy D16 odstaje od innych doubli albo checkouty spadły w tym tygodniu, ekran główny podpowie właściwe ćwiczenie.",
        "card_private": "Dane zostają u Ciebie",
        "card_private_p": "Bez konta i rejestracji. Wszystko jest zapisane na telefonie, a kopię zapasową wyeksportujesz w każdej chwili.",
        "card_themes": "Jasny i ciemny",
        "card_themes_p": "Wygodnie w jasnym klubie i w ciemnym garażu – aplikacja dopasowuje się do motywu telefonu.",
        "card_entry": "Szybkie wpisywanie",
        "card_entry_p": "Wpisz całą wizytę naraz albo każdą rzutkę, gdy chcesz więcej szczegółów. Zaprojektowane do używania między rzutami.",
        "pro_eyebrow": "Darmowa wersja i Pro",
        "pro_h2": "Płacisz raz, masz na zawsze.",
        "free_h3": "Darmowa",
        "free_price": "0 zł",
        "free_1": "Wszystkie pięć ćwiczeń i 501",
        "free_2": "Statystyki z ostatnich 30 dni",
        "free_3": "Do 3 własnych treningów",
        "free_4": "Analiza rzutu: 9 darmowych lotek",
        "free_5": "Reklamy",
        "pro_h3": "Pro",
        "pro_price": "Jednorazowy zakup · bez abonamentu",
        "pro_1": "Analiza rzutu w każdej sesji, z historią i porównaniem",
        "pro_2": "Pełna historia statystyk",
        "pro_3": "Nieograniczona liczba własnych treningów",
        "pro_4": "Podpowiedzi trenera na podstawie całej historii",
        "pro_5": "Bez reklam",
        "faq_h2": "Pytania",
        "q1": "Czy aplikacja nagrywa mnie kamerą?",
        "a1": "Nie. Analiza rzutu patrzy na obraz z kamery na telefonie, znajduje rękę i sylwetkę, a obraz od razu odrzuca. Zapisywane są tylko pomiary każdej lotki, na Twoim telefonie.",
        "q2": "Gdzie postawić telefon?",
        "a2": "Pionowo, bokiem do linii rzutu, około 2–3 metry od siebie i mniej więcej na wysokości łokcia, tak żeby cała sylwetka była w kadrze. Przedni aparat pozwala Ci widzieć siebie podczas rzucania.",
        "q3": "Na jakich telefonach działa?",
        "a3": "Na iPhone'ach oraz telefonach i tabletach z Androidem. Analiza rzutu działa najlepiej na nowszych telefonach, które sprawdzają więcej klatek na sekundę.",
        "q4": "Czy to naprawdę za darmo?",
        "a4": "Tak – wszystkie ćwiczenia, statystyki z 30 dni, trzy własne treningi i 9 lotek analizy rzutu są za darmo. Pro odblokowuje resztę jednym zakupem.",
        "q5": "Czy muszę zakładać konto?",
        "a5": "Nie. Nie ma rejestracji i nic nie jest zapisywane na serwerze. Kopię zapasową sesji wyeksportujesz, kiedy chcesz.",
        "q6": "W jakich językach jest aplikacja?",
        "a6": "Po polsku i po angielsku. Aplikacja dopasowuje się do języka telefonu.",
        "cta_h2": "Czas na rzucanie?",
        "cta_p": "Pobierz Darts Training i zobacz, co naprawdę robi Twoja ręka.",
        "privacy": "Polityka prywatności",
        "contact": "Kontakt",
        "rights": "Darts Training",
    },
}

PRIVACY = {
    "en": {
        "title": "Privacy policy – Darts Training",
        "h1": "Privacy policy",
        "updated": "Last updated: {updated}",
        "body": """
<p>This policy explains what the Darts Training app (“the app”) for iPhone and Android does with your data. In short: your training data stays on your phone, the camera picture is never recorded or sent anywhere, and there is no account.</p>
<h2>Who is responsible</h2>
<p>The app is developed and published by Krzysztof Martys, the developer named on the App Store and Google Play.{contact_sentence}</p>
<h2>Data stored on your phone</h2>
<ul>
<li>Your training sessions, scores, statistics, custom trainings and settings are stored only on your device. They are not sent to us or to any server.</li>
<li>You can export a backup file yourself. Where you send that file is up to you.</li>
<li>Deleting the app, or using “Delete all sessions” in the app, removes this data.</li>
</ul>
<h2>Camera (Throw analysis)</h2>
<ul>
<li>Throw analysis uses the camera only while you have it open. The picture is analysed on your device to find body points such as your shoulder, elbow and wrist.</li>
<li>The picture is never recorded, stored or uploaded. Only the measurements of each dart (for example elbow height and timing) and the body points around each throw are saved, on your device, so you can review and compare throws.</li>
<li>You can refuse or withdraw camera access in your phone's settings at any time; the rest of the app keeps working.</li>
</ul>
<h2>Purchases</h2>
<p>The Pro upgrade is sold through the App Store or Google Play. Payments are handled entirely by Apple or Google; we never receive your payment details. The app only asks the store whether Pro has been bought.</p>
<h2>Advertising</h2>
<p>The free version can show ads from Google AdMob. To show and measure ads, Google may collect information such as device identifiers, IP address and ad interactions, as described in <a href="https://policies.google.com/technologies/ads">Google's advertising policies</a>. Depending on where you live, you may be asked for consent, and you can limit ad tracking in your phone's settings. Buying Pro removes ads.</p>
<h2>No analytics, no account</h2>
<p>The app does not use analytics or crash-reporting services and does not ask you to create an account.</p>
<h2>Children</h2>
<p>The app is not directed at children under 13 and does not knowingly collect data from them.</p>
<h2>Your rights</h2>
<p>Because your training data stays on your device, you are in full control of it: you can view, export or delete it in the app. For questions about ads data collected by Google, see <a href="https://policies.google.com/privacy">Google's privacy policy</a>.</p>
<h2>Changes</h2>
<p>If this policy changes, the new version will be published on this page with a new date.</p>
""",
    },
    "pl": {
        "title": "Polityka prywatności – Darts Training",
        "h1": "Polityka prywatności",
        "updated": "Ostatnia aktualizacja: {updated}",
        "body": """
<p>Ta polityka wyjaśnia, co aplikacja Darts Training („aplikacja”) na iPhone'a i Androida robi z Twoimi danymi. W skrócie: dane treningowe zostają na Twoim telefonie, obraz z kamery nigdy nie jest nagrywany ani nigdzie wysyłany, a konto nie jest potrzebne.</p>
<h2>Kto odpowiada za dane</h2>
<p>Aplikację tworzy i publikuje Krzysztof Martys, deweloper wskazany w App Store i Google Play.{contact_sentence}</p>
<h2>Dane zapisane na telefonie</h2>
<ul>
<li>Sesje treningowe, wyniki, statystyki, własne treningi i ustawienia są zapisywane wyłącznie na Twoim urządzeniu. Nie trafiają do nas ani na żaden serwer.</li>
<li>Możesz sam wyeksportować plik kopii zapasowej. To, gdzie go wyślesz, zależy od Ciebie.</li>
<li>Usunięcie aplikacji albo opcja „Usuń wszystkie sesje” w aplikacji kasuje te dane.</li>
</ul>
<h2>Kamera (analiza rzutu)</h2>
<ul>
<li>Analiza rzutu korzysta z kamery tylko wtedy, gdy masz ją otwartą. Obraz jest analizowany na urządzeniu, żeby znaleźć punkty sylwetki, takie jak bark, łokieć i nadgarstek.</li>
<li>Obraz nigdy nie jest nagrywany, zapisywany ani wysyłany. Na urządzeniu zapisywane są tylko pomiary każdej lotki (np. wysokość łokcia i czas rzutu) oraz punkty sylwetki wokół rzutu, żebyś mógł przeglądać i porównywać rzuty.</li>
<li>W każdej chwili możesz odmówić dostępu do kamery albo go cofnąć w ustawieniach telefonu; reszta aplikacji działa dalej.</li>
</ul>
<h2>Zakupy</h2>
<p>Wersję Pro kupujesz przez App Store lub Google Play. Płatności w całości obsługuje Apple lub Google; nie otrzymujemy Twoich danych płatniczych. Aplikacja pyta sklep tylko o to, czy Pro zostało kupione.</p>
<h2>Reklamy</h2>
<p>Darmowa wersja może wyświetlać reklamy Google AdMob. Aby wyświetlać i mierzyć reklamy, Google może zbierać informacje takie jak identyfikatory urządzenia, adres IP i interakcje z reklamami, zgodnie z <a href="https://policies.google.com/technologies/ads">zasadami reklamowymi Google</a>. W zależności od miejsca zamieszkania możesz zostać poproszony o zgodę, a śledzenie reklam ograniczysz w ustawieniach telefonu. Zakup Pro usuwa reklamy.</p>
<h2>Bez analityki i bez konta</h2>
<p>Aplikacja nie korzysta z usług analitycznych ani raportowania awarii i nie wymaga zakładania konta.</p>
<h2>Dzieci</h2>
<p>Aplikacja nie jest skierowana do dzieci poniżej 13 roku życia i świadomie nie zbiera ich danych.</p>
<h2>Twoje prawa</h2>
<p>Dane treningowe zostają na Twoim urządzeniu, więc masz nad nimi pełną kontrolę: możesz je przeglądać, eksportować i usuwać w aplikacji. W sprawie danych reklamowych zbieranych przez Google zobacz <a href="https://policies.google.com/privacy">politykę prywatności Google</a>.</p>
<h2>Zmiany</h2>
<p>Jeśli ta polityka się zmieni, nowa wersja zostanie opublikowana na tej stronie z nową datą.</p>
""",
    },
}

CONTACT_SENTENCE = {"en": " Contact: <a href=\"mailto:{email}\">{email}</a>.", "pl": " Kontakt: <a href=\"mailto:{email}\">{email}</a>."}


def fill(template: str, values: dict) -> str:
    for key, value in values.items():
        template = template.replace("{{" + key + "}}", value)
    assert "{{" not in template, f"unfilled placeholder near: {template[template.index('{{'):][:40]}"
    return template


def main():
    page = (SRC / "page.html").read_text()
    legal = (SRC / "privacy.html").read_text()
    contact_link = {
        lang: (f'<a href="mailto:{CONTACT_EMAIL}">{TEXT[lang]["contact"]}</a>' if CONTACT_EMAIL else "")
        for lang in TEXT
    }
    for lang, text in TEXT.items():
        out = SITE if lang == "en" else SITE / lang
        out.mkdir(parents=True, exist_ok=True)
        common = {**text, "app_store": APP_STORE, "google_play": GOOGLE_PLAY, "contact_link": contact_link[lang]}
        (out / "index.html").write_text(fill(page, common))
        policy = PRIVACY[lang]
        body = policy["body"].replace(
            "{contact_sentence}", CONTACT_SENTENCE[lang].format(email=CONTACT_EMAIL) if CONTACT_EMAIL else ""
        )
        (out / "privacy.html").write_text(fill(legal, {
            **common,
            "page_title": policy["title"],
            "h1": policy["h1"],
            "updated": policy["updated"].format(updated=UPDATED[lang]),
            "body": body,
        }))
        print(f"{lang}: {out.relative_to(SITE.parent)}")
    if not CONTACT_EMAIL:
        print("note: CONTACT_EMAIL is empty, so no contact address is shown yet")


if __name__ == "__main__":
    main()
