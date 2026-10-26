#----------------------------------------------------
# Programa: Substitució de contingut
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 19 / 10 / 2026
#
# Especificacions d'entrada: 1 frase, únicament text
#----------------------------------------------------

# Demanem una frase especificant que s'ha de complir la següent norma
frase = input("Introdueix una frase que contingut una paraula repetida: \n")
# Demanem també la paraula repetida a la frase i per la que es vol subtituïr
paraula_repetida = input("Introdueix la para que es repeteix: \n")
paraula_nova = input("Introdueix un paraula per a subtituïr-la: \n")
# Fent servir la funció replace substituïm la paraula repetida per la nova
frase_nova = frase.replace(paraula_repetida,paraula_nova)
print(frase_nova)
