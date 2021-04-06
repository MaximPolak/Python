from random import sample
import os
import time
import enum
import PySimpleGUI as sg

class Stav(enum.Enum):
    HRA = 0
    VYHRA = 1
    PROHRA = 2

class Pexeso:
    def __init__(self, zadni_strana, predni_strany):
        self.predni_strany = sample(predni_strany * 2, len(predni_strany) * 2)
        self.zadni_strana = zadni_strana
        self.otocene = [False for _ in self.predni_strany] #[False] * len(self.predni_strany)
        self.otocene_predtim = [False for _ in self.predni_strany]
        self.otocene_v_tomto_kole = []
        self.stav_hry = Stav.HRA
        self.zbyvajici_tahy = len(self.predni_strany) // 2
    
    def otoc(self, index):
        self.otoc_spatne_karty()

        if self.otocene[index]:
            raise ValueError    
            
        self.otocene[index] = True #pro otaceni obou stran self.otocene[index] = not self.otocene[index]
        self.otocene_v_tomto_kole.append(index)
        
        if False not in self.otocene:
            self.stav_hry = Stav.VYHRA

    def otoc_spatne_karty(self):
        if len(self.otocene_v_tomto_kole) == 2:
            if self.predni_strany[self.otocene_v_tomto_kole[0]] != self.predni_strany[self.otocene_v_tomto_kole[1]]:
                self.otocene[self.otocene_v_tomto_kole[0]] = self.otocene[self.otocene_v_tomto_kole[1]] = False
                self.zbyvajici_tahy -= 1
                if self.zbyvajici_tahy == 0:
                    self.stav_hry = Stav.PROHRA
            self.otocene_v_tomto_kole.clear()

    def podat_se(self):
        if self.stav_hry == Stav.VYHRA:
            raise ValueError
        pexeso.stav_hry = Stav.PROHRA
        for pozice, _ in enumerate(pexeso.otocene):
            pexeso.otocene[pozice] = True
        
    def najdi_zmeny(self):

        zmeny = [
            (index, predni_strana) 
            for index, (otoceno, otoceno_predtim, predni_strana) in enumerate(zip(self.otocene, self.otocene_predtim, self.predni_strany))
            if otoceno != otoceno_predtim
        ] 
        self.otocene_predtim = self.otocene

        return zmeny

    @property
    def viditelne(self):
        return [
            predni_strana if otoceno else self.zadni_strana
            for otoceno, predni_strana in zip(self.otocene, self.predni_strany)
            ]

def nejblizsi_cinitele(cislo):
    for i in range(int(cislo ** (1/2)), 0, -1):
        if cislo % i == 0:
            prvni_cinitel = i
            druhy_cinitel = cislo // prvni_cinitel
            return (prvni_cinitel, druhy_cinitel)

"""
Pomalejší řešení!            
def nejblizsi_cinitele(cislo): 
    prvni_cinitel = 1
    druhy_cinitel = cislo 
    for i in range(1, (cislo // 2) + 1):
        if prvni_cinitel >= druhy_cinitel:
            break
        if cislo % i == 0:
            prvni_cinitel = i
            druhy_cinitel = cislo // prvni_cinitel
    return (druhy_cinitel, prvni_cinitel) if druhy_cinitel <= prvni_cinitel else (prvni_cinitel, druhy_cinitel)
"""

cesty = [os.path.join("Obrazky", nazev) for nazev in sorted(os.listdir("Obrazky"))]
pexeso = Pexeso(cesty[-1], cesty[:-1])

radky, sloupce = nejblizsi_cinitele(len(pexeso.predni_strany))

levy_sloupec = [
    [sg.Image(key=i+j*sloupce, filename=pexeso.zadni_strana, enable_events=True) for i in range(sloupce)]
    for j in range(radky)
    ]

levy_sloupec += [[sg.StatusBar("", key="-CHYBA-", size=(20, 1))]]
pravy_sloupec = [
        [sg.Button("Podat se", size=(10, 1))], 
        [sg.Button("Nová hra", size=(10, 1))],
        [sg.Text(f"Tahy: {len(cesty[:-1])}", key="-TAHY-", size=(10, 1))],
        [sg.Text("", key="-HLASKA-", size=(10, 1))]
    ]

layout = [
    [sg.Column(levy_sloupec), sg.Column(pravy_sloupec)]
]

window = sg.Window("Pexeso", layout)

hlasky = {Stav.HRA: "", Stav.VYHRA: "Vyhráli jste", Stav.PROHRA: "Prohráli jste"}

while True:
    udalost, hodnoty = window.read(timeout=1000)

    if pexeso.stav_hry == Stav.VYHRA:
        window["Podat se"].update(disabled=True)
        
    
    pexeso.otoc_spatne_karty()
    
    if udalost == sg.WIN_CLOSED:
        break
    
    if udalost:
        window["-CHYBA-"].update("")

    if udalost == "Nová hra":
        window["Podat se"].update(disabled=False)
        pexeso = Pexeso(cesty[-1], cesty[:-1])

    elif udalost == "Podat se":
        pexeso.podat_se()

    elif udalost != sg.TIMEOUT_KEY and pexeso.stav_hry == Stav.HRA:
        try:
            pexeso.otoc(udalost)
        except ValueError:
            window["-CHYBA-"].update("Karta je  již otočená")

    window["-HLASKA-"].update(hlasky[pexeso.stav_hry])
    window["-TAHY-"].update(f"Tahy: {pexeso.zbyvajici_tahy}")    

    for i, karta in pexeso.najdi_zmeny():
        window[i].update(filename=karta)
