
#Fisica 3 Proyecto 2
#Universidad del valle 

#Imports	
from numpy import *
import math
import matplotlib.pyplot as plt

"""
En esta función se hace plot de cada particula
"""

def plot():

	print("""

	            Cargas		Masas
	Electrón =   -1.6		9.11
	Positrón =   1.6		9.11
	Protón =     -1.6		1.67
	Neutrón =    1.67		1.67

	
	""")
	v = float(input("\tEscribe la velocidad Inicial de la particula m/s (en números):"))
	q = float(input("\tEscribe la carga de la particula (en números):"))
	d = 0.0001
	luz = 3*(10**+8)
	m = float(input("\tEscribe la masa de la particula (en números):")) #9.10938291*(10**-31)
	V = 1*(10**-19)
	pq =1*(10**-31)
	E = float(9.2) #esto ya no va
	l = int(input("\tEn milimetros escribe Longitud de la región (en números):"))
	t= linspace(0,10,15)

	ecuation = ((+(((q*V)+v/(d*(m*pq)))*t*t))/10) + l
	
	a = (q*(E*V)/m)
	x = v*t
	y = v*t+((a*t**2)/2)



	#trazar los datos como puntos de dispersión
	plt.plot(t,ecuation,'r')
	plt.ylabel('y (m)')
	plt.xlabel('x (m)')
	plt.title('Trayectoria')

#Se pregunta con cuantas particulas se quiere trabajar

particles = int(input("Escribe la cantidad de particulas que deseas generar (en números):"))
for i in range(0,particles):
	print("\nParticula " + str(i+1) + ":")
	plot()
plt.show()