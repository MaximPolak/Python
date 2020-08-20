""" 
Máme číslo, zkusíme ho vydělit prvočíslem (nejnižším)
Pokud to jde: --> uložíme si prvočíslo a vydělíme (nahradíme původní číslo číslem vyděleným), opakujeme, dokud do jde
                pokud to už nejde, pokračujeme s "Pokud ne:"
Pokud ne: --> změníme prvočíslo (prvocislo + 1)
Řádek 3-5 opakujeme, dokud se nedostaneme na jedničku
"""
#28:2 -> 14:2 -> 7

cislo = int(input("Zadejte číslo, které chcete rozložit na prvočinitele: "))

def rozloz_na_prvocinitele(cislo):
    prvocislo = 2
    seznam_prvocinitelu = []
    
    while cislo > 1:
        if cislo % prvocislo == 0:

            seznam_prvocinitelu.append(prvocislo)
            cislo //= prvocislo
            
        else:
            prvocislo += 1
        
    return seznam_prvocinitelu     

assert rozloz_na_prvocinitele(28) == [2, 2, 7]
assert rozloz_na_prvocinitele(54) == [2, 3, 3, 3]

seznam = rozloz_na_prvocinitele(cislo)

for prvek in seznam:
    print(prvek)