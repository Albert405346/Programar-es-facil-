#---------------------------------------------------------------
# Programa: Calcul del quadrat i l'àrea d'un cercle
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 19 / 10 / 2026
#
# Especificacions d'entrada: el radi, variable numérica decimal
#---------------------------------------------------------------

# Definim el núemro PI com a constant i demanem el radi
PI = 3.1416
radi = float(input("Introdueix el radi de la circumferència: \n"))
# Calculem l'àrea amb la següent fórmula i imprimi el resultat amb un missatge ben presentat
area = PI * radi ** 2
print("El radi de la circumferència és", area)
