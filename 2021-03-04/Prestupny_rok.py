import PySimpleGUI as sg

def je_prestupny(rok):
    return rok % 400 == 0 or (rok % 4 == 0 and rok % 100 != 0)

rozmisteni = [
    [sg.Text("Zadejte rok"), sg.Input(), sg.Button("Vyhodnoť")],
    [sg.Text("", key="-VYSTUP-", size=(30, 1))]
]

okno = sg.Window("Přestupný rok", rozmisteni)

while True:
    udalost, hodnoty = okno.read()

    if udalost == sg.WIN_CLOSED:
        break
    if udalost == "Vyhodnoť":
        if not hodnoty[0] == "":
            try:
                okno["-VYSTUP-"].update(f"Rok {hodnoty[0]} {'je' if je_prestupny(int(hodnoty[0])) else 'není'} přestupný")
            except (TypeError, ValueError):
                okno["-VYSTUP-"].update("ZADEJTE ROK")

okno.close()
