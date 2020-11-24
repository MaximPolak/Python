""" Tento skript čte slova ze standartního vstupu a na standartní výstup je vypisuje spolu s jejich četností a dalšími třemi nejčastějšími následujícími slovy také s jejich četností ve vstupu. """

from collections import defaultdict, Counter
import sys

vstup = sys.stdin.read().split()
slovnik = defaultdict(lambda: [0, Counter()])

for pozice, prvni_slovo in enumerate(vstup[:-1]):
    druhe_slovo = vstup[pozice + 1]

    slovnik[prvni_slovo][0] += 1
    slovnik[prvni_slovo][1][druhe_slovo] += 1

for prvni_slovo, seznam in slovnik.items():
    print(prvni_slovo, seznam[0])

    for druhe_slovo, cetnost in seznam[1].most_common(3):
        print("\t", druhe_slovo, cetnost)