def prevadeni_minut(minutovy_vstup):
    cas = minutovy_vstup
    dny = cas // (60 * 24)
    cas %= 60 * 24
    hodiny = cas // 60
    cas %= 60
    minuty = cas
    print(f"{minutovy_vstup} min = {dny} d {hodiny} h {minuty} min")

prevadeni_minut(828181818)