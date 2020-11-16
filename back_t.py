"""
María Paula Valdés
Rene Ventura
Andree Toledo
Carné: 19146

"""
velocidad=0
##lista de partículas seleccionadas
selected=[]
##
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
#crear la nueva particula
def nuevaP(e,p,n):
    e1=float(e)
    p1=float(p)
    n1=float(n)
    masa=e1*(9.1e-31)+(p1+n1)*(1.67e-27)
    carga=e1*(-1.06e-19)+p1*(1.06-19)
    n=particula("Costumizada",masa,carga)
    selected.append(n)
##crea una lista ´selected´que cambia para cada tres particulas elegidas
def det(a,b,c):
    nueva=[]
    for p in particulas:
        if a==p.name:
            nueva.append(p)
        if b==p.name:
            nueva.append(p)
        if c==p.name:
            nueva.append(p)
    global selected
    selected=nueva## sobreescribe la lista cada vez
    
def pp():## ESTE METODO SE DEBE BORRAR AL FINAL
    for i in range(len(selected)):
        print(selected[i].name)
        
def campoE(V):
    global velocidad
    E=V/2
    
    
    

    

    
        
    
    