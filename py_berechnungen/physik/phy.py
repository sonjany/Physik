class Physik:
    G = 9.81  #m/s²
    C = 299792.458  #m/s
    LY = 9.4607e15  #m
    PC = 3.0857e16  #Ly
    SATURN = 5.7e26 #kg
    RIGEL = 864.3 #Ly
    
    def __init__(self, masse, weg, zeit):
        self.masse = masse
        self.weg = weg
        self.zeit = zeit
        self.G = 9.81
        
    
    def geschwindigkeit(self): #v=s/t
        if self.zeit != 0:
            v = round(self.weg / self.zeit,3)
            print(f"Die Geschwindigkeit beträgt: {v} m/s")
        else:
            print(f"Zeit darf nicht 0 sein!")

    def gewichtskraft(self): #Fg=m*G
        if self.masse != 0:
            Fg = round(self.masse * self.G, 3)
            print(f"Die Gewichstkraft beträgt {Fg} N")
        else:
            print(f"Masse darf nicht 0 sein!")

masse = 20 # kg
weg = 1000 # m
zeit = 30 # s
G = 9.81 #kg*m/s

p = Physik(masse, weg, zeit)
p.geschwindigkeit()
p.gewichtskraft()

