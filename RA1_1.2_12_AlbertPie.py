#----------------------------------------------------
# Programa: Substitució d'una paraula en una frase
# Autor: Albert Pie Santamaria
# Curs: 1rº ASIX
# Data: 5 / 10 / 2026
#
# Especificacions d'entrada: 1 frase, únicament text
#----------------------------------------------------

# Demanem els valors
frase = input("Introdueix una frase: \n")
# Demanem la paraula que es vol subtutuir
paraula_sustituida = input("Introdueix la paraula a subtituir, present a la frase anterior: \n")
# Demanem la paraula subtituta
paraula_nova = input("Introdueix la paraula substituta: \n")
# Construim la subtitució amb la funció replace i imprimim
frase_nova = frase.replace(paraula_sustituida, paraula_nova)
print(frase_nova)
