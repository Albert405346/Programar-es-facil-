#----------------------------------------------------------------
# Programa: Construcció d'una frase amb espais
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 19 / 10 / 2026
#
# Especificacions d'entrada: 3 paraules, variables de tipus text
#----------------------------------------------------------------

# Demanem les tres paraules amb les que construir la frase
paraula_1 = input("Introdueix una paraula: \n")
paraula_2 = input("Introdueix una segona paraula: \n")
paraula_3 = input("Introdueix una tercera paraula: \n")
# Concatenem la frase amb + i les " " per a afegir espais entre les paraules
frase = paraula_1 + " " + paraula_2 + " " + paraula_3 + "."
print(frase)
