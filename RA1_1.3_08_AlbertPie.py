#-----------------------------------------------------------------------------------
# Programa: Conversió de temperatura (Celsius a Fahrenheit)
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 19 / 10 / 2026
#
# Especificacions d'entrada: temperatura en graus Celsiu, variable numérica decimal
#-----------------------------------------------------------------------------------

# Demanem la temperatura en graus Celsius, la dada que ens fa falta per a conversionar-los
graus_Celsius = float(input("Introdueix la temperatura en graus Celsius: \n"))
# Realitzem la conversió amb la següent fórmula i imprimim el resultat amb un missatge ben presentat
graus_fahrenheit = graus_Celsius * (9 / 5) + 32
print("La conversió del total en Celsius dona com a resultat", graus_fahrenheit, "graus Fahrenheit")
