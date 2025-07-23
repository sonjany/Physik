from physik.phy import Physik
from astrophysik import konstanten as k
from astrophysik import formeln as f

class AstroPhysik(Physik):
    def __init__(self, masse, weg, zeit):
        super().__init__(masse, weg, zeit)
        self.planet_masse_a = masse
        self.weg = weg
        self.zeit = zeit
        self.G = k.G

    def lichtjahr_skm(self):  # s/km
        skm = f.berechne_lichtjahr_skm()
        print(f"Licht braucht {skm} s für 1 Lichtjahr")

    def lichtjahr_pc(self):  # LY in PC
        pc = f.berechne_lichtjahr_pc()
        print(f"Rigel ist {pc} Parsec von der Erde entfernt")

    def lichtjahr_km(self):  # km
        ri_km = f.berechne_lichtjahr_km()
        print(f"Rigel ist {ri_km} km von der Erde entfernt")

    def spass_mit_saturn(self):  # N
        quatsch = f.quatsch_spass_mit_saturn(self.masse)
        if quatsch == "mini":
            print("Kleines Planetchen")
        elif quatsch == "größer":
            print("Grooooßer Gasbrocken")
        else:
            print(f"Mist! du bist mit {quatsch} N auf die Erde gefallen")

