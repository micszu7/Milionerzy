import random

kola_ratunkowe = ["Telefon do przyjaciela", "Pół na pół", "Pytanie do publiczności"]

mozliwe_odp = ["A","B","C","D"]
odp_wagi1 = [0.85,0.05,0.05,0.05]
odp_wagi2 = [0.7,0.1,0.1,0.1]
odp_wagi3 = [0.55,0.15,0.15,0.15]

kola_ratunkowe1=kola_ratunkowe
print("Masz dostęp do kół ratunkowych:\n" ,"1. ", kola_ratunkowe1[0], "\n2. ", kola_ratunkowe1[1], "\n3. ", kola_ratunkowe1[2],"\n")

kolo = str(input("Czy chcesz wykorzystać koło ratunkowe?\n"))

if kolo == "tak":
    x=0
    while x<1:
        print("Które koło chcesz wykorzystać?")
        kolo_wybor = int(input())
        if kola_ratunkowe1[kolo_wybor - 1]=="X":
            print("To koło zostało już wybrane")
        else:
            x=+1
    if kolo_wybor == 1:
        print("Wybrałeś: ", kola_ratunkowe[0])
        print("Dzwonimy do Twojej mamy bo nie masz przyjaciół")
        print("Dzień dobry pani mamo, jaka według pani będzie prawidłowa odpowiedź?")
        p2 = mozliwe_odp
        for n in p2[:]:
            if n == odpowiedzi[i]:
                p2.remove(n)
        p3 = [odpowiedzi[i],p2[0],p2[1],p2[2]]
        if licznik <= 5:
            podpowiedz = random.choices(p3,odp_wagi1)
        elif licznik > 5 and licznik <= 9:
            podpowiedz = random.choices(p3,odp_wagi2)
        elif licznik > 9 and licznik <= 12:
            podpowiedz = random.choices(p3,odp_wagi3)


        print("MAMA: Według mnie odpowiedzią na to pytanie będzie: ", podpowiedz, "\nA na obiad będą ziemniaki\n")
        kola_ratunkowe1[0]="X"
    elif kolo_wybor == 2:
        print("Wybrałeś: ", kola_ratunkowe[1])
        print("Proszę o usunięcie połowy odpowiedzi")
        p2 = mozliwe_odp
        for n in p2[:]:
            if n == odpowiedzi[i]:
                p2.remove(n)
        podpowiedz2 = random.choice(p2)
        print("Pozostawione odpowiedzi: ", odpowiedzi[i],"oraz", podpowiedz2)
        kola_ratunkowe1[1]="X"
    elif kolo_wybor == 3:
        print("Wybrałeś: ", kola_ratunkowe[2])
        print("Jaka odpowiedż jest prawidłowa według publiczności?")
        p2 = mozliwe_odp
        for n in p2[:]:
            if n == odpowiedzi[i]:
                p2.remove(n)
        p3 = [odpowiedzi[i],p2[0],p2[1],p2[2]]
        if licznik <= 5:
            podpowiedz = random.choices(p3,odp_wagi1)
        elif licznik > 5 and licznik <= 9:
            podpowiedz = random.choices(p3,odp_wagi2)
        elif licznik > 9 and licznik <= 12:
            podpowiedz = random.choices(p3,odp_wagi3)
        print("Publiczność zadecydowała! Według nich odpowiedzią będzie:  ", podpowiedz)
        kola_ratunkowe1[2]="X"
else:
    print("No to jesteś zdany na samego siebie")
