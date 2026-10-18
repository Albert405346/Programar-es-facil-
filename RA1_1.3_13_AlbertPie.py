#--------------------------------------------------------------
# Programa: Repetir un paraula
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 19 / 10 / 2026
#
# Especificacions d'entrada: 1 paraula, variable de tipus text
#--------------------------------------------------------------

# Demanem la paraula i la mutipliquem per a mostrar-la 4 vegades
paraula_1= input("Introdeix una paraula: \n")
vegades_1 = paraula_1 * 4
print(vegades_1)
# Multipliquem la paraula 4 vegades separant-la amb espais i afegim parèntesis per a respetar l'ordre operacional
vegades_2 = ((paraula_1 + " ") * 3)
print(vegades_2)
