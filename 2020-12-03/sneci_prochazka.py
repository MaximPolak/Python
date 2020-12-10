from Vektor import Vektor, Objekt

snek = Objekt(souradnice=Vektor(2, 3), smer_i=0, rychlost=1)

#vytvoření mapy
mapa = []
for i in range(10):
    mapa.append([])
    for j in range(10):
        mapa[i].append(["."])

for i in range(4):
    for j in range(4):
        snek.pohni_se()
        mapa[snek.souradnice.y - 1][snek.souradnice.x - 1] = ['*']
    snek.otoc_se_doprava()

#tisknutí mapy
for radek in mapa[::-1]:
    print(radek)