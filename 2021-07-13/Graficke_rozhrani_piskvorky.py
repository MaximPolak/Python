import sys, os.path, time, random
from tkinter.constants import DISABLED
import PySimpleGUI as sg

sys.path.insert(0, os.path.join("..", "2021-06-24"))
import Piskvorky

rozmer = 3
hra = Piskvorky.Piskvorky(3, 3, 3)

rozmisteni = [[sg.Button("", key=(radek, sloupec), size=(2, 1)) for sloupec in range(rozmer)] for radek in range(rozmer)]

okno = sg.Window("Piškvorky", rozmisteni)

KRIZEK, KOLECKO = ("x", "o")

while True:
    if hra.vrat_indexy_volnych_poli() == []:
        break

    udalost, hodnoty = okno.read()
    if udalost == sg.WINDOW_CLOSED:
        break

    hra.vepis_do_pole(udalost, KRIZEK)
    okno[udalost].update(KRIZEK, disabled=True)
    okno.refresh()

    vitezny_znak = hra.zjisti_vyhru()
    if vitezny_znak != " ":
        sg.Popup("Vyhrál", vitezny_znak)
        break

    time.sleep(2)
    okno[random.choice(hra.vrat_indexy_volnych_poli())].update(KOLECKO, disabled = True)

    vitezny_znak = hra.zjisti_vyhru()
    if vitezny_znak != " ":
        sg.Popup("Vyhrál", vitezny_znak)
        break

okno.close()    