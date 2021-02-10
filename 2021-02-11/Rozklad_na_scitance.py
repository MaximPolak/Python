def rozloz(cislo):
    if cislo == 0:
        yield []
    else:
        for zaklad in range(cislo, 0, -1):
            zbytek = cislo - zaklad
            for zpusob in rozloz(zbytek):
                yield [zaklad] + zpusob
                
if __name__ == "__main__":
    import sys
    try:
        cislo = int(sys.argv[1])

        for i in rozloz(cislo):
            print(i)
    except IndexError:
        print("Přidejte argument")