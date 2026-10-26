#------------------------------------------------------
# Programa: Indicar quin dels tres números és més gran
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 26 / 10 / 2026
#
# Especificacions d'entrada: 3 números enters
#------------------------------------------------------

# Demanem tres números.
a = int(input("Introdueix un primer número: \n"))
b = int(input("Introdueix un segon número: \n"))
c = int(input("Introdueix un tercer número: \n"))

# Els comparem entre si, tots amb tots, per a saber quins dels tres és major que els altres dos.
if (a > b and a > c):
    print("El més gran és: ", a)
if (b > a and b > c):
    print("El més gran és: ", b)
if (c > a and c > b): 
    print("El més gran és: ", c)
