def binarne_vyhledej(prvek, seznam, zacatek, konec):
    stred = (zacatek + konec) // 2
    
    if zacatek > konec:
        raise IndexError("Prvek není v daném seznamu")
    elif prvek == seznam[stred]:
        return stred
    elif prvek < seznam[stred]:
        return binarne_vyhledej(prvek, seznam, zacatek, stred - 1)
    else:
        return binarne_vyhledej(prvek, seznam, stred + 1, konec)