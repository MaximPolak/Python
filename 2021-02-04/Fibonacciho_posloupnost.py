def generator_fibonacciho_clenu(cislo):
    soucasne = 0
    nasledujici = 1

    for _ in range(cislo):
        yield soucasne
        soucasne, nasledujici = (nasledujici, soucasne + nasledujici)

def generator_cisel(start=0, stop=None, step=1):
    if stop == None:
        while True:
            yield start
            start += step
    else:
        while start <= stop:
            yield start
            start += step

for i in generator_cisel(start=0, stop=-1):
    print(i)