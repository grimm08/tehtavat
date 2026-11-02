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

class Ev_car(Auto):
    def __init__(self, rekisteri, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteri, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Feul_car(Auto):
    def __init__(self, rekisteri, huippunopeus, tank):
        super().__init__(rekisteri, huippunopeus)
        self.tank = tank


ev_car = Ev_car("ABC-15", 180, 52.5)
feuled = Feul_car("ACD-123", 165, 32.3)
ev_car.kiihdyta(120)
feuled.kiihdyta(100)

ev_car.kulje(3)
feuled.kulje(3)

print(f"Sähköauto {ev_car.rekisteri}: matkamittari {ev_car.matka} km")
print(f"Polttomoottoriauto {feuled.rekisteri}: matkamittari {feuled.matka} km")