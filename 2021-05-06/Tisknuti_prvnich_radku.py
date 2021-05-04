import sys

class Queue:
    def __init__(self, kapacita, iterovatelny_objekt=()):
        self.kapacita = kapacita
        self._zacatek = 0
        self._delka = 0
        self._queue = [None for _ in range(kapacita)] 
        for objekt in iterovatelny_objekt:
            self.enqueue(objekt)
    def enqueue(self, prvek):
        self._queue[(self._zacatek + self._delka) % self.kapacita] = prvek
        if self.is_full():
            self._zacatek = (self._zacatek + 1) % self.kapacita
        else:
            self._delka += 1
    def dequeue(self):
        if self._delka == 0:
            raise IndexError 
        prvni_prvek = self._queue[self._zacatek]
        self._queue[self._zacatek] = None
        self._zacatek = (self._zacatek + 1) % self.kapacita
        self._delka -= 1
        return prvni_prvek
    def is_full(self):
        return self._delka == self.kapacita 
    def __len__(self):
        return self._delka
    def __getitem__(self, index):
        if index not in range(-self._delka, self._delka):
            raise IndexError
        if index < 0:
            index = self._delka + index
        return self._queue[(index + self._zacatek) % self.kapacita]
    def __iter__(self):
        return (self._queue[i % self.kapacita] for i in range(self._zacatek, self._zacatek + self._delka))
    def __reversed__(self):
        return (self._queue[i % self.kapacita] for i in range(self._zacatek + self._delka - 1, self._zacatek - 1, -1))


try:
    pocet_radku = int(sys.argv[1])
except IndexError:
    pocet_radku = 10

f = Queue(pocet_radku)

for radek in sys.stdin:
    if not f.is_full():
        f.enqueue(radek)
for i in f:
    print(i, end="")