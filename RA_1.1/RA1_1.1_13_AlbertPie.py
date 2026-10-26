#-------------------------------------------------------------
# Programa: Conversió de graus Celcius (ºC) a Fahrenheit (ºF)
# Autor: Albert Pie Santamaria
# Data: 28 / 09 / 2026
#-------------------------------------------------------------

graus = float(input("Quina es la temperatura actual en graus Celsius? \n"))
# Afegim parèntesis ja que la multiplicació té prioritat respecte la suma.
temperatura_fahrenheit = graus * (9 / 5) + 32
print (temperatura_fahrenheit)
