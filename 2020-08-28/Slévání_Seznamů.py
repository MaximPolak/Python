def spoj(seznam1, seznam2):
    pozice_seznamu_1 = 0
    pozice_seznamu_2 = 0

    serazene_seznamy = []

    while pozice_seznamu_1 < len(seznam1) and pozice_seznamu_2 < len(seznam2):
        if seznam1[pozice_seznamu_1] < seznam2[pozice_seznamu_2]:
            serazene_seznamy.append(seznam1[pozice_seznamu_1])
            pozice_seznamu_1 += 1
        else:
            serazene_seznamy.append(seznam2[pozice_seznamu_2])
            pozice_seznamu_2 += 1
    
    serazene_seznamy = serazene_seznamy + seznam1[pozice_seznamu_1:] + seznam2[pozice_seznamu_2:]
    
    return serazene_seznamy

def test_spoj():
    assert spoj([1, 2, 4], [2, 6, 10]) == [1, 2, 2, 4, 6, 10]
    assert spoj([5, 6, 8, 8, 8, 10], [1, 4, 6, 7]) == [1, 4, 5, 6, 6, 7, 8, 8, 8, 10]

test_spoj()