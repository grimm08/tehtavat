class Car:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

auto = Car("ABC-123",142)

print(f"Auto {auto.rekisteri} huippunopeus: {auto.huippunopeus} km/h \nja auton kilometria: {auto.matka}"
      f" auton nopeus nyt: {auto.nopeus}")
