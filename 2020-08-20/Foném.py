def test_je_minimalni_par():
    assert je_minimalni_par('lety', 'ledy')
    assert not je_minimalni_par('led', 'ledy')


def je_minimalni_par(slovo1, slovo2):
    if len(slovo1) == len(slovo2):
        delka = len(slovo1)
        pozice = 0
        zmeny = 0
        for (znak1, znak2) in zip(slovo1, slovo2):
            if znak1 != znak2:
                zmeny += 1
                if zmeny == 2:
                    return False
        if zmeny == 1:
            return True
    return False                    

test_je_minimalni_par()

