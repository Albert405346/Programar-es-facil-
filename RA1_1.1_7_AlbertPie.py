#------------------------------------------------------------
# Programa: Realització d'una resta, multiplicació i divisió
# Autor: Albert Pie Santamaria
# Data: 28 / 09 / 2026
#------------------------------------------------------------

# Demanem dos variables per a dos números en cada una de les operacions, definim i imprimim la fórmula. 
numero_r1 = int(input("Introdueix un numero per a restar \n"))
numero_r2 = int(input("Introdueix un segon numero per a completar la resta \n"))
# Restem amb una guió.
resta = (numero_r1 - numero_r2)
print (resta)
numero_m1 = int(input("Introdueix un numero per a multiplicar \n"))
numero_m2 = int(input("Introdueix un segon numero per a completar la multiplicacio \n"))
# Multipliquem amb un asterisc.
multiplicacio = (numero_m1 * numero_m2)
print (multiplicacio)
numero_d1 = int(input("Introdueix un numero per a dividir \n"))
numero_d2 = int(input("Introdueix un segon numero per a completar la divisio \n"))
# Dividim amb una barra. 
divisio = (numero_d1 // numero_d2)
print (divisio)
