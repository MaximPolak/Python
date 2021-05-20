def klouzavy_prumer(prvky, delka):
    zacatek = 0
    k = delka
    while k - 1 < len(prvky):
        yield sum(prvky[zacatek:k]) / delka
        zacatek += 1
        k += 1

for i in klouzavy_prumer([1, 2, 3, 4, 5, 6], 2):
    print(i)