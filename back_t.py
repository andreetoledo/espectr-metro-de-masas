"""
María Paula Valdés
Rene Ventura
Andree Toledo 18439
Carné: 19146
El valor del campo magnetico:1Gauss--1e-04 Teslas
"""
from tkinter import messagebox
from numpy import *
import math
import time
import matplotlib.pyplot as plt

R1=0
R2=0
R3=0
R4=0
velocidad=0
B=1e-4
selected=[]#lista de partículas seleccionadas
radios=[]
masas=[]

#

class particula:
    def __init__(self, name,mass,charge):
        self.name = name
        self.mass = mass
        self.charge = charge
        
electron = particula("Electrón",1.673E-27,1.6E-19)
proton=particula("Protón",1.673E-27,1.6E-19)
nucleoS=particula("Núcleo de Sodio",3.679e-27,3.52e-19)
particula_alfa=particula("Partícula Alfa",6.64E-27,3.2E-19)
nucleoD= particula("Núcleo de Deuterio",3.34E-27,1.602E-19)
nucleoC= particula("Núcleo de Calcio",6.68E-26,6.408E-18)
nucleoH= particula("Núcleo de Hierro",9.352E-26,4.1652E-18)
Tau=particula("Tau", 3.16E-27,-1.6E-19)

particulas=[electron,proton,nucleoS,particula_alfa,nucleoD,nucleoC,nucleoH,Tau]

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
    J= float(V)
    E=J/2
    velocidad=E/B
    if velocidad > 3e08:
        messagebox.showinfo(title="Cuidado", message="La velocidad no puede ser mayor que la velocidad luz. Revise su entrada por favor.")
    ##print(velocidad)

##Función de graficar 
def graph():
    ##R = (selected[0].mass*velocidad)/(selected[0].charge*B)

    ##Variable de tiempo, es un array
    t= linspace(0,10,15)

    Rs = [R1, R2, R3, R4]
    
    ##Por cada particula, se operan los cosenos y senos de la velocidad * el valor de tiempo
    ## y se multiplican por la respectiva R de la particula, luego se hace una grafica
    for i in range(0, len(selected)):
        print(selected[i].name)
        print(selected[i].mass)
        print(selected[i].charge)
        print("\n")
        R = (selected[i].mass*velocidad)/(selected[i].charge*B)
        print(R)
        cosvals = []
        sinvals = []
        for val in t:
            cosvals.append(R * math.cos(velocidad*val))
            sinvals.append(R * math.sin(velocidad*val))
            plt.plot(cosvals, sinvals, label="Particula " + str(i))
        
    plt.ylabel('y (m)')
    plt.xlabel('x (m)')
    plt.title('Trayectoria')
    plt.show()

