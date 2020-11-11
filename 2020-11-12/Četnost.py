from collections import Counter
import sys
#neudělal jsem jednotlivé skripty, ale funkce, aby se vše vešlo do jednoho souboru

def cetnost_slov():
    vstup = input()
    for (klic, hodnota) in Counter(vstup.split()).items():
        print(klic, hodnota)

def cetnost_slov_tezsi():
    vstup = input()
    {print(i, y) for i, y in Counter(vstup.split()).most_common() if y != 1}