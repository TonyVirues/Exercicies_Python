#Convertir todas las letras a mayúsculas o minúsculas usando ciclos y sumas de caracteres (sin usar los métodos upper() o lower()).

cadenaMayus = "caracola"
cadenaLower = ""

for i in range (len(cadenaMayus)):
    cadenaMayus += chr(ord(cadenaLower[i])-32)
print(cadenaMayus)
