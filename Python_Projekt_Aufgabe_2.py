
spielfeld = [
    [" ","1","2","3","4","5"],
    ["4"," "," "," "," "," "],
    ["3"," "," "," "," "," "],
    ["2"," "," "," "," "," "],
    ["1"," "," "," "," "," "]
]


def spielfeld_anzeigen():
    for reihe in range(0,5):
        for spalte in range(0,6):
            print(spielfeld[reihe][spalte],end = "")
            print("|", end = "")
        print("")

spielfeld_anzeigen()

def spalten_platz_finden(spalte):
    for reihe in range(4,0,-1):
        if spielfeld[reihe][spalte] == " ":
            return reihe
    return False

def muenze_einwerfen(spalte,muenze):
    if spalte <1 or spalte >5:
        print("Ungültige Spalte!")
        return 0
    platz = spalten_platz_finden(spalte)
    if platz == False:
        print("Spalte voll! Wählen Sie bitte beim nächsten mal eine andere Spalte!")
    else:
        spielfeld[platz][spalte] = muenze


def gewonnen():
    if spielfeld[1][1] == spielfeld[1][2] and spielfeld[1][1] == spielfeld[1][3] and spielfeld[1][1] == spielfeld[1][4] and spielfeld[1][1] != " ":
        print("Spieler "+ spielfeld[1][1] + " hat GEWONNEN!" )
        return spielfeld[1][1]

    elif spielfeld[1][5] == spielfeld[1][4] and spielfeld[1][5] == spielfeld[1][3] and spielfeld[1][5] == spielfeld[1][2] and spielfeld[1][5] != " ":
        print("Spieler "+ spielfeld[1][5] + " hat GEWONNEN!" )
        return spielfeld[1][5]

    elif spielfeld[2][1] == spielfeld[2][2] and spielfeld[2][1] == spielfeld[2][3] and spielfeld[2][1] == spielfeld[2][4] and spielfeld[2][1] != " ":
        print("Spieler "+ spielfeld[2][1] + " hat GEWONNEN!" )
        return spielfeld[2][1]

    elif spielfeld[2][5] == spielfeld[2][4] and spielfeld[2][5] == spielfeld[2][3] and spielfeld[2][5] == spielfeld[2][2] and spielfeld[2][5] != " ":
        print("Spieler "+ spielfeld[2][5] + " hat GEWONNEN!" )
        return spielfeld[2][5]

    elif spielfeld[3][1] == spielfeld[3][2] and spielfeld[3][1] == spielfeld[3][3] and spielfeld[3][1] == spielfeld[3][4] and spielfeld[3][1] != " ":
        print("Spieler "+ spielfeld[3][1] + " hat GEWONNEN!" )
        return spielfeld[3][1]

    elif spielfeld[3][5] == spielfeld[3][4] and spielfeld[3][5] == spielfeld[3][3] and spielfeld[3][5] == spielfeld[3][2] and spielfeld[3][5] != " ":
        print("Spieler "+ spielfeld[3][5] + " hat GEWONNEN!" )
        return spielfeld[3][5]

    elif spielfeld[4][1] == spielfeld[4][2] and spielfeld[4][1] == spielfeld[4][3] and spielfeld[4][1] == spielfeld[4][4] and spielfeld[4][1] != " ":
        print("Spieler "+ spielfeld[4][1] + " hat GEWONNEN!" )
        return spielfeld[4][1]

    elif spielfeld[4][5] == spielfeld[4][4] and spielfeld[4][5] == spielfeld[4][3] and spielfeld[4][5] == spielfeld[4][2] and spielfeld[4][5] != " ":
        print("Spieler "+ spielfeld[4][5] + " hat GEWONNEN!" )
        return spielfeld[4][5]

    elif spielfeld[1][1] == spielfeld[2][1] and spielfeld[1][1] == spielfeld[3][1] and spielfeld[1][1] == spielfeld[4][1] and spielfeld[1][1] != " ":
        print("Spieler "+ spielfeld[1][1] + " hat GEWONNEN!" )
        return spielfeld[1][1]

    elif spielfeld[1][2] == spielfeld[2][2] and spielfeld[1][2] == spielfeld[3][2] and spielfeld[1][2] == spielfeld[4][2] and spielfeld[1][2] != " ":
        print("Spieler "+ spielfeld[1][2] + " hat GEWONNEN!" )
        return spielfeld[1][2]

    elif spielfeld[1][3] == spielfeld[2][3] and spielfeld[1][3] == spielfeld[3][3] and spielfeld[1][3] == spielfeld[4][3] and spielfeld[1][3] != " ":
        print("Spieler "+ spielfeld[1][3] + " hat GEWONNEN!" )
        return spielfeld[1][3]

    elif spielfeld[1][4] == spielfeld[2][4] and spielfeld[1][4] == spielfeld[3][4] and spielfeld[1][4] == spielfeld[4][4] and spielfeld[1][4] != " ":
        print("Spieler "+ spielfeld[1][4] + " hat GEWONNEN!" )
        return spielfeld[1][4]

    elif spielfeld[1][5] == spielfeld[2][5] and spielfeld[1][5] == spielfeld[3][5] and spielfeld[1][5] == spielfeld[4][5] and spielfeld[1][5] != " ":
        print("Spieler "+ spielfeld[1][5] + " hat GEWONNEN!" )
        return spielfeld[1][5]

    elif spielfeld[1][1] == spielfeld[2][2] and spielfeld[1][1] == spielfeld[3][3] and spielfeld[1][1] == spielfeld[4][4] and spielfeld[1][1] != " ":
        print("Spieler "+ spielfeld[1][1] + " hat GEWONNEN!" )
        return spielfeld[1][1]

    elif spielfeld[1][2] == spielfeld[2][3] and spielfeld[1][2] == spielfeld[3][4] and spielfeld[1][2] == spielfeld[4][5] and spielfeld[1][2] != " ":
        print("Spieler "+ spielfeld[1][2] + " hat GEWONNEN!" )
        return spielfeld[1][2]

    elif spielfeld[1][5] == spielfeld[2][4] and spielfeld[1][5] == spielfeld[3][3] and spielfeld[1][5] == spielfeld[4][2] and spielfeld[1][5] != " ":
        print("Spieler "+ spielfeld[1][5] + " hat GEWONNEN!" )
        return spielfeld[1][5]

    elif spielfeld[1][4] == spielfeld[2][3] and spielfeld[1][4] == spielfeld[3][2] and spielfeld[1][4] == spielfeld[4][1] and spielfeld[1][4] != " ":
        print("Spieler "+ spielfeld[1][4] + " hat GEWONNEN!" )
        return spielfeld[1][4]
    else:
        return False

def unentschieden():
    if  spielfeld[1][1] != " "  and spielfeld[1][2] != " "  and spielfeld[1][3] != " "  and spielfeld[1][4] != " "  and spielfeld[1][5] != " "  and spielfeld[2][1] != " "  and spielfeld[2][2] != " "  and spielfeld[2][3] != " "  and spielfeld[2][4] != " "  and spielfeld[2][5] != " "  and spielfeld[3][1] != " "  and spielfeld[3][2] != " "  and spielfeld[3][3] != " "  and spielfeld[3][4] != " "  and spielfeld[3][5] != " "  and spielfeld[4][1] != " "  and spielfeld[4][2] != " "  and spielfeld[4][3] != " "  and spielfeld[4][4] != " "  and spielfeld[4][5] != " " :
        print("Das Spiel endete Unentschieden.")
        return True

def spiel():
    spieler_1 = "x"
    spieler_2 = "o"
    print("Herzlich Willkommen beim Spiel: 4 Gewinnt!")
    print("Im Folgenden spielen Spieler 'x' und Spieler 'o' gegeneinander! Viel Glück!")
    print("Spieler 'x' beginnt.")
    aktiver_spieler = spieler_1
    while gewonnen() == False:
        eingabe = 0
        while eingabe < 1 or eingabe > 5:
            try:
                eingabe = int(input(aktiver_spieler + " : In welche Spalte willst du die Münze einwerfen? "))
            except:ValueError: print("Ungültige Eingabe")
            if eingabe < 1 or eingabe > 5:
                print("Ungültige Eingabe! Man kann sich nur zwischen der 1. und 5. Spalte entscheiden!")
                print("Mögliche Eingaben sind: 1 , 2 , 3 , 4 , 5")
                print("Versuchen Sie es erneut!")
        muenze_einwerfen(eingabe, aktiver_spieler)
        spielfeld_anzeigen()
        if aktiver_spieler == spieler_1:
            aktiver_spieler = spieler_2
        else:
            aktiver_spieler = spieler_1
        if unentschieden() == True:
            exit()


spiel()
