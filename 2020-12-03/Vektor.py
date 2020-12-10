class Vektor:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):
        return f"Vektor(x={self.x!r}, y={self.y!r})"
    def __add__(self, druhy_vektor): 
        return Vektor(self.x + druhy_vektor.x, self.y + druhy_vektor.y)
    def __mul__(self, cislo):
        return Vektor(self.x * cislo, self.y * cislo)
    def __rmul__(self, cislo):
        return self.__mul__(cislo) #self * cislo
    def __div__(self, cislo):
        return Vektor(self.x / cislo, self.y / cislo)
    def __sub__(self, druhy_vektor):
        return self + (-1 *druhy_vektor)

sipka = Vektor(5, 0)
sipka2 = Vektor(0, 5)

SEZNAM_SMERU = (Vektor(0, 1), Vektor(1, 0), Vektor(0, -1), Vektor(-1, 0))
class Objekt:
    def __init__(self, souradnice, smer_i, rychlost):
        self.souradnice, self.smer_i, self.rychlost = souradnice, smer_i, rychlost
    def __repr__(self):
        return f"Objekt(souradnice={self.souradnice!r}, smer_i={self.smer_i!r}, rychlost={self.rychlost!r})"
    def pohni_se(self):
        self.souradnice += self.rychlost * SEZNAM_SMERU[self.smer_i]
    def otoc_se_doprava(self):
        self.smer_i = (self.smer_i + 1) % 4
    def otoc_se_doleva(self):
        self.smer_i = (self.smer_i - 1) % 4
    def obrat_se(self):
        self.smer_i = (self.smer_i - 2) % 4