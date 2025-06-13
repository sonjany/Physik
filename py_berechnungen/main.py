from astrophysik.astro import AstroPhysik

def main():
    masse = 5.7e26
    weg = 1000
    zeit = 30

    print("Astrophysik-Testdaten:")
    astro = AstroPhysik(masse, weg, zeit)

    astro.geschwindigkeit()
    astro.gewichtskraft()
    astro.lichtjahr_pc()
    astro.lichtjahr_skm()
    astro.lichtjahr_km()
    astro.spass_mit_saturn()

if __name__ == "__main__":
    main()