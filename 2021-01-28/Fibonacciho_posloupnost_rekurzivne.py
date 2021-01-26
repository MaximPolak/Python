def Fibonacciho_cislo(cislo):
    if cislo == 0:
        return 0
    elif cislo == 1:
        return 1
    else:
        return Fibonacciho_cislo(cislo - 1) + Fibonacciho_cislo(cislo - 2)