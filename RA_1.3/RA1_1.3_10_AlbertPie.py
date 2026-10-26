#-------------------------------------------------------------------
# Programa: Calcul de la mitjana de tres notes
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 19 / 10 / 2026
#
# Especificacions d'entrada: 3 notes, variables mumériques decimals
#-------------------------------------------------------------------

# Demanem les 3 notes
nota_1 = float(input("Introdueix la primera nota: \n"))
nota_2 = float(input("Introdueix la segona nota: \n"))
nota_3 = float(input("Introdueix la tercera nota: \n"))
# Calculem la mitjana i imprimim el resultat
mitjana = (nota_1 + nota_2 + nota_3) / 3
print("La mitjana de les 3 notres és de", mitjana)
