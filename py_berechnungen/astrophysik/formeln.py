from astrophysik import konstanten as k


def berechne_lichtjahr_skm():  # s/km
        skm = ((k.LY/1000)/k.C)
        return skm
    
def berechne_lichtjahr_pc():  # LY in PC
        pc = ((k.RIGEL * k.LY) / k.PC)
        return pc
          
def berechne_lichtjahr_km():  # km
        ri_km = ((k.RIGEL * k.LY)/ 1000)
        return ri_km
    
def quatsch_spass_mit_saturn(masse):  # N
        if masse < k.SATURN_M:
            return "mini"
        elif masse > k.SATURN_M:
            return "größer"
        else:
            quatsch = (k.SATURN_M * k.G)
            return quatsch

#planet_masse = 7.7e30