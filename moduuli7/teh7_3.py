lentoasemat ={}

entry = input("haluatko:\n1. syöttää uuden lentoasema?\n2. hakea jo syötetyn lentoaseman tiedot?\n3. lopettaa?\nvalitse 1, 2 tai 3: ")
while entry != "3":
    if entry == "1":
        asema = input("Anna lentoaseman nimi? ")
        koodi = input("Anna lentoaseman ICAO ? ")

        if  asema in lentoasemat:
            print ("asema on olemassa")
        else:
            lentoasemat.update({koodi:asema})

    elif entry == "2":
        aseman_koodi = input("Anna lentoaseman ICAO? ")
        if aseman_koodi in lentoasemat:
            print (lentoasemat[aseman_koodi])
        else:
            print ("lentoasema ei ole olemassa")

    entry = input("haluatko:\n1. syöttää uuden lentoasema?\n2.hakea jo syötetyn lentoaseman tiedot?\n3. lopettaa?")

print ("näkämiin!")