"""
María Paula Valdés
Hector Aaron Pivaral
Carné: 19146
Carne: 19640
"""
#par1=
#par2=
#par3=
class particula:
    def __init__(self, name,mass,charge):
        self.name = name
        self.mass = mass
        self.charge = charge
        
electron = particula("Electrón",1.673E-27,1.6E-19)
proton=particula("Protón",1.673E-27,1.6E-19)
neutron=particula("Neutron",1.675E-27,0)
particula_alfa=particula("Partícula Alfa",6.64E-27,3.2E-19)
nucleoD= particula("Núcleo de Deuterio",3.34E-27,1.602E-19)
nucleoC= particula("Núcleo de Calcio",6.68E-26,6.408E-18)
nucleoH= particula("Núcleo de Hierro",9.352E-26,4.1652E-18)
Tau=particula("Tau", 3.16E-27,-1.6E-19)
particulas=[electron,proton,neutron,particula_alfa,nucleoD,nucleoC,nucleoH,Tau]
nom=[]
for part in particulas:
    nom.append(part.name)
    
def lista():
    return(nom)
"""
def det(a,b,c):
    for p in particulas
        if a=p.name:
            seleccionaa
"""
    
    
        
    
    