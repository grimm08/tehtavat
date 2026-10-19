class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

car = Auto("ABC-123",142)

print(f"Auto {car.rekisteri} huippunopeus: {car.huippunopeus} km/h \nja auton kilometria: {car.matka}"
      f" auton nopeus nyt: {car.nopeus}")
