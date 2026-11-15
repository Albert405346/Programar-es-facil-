
#------------------------------------------------------------------------------
# Programa: Tots els nombres primers des de 2 fins a l'introduit per l'usuari.
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 16 / 11 / 2026
#
# Especificacions d'entrada: 1 número enter.
# Gestió: El número ha de ser enter, obligatoriament.
#------------------------------------------------------------------------------

try:

# Implementem una funció (es_primer(n)) que determinar si és primer,
# i amb un condicional comprovem que no sigui major a 2.
    def es_primer(n):
        if n < 2:
            return False

# Aquest bucle recorre des del 2 fins a l'introduit per l'usuari, calculant el residu amb el modul (%).
# Si és 0, retornarà false, si no, true.
        for i in range(2, n):
            if n % i == 0:
                return False

        return True


    numero = int(input("Introdueix un nombre enter: \n"))

# Aquest tercer bucle recorre la seqüencia, comprova si és primer, si ho és, l'imprimeix.
    for i in range(2, numero + 1):
        if es_primer(i):
            print(i)

except ValueError:
    print("Ha de ser un número enter!")
