#---------------------------------------------------
# Programa: Mostrar les vocals que conté una frase.
# Autor: Albert Pie Santamaria
# Curs: 1rº asix
# Data: 2 / 11 / 2026
#
# Especificacions d'entrada: Una cadena de text.
#--------------------------------------------------

cadena = input("Introdueix una frase: \n")
# Convertim la frase a minúscules per a evitar comprovar per separat les vocals, si són minúscula o majúscula.
text_minuscules = cadena.lower()
vocals = "aeiou"
contador = 0

# El següent bucle va recorrent cada lletra del text, comprovant si la lletra actual esta dins la variable vocals.
for lletra in text_minuscules:
    if lletra in vocals:
# Sumem 1 al contador a cada ronda per a portar un compte del total.
        contador += 1

print("La quantitat de vocals que conté la frase és:", contador)
