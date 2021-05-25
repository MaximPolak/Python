import sys
from collections import deque

def cyklicka_obsluha(*iterovatelne_objekty):
    iteratory = [iter(i) for i in iterovatelne_objekty]
    iteratory_k_odebrani = []
       
    while True:
        for i, iterator in enumerate(iteratory):
            try:
                yield next(iterator)
                iteratory_k_odebrani.clear()

            except Exception:
                iteratory_k_odebrani.append(i)

        for i in iteratory_k_odebrani:
            try:
                iteratory.remove(i)
            except ValueError: # nevěděl jsem, jak jinak vyřešit problém se standardním vstupem
                break

        if not iteratory:
            break
        