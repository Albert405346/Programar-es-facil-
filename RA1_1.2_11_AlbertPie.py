#---------------------------------------------------------------------------------------
# Programa: Eliminació dels espais del principi/final en una frase
# Autor: Albert Pie Santamaria
# Curs: 1rº ASIX
# Data: 5 / 10 / 2026
#
# Especificacions d'entrada: 1 frase, únicament text, amb espais al principi i al final
#---------------------------------------------------------------------------------------

# Demanem els valors
frase = input("Introdueix una frase amb espais al principi/final: \n")
# Declarem la variable longitud amb la funció len per a saber quant mesura la frase i indicar la posició d'inici (1) fins al final
longitud = len(frase)
print(frase[1: longitud -1])
