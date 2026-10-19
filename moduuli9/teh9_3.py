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


travel = float(input("speed? "))
distance = float(input("distance? "))
hours = float(input("hours? "))
car = Auto("ABC_123", 142)
car.kiihdyta(travel)
car.kulje(hours)
print(f"Auto {car.rekisteri} matkusta {distance} km nopeus {travel} km/h {hours}, etäisyys on {car.matka} km ")