#-----------------------------------------------------------------------------------------------
# Programa: Fitxa de l'alumne
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 19 / 10 / 2026
#
# Especificacions d'entrada: Nom complet, ciutat i cicle, únicament text i l'edat, número enter
#-----------------------------------------------------------------------------------------------

# Demanem les dades necessàries per a construir la fitxa de l'alumne
nom = input("Quin és el teu nom? \n")
congnom = input("Quin és el teu cognom? \n")
edat = int(input("Quants anys tens? \n"))
ciutat = input("On vius? \n")
cicle = input("Què estudies? \n")
# Realitzem l'operació per a determinar l'edat l'any vinent
edat_pròxima = edat + 1

# Contruim la fitxa de l'alumne mostrant el nom complet en majúscules, concatenant-lo amb + (amb el correu igual), l'operació i els demés paràmetres
print("===FITXA DE L'ALUMNE===")
print("Nom complet: ", nom.upper() + congnom.upper())
print("L'edat que tindràs l'any vinent és: ", edat_pròxima)
print("Ciutat: ", ciutat)
print("Cicle: ", cicle)
print(nom.lower() + "." + congnom.lower() + "@alumnes.cat")
