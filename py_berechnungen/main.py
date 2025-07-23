from physik.phy import Physik
from astrophysik.astro import AstroPhysik
from gui.hauptmenue import starte_menue


def test():
    #physik Werte
    masse_p = 20 # kg
    weg_p = 1000 # m
    zeit_p = 30 # s
    
    #astrophysik Werte
    masse_a = 5.7e26 #kg
    weg_a = 1000 #m
    zeit_a = 30 #s


    print("Physik-Testdaten:")
    p = Physik(masse_p, weg_p, zeit_p)
    print()
    p.geschwindigkeit()
    p.gewichtskraft()
    print()
    print("Astrophysik-Testdaten:")
    astro = AstroPhysik(masse_a, weg_a, zeit_a)
    print()
    astro.lichtjahr_pc()
    astro.lichtjahr_skm()
    astro.lichtjahr_km()
    astro.spass_mit_saturn()

if __name__ == "__main__":
        #test()
        starte_menue()
