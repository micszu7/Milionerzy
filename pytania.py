import random

pytania=["Jak określa się osobę na pozór spokojną i nieśmiałą?:\n A.ogień i woda B.Słomiany ogień C.Anielska woda D.Cicha woda",
"Umowa cywilnoprawna, zawierana zazwyczaj zamiast umowy o pracę, to tak zwana umowa:\n A.odpadkowa B.śmieciowa C.resztkowa D.okrawkowa",
"Co zalewa ten, kto nie wylewa za kołnierz?:\nA.fundamenty B.ognisko C.zioła D.robaka",
"Co ma na nogach panczenista?:\n A.korki B.narty C.łyżwy D.płetwy",
"Czym bez obaw mozna popić zażywane lekarstwa?:\n A.sokiem z grejfruta B.letnią wodą C.mocną kawą D.gorącą herbatą",
"Jaką cześć liter w wyrazie 'bajzel' stanowią samogłoski?:\nA.jedną piątą B.jedną czwartą C.jedną trzecią D.jedną drugą",
"Litr chłodnej wody waży w przybliżeniu:\nA.10 funtów B.kilogram C.2 dekagramy D.10 uncji",
"Przydomek wiedźmina Geralta wskazuje na to, że bohater sagi Andrzeja Sapkowskiego pochodzi z...\nA.Vengerbergu B.Oxenfurtu C.Rivii D.Tretogoru",
"Ile linii metra jest w Warszawie?\nA.1 B.2 C.3 D.4",
"Pierwsze litery tablicy rejestracyjnej jakiego powiatu tłumaczy się żartobliwie jako Centrum Tadeusza R. albo Co Tu Robisz?\nA.tarnobrzeskiego B.toruńskiego C.tyskiego D.tureckiego",
"Agata Duda witała się ze swoimi uczniami, mówiąc:\nA.Guten Morgen B.Good Morning C.Bonjour D.Boungiorno",
"Które z państw na Bliskim Wschodzie nie graniczy z pozostałymi?\nA.Arabia Saudyjska B.Oman C.Jemen D.Syria",
"Zje pozostałe:\nA.kijanka B.żyworódka rzeczna C.rzęsorek rzeczek D.larwa chruścika",
"Ferruccio Lamborghini, zanim zajął się produkcją samochodów, był producentem przede wszystkim:\nA.motocykli B.tokarek C.ciągników D.maszyn przędzalniczych",
"Dokończ słowa Agnieszki Osieckiej:Do domu wrócimy, w piecu napalimy, nakarmimy psa. Przed nocą zdążymy...\nA.szkopom dołożymy B.tylko zwyciężymy C.wojna to nie gra D.w oku błyśnie łza",
"Robert Pasut, Rafał Masny i Czarek Jóźwik to youtuberzy:\nA.Lekcewarzy B.Abstrachuje C.Ignoróje D.Ómniejsza",
"Płetwą grzbietową nie pruje wody:\nA.Długoszpar B.Kosogon C.Orka D.Wal grenlandzki",
"Który utwór Juliusza Słowackiego napisany jest prozą?\n A.'Godzina myśli' B.'W Szwajcarii' C.'Anheli' D.'Arab'",
"Likier maraskino produkuje się z maraski, czyli odmiany:\nA.wiśni B.jabłoni C.Figi D.Gruszy",
"Który aktor urodził się w roku opatentowania kinematografu braci Lumière?:\nA.Rudolph Valentino B.Humphrey Bogart C.Charlie Chaplin D.Fred Astaire",
"Komiksowym 'dzieckiem' rysownika Boba Kane'a jest:\nA.Superman B.Batman C.Spider-Man D.Captain America",
"Kto jest mistrzem tego samego oręża, w jakim specjalizowała się mitologiczna Artemida?:\nA.Zorro B.Legolas C.Don Kichot D.Longinus Podbipięta",
"Mowa w obronie poety Archiasza przeszła do historii jako jeden z najświetniejszych popisów retorycznych:\nA.Izokratesa B.Cycerona C.Demostenesa D.Kwintyliana",
"Rybą nie jest:\nA.Świnka B.Rozpiór C.Krasnopiórka D.Kraska",
"Odrażający drab z Kabaretu Starszych Panów dubeltówkę weźmie, wyjdzie i...\nA.Rach-ciach! B.Buch,Buch! C.Z rur dwóch D.Bum w brzuch",
"Kto był nadwornym malarzem króla Filipa IV Habsburga?:\nA.Marcello Bociarelli B.Jan van Eyck C. Diego Velazquez D.Jaques-Louis David",
"Z gry na jakim instrumencie słynie Czesław Mozil?:z\nA.Na kornecie B.Na akordeonie C.Na djembe D.Na ksylofonie"]

odpowiedzi=["D","B","D","C","B","C","B","C","B","B","A","D","C","C","B","B","D","C","A","A","B","B","D","D","B","C","D"]

licznik = 0

kwoty = ["500 zł","1 000 zł", "2 000 zł", "5 000 zł", "10 000 zł", "20 000 zł", "40 000 zł", "75 000 zł", "125 000 zł", "250 000 zł", "500 000 zł", "1 000 000 zł"]

numer_pytania = []
while len(numer_pytania)<12:
    r = random.randint(0,25)
    if r not in numer_pytania:
        numer_pytania.append(r)

while True:
    i = numer_pytania[licznik]
    licznik += 1
    print("Pytanie:",pytania[i])
    print("Jaka jest Twoja odpowiedź?")
    odpowiedz=input()
    l=licznik-1
    if odpowiedz==odpowiedzi[i]:
            if licznik<12:
                print("To jest poprawna odpowiedź.\n Zdobywasz " , kwoty[l], "\n")
                if licznik == 2 or licznik == 7:
                    print("To kwota gwarantowana\n")
            if licznik == 12:
                print("TO DOBRA ODPOWIEDŻ! WYGRYWASZ 1 000  000 ZŁOTYCH!")
                break
    else:
        print("To zła odpowiedź\n Dla Ciebie ",uczestnik," nasza przygoda po   milion się kończy!")
        if licznik >= 2 and licznik < 7:
            print("Otrzymujesz kwotę gwarantowaną 1 000 zł!")
        elif licznik >= 7:
            print("Otrzymujesz kwotę gwarantowaną 40 000 zł!")
        break
