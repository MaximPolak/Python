from collections import deque


def generator():
    fronta = deque()
    fronta.append("1")

    while True:
        prvni_prvek = fronta.popleft()
        yield prvni_prvek
        for i in range(2):
            fronta.append(f"{prvni_prvek}{i}")

for _, i in zip(range(10), generator()):
    print(i)

"""
1          1
2         10
3         11
4        100
5        101
6        110
7        111
8       1000
9       1001
10      1010
"""