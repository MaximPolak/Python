import sys

def kontrola_zavorek(vyraz):
    zasobnik = []
    pozice_chyby = None
    odpovidajici_zavorky = dict(zip(")]}", "([{"))
    for pozice, i in enumerate(vyraz):
        if i not in "()[]{}":
            continue
        if i in "([{":
            if len(zasobnik) == 0:
                pozice_chyby = pozice
            zasobnik.append(i)
        elif len(zasobnik) == 0:
            pozice_chyby = pozice
            return (pozice_chyby, "CHYBA: Některé závorky nejsou otevřené.")
        elif odpovidajici_zavorky[i] != zasobnik.pop():
            pozice_chyby = pozice
            return (pozice_chyby, "CHYBA: Některé závorky si neodpovídají.")

    if len(zasobnik) == 0:
        return (None, "OK")
    else:
        return (pozice_chyby, "CHYBA: Některé závorky nejsou zavřené.")

for i in sys.stdin:
    hlasky = kontrola_zavorek(i)
    if hlasky[0] != None:
        seznam = [" " for i in range(hlasky[0])] + ["^"]
        print("".join(seznam))
    print(hlasky[1])
    