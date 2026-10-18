vuosi = int(input("Anna vuosiluku:\n"))
leap = vuosi % 4
vuosisadan = vuosi%100
vuosisadan_leap = vuosi%400
if leap == 0:
    if vuosisadan != 0:
        print (f"vuosi {vuosi} on karkausvuosi")
    else:
        if vuosisadan_leap == 0:
            print (f"vuosi {vuosi} on karkausvuosi")
        else:
            print (f"vuosi {vuosi} ei ole karkausvuotta")
else:
    print("vuosi ei ole karkausvuosi")