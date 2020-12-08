from Vektor import Vektor, Objekt

snek = Objekt([2, 3], 0, 1)

#vytvoření mapy
mapa = []
for i in range(10):
    mapa.append([])
    for j in range(10):
        mapa[i].append(["."])

for i in range(4):
    for j in range(4):
        snek.pohni_se()
        mapa[snek.souradnice[1] - 1][snek.souradnice[0] - 1] = ['*']
    snek.otoc_se_doprava()

#tisknutí mapy
for radek in mapa[::-1]:
    print(radek)