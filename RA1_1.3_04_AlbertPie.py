#----------------------------------------------------
# Programa: Detectar i corregir un error
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 19 / 10 / 2026
#
# Especificacions d'entrada: Una edat, número enter
#---------------------------------------------------

# Demanem l'edat. L'error està aquì, falta l'int, sense això, el valor es guarda com a text i no es pot operar correctament.
# Codi corregit:
edat = int(input("Quants anys tens? "))
edat_futura = edat + 5
print(edat_futura)