#-----------------------------------------------------
# Programa: Indicar si un número és parrel o imparell
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 26 / 10 / 2026
#
# Especificacions d'entrada: 1 número enter
#-----------------------------------------------------

# Demanem un número i calculem el residu per a sabar si és igual a zero o no.
número = int(input("Introdueix un número: \n"))

residu = número % 2

# Si si ho és serà parell, si no senar.
if (residu == 0):
    print("És parell.")
else:
    print("És senar.")
