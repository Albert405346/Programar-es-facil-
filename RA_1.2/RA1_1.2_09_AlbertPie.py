#------------------------------------------------------------
# Programa: Construcció d'una adreça electrònica
# Autor: Albert Pie Santamaria
# Curs: 1rº ASIX
# Data: 5 / 10 / 2026
#
# Especificacions d'entrada: 1 nom i cognom, únicament text
#-----------------------------------------------------------

# Demanem els valors
nom = input("Introdueix el teu nom: \n")
cognom = input("Introdueix el teu cognom \n")
# Construcció del format
print("Nom:", nom)
print("Cognom:", cognom)
# I de l'adreça electrònica
correu = nom + "." + cognom + "@institut.cat"
print(correu)
