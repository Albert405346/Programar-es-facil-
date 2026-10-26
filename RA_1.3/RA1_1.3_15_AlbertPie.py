#------------------------------------------------------
# Programa: Inversió d'una paraula
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 19 / 10 / 2026
#
# Especificacions d'entrada: 1 variable de tipus text
#-----------------------------------------------------

# Demanem una paraula
paraula = input("Introdueix una paraula: \n")
# Mostre la versió original
print("Paraula original: ", paraula)
# Mostre l'string invertida
# Els dos punts indiquen que es vol recòrrer la sentència completa sense especificar un inici i un final
# El -1 indica que es vol que es llegeixi del final cap al principi
print(paraula[:: -1])
