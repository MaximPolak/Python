cislo = int(input("Zadejte číslo, které chcete rozložit na prvočinitele: "))

for prvocinitel in range(1, cislo + 1):
    if cislo % prvocinitel == 0:
        print(prvocinitel)