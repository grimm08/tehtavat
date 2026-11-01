class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin= ylin
        self.kerros = alin


    def kerros_ylös(self):
        if self.kerros < self.ylin:
            self.kerros +=1
        print(f"Hissi on nyt {self.kerros} kerroksessa")

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -=1
        print(f"Hissi on nyt {self.kerros} kerroksessa")


    def siirry_kerrokseen(self, kohdekerros):
        if kohdekerros < self.alin or kohdekerros > self.ylin:
            print (f"kerrosta {kohdekerros} ei ole.")
            return
        while self.kerros  < kohdekerros:
            self.kerros_ylös()
        while self.kerros > kohdekerros:
            self.kerros_alas()

class Talo:
    def __init__(self, alin, ylin, talon_hissi):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []
        for i in  range(talon_hissi):
            self.hissit.append(Hissi(alin, ylin))
    def aja_hissiä(self, hissi_numero, kohdekerros):
        if hissi_numero < 1 or hissi_numero > len(self.hissit):
            print(f"Hissiä {hissi_numero} ei ole.")
            return
        print(f"Ajetaan hissiä {hissi_numero}:")
        self.hissit[hissi_numero-1].siirry_kerrokseen(kohdekerros)

talo = Talo(1, 10, 3)
talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 8)
talo.aja_hissiä(1, 1)