class Osoba:
    def __init__(self, jmeno, prijmeni, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
    def predstaveni(self):
        print(f"Jmenuji se {self.jmeno} {self.prijmeni} a je mi {self.vek} let.")