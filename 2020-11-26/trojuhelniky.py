from body import Bod
from math import sqrt
import sys

def je_trojuhlenik(bod1, bod2, bod3):
    a = bod2.vzdalenost(bod3)
    b = bod3.vzdalenost(bod1)
    c = bod1.vzdalenost(bod2)
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True

vysledky = []

for radek in sys.stdin:
    body = radek.split(", ")

    souradnice1x = int(body[0][0])
    souradnice1y = int(body[0][2])
    souradnice2x = int(body[1][0])
    souradnice2y = int(body[1][2])
    souradnice3x = int(body[2][0])
    souradnice3y = int(body[2][2])

    bod1 = Bod(souradnice1x, souradnice1y)
    bod2 = Bod(souradnice2x, souradnice2y)
    bod3 = Bod(souradnice3x, souradnice3y)
    
    if je_trojuhlenik(bod1, bod2, bod3):
        vysledky.append("ANO")
    else:
        vysledky.append("NE")

for vysledek in vysledky:
    print(vysledek)