class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0


    def kiihdyta(self, speed_change):
        new_speed = self.nopeus + speed_change
        if  new_speed > self.huippunopeus:
            new_speed = self.huippunopeus

        elif new_speed < 0:
            new_speed = 0

        self.nopeus = new_speed

car = Auto("ABC_123", 142)

car.kiihdyta(30)
car.kiihdyta(70)
car.kiihdyta(50)
print(f"Auto {car.rekisteri} uusi nopeus on {car.nopeus} km/h")

car.kiihdyta(-200)

print(f"Auto {car.rekisteri} uusi nopeus on {car.nopeus} km/h")