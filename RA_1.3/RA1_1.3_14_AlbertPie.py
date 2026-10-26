#-------------------------------------------------------
# Programa: Construcció d'una adreça electrònica
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 19 / 10 / 2026
#
# Especificacions d'entrada: 2 variables de tipus text
#------------------------------------------------------

# Demanem les dades necessàries que una adreça electrònica ha de portar
nom = input("Introdueix el teu nom: \n")
cognom = input("Introdueix el teu cognom: \n")
# Construim els correu contanant variables i text
correu = nom + cognom + "@alumnes.cat."
print(correu.lower())
