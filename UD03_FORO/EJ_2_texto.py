#Concatenar caracteres o cadenas utilizando el operador + para formar nuevas cadenas.
cadena=input("Digame algo: ")
agregar=input("¿Qué letra quieres agregar?: ")
posicion=int(input("¿En que posición?: "))

cadena = agregar + cadena[posicion:]
print(cadena)