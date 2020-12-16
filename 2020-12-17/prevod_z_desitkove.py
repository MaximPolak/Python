import sys

def preved_z_desitkove(cislo: int, soustava: int=2):
    """ Převede vstupní celé číslo z desítkové soustavy do jiné """

    if not isinstance(cislo, int):
        raise TypeError("Vstup musí být celé číslo")

    serazene_zbytky = []
    while cislo > 0:
        serazene_zbytky.insert(0, cislo % soustava)
        cislo = cislo // soustava

    vysledek = ""
    for cislice in serazene_zbytky:
        vysledek += str(cislice)
    
    return vysledek

if __name__ == "__main__":
    try:
        vstupni_cislo = int(sys.argv[1])
        vstupni_soustava = int(sys.argv[2])

        if vstupni_soustava < 2 or vstupni_soustava > 10:
            raise ValueError
        print(preved_z_desitkove(vstupni_cislo, vstupni_soustava))

    except (ValueError, IndexError):
        sys.stderr.write("Něco je špatně")
    finally:
        sys.stderr.write("\nPROGRAM SKONČIL")  
