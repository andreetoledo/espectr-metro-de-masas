"""
María Paula Valdés
Hector Aaron Pivaral
Carné: 19146
Carne: 19640
"""
from tkinter import *
from back_t import*
from tkinter import ttk
 

raiz=Tk()
#raiz.config(bg=white)"
raiz.geometry("700x400")
raiz.title("Simulación de campo eléctrico 2020")
Bienvenida = Label(raiz,text= "Simulación espectrómetro de masas", font="Times 20")
Bienvenida.grid(row=0, column=1,columnspan=6)

electron = particula("electron",1.673E-27,1.6E-19)
proton=particula("Proton",1.673E-27,1.6E-19)
neutron=particula("Neutron",1.675E-27,0)
particula_alfa=particula("Partícula Alfa",6.64E-27,3.2E-19)
nucleoD= particula("Núcleo de Deuterio",3.34E-27,1.602E-19)
nucleoC= particula("Núcleo de Calcio",6.68E-26,6.408E-18)
nucleoH= particula("Núcleo de Hierro",9.352E-26,4.1652E-18)
Tau=particula("Tau", 3.16E-27,-1.6E-19)
particulas=[electron,proton,neutron,particula_alfa,nucleoD,nucleoC,nucleoH,Tau]

x=len(particulas)

n=0
comboExample = ttk.Combobox(raiz, values=particulas[x].name)
comboExample.grid(row=1,column=1)
  

raiz.mainloop()