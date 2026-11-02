#-----------------------------------------------
# Programa: Mostrar el següent dibuix.
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 2 / 11 / 2026
#
# Especificacions d'entrada: No es requereixen.
#-----------------------------------------------

for i in range(1, 7):
# La següent combinació permet:
# " " --> Representa espais en blanc.
# * --> multiplica (6 - 1), que calcula quants espais s'han de posar.
# "* " --> Representa una estrella.
# * i --> Repeteix les estrelles segons el valor de i.
# El primer multiplicador repeteix els espais per a centre l'arbre.
# El segon, repeteix les estrelles per a forma l'arbre. 
    print(" " * (6 - i) + "* " * i)
