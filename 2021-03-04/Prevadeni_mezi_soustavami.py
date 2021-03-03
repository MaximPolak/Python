import PySimpleGUI as sg

rozmisteni = [
    [sg.Text("10", size=(3, 1)), sg.Input(key="-DESITKOVY_VSTUP-", size=(12, 1)),
    sg.Button("10 -> 2", size=(8, 1))],
    [sg.Text("2", size=(3, 1)), sg.Input(key="-DVOJKOVY_VSTUP-", size=(12, 1)),
    sg.Button("2 -> 10", size=(8, 1))],
    [sg.StatusBar("zadejte číslo v desítkovém zápisu")]
]
okno =  sg.Window(title="10 <-> 2", layout=rozmisteni)

while True:
    udalost, hodnoty = okno.read()
    if udalost == sg.WIN_CLOSED:
        break

    vstup1 = hodnoty["-DESITKOVY_VSTUP-"]
    vstup2 = hodnoty["-DVOJKOVY_VSTUP-"]

    if udalost == "10 -> 2":
        if vstup1 != "":
            cislo_ve_dvojkove = str(bin(int(vstup1)))
            okno["-DVOJKOVY_VSTUP-"].update(cislo_ve_dvojkove[2:])
    elif udalost == "2 -> 10":
        if vstup2 != "":
            cislo_v_desitkove = str(int(vstup2, 2))
            okno["-DESITKOVY_VSTUP-"].update(cislo_v_desitkove)

okno.close()
