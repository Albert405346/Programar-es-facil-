#--------------------------------------------------------------------------------
# Programa: Seleciconar un número d'entre 1 - 100 per a que l'usuari l'endevini.
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 2 / 11 / 2026
#
# Especificacions d'entrada: L'usuari ha d'endevinar el número.
#---------------------------------------------------------------------------------

# Funcions que ens permeten adquirir una llibreria amb la que generar el número aleatori.
import random
numero = random.randint(1, 100)

intent = int(input("Adivina el número: \n"))

# != vol dir que, mentre l'intent sigui distint al número seleccionat, es repetirà el bucle.
while(intent != numero):
    if intent > numero:
        print("Massa alt")
    else:
        print("Massa baix")
    intent = int(input("Prova una altra vegada: \n"))

print("Correcte! Has encertat.")
