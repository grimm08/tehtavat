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


cars = []
for i in range(1, 11):
    cars.append(Auto("ABC-" + str(i), random.randint(100, 200)))

    gig = True
while gig:
    for car in cars:
        car.kiihdyta(random.randint(-10, 15))
        car.kulje(1)
        if car.matka >= 10000:
            gig = False

for car in cars:
    print(f"Auto {car.rekisteri:<6}: huippunopeus = {car.huippunopeus}, nopeus = {car.nopeus} ja matka = {car.matka}")