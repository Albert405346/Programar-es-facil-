#------------------------------------------------------------
# Programa: 10 primers membres de la seqüència de Fibonacci.
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 2 / 11 / 2026
#
# Especificacions d'entrada: No es requereixen.
#-------------------------------------------------------------

a = 0
b = 1

contador = 0

while(contador < 10):
    print(a)
# Suma dels dos números anteriors. 
    següent = a + b
# El segon número passa a ser el primer.
    a = b
    b = següent
# Aumenta el contador en 1.
    contador += 1
