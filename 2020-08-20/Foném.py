def test_je_minimalni_par():
    assert je_minimalni_par('lety', 'ledy')
    assert not je_minimalni_par('led', 'ledy')


def je_minimalni_par(slovo1, slovo2):
    if len(slovo1) == len(slovo2):
        delka = len(slovo1)
        pozice = 0
        zmeny = 0
        for pozice in range(delka):
            if slovo1[pozice] != slovo2[pozice]:
                zmeny += 1
                if zmeny == 2:
                    return False
        if zmeny == 1:
            return True
        else:
            return False
    else:
        return False
                    

test_je_minimalni_par()