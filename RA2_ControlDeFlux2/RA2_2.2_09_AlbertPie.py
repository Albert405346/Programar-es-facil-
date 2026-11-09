#------------------------------------------------------------------------------------------------------
# Programa: Trobar el nombre més gran d'una llista de nombres.
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 2 / 11 / 2026
#
# Especificacions d'entrada: Llista de números, que poden ser: positius, negatius, enters i decimals.
#-----------------------------------------------------------------------------------------------------

# Necessitem convertir els números en una llista per a treballar millor.
# Concretament, les funcions strip() i split() serveixen per a eliminar els espais sobrants i separar per espais, salts de linea o tabulacions.
numero = input("Introdueix una llista de números: \n")
llista = [int(n.strip()) for n in numero.split()]

maxim = llista[0]

#També, hem de guardar el primer número com a màxim;
#Serà inicialment el més gran, però, si el bucle troba un més alt, canviarà.
for numero in llista:
    if numero > maxim:
        maxim = numero

print("El número més gran és:", maxim)
