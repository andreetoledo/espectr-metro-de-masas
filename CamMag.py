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
Bienvenida.grid(row=0, column=1,columnspan=11)
##lista de nombre de las partículas
P_names= lista()

#voltaje
Vol= Label(raiz,text= "Voltaje (V): ", font="Times 12")
Vol.grid(row=1, column=1)
volt= Entry(raiz,background="lightgreen",width=14, font= "Cambria 12")
volt.grid(row=2,column=1)
#realización de los combobox de selección
Selec = Label(raiz,text= "Seleccione las partículas que desee:", font="Times 12")
Selec.grid(row=3, column=1)
combo_1 = ttk.Combobox(raiz,foreground ="green",values=P_names)
combo_1.grid(row=4,column=1)
combo_2 = ttk.Combobox(raiz,foreground ="green",values=P_names)
combo_2.grid(row=6,column=1)
combo_3 = ttk.Combobox(raiz,foreground ="green", values=P_names)
combo_3.grid(row=8,column=1)
#nueva partícula
Nueva = Label(raiz,text= "Complete los datos para la partícula \n que desee introducir:", font="Times 12")
Nueva.grid(row=1, column=10)
F = LabelFrame(raiz,bd=4, background="lightblue",width=180, height=250,padx=3, pady=3).grid(row=2,column=10,rowspan=6)
m1= Label(raiz,F,background="lightblue",text= "Protones de partícula:", font="Times 12")
m1.grid(row=2, column=10)
Prot= Entry(raiz,F,width=14, font= "Cambria 12")
Prot.grid(row=3,column=10)
m2= Label(raiz,F,background="lightblue",text= "Neutrones de partícula:", font="Times 12")
m2.grid(row=4, column=10, columnspan=2)
Neu= Entry(raiz,F,width=14, font= "Cambria 12")
Neu.grid(row=5,column=10)
m3= Label(raiz,F,background="lightblue",text= "Electrones de partícula:", font="Times 12")
m3.grid(row=6, column=10, columnspan=2)
Elec= Entry(raiz,F,width=14, font= "Cambria 12")
Elec.grid(row=7,column=10)
#Obtener los valores
def obtener():
    a=combo_1.get()
    b=combo_2.get()
    c=combo_3.get()
    det(a,b,c)

## Botones para realizar la simulacion
aceptar = Button(raiz,text="Mostrar simulacion",font="Cambria 12",command=obtener)
aceptar.grid(row=8, column=5)

  

raiz.mainloop()