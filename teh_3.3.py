suku = input("Valitare suku (m: mies, n: nainen):\n")

if suku == 'n':
    hemo = float(input("Anna hemoglobiiniarvo:\n"))
    if 117 <= hemo <= 175:
        print ("normaali")
    elif hemo < 117:
        print("alhainen")
    elif hemo > 175:
        print("korkea")
    else:
        print ("virheellinen syöttö")
elif suku == 'm':
    hemo = float(input("Anna hemoglobiiniarvo:\n"))
    if 134<= hemo <= 195:
        print("normaali")
    elif hemo < 134:
        print("alhainen")
    elif hemo > 195:
        print("korkea")
    else:
        print("virheellinen syöttö")
else:
    print("virheellinen suku")