#-------------------------------------------------------------
# Programa: Mostrar una paraula 3 vegades seguides amb espais
# Autor: Albert Pie Santamaria
# Curs: 1rº ASIX
# Data: 5 / 10 / 2026
#
# Especificacions d'entrada: 1 paraula, únicament text
#------------------------------------------------------

# Demane el valor
paraula = input("Introdueix una paraula: \n")
# Concatenem el valor, els espais i el nombre de vegades respectant l'ordre d'operació
vegades = ((paraula + " ") * 3)
print(vegades)
