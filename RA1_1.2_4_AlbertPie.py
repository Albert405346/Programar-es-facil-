#------------------------------------------------------------------------------------------------------
# Programa: Calculadora que mostra la operació a executar (no calcula)
# Autor: Albert Pie Santamaria
# Curs: 1rº ASIX
# Data: 5 / 10 / 2026
#
# Especificacions d'entrada: 2 enters o decimals i el signe operatiu corresponent (+, -, *, /, //, %)
#-----------------------------------------------------------------------------------------------------

# Demanem els dos números i el signe operatiu
número_1 = int(input("Introdueix el primer número \n"))
número_2 = int(input("Introdueix el segón número \n"))
signe = input("Quina operació vols executar? \n")
# Definim la variable operació i concatenem els valors amb comes. Indiquem que els números són str; no es pot sumar entern i text. 
operació = str(número_1) + signe + str(número_2)
# Imprimim operació
print(operació)
