from physik.phy import Physik

class AstroPhysik(Physik):
    def __init__(self, masse=5.7e26, weg=0, zeit=1):
        super().__init__(masse, weg, zeit)
        self.planet_masse = masse

    def lichtjahr_skm(self):  # s/km
        sly = self.LY / 1000
        sc = self.C
        skm = sly / sc
        print(f"Licht braucht {skm:.2e} s für 1 Lichtjahr")

    def lichtjahr_pc(self):  # LY in PC
        ri_m = self.RIGEL * self.LY
        pc = ri_m / self.PC
        print(f"Rigel ist {pc:.2f} Parsec von der Erde entfernt")

    def lichtjahr_km(self):  # km
        ri_km = self.RIGEL * self.LY / 1000
        print(f"Rigel ist {ri_km:.2e} km von der Erde entfernt")

    def spass_mit_saturn(self):  # N
        if self.planet_masse < self.SATURN:
            print("Kleines Planetchen")
        elif self.planet_masse > self.SATURN:
            print("Grooooßer Gasbrocken")
        else:
            result = self.SATURN * self.G
            print(f"Jetzt bist du mit {result:.2e} N auf die Erde gefallen")