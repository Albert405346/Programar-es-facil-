
#-------------------------------------------------------------------------------------------------------------------
# Programa: Recorrer la seqüència de números, des de 0 fins a l'introduit per l'usuari, mostrant només els parells.
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 16 / 11 / 2026
#
# Especificacions d'entrada: 1 número enter.
# Gestió: El número ha de ser enter i positiu, obligatoriament.
#-------------------------------------------------------------------------------------------------------------------

try:
    numero = int(input("Introdueix un nombre enter: \n"))

# El següent range opera des del 0, fins a l'introduit per l'usuari, saltan de dos en dos.
    for i in range(0, numero + 1, 2):
        print(i)

except ValueError:
    print("Ha de ser un número enter i positiu!")