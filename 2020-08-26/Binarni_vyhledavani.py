def binarne_vyhledej(prvek, seznam):
    zacatek = 0
    konec = len(seznam) - 1

    while zacatek <= konec:
        pozice = (zacatek + konec) // 2
        if seznam[pozice] == prvek:
            return pozice
        elif prvek < seznam[pozice]:
            konec = pozice - 1
        else:
            zacatek = pozice + 1
    return -1

def test_binarne_vyhledej():
    seznam = [0,1,1,1,5]
    assert binarne_vyhledej(0, seznam) == 0
    assert binarne_vyhledej(2, seznam) == -1

test_binarne_vyhledej()
