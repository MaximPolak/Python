def prevadeni_minut(vstup):
    if type(vstup) == str:
        rozdeleny_vstup = vstup.split()
        for prvek in rozdeleny_vstup:
            try:
                cas = int(prvek)
                dny = cas // (60 * 24)
                cas %= 60 * 24
                hodiny = cas // 60
                cas %= 60
                minuty = cas
                print(f"{prvek} min = {dny} d {hodiny} h {minuty} min")
            except ValueError:
                print(f"CHYBA: {prvek} není nezáporné celé číslo")
    elif type(vstup) == int:
            cas = vstup
            dny = cas // (60 * 24)
            cas %= 60 * 24
            hodiny = cas // 60
            cas %= 60
            minuty = cas
            print(f"{vstup} min = {dny} d {hodiny} h {minuty} min")
    else:
        print(f"CHYBA: {vstup} není nezáporné celé číslo")

prevadeni_minut(input("Zadejte vstup:  "))