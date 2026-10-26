#---------------------------------------------------------------------
# Programa: Conversió de minuts a hores, calculant els minuts sobrants
# Autor: Albert Pie Santamaria
# Data: 28 / 09 / 2026
#---------------------------------------------------------------------

minuts = int(input("Introdueix el nombre total de minuts \n"))
# Calculem les hores totals fent dues barres (per a divisió sencera).
hores = minuts // 60
# Calculem els minuts restants amb l'operador módul, el qual ens dona la resta d'una divisió. 
minuts_sobrants = minuts % 60 
# Mostrem el resultat de l'operació convinant l'impresió de contingut en text i variables.
print ("Tens", hores, "hores i", minuts_sobrants, "minuts")
