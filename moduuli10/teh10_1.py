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

h = Hissi(1, 10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(h.alin)