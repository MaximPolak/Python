class ZvlastniError(Exception):
    pass

class Piskvorky:
    def __init__(self, vyska, sirka, delka_vitezne_rady):
        self.vyska = vyska
        self.sirka = sirka
        self.delka = delka_vitezne_rady
        self.hraci_plocha = [[" " for _ in range(self.sirka)] for _ in range(self.vyska)]
        self.smery = ((0, 1), (1, 0), (1, 1), (1, -1))
    def indexy(self):
        for radek in range(self.vyska):
            for sloupec in range(self.sirka):
                yield (radek, sloupec)
        #return ((radek, sloupec) for radek in range(vyska) for sloupec in range(sirka))
    def zjisti_index_moznych_vyher(self):
        for radek, sloupec in self.indexy(): # radek, sloupec
            for smer in self.smery:
                ntice_indexu = tuple((radek + smer[0] * k, sloupec + smer[1] * k) for k in range(self.delka))
                if ntice_indexu[-1] in self.indexy():
                    yield ntice_indexu

               #if all(ntice in self.indexy() for ntice in ntice_indexu):     !neúsporné
                   #yield ntice_indexu
    def zjisti_vyhru(self):
        for indexy_vyhry in self.zjisti_index_moznych_vyher():
            ntice = tuple(self.hraci_plocha[radek][sloupec] for radek, sloupec in indexy_vyhry)

            
            if ntice[0] != " " and all(i == ntice[0] for i in ntice):
                return ntice[0]
        return " "
        
            #if ntice[0] != " " and ntice.count(ntice[0]) == len(ntice):
                #return ntice[0]

    def vepis_do_pole(self, index_pole, znak):
        if self.hraci_plocha[index_pole[0]][index_pole[1]] != " ":
            raise ZvlastniError
        self.hraci_plocha[index_pole[0]][index_pole[1]] = znak

    def vrat_indexy_volnych_poli(self):
        indexy_volnych_poli = []
        for radek, sloupec in self.indexy():
            if self.hraci_plocha[radek][sloupec] == " ":
                indexy_volnych_poli.append((radek, sloupec))
        return indexy_volnych_poli

"""
1 2 3           1: 2,3 ; 4,7 ; 5,9
4 5 6           2: 5,8
7 8 9       d   3: 6,9 ; 5,7
if sloupec + delka < sirka
if radek + delka < vyska
if 0 <= sloupec - delka < sirka
if oboje

i

r, s; r, s + 1; r, s + 2 --> (0, 1)
r, s; r + 1, s; r + 2, s --> (1, 0)
r, s; r + 1, s + 1; r + 2, s + 2 --> (1, 1)
r, s; r + 1, s - 1; r + 2, s - 2 --> (1, -1)

(r, s), (r + a, s + b), (r + 2a, s + 2b)
(r + ka, s + kb)
"""