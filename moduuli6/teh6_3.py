from os import error


def muunttaja(g):
    l = g*3.785
    print(f"{g} gallona on {l:.3f} litraa")
    return


gal = float(input("Anna gallonoiden määrä (negatiivinen määrä lopettaa): "))
while gal >= 0:
    muunttaja(gal)
    gal = float(input("Anna gallonoiden määrä (negatiivinen määrä lopettaa): "))

print("kiitos käynnistä")

