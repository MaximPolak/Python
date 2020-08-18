cislo = int(input("Zadejte číslo, které chcete rozložit na prvočinitele: "))

def rozloz_na_prvocinitele(cislo):
    seznam_prvocinitelu = []
    for prvocinitel in range(1, cislo + 1):
        if cislo % prvocinitel == 0:
            seznam_prvocinitelu.append(prvocinitel)
    return seznam_prvocinitelu

seznam = rozloz_na_prvocinitele(cislo)

for prvek in seznam:
    print(prvek)