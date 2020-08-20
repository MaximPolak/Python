def test_je_minimalni_par():
    assert je_minimalni_par('lety', 'ledy')
    assert not je_minimalni_par('led', 'ledy')

def test_najdi_lisici_se_znaky():
    assert najdi_lisici_se_znaky("let", "led") == ("t", "d")
    assert najdi_lisici_se_znaky("let", "lety") == None

def je_minimalni_par(slovo1, slovo2):
    if len(slovo1) == len(slovo2):
        delka = len(slovo1)
        zmeny = 0
        for (znak1, znak2) in zip(slovo1, slovo2):
            if znak1 != znak2:
                
                zmeny += 1
                if zmeny == 2:
                    return False
        if zmeny == 1:
            return True
    return False         

def najdi_lisici_se_znaky(slovo1, slovo2):
    if len(slovo1) == len(slovo2):
        delka = len(slovo1)
        zmeny = 0
        for (znak1, znak2) in zip(slovo1, slovo2):
            if znak1 != znak2:
                zmeny += 1
                lisici_se_znaky = (znak1, znak2)
                if zmeny == 2:
                    return None
        if zmeny == 1:
            return lisici_se_znaky
    return None                               

test_je_minimalni_par()
test_najdi_lisici_se_znaky()