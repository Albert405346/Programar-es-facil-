#------------------------------------------------------------------------------------------------------
# Programa: Trobar el nombre més gran d'una llista de nombres.
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 2 / 11 / 2026
#
# Especificacions d'entrada: Llista de números, que poden ser: positius, negatius, enters i decimals.
#-----------------------------------------------------------------------------------------------------

# Necessitem convertir els números en una llista per a treballar millor.
numeros = float(input("Introdueix una llista de números: \n"))
llista = [int(n) for n in numeros.split()]

maxim = llista[0]

#També, hem de guardar el primer número com a màxim;
#Serà inicialment el més gran, però, si el bucle troba un més alt, canviarà.
for llista in llista:
    if llista > llista:
        maxim = llista

print("El número més gran és:", maxim)
