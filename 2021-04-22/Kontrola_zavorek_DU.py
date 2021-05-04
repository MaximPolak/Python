import sys

def kontrola_zavorek(vyraz):
    zasobnik = []
    pozice_chyby = None
    nejhlubsi_leva = (0, "") # (úrověň_vnoření, typ_závorky)
    pozice_nejhlubsich_zavorek = [0, 0]
    odpovidajici_zavorky = dict(zip(")]}", "([{"))
    predchazejici_zavorky = dict(zip("([{", "[{("))
    for pozice, znak in enumerate(vyraz):
        if znak not in "()[]{}":
            continue
        if znak in "([{":
            if len(zasobnik) != 0 and predchazejici_zavorky[znak] != zasobnik[-1][0]:
                pozice_chyby = (pozice,)
                return (pozice_chyby, "CHYBA: Jdou po sobě špatné závorky") 
            zasobnik.append((znak, pozice))

            delka_zasobniku = len(zasobnik)
            if nejhlubsi_leva[0] < delka_zasobniku:
                nejhlubsi_leva = (delka_zasobniku, znak)
                pozice_nejhlubsich_zavorek[0] = pozice
                pamatovat_si_dalsi_zavrenou = True

        elif len(zasobnik) == 0:
            pozice_chyby = (pozice,)
            return (pozice_chyby, "CHYBA: Některé závorky nejsou otevřené.")
        else:
            posledni_zavorka, index = zasobnik.pop()

            if pamatovat_si_dalsi_zavrenou:
                pozice_nejhlubsich_zavorek[1] = pozice
                pamatovat_si_dalsi_zavrenou = False

            if odpovidajici_zavorky[znak] != posledni_zavorka:
                pozice_chyby = index, pozice
                return (pozice_chyby, "CHYBA: Některé závorky si neodpovídají.")
            
    if len(zasobnik) == 0:
        if nejhlubsi_leva[1] not in ("", "("):
            pozice_chyby = tuple(pozice_nejhlubsich_zavorek)
            return (pozice_chyby, "CHYBA: Nejhlubší závorky nejsou kulaté")
        return (None, "OK")
    else:
        pozice_chyby = tuple(i for _, i in zasobnik)
        return (pozice_chyby, "CHYBA: Některé závorky nejsou zavřené.")

for radek in sys.stdin:
    pozice, hlaska = kontrola_zavorek(radek)
    if hlaska != "OK":
        seznam = [" " if i not in pozice else "^" for i in range(len(radek))]
        print("".join(seznam))
    print(hlaska)
    