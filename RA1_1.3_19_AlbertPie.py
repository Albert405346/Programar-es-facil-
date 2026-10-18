#------------------------------------------------------
# Programa: Preparació d'un nom d'usuari
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 19 / 10 / 2026
#
# Especificacions d'entrada: 1 variable de tipus text
#-----------------------------------------------------

# Demanem el nom especificant el format
nom = input("Introdueix el teu nom (ha de ser amb espais al principi/final i en majúscules): \n")
# Determinem la longitud
longitud = len(nom)
# El mostrem en minúscules trient els espais
print(nom.lower()[1: longitud -1])
# Mostrem també el total de caràcters
print("El nombre de caràcters total és: ", longitud)
