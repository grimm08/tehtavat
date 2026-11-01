import random

class Auto:

    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0


    def kiihdyta(self, speed_change):
        new_speed = self.nopeus + speed_change
        if new_speed > self.huippunopeus:
            new_speed = self.huippunopeus

        elif new_speed < 0:
            new_speed = 0

        self.nopeus = new_speed


    def kulje(self, hours):
        distance = self.matka + (self.nopeus * hours)
        self.matka = distance


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje(1)
    def tulosta_tilanne(self):

        for auto in self.autot:
            print(f"Rekisteri {auto.rekisteri}, Huippunopeus {auto.huippunopeus} km/h, Nopeus {auto.nopeus} km/h, matka {auto.matka} km")

        print()
    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False

cars = []
for i in range(1, 11):
    cars.append(Auto("ABC-" + str(i), random.randint(100, 200)))

kilpailu = Kilpailu("Suuri romuralli", 8000, cars)

tunnit =0
print(f"{kilpailu.nimi} ({kilpailu.pituus} km)\n")


while True:
    kilpailu.tunti_kuluu()
    tunnit += 1

    if tunnit % 10 == 0:
        print(f"Tilanne {tunnit} tunnin jälkeen")
        kilpailu.tulosta_tilanne()

    if kilpailu.kilpailu_ohi():
        break

print(f"kilpailu päättyi {tunnit} tunnin jälkeen. Lopputilanne:")
kilpailu.tulosta_tilanne()