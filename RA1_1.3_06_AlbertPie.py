#-------------------------------------------------------------
# Programa: Calculador bàsica
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 19 / 10 / 2026
#
# Especificacions d'entrada: 2 números decimals majors a cero
#-------------------------------------------------------------

# Demanem dos nombres amb els que realitzar les operacions
nombre_1 = float(input("Introdueix un nombre decimal: \n"))
nombre_2 = float(input("Introdueix un segón nombre decimal: \n"))
# Operem fent servir etiquetes 
suma = nombre_1 + nombre_2
resta = nombre_1 - nombre_2
multiplicació = nombre_1 * nombre_2
divisió = nombre_1 / nombre_2
# Mostrem els resultats amb missatges ben presentats
print("El resultat de la suma és", suma)
print("El resultat de la resta és", resta)
print("El resultat de la multiplicació és", multiplicació)
print("El resultat de la divisió és", divisió)
