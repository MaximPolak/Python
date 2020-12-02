from collections import namedtuple
Bod = namedtuple("Bod", ["x", "y"])
Kruh = namedtuple("Kruh", ["stred", "polomer"])

class Ctverec:
    def __init__(self, roh, delka):
        self.roh, self.delka = roh, delka
    def __repr__(self):
        return f"Ctverec(roh = {self.roh}, delka = {self.delka})"
    def obsah(self):
        return self.delka ** 2
    def je_bod_uvnitr(self, bod):
        if self.roh[0] < bod[0] and (self.roh[0] + self.delka > bod[0]):
            if self.roh[1] < bod[1] and (self.roh[1] + self.delka > bod[1]):
                return True
        return False
    def vepis_kruh(self):
        pulka_strany = self.delka / 2
        return Kruh(Bod(self.roh[0] + self.delka / 2, self.roh[1] + pulka_strany), pulka_strany)
    def opis_kruh(self):
        pulka_strany = self.delka / 2
        return Kruh(Bod(self.roh[0] + self.delka / 2, self.roh[1] + pulka_strany), pulka_strany * (2**(1/2)))