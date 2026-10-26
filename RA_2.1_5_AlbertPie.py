#------------------------------------------------------------------------
# Programa: Indicar si ets o no major d'edat segons la data de naixement
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 26 / 10 / 2026
#
# Especificacions d'entrada: Dia, mes i any en números enters
#------------------------------------------------------------------------

# Demanem la data de naixement composta per el dia, el mes i l'any.
dia = int(input("Introdueix el teu dia de naixement: \n"))
mes = int(input("Introdueix el teu mes de naixement: \n"))
any = int(input("Introdueix el teu any de naixement: \n"))

# Importem la data d'avui per a saber quin dia és, i restem l'any al que estem menys al que va nèixer.
from datetime import date
data_avui = date.today()
anys = data_avui.year - any

# Calculem tenint en compte si:
# La resta dóna més, menys o igual a 18 anys.
if (anys > 18):
    print("Ets major d'edat.")
if (anys < 18):
    print("Ets menor d'edat.")
if (anys == 18):
# Si és el mateix, determinem si el mes introduit ha passat, ha de passar o és el mateix.
    if (data_avui.month() > mes):
        print("Ets major d'edat.")
    if (data_avui.month() < mes):
        print("Ets manor d'edat.")
    if (data_avui.month() == mes):
# Si és el mateix, determinem si el dia introduit ha passat, ha de passar o és el mateix.
        if (data_avui.day() > dia):
            print("Ets major d'edat.")
        if (data_avui.day() < dia):
            print("Ets major d'edat.")
        if (data_avui.day() == dia):
            print("Ets major d'edat.")
