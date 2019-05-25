komentarz_pytanie = ["Czy to jest Twoja ostateczna odpowiedź?",
"Czy jesteś pewnien swojej odpowiedzi?",
"Jesteś pewien, że nie chcesz zmienić odpowiedzi?",
"Definitywnie?",
"Czy to jest twoja ostateczna decyzja?",
"Obstajesz przy swoim?",
"Czy Twoja mama poparłaby Twój wybór?",
"Zastanowiłeś się dobrze?",
"Rozumiem, że nie zmienisz już zdania?",
"Czy to jest na 100% dobra odpowiedź?",
"Widzę, że się nie wahasz. Mam rację?",
"Na pewno ta odpowiedź?"]

print("Witam, nazywam się Hubert Urbański i będę prowadził Twoją dzisiejszą grę. \nPowiedz jak się nazywasz uczestniku!")
uczestnik = input()
while True:
    j = random.randint(0,11)
    print(komentarz_pytanie[j])
    odp1 = input()
    if odp1 == "tak" or odp1 == "Tak":
        print("W takim razie zaznaczam odpowiedź ", odpowiedz)
        break
    elif odp1 == "nie" or odp1 == "Nie":
        print(uczestnik, ", czy w takim razie chcesz zmienić swoją odpowiedź?")
        odp2 = input()
        if odp2 == "tak" or odp2 == "Tak":
            print("Na którą opcję zmieniasz?")
            odpowiedz2 = input()
            odpowiedz = odpowiedz2
        elif odp2 == "nie" or odp2 == "Nie":
            print("Skoro tak mówisz, zaznaczam odpowiedź ", odpowiedz)
        else:
            print(uczestnik,",konkretnie proszę - tak czy nie?")
    else:
        print(uczestnik, ", nie ma, że \"",odp1, "\" potrzebuję definitywnej odpowiedzi - tak lub nie!")
