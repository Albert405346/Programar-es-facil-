#------------------------------------------------
# Programa: Calculem l'àrea d'una circumferència
# Autor: Albert Pie Santamaria
# Data: 28 / 09 / 2026
#------------------------------------------------

PI = 3.1416
# Demanem el radi, amb float per a marcar que ha de ser un número decimal.
radi = float(input("Quin es el radi de la teva circunferencia? \n"))
# Fem servir dos ** com a operador de potenciació (per a el número introduit es multipliqui dues vagades pel seu valor). 
# Indiquem al programa que faci servir la constant definida i la variable demanada per a resoldre la fórmula.
area = PI * radi ** 2
print (area)
