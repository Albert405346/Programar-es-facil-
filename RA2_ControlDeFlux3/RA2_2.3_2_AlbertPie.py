
#------------------------------------------------------------------
# Programa: Suma des de 0 fins a el número introduit per l'usuari.
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 16 / 11 / 2026
#
# Especificacions d'entrada: 1 número enter.
# Gestió: El número ha de ser enter i positiu, obligatoriament.
#------------------------------------------------------------------

try:
    numero = int(input("Introdueix un nombre enter: \n"))

# Declarem aquesta variable, a la que guardarem la suma de tots el nombres des del 0 fins a l'introduit per l'usuari.
    suma = sum(range(0, numero + 1))
    print("La suma és: ", suma)

# Aquí la excepció passa a ser: enter i positiu.
except ValueError:
    print("Ha de ser un número enter i positiu!")
