import random, sys

slova = []

with open("2020-12-17_frekvence.txt", 'r', encoding="utf-8") as soubor:
    for radek in soubor:
        slovo = radek.split()[0]
        if radek.islower() and 3 < len(slovo) < 10:
            slova.append(slovo)

casti = [slova[i:i + 10] for i in range(0, len(slova), 10)]

try: 
    with open(sys.argv[1], "w") as novy_soubor:
        for slovo in random.choice(casti):
            novy_soubor.write(slovo + "\n")            
except IndexError:
    for slovo in random.choice(casti):
        print(slovo)
