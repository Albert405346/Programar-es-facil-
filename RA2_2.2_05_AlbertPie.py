#------------------------------------------------------
# Programa: Determinar si el número és primer o no.
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 2 / 11 / 2026
#
# Especificacions d'entrada: Un número enter, positiu.
#------------------------------------------------------

numero = int(input("Introdueix un número enter i postitiu: \n"))

# Primer, comprovem si és divisible entre dos. Els que ho siguin no són primers.
divisor = 2
es_primer = True

# Si és menor que 2, no ho és. 
if numero < 2:
    es_primer = False
# Si sí que ho és:
# Comprovem si es pot dividir entre números menors que ell i si la divisió és exacta.
else:
    while divisor < numero:
        if numero % divisor == 0:
            es_primer = False
            break
# Si no troba cap divisor, prova amb un número més. 
        divisor += 1

if es_primer:
    print("Es un número primer.")
else:
    print("No es un número primer.")
