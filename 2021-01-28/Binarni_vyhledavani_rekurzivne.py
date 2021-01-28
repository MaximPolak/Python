def binarne_vyhledej(prvek, seznam):
    def vnitrni_funkce(prvek, seznam, zacatek, konec):
        stred = (zacatek + konec) // 2
        
        if zacatek > konec:
            raise ValueError("Prvek není v daném seznamu")
        elif prvek == seznam[stred]:
            return stred
        elif prvek < seznam[stred]:
            return vnitrni_funkce(zacatek, stred - 1)
        else:
            return vnitrni_funkce(stred + 1, konec)

    return vnitrni_funkce(prvek, seznam, 0, len(seznam) - 1)