#-------------------------------------------------------
# Programa: Mostrar una paraula al revés
# Autor: Albert Pie Santamaria
# Curs: 1rº ASIX
# Data: 5 / 10 / 2026
#
# Especificacions d'entrada: 1 paraula, únicament text
#------------------------------------------------------

# Demanem els valors 
paraula = input("Introdueix una paraula: \n")
# Imprimim la cadena amb l'operació per a mostrar la paraula al revés
print(paraula[:: -1])
