season = ("talvi", "kevät", "kesä", "syksy")
x = int(input("Anna kuukausi numero(1-12): "))
if x == 1 or x == 2 or x == 12:
    print(season[0])
elif x == 3 or x == 4 or x == 5:
    print(season[1])
elif x == 6 or x == 7 or x == 8:
    print(season[2])
elif x == 9 or x == 10 or x == 11:
    print(season[3])