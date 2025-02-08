

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
        print("Spalte voll!")
    else:
        spielfeld[platz][spalte] = muenze


muenze_einwerfen(1, "x")
muenze_einwerfen(2,"o")
spielfeld_anzeigen()


#    1 2 3 4 5
# 4 | | | | | |
# 3 | | | | | |
# 2 | | | | | |
# 1 | |x|x|x|x|

#    1 2 3 4 5
# 4 | | | | | |
# 3 | | | | | |
# 2 | | | | | |
# 1 |x|x|x|x| |

#    1 2 3 4 5
# 4 |x|x|x|x| |
# 3 | | | | | |
# 2 | | | | | |
# 1 | | | | | |

#    1 2 3 4 5
# 4 | |x|x|x|x|
# 3 | | | | | |
# 2 | | | | | |
# 1 | | | | | |

#    1 2 3 4 5
# 4 | | | | | |
# 3 |x|x|x|x| |
# 2 | | | | | |
# 1 | | | | | |

#    1 2 3 4 5
# 4 | | | | | |
# 3 | |x|x|x|x|
# 2 | | | | | |
# 1 | | | | | |

#    1 2 3 4 5
# 4 | | | | | |
# 3 | | | | | |
# 2 |x|x|x|x| |
# 1 | | | | | |

#    1 2 3 4 5
# 4 | | | | | |
# 3 | | | | | |
# 2 | |x|x|x|x|
# 1 | | | | | |

#    1 2 3 4 5
# 4 |x| | | | |
# 3 |x| | | | |
# 2 |x| | | | |
# 1 |x| | | | |

#    1 2 3 4 5
# 4 | |x| | | |
# 3 | |x| | | |
# 2 | |x| | | |
# 1 | |x| | | |

#    1 2 3 4 5
# 4 | | |x| | |
# 3 | | |x| | |
# 2 | | |x| | |
# 1 | | |x| | |

#    1 2 3 4 5
# 4 | | | |x| |
# 3 | | | |x| |
# 2 | | | |x| |
# 1 | | | |x| |

#    1 2 3 4 5
# 4 | | | | |x|
# 3 | | | | |x|
# 2 | | | | |x|
# 1 | | | | |x|

#    1 2 3 4 5
# 4 |x| | | | |
# 3 | |x| | | |
# 2 | | |x| | |
# 1 | | | |x| |

#    1 2 3 4 5
# 4 | |x| | | |
# 3 | | |x| | |
# 2 | | | |x| |
# 1 | | | | |x|

#    1 2 3 4 5
# 4 | | | | |x|
# 3 | | | |x| |
# 2 | | |x| | |
# 1 | |x| | | |

#    1 2 3 4 5
# 4 | | | |x| |
# 3 | | |x| | |
# 2 | |x| | | |
# 1 |x| | | | |



def gewonnen():
    if spielfeld[1][1] == spielfeld[1][2] and spielfeld[1][1] == spielfeld[1][3] and spielfeld[1][1] == spielfeld[1][4] and spielfeld[1][1] != " ":
        print("Spieler "+ spielfeld[1][1] + " hat gewonnen!" )
        return spielfeld[1][1]
    
    elif spielfeld[1][5] == spielfeld[1][4] and spielfeld[1][5] == spielfeld[1][3] and spielfeld[1][5] == spielfeld[1][2] and spielfeld[1][5] != " ":
        print("Spieler "+ spielfeld[1][5] + " hat gewonnen!" )
        return spielfeld[1][5]

    elif spielfeld[2][1] == spielfeld[2][2] and spielfeld[2][1] == spielfeld[2][3] and spielfeld[2][1] == spielfeld[2][4] and spielfeld[2][1] != " ":
        print("Spieler "+ spielfeld[2][1] + " hat gewonnen!" )
        return spielfeld[2][1]

    elif spielfeld[2][5] == spielfeld[2][4] and spielfeld[2][5] == spielfeld[2][3] and spielfeld[2][5] == spielfeld[2][2] and spielfeld[2][5] != " ":
        print("Spieler "+ spielfeld[2][5] + " hat gewonnen!" )
        return spielfeld[2][5]

    elif spielfeld[3][1] == spielfeld[3][2] and spielfeld[3][1] == spielfeld[3][3] and spielfeld[3][1] == spielfeld[3][4] and spielfeld[3][1] != " ":
        print("Spieler "+ spielfeld[3][1] + " hat gewonnen!" )
        return spielfeld[3][1]

    elif spielfeld[3][5] == spielfeld[3][4] and spielfeld[3][5] == spielfeld[3][3] and spielfeld[3][5] == spielfeld[3][2] and spielfeld[3][5] != " ":
        print("Spieler "+ spielfeld[3][5] + " hat gewonnen!" )
        return spielfeld[3][5]

    elif spielfeld[4][1] == spielfeld[4][2] and spielfeld[4][1] == spielfeld[4][3] and spielfeld[4][1] == spielfeld[4][4] and spielfeld[4][1] != " ":
        print("Spieler "+ spielfeld[4][1] + " hat gewonnen!" )
        return spielfeld[4][1]

    elif spielfeld[4][5] == spielfeld[4][4] and spielfeld[4][5] == spielfeld[4][3] and spielfeld[4][5] == spielfeld[4][2] and spielfeld[4][5] != " ":
        print("Spieler "+ spielfeld[4][5] + " hat gewonnen!" )
        return spielfeld[4][5]

    elif spielfeld[1][1] == spielfeld[2][1] and spielfeld[1][1] == spielfeld[3][1] and spielfeld[1][1] == spielfeld[4][1] and spielfeld[1][1] != " ":
        print("Spieler "+ spielfeld[1][1] + " hat gewonnen!" )
        return spielfeld[1][1]

    elif spielfeld[1][2] == spielfeld[2][2] and spielfeld[1][2] == spielfeld[3][2] and spielfeld[1][2] == spielfeld[4][2] and spielfeld[1][2] != " ":
        print("Spieler "+ spielfeld[1][2] + " hat gewonnen!" )
        return spielfeld[1][2]

    elif spielfeld[1][3] == spielfeld[2][3] and spielfeld[1][3] == spielfeld[3][3] and spielfeld[1][3] == spielfeld[4][3] and spielfeld[1][3] != " ":
        print("Spieler "+ spielfeld[1][3] + " hat gewonnen!" )
        return spielfeld[1][3]

    elif spielfeld[1][4] == spielfeld[2][4] and spielfeld[1][4] == spielfeld[3][4] and spielfeld[1][4] == spielfeld[4][4] and spielfeld[1][4] != " ":
        print("Spieler "+ spielfeld[1][4] + " hat gewonnen!" )
        return spielfeld[1][4]

    elif spielfeld[1][5] == spielfeld[2][5] and spielfeld[1][5] == spielfeld[3][5] and spielfeld[1][5] == spielfeld[4][5] and spielfeld[1][5] != " ":
        print("Spieler "+ spielfeld[1][5] + " hat gewonnen!" )
        return spielfeld[1][5]

    elif spielfeld[1][1] == spielfeld[2][2] and spielfeld[1][1] == spielfeld[3][3] and spielfeld[1][1] == spielfeld[4][4] and spielfeld[1][1] != " ":
        print("Spieler "+ spielfeld[1][1] + " hat gewonnen!" )
        return spielfeld[1][1]

    elif spielfeld[1][2] == spielfeld[2][3] and spielfeld[1][2] == spielfeld[3][4] and spielfeld[1][2] == spielfeld[4][5] and spielfeld[1][2] != " ":
        print("Spieler "+ spielfeld[1][2] + " hat gewonnen!" )
        return spielfeld[1][2]

    elif spielfeld[1][5] == spielfeld[2][4] and spielfeld[1][5] == spielfeld[3][3] and spielfeld[1][5] == spielfeld[4][2] and spielfeld[1][5] != " ":
        print("Spieler "+ spielfeld[1][5] + " hat gewonnen!" )
        return spielfeld[1][5]

    elif spielfeld[1][4] == spielfeld[2][3] and spielfeld[1][4] == spielfeld[3][2] and spielfeld[1][4] == spielfeld[4][1] and spielfeld[1][4] != " ":
        print("Spieler "+ spielfeld[1][4] + " hat gewonnen!" )
        return spielfeld[1][4]
    else:
        return False


muenze_einwerfen(1, "x")
spielfeld_anzeigen()
gewonnen()
muenze_einwerfen(1,"o")
spielfeld_anzeigen()
gewonnen()
muenze_einwerfen(2,"x")
spielfeld_anzeigen()
gewonnen()
muenze_einwerfen(3,"o")
spielfeld_anzeigen()
gewonnen()
muenze_einwerfen(3,"x")
spielfeld_anzeigen()
gewonnen()
muenze_einwerfen(5,"o")
spielfeld_anzeigen()
gewonnen()
muenze_einwerfen(4,"x")
spielfeld_anzeigen()
gewonnen()
muenze_einwerfen(5,"o")
spielfeld_anzeigen()
gewonnen()
muenze_einwerfen(1,"x")
spielfeld_anzeigen()
gewonnen()
muenze_einwerfen(4,"o")
spielfeld_anzeigen()
gewonnen()
muenze_einwerfen(2,"x")
spielfeld_anzeigen()
gewonnen()


