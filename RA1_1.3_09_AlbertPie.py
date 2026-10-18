#----------------------------------------------------------------------------------------------------------
# Programa: Calculs d'una compra amb IVA
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 19 / 10 / 2026
#
# Especificacions d'entrada: preu del producte/quantitat d'unitats, variables numériques entera i decimal
#---------------------------------------------------------------------------------------------------------

# Definim IVA com a constant, 0.21 %
IVA = 0.21
# Demanem les dades
preu = float(input("Introdueix el preu de la compra: \n"))
quantitat = int(input("Introdueix la quantitat d'unitats: \n"))
# Calculem l'import de la compra sense IVA i imprimim el resultat
compra = preu * quantitat
print("L'import de la compra sense IVA és de", compra)
# Calculem l'import de la compra amb IVA i imprimim el resultat
preu_iva = (preu *  IVA) + preu
print("L'import de la compra amb el IVA afegit és de", preu_iva)
