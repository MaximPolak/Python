seznam = []
for i in range(1, 1001):
    seznam.append(i)
print(seznam)

suda_cisla = list(range(2, 1001, 2))

seznam2 = []
for i in range(1, 1001):
    if i % 3 == 0:
        seznam.append(i)
    elif i % 5 == 0:
        seznam.append(i)
    
