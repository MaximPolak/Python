import sys
from collections import deque

def generator(iterovatelny_objekt, k):
    fronta = deque(iterovatelny_objekt)

    while True:
        for _ in range(k - 1):
            fronta.append(fronta.popleft())

        yield fronta.popleft()

        if len(fronta) == 0:
            break

if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
        k = int(sys.argv[2])

        for cislo in generator(range(1, n + 1), k):
            print(cislo)
    except Exception:
        pass

  