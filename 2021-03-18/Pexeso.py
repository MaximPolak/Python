from random import sample
import os
import PySimpleGUI as sg

class Pexeso:
    def __init__(self, zadni_strana, predni_strany):
        self.predni_strany = sample(predni_strany * 2, len(predni_strany) * 2)
        self.zadni_strana = zadni_strana
        self.otocene = [False for _ in self.predni_strany] #[False] * len(self.predni_strany)
    
    def otoc(self, index):
        if self.otocene[index] == True:
            self.otocene[index] = False
        else:
            self.otocene[index] = True

    @property
    def viditelne(self):
        return [
            predni_strana if otoceno else self.zadni_strana
            for otoceno, predni_strana in zip(self.otocene, self.predni_strany)
            ]

def nejblizsi_cinitele(cislo): 
    prvni_cinitel = 1
    druhy_cinitel = cislo 
    for i in range(1, (cislo // 2) + 1):
        if prvni_cinitel >= druhy_cinitel:
            break
        if cislo % i == 0:
            prvni_cinitel = i
            druhy_cinitel = cislo // prvni_cinitel
    return (druhy_cinitel, prvni_cinitel)

nazvy_obrazku = os.listdir("Obrazky")[:-1]
cesty = [os.path.join("Obrazky", nazev) for nazev in nazvy_obrazku]
pexeso = Pexeso(os.path.join("Obrazky", os.listdir("Obrazky")[-1]), cesty)

radky, sloupce = nejblizsi_cinitele(16)

layout = [
    [sg.Image(key=i+j*sloupce, filename=pexeso.zadni_strana, enable_events=True) for i in range(sloupce)]
    for j in range(radky)
    ]

window = sg.Window("Pexeso", layout)

while True:
    udalost, hodnoty = window.read()
    if udalost == sg.WIN_CLOSED:
        break
    if udalost:
        index = udalost
        pexeso.otoc(index)
    
    for i, karta in enumerate(pexeso.viditelne):
        window[i].update(filename=karta)
    