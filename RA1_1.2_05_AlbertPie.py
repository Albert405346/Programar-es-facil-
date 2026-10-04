#-----------------------------------------------------------
# Programa: Concatenació d'un nom i cognom
# Autor: Albert Pie Santamaria
# Curs: 1rº ASIX
# Data: 5 / 10 / 2026
#
# Especificacions d'entrada: 1 nom y cognom, únicament text
#-----------------------------------------------------------

# Demanem els valors
nom = input("Quin és el teu nom? \n")
cognom = input("Quin és el teu cognom? \n")
# Concatenem amb + i fem servir les cometes per a espaiar cada valor
nom_complet = (nom + " " + cognom)
# Imprimim
print(nom_complet)
