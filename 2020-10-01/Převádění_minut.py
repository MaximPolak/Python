def pocitani_minut(vstup):
    (dny, cas) = divmod(vstup, 60*24)
    (hodiny, minuty) = divmod(cas, 60)
    return (dny, hodiny, minuty)

def prevadeni_vstupu(vstup):
    if isinstance(vstup, str) == True:
        rozdeleny_vstup = vstup.split()
        for prvek in rozdeleny_vstup:
            if prvek.isdigit() == True:
                (dny, hodiny, minuty) = pocitani_minut(int(prvek))
                print(f"{prvek} min = {dny} d {hodiny} h {minuty} min")
            else:
                print(f"CHYBA: '{prvek}' není nezáporné celé číslo")
    elif isinstance(vstup, int) == True:
        (dny, hodiny, minuty) = pocitani_minut(vstup)
        print(f"{vstup} min = {dny} d {hodiny} h {minuty} min")
    else:
        print(f"CHYBA: '{vstup}' není nezáporné celé číslo")

prevadeni_vstupu("0 vznášedlo 62 5 46800")