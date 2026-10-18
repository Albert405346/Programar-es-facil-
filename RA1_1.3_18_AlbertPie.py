#----------------------------------------------------
# Programa: Majúscules, minúscules i longitud
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 19 / 10 / 2026
#
# Especificacions d'entrada: 1 frase, únicament text
#----------------------------------------------------

# Demanem una frase
frase = input("Introdueix un frase: \n")
# La convertim a majúscules, minúscules i determinem la seva longitud
majúscules = frase.upper()
minúscules = frase.lower()
longitud = len(frase)
# Mostrem la frase original, aquesta en majúscules, minúscules i es caràcters totals
print("La frase original és:", frase)
print(majúscules)
print(minúscules)
print("La frase té", longitud, "caràcters")
