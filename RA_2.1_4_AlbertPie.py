#------------------------------------------------------------------
# Programa: Indicar si has aprovat o suspés
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 26 / 10 / 2026
#
# Especificacions d'entrada: 1 número de l'1 al 10 enter o decimal
#------------------------------------------------------------------

# Demanem la nota.
número = float(input("Introdueix un número de l'1 al 10: \n"))

# Si es compleixen aquestes característiques, suspendrà o aprovarà.
if (número < 5):
    print("Has suspés!")
else:
    print("Has aprovat!")
