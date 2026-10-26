#------------------------------------------------------------------
# Programa: Explicar i comentar un codi
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 19 / 10 / 2026
#
# Especificacions d'entrada: 1 preu decimal i un quantitat entera
#-----------------------------------------------------------------

# Es defineix una variable per a preguntar el preu unitari.
preu = float(input("Preu: "))
# Es defineix una variable per a preguntar la quantitat d'unitats.
quantitat = int(input("Quantitat: "))
# Es calcula el preu total tenint en compte la quantitat.
total = preu * quantitat
# Mostra el resultat de l'operació, però, afegint str, ja que, és un número y Python no permet concatenar-ho amb + si no és text.
print("Total: " + str(total) + " euros")
