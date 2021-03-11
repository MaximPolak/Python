import string
import PySimpleGUI as sg


def posun_abecedu(abeceda, posun):
    return {znak:abeceda[(pozice + posun) % len(abeceda)] for pozice, znak in enumerate(abeceda)}

sg.theme("LightGray1")
levy_sloupec = [
    [sg.Frame("Původní text", [[sg.Multiline(key="-FROM-", enable_events=True)]])],
    [sg.Frame("Zašifrovaný text", [[sg.Multiline(key="-TO-", enable_events=True)]])]
]
pravy_sloupec = [
    [sg.Frame("Posun", [[sg.Slider(range=(25, 0), default_value=0, key="-POSUN-", enable_events=True)]])]
]
rozmisteni = [
    [sg.Column(levy_sloupec), sg.Column(pravy_sloupec)]
]
okno = sg.Window("Caesarova šifra", rozmisteni)

abeceda = string.ascii_uppercase

from_, to = "-FROM-", "-TO-"

while True:
    udalost, hodnoty = okno.read()
    if udalost == sg.WIN_CLOSED:
        break
    print(udalost, hodnoty)

    posun = int(hodnoty["-POSUN-"])

    if udalost != "-POSUN-":
        from_ = "-FROM-"
        to = "-TO-"    

    if udalost == "-TO-":
        from_, to = to, from_
        posun *= -1

    slovnik = posun_abecedu(abeceda, posun)
    text = hodnoty[from_].upper().rstrip()
    vystup = "".join(slovnik.get(znak, znak) for znak in text)

    okno[to].update(vystup)

okno.close()
