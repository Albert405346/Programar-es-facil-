#-------------------------------------------------
# Programa: Mostrar una cadena de text invertida.
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 2 / 11 / 2026
#
# Especificacions d'entrada: Una cadena de text.
#------------------------------------------------

cadena = input("Introdueix una frase: \n")

cadena_invertida = cadena[:: -1]

print("La frase invertida:", cadena_invertida)
