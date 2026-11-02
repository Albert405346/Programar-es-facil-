#--------------------------------------------------------------------------
# Programa: Calcul de la suma dels primers 100 nombres, enters i positius.
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 2 / 11 / 2026
#
# Especificacions d'entrada: No es requereixen.
#---------------------------------------------------------------------------

suma = 0
numero = 1

while(numero <= 100):
# Els següents símbols afegeixen el número actual a la suma i l'aumentan en 1.
    suma += numero
    numero += 1
print("El resultat és", suma)
