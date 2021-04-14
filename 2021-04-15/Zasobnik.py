import sys

class StackUnderflowError(Exception):
    pass

class Stack:
    def __init__(self):
        self._posloupnost = []
    def push(self, hodnota):
        self._posloupnost.append(hodnota)
    def pop(self):
        if self.is_empty():
            raise StackUnderflowError
        return self._posloupnost.pop()
    def peek(self):
        if self.is_empty():
            raise StackUnderflowError 
        return self._posloupnost[-1]
    def is_empty(self) -> bool:
        return self._posloupnost == []

zasobnik = Stack()
for radek in sys.stdin:
    zasobnik.push(radek)
while True:
    try:
        print(zasobnik.peek(), end="")
        zasobnik.pop()
    except StackUnderflowError:
        break
