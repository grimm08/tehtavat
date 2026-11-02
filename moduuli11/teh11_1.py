class Julksisu:
    def __init__(self,name):
        self.name = name

    def tulosta_tiedot(self):
        print(f"nimi: {self.name}")


class Book(Julksisu):
    def __init__(self,name, auther, pages):
        super().__init__(name)
        self.auther = auther
        self.pages = pages
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"kirjoittaja: {self.auther}")
        print(f"Sivumäärä: {self.pages}")

class News(Julksisu):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"editor: {self.editor}")
julkaisut = []
julkaisut.append(News("Aku Ankka", "aki hyppä"))
julkaisut.append(Book("Hytti n:o 6", "Rosa Liksom", 200))

for j in julkaisut:
    j.tulosta_tiedot()