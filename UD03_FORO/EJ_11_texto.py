#Construir una nueva cadena con todos los caracteres de la cadena original, pero duplicando cada vocal.

cadena = input("Dígame una palabra: ")
vocales = "aeiouAEIOU"
nuevaCadena = ""

for i in cadena:
    if i in vocales:
        nuevaCadena = nuevaCadena + (i)*2
    else:
        nuevaCadena += i
        print()
print(nuevaCadena)