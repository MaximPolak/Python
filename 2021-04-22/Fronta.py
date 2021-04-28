class Queue:
    def __init__(self, kapacita):
        self.kapacita = kapacita
        self._zacatek = 0
        self._delka = 0
        self._queue = [None for _ in range(kapacita)]
    def enqueue(self, prvek):
        self._queue[(self._zacatek + self._delka) % self.kapacita] = prvek
        if self.is_full():
            self._zacatek += 1
        else:
            self._delka += 1
    def dequeue(self):
        prvni_prvek = self._queue[self._zacatek]
        self._queue[self._zacatek] = None
        self._zacatek = (self._zacatek + 1) % self.kapacita
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
        return (self._queue[i % self.kapacita] for i in range(self._zacatek, self._delka))
    def __reversed__(self):
        prevraceny = [prvek for prvek in self.__iter__()]
        return (prvek for prvek in prevraceny[::-1])   