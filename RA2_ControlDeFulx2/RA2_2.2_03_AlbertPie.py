#--------------------------------------------------------------
# Programa: Mostrar la taula de multiplicar d'un número enter.
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 2 / 11 / 2026
#
# Especificacions d'entrada: Un número enter.
#---------------------------------------------------------------

numero = int(input("Introdueix un número enter: \n"))

multiplicador = 1

# Es repeteix el bucle fins a arribar a 10.
# resultat calcula la mutiplicació i es mostra detalladament.
# Aumenta el multiplicador en 1.
while(multiplicador <= 10):
    resultat = numero * multiplicador
    print(numero, "X", multiplicador, "=", resultat)
    multiplicador += 1
