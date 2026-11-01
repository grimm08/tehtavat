class Publication:
    def __init__(self,name):
        self.name = name

class Book(Publication):
    def __init__(self,auther, pages):
        self.auther = auther
        self.pages = pages


class Ndws(Publication):
    def __init__(self, polisher, pages):
        super().__init__(polisher)
        self.polisher = polisher
