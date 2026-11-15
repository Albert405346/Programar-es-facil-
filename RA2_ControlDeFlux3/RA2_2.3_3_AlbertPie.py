
#--------------------------------------------------------------------------------------
# Programa: Construcció de la taula de multiplicar d'un número introduit per l'usuari.
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 16 / 11 / 2026
#
# Especificacions d'entrada: 1 número enter.
# Gestió: El número ha de ser enter, obligatoriament.
#---------------------------------------------------------------------------

try:
    numero = int(input("Introdueix un número: \n"))

# Construim un bucle que recorri 10 voltes, on a cada una es múltiplica la i (número exitent a la volta) pel que ha introduit l'usuari.
# L'imprimi amb format de taula multiplicar. 
    for i in range(1, 11):
        resultat = i * numero
        print(numero, "X", i, "=", resultat)

except ValueError:
    print("Ha de ser un número enter!")