#Leer una cadena y construir una nueva cadena con los caracteres en orden inverso.

cadena = input("Dígame una palabra: ")
nuevaCadena = ""

for i in range(len(cadena)):
    nuevaCadena=nuevaCadena+cadena[-i-1]
print(nuevaCadena)