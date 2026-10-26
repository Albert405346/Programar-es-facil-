#----------------------------------------------------
# Programa: Presentació personal
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 19 / 10 / 2026
#
# Especificacions d'entrada: 1 frase, únicament text
#----------------------------------------------------

# Demanem una frase especificant que s'han de complir les següent normes
frase = input("Introdueix una frase amb espais al principi i al final: \n")
# Fent servir la funció len, determinem la longitud (caràcters) que aquesta té
longitud = len(frase)
# Imprimim els resultats entre claudàtors i eliminem els espais demanats amb la següent operació
# 1:/-1 fan que no s'inclogui al resultat que es mostra el primer i últim caràcter
frase_nova = (frase[1: longitud -1])
print("[" + frase_nova + "]")
