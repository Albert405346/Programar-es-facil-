#-------------------------------------------------------
# Programa: Presentació personal
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 19 / 10 / 2026
#
# Especificacions d'entrada: 3 variables de tipus text
#------------------------------------------------------

# Demanem les variables nom, edat i ciutat per a formar el miisatge
nom = input("Quin és el el teu nom? \n")
edat = input("Quina és la teva edat? \n")
ciutat = input("On vius? \n")
# Concatenem el text que volem mostrar amb les variables i l'imprimim
presentació_personal = "Hem dic" + " " + nom + "," + " " + "tinc" + " " + edat + " " + "anys i visc a" + " " + ciutat + "."
print(presentació_personal)
