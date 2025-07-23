from physik import konstanten as k


def berechne_geschwindigkeit(weg, zeit): #v=s/t
        if zeit == 0:
            raise ValueError("Zeit != 0!!!!")
        return round(weg / zeit, 4)

def berechne_gewichtskraft(masse, G): #Fg=m*G
        if masse == 0:
            raise ValueError("Masse != 0!!!!")
        return round(masse * k.G, 4)

def berechne_kraft(masse, beschleunigung):
    return round(masse * beschleunigung, 4)