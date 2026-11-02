#---------------------------------------------------------------
# Programa: Indicar si una lletra és vocal o consonant
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 26 / 10 / 2026
#
# Especificacions d'entrada: Una lletra, variable de tipus text
#---------------------------------------------------------------

# Demanem un lletra i formen una string amb les vocals de l'abecedari.
lletra = input("Introdueix una lletra: \n")

vocal = "aeiou"

# Comparem si la lletra introduida coincideix amb alguna de les que formen la string.
# Si coincideix serà vocal, sino consonant.
if (lletra == vocal[0] and lletra == vocal[1] and lletra == vocal[2] and lletra == vocal[3] and lletra == vocal[4]):
    print("La lletra és vocal.")
else:
    print("La lletra és consonant.")
