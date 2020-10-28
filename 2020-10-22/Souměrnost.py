import sys
def svisla_soumernost(matice):
    rozmer = len(matice)
    for radek in range(rozmer):
        for sloupec in range(rozmer // 2):
            if matice[radek][sloupec] != matice[radek][-1 -sloupec]:
                return False
    return True
def test_svisla_soumernost():
    assert svisla_soumernost(([1, 1], [2, 2])) == True
    assert svisla_soumernost(([1, 4], [5, 8])) == False

def vodorovna_soumernost(matice):
    rozmer = len(matice)
    for radek in range(rozmer // 2):
        for sloupec in range(rozmer):
            if matice[radek][sloupec] !=  matice[-1 - radek][sloupec]:
                return False
    return True
def test_vodorovna_soumernost():
    assert vodorovna_soumernost(([1, 2], [1, 2])) == True
    assert vodorovna_soumernost(([1, 4], [5, 8])) == False

def hlavni_soumernost(matice):
    rozmer = len(matice)
    for radek in range(rozmer):
        for sloupec in range(rozmer):
            if matice[radek][sloupec] != matice[sloupec][radek]:
                return False
    return True
def test_hlavni_soumernost():
    assert hlavni_soumernost(([1, 2], [2, 1])) == True
    assert hlavni_soumernost(([1, 4], [5, 8])) == False

def vedlejsi_soumernost(matice):
    rozmer = len(matice)
    for radek in range(rozmer):
        for sloupec in range(rozmer):
            if matice[radek][sloupec] != matice[-1 -sloupec][-1 -radek]:
                return False
    return True
def test_vedlejsi_soumernost():
    assert vedlejsi_soumernost(([1, 2], [2, 1])) == True
    assert vedlejsi_soumernost(([1, 4], [5, 8])) == False

def main():
    matice = []
    for radek in sys.stdin():
        matice.append(radek.split())

    ano = "ANO"
    ne = "NE"
    if svisla_soumernost(matice):
        print("svislá osa:", ano)
    else:
        print("svislá osa:", ne)
    if vodorovna_soumernost(matice):
        print("vodorovná osa:", ano)
    else:
        print("vodorovná osa:", ne)
    if hlavni_soumernost(matice):
        print("hlavní úhlopříčka:", ano)
    else:
        print("hlavní úhlopříčka:", ne)
    if vedlejsi_soumernost(matice):
        print("vedlejší úhlopříčka:", ano)
    else:
        print("vedlejší úhlopříčka:", ne)

test_hlavni_soumernost()
test_vedlejsi_soumernost()
test_svisla_soumernost()
test_vodorovna_soumernost()