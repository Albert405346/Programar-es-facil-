#---------------------------------------------------------------------------
# Programa: Seqüència de nombres des de O fins a un introduit per l'usuari.
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 16 / 11 / 2026
#
# Especificacions d'entrada: 1 número enter.
# Gestió: El número ha de ser enter, obligatoriament.
#---------------------------------------------------------------------------

try: # Utilitzem try com a gestor per a la captura d'errors.
    numero = int(input("Introdueix un número: \n"))

# Amb aquest bucle, iniciem des de 0, recorrent la seqüència fins al número introduit per a mostrar-la.
    for i in range(0, numero +1):
        print(i)

except ValueError: # Utilitzem ValueError ja que necessitem detectar si el codi rep un argument amb valor inapropiat.
    print("Ha de ser un número enter!")
