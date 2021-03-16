import PySimpleGUI as sg 

rozmisteni = [
    [sg.Multiline(key="-CHAT-", size=(51, 20), autoscroll=True, disabled=True)],
    [sg.Input(key="-IN-"), sg.Button("Poslat")]
]

okno = sg.Window("Chat s Emilem", rozmisteni)

class NeaktivniRobotError(Exception):
    pass

class Robot:
    def __init__(self, jmeno, pocet_zprav):
        self.jmeno = jmeno
        self.cislo_aktualni_zpravy = 1
        self.pocet_zprav = pocet_zprav
        self.poslane_zpravy = []
        self.aktivita = True

    def odpovez(self, zprava):
        if self.cislo_aktualni_zpravy == 1:
            text = "no"
        elif self.cislo_aktualni_zpravy == self.pocet_zprav:
            text = "musím končit"
        elif self.cislo_aktualni_zpravy > self.pocet_zprav:
            self.aktivita = False
            raise NeaktivniRobotError
        elif zprava in self.poslane_zpravy:
            text = "nemusíš mi to říkat stokrát"
        elif zprava.isupper():
            text = "neřvi na mě"
        elif zprava[-1] == "?":
            text = "nvm"
        elif len(zprava) > 50:
            text = "aha"
        else:
            text = "hm"
        self.poslane_zpravy.append(zprava)
        self.cislo_aktualni_zpravy += 1
        return f"{self.jmeno}: {text}"

    @property
    def aktivni(self):
        return self.aktivita

robot = Robot("Emil", 10)

while True:
    udalost, hodnoty = okno.read()
    if udalost == sg.WIN_CLOSED:
        break

    if udalost == "Poslat" and hodnoty["-IN-"] != "":
        okno["-CHAT-"].print((hodnoty["-IN-"]), justification="r")
        try:
            okno["-CHAT-"].print(robot.odpovez(hodnoty["-IN-"]))
        except NeaktivniRobotError:
            pass
        okno["-IN-"].update("")

okno.close()
