import string
import PySimpleGUI as sg


def posun_abecedu(abeceda, posun):
    return {znak:abeceda[(pozice + posun) % len(abeceda)] for pozice, znak in enumerate(abeceda)}

sg.theme("LightGray1")
levy_sloupec = [
    [sg.Frame("Původní text", [[sg.Multiline(key="-FROM-")]])],
    [sg.Frame("Zašifrovaný text", [[sg.Multiline(key="-TO-")]])],
    [sg.Button("Zašifruj"), sg.Button("Dešifruj")]
]
pravy_sloupec = [
    [sg.Frame("Posun", [[sg.Slider(range=(25, 0), default_value=0, key="-POSUN-")]])]
]
rozmisteni = [
    [sg.Column(levy_sloupec), sg.Column(pravy_sloupec)]
]
okno = sg.Window("Caesarova šifra", rozmisteni)

slovnik = {}
vystup = ""
abeceda = string.ascii_uppercase

while True:
    udalost, hodnoty = okno.read()
    if udalost == sg.WIN_CLOSED:
        break
    
    posun = int(hodnoty["-POSUN-"])
    for pozice, pismeno in enumerate(abeceda):
        slovnik[pismeno] = abeceda[(pozice + posun) % len(abeceda)]

    if udalost == "Zašifruj":
        text = hodnoty["-FROM-"].upper()
        for prvek in text:
            vystup += slovnik.get(prvek, prvek)
        okno["-TO-"].update(vystup)
    if udalost == "Dešifruj":
        text = hodnoty["-TO-"].upper()
        for prvek in text:
            vystup += slovnik.get(prvek, prvek)
        okno["-FROM-"].update(vystup)
    vystup = ""

okno.close()
