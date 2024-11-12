while True:
    kysymys=input("haluutko rekisteröityä(y) vai onko sinulla jo käyttäjä(n)? \n [y/n]:")
    if kysymys=="n":
        tunnus=input("millä nimellä haluat että me kutsumme sinua?\n")
        break
#kysytään tunnus
    if kysymys=="y":
        tunnus=input("rekisteröi käyttäjä. anna käyttäjätunnuksesi, väh. 3 merkkiä, ei saa olla isoa kirjainta tai numeroa.\n")
        NUMTUNNUS=False
        ISOTUNNUS=False
        for tarkistaja in tunnus:
            if tarkistaja.isupper():
                ISOTUNNUS=True
            if tarkistaja.isdigit():
                NUMTUNNUS=True
        if len(tunnus)>=3 and not ISOTUNNUS and not NUMTUNNUS:
            print("käyttäjätunnus hyväksyttiin.")
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
            print("salasana hyväksyttiin!")
            print("kiitos rekisteröitymisestä!")
            break
        elif len(salasana)<8:
            print("salasana on alle 8 merkkiä")
        elif not NUMSALASANA:
            print("salasanassa ei ole numeora")
        elif not ISOSALASANA:
            print("salasanassa ei ole isoja kirjaimia")
    else:
        print("tunnustasi ei voitu hyväksyä")
#haluaako asiakas kirjautua vai mennä ilman kirjautumatta
while True:
    kysymys2=input("haluatko kirjautua \n[y/n]:")
    if kysymys2=="n":
        break
#kysytään tunnus ja salasana
    if kysymys2=="y":
        frtunnus=input("kirjoita käyttäjätunnuksesi\n")
        if frtunnus == tunnus:
            print("valitse salasana")
            frsalasana=input("syötä salasana\n")
            if frsalasana == salasana:
                print("tervetuloa")
                break
        elif frtunnus != tunnus:
            print("väärä käyttäjätunnus")
        elif frsalasana!=salasana:
            print("väärä salasana")
while True:
    print("tervetuloa sisään", tunnus,"! \n:)\npaina ENTER jatkaaksesi.\n")
    input("")
    break
while True:
#asiakas on kirjautunut tai mennyt vierailijana ja nyt kysytään halutaanko laskinta tai celsiuksesta fahrenheitteihin laskuria.
    print("mitä haluaisit tehdä?")
    kysymys3=input("laskin(L) / Celsiuksesta Fahrenheitteihin laskin(cf).\n[L/CF]:")
    if kysymys3 == "L":
        num1=float(input("anna ensimmäinen numero"))
        num2=float(input("anna toinen numero"))
        laskutapa=input("anna laskutapa\n [+|-|/|*]: ")
        if laskutapa == "+":
            print(num1+num2)
        if laskutapa=="-":
            print(num1-num2)
        if laskutapa=="/":
            if num1 =="0" or num2 ==0:
                print("et voi jakaa nollalla mitään!")
            else:
                print(num1/num2)
        if laskutapa=="*":
            print(num1*num2)
    if kysymys3=="CF":
        num11=float(input("anna celsius asteessa oleva numero"))
        print(9/5 * num11 + 32)
        input("paina ENTER kun haluat jatkaa.")
