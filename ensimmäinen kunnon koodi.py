from time import sleep

while True:
    kysymys=input("haluutko rekisteröityä(y) vai haluatko kirjautua vieraana(n)? \n [y/n]:")
    if kysymys=="n":
        tunnus1=input("millä nimellä haluat että me kutsumme sinua?\n")
        break
#kysytään tunnus
    if kysymys=="y":
        tunnus2=input("rekisteröi käyttäjä. anna käyttäjätunnuksesi, väh. 3 merkkiä, ei saa olla isoa kirjainta tai numeroa.\n")
        NUMTUNNUS=False
        ISOTUNNUS=False
        for tarkistaja in tunnus2:
            if tarkistaja.isupper():
                ISOTUNNUS=True
            if tarkistaja.isdigit():
                NUMTUNNUS=True
        if len(tunnus2)>=3 and not ISOTUNNUS and not NUMTUNNUS:
            sleep(1)
            print("käyttäjätunnus hyväksyttiin.")
        else:
            exit()
#kysytään salasana
        salasana=input("Luo salasanasi, vähintään 8 kirjainta, numero ja iso kirjain.\n")
        NUMSALASANA=False
        ISOSALASANA=False
        for tarkistaja2 in salasana:
            if tarkistaja2.isupper():
                ISOSALASANA=True
            if tarkistaja2.isdigit():
                NUMSALASANA=True
        if len(salasana)>=8 and NUMSALASANA is True and ISOSALASANA is True:
            sleep(0.5)
            print("salasana hyväksyttiin!")
            print("kiitos rekisteröitymisestä!")
            break
        elif len(salasana)<=8:
            sleep(1)
            print("salasana on alle 8 merkkiä")
        elif not NUMSALASANA:
            sleep(1)
            print("salasanassa ei ole numeroa")
        elif not ISOSALASANA:
            sleep(1)
            print("salasanassa ei ole isoja kirjaimia")
    else:
        sleep(3)
        print("tunnustasi ei voitu hyväksyä tai vastasit väärin kysymykseen")
#haluaako asiakas kirjautua vai mennä ilman kirjautumatta
while True:
    if kysymys == "y":  # If user registered
        kysymys2=input("haluatko kirjautua \n[y/n]:")
        if kysymys2=="n":

            break
        elif kysymys2=="y":
            frtunnus=input("kirjoita käyttäjätunnuksesi\n")
            if frtunnus == tunnus2:
                frsalasana=input("syötä salasana\n")
                if frsalasana == salasana:
                    print("tervetuloa")
                    break
                else:
                    print("väärä salasana")
            else:
                print("väärä käyttäjätunnus")
        else:
            print("väärä kirjain (koita pieniä kirjaimia)")
    else:
        break

#kysytään tunnus ja salasana

while True:
    if kysymys == "y" and kysymys2 == "y":
        print("tervetuloa sisään", tunnus2,"! \n:)\npaina ENTER jatkaaksesi.\n")
        input("")
        break
    elif kysymys == "n":
        print("tervetuloa sisään", tunnus1,"! \n:)\npaina ENTER jatkaaksesi.\n")
        input("")
        break
    elif kysymys == "y" and kysymys2 == "n":
        print("tervetuloa sisään", tunnus2,"! \n:)\npaina ENTER jatkaaksesi.\n")
        input("")
        break
    else:
        break
while True:
#asiakas on kirjautunut tai mennyt vierailijana ja nyt kysytään halutaanko laskinta tai celsiuksesta fahrenheitteihin laskuria.
    print("mitä haluaisit tehdä?")
    kysymys3=input("laskin(L) / Celsiuksesta Fahrenheitteihin laskin(cf).\n[L/CF]:")
    if kysymys3 == "L":
        num1=float(input("anna ensimmäinen numero\n"))
        num2=float(input("anna toinen numero\n"))
        laskutapa=input("anna laskutapa\n [+|-|/|*]\n: ")
        if laskutapa == "+":
            print(num1+num2)
        if laskutapa=="-":
            print(num1-num2)
        if laskutapa=="/":
            if num2 == 0:
                print("et voi jakaa nollalla mitään!")
            elif num1 == 0:
                print("et voi jakaa nollalla mitään!")
            else:
                print(num1/num2)
        if laskutapa=="*":
            print(num1*num2)
    if kysymys3=="CF":
        num11=float(input("anna celsius asteessa oleva numero\n"))
        print(9/5 * num11 + 32)
        input("paina ENTER kun haluat jatkaa.")
