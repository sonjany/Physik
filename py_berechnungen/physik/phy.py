from physik import konstanten as k
from physik import formeln as f

class Physik:
    
    def __init__(self, masse, weg, zeit):
        self.masse = masse
        self.weg = weg
        self.zeit = zeit
        #self.G = 9.81
        
    
    def geschwindigkeit(self): #v=s/t
        try:
            v = f.berechne_geschwindigkeit(self.weg, self.zeit)
            print(f"Die Geschwindigkeit beträgt: {v} m/s")
        except ValueError as ex:
            print(ex)


    def gewichtskraft(self): #Fg=m*G
        try:
            Fg = f.berechne_gewichtskraft(self.masse, k.G)
            print(f"Die Gewichstkraft beträgt: {Fg} N")
        except ValueError as ex:
            print(ex)


    def kraft(self,beschleunigung):  #F=m*a
        try:
            F_ges = f.berechne_kraft(self.masse, beschleunigung)
            print(f"Die Kraft beträgt: {F_ges} N")
        except ValueError as ex:
            print(ex)
        

