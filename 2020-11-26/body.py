from math import sqrt
class Bod:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def vzdalenost(self, jiny_bod):
        vzdalenost_x = abs(self.x - jiny_bod.x)
        vzdalenost_y = abs(self.y - jiny_bod.y)
        uhlopricka = sqrt(vzdalenost_x ** 2 + vzdalenost_y ** 2)
        return uhlopricka

auto = Bod(15, 15)
auto.x
auto.y
autobus = Bod(200, 50)
if __name__ == "__main__":
    print(auto.vzdalenost(autobus))