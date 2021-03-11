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

abeceda = string.ascii_uppercase

while True:
    udalost, hodnoty = okno.read()
    if udalost == sg.WIN_CLOSED:
        break
    
    posun = int(hodnoty["-POSUN-"])

    from_ = "-FROM-"
    to = "-TO-"    
    if udalost == "Dešifruj":
        from_, to = to, from_
        posun *= -1

    slovnik = posun_abecedu(abeceda, posun)
    text = hodnoty[from_].upper()
    vystup = "".join(slovnik.get(znak, znak) for znak in text)

    okno[to].update(vystup)

okno.close()
