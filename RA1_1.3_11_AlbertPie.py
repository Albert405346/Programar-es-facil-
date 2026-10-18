#-------------------------------------------------------------------------------
# Programa: Conversió de minuts a hores i minuts restants
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 19 / 10 / 2026
#
# Especificacions d'entrada: nombre de minuts totals, variable numérica entera
#------------------------------------------------------------------------------

# Demanem els minuts
minuts = int(input("Introdueix el nombre total de minuts: \n"))
# Els conversionem a hores i calculem els minuts restants amb les següent fórmules
hores = minuts // 60
minuts_restants = minuts % 60
# Imprimim els resultats
print("Tens un total de", hores, "hores i", minuts_restants, "minuts")
