#Reemplazar un carácter por otro recorriendo la cadena y concatenando a una nueva cadena.

cadena = input("Digame una palabra: ")
letra = input("Digame la letra que deseas agregar: ")
posicion = int(input("En que posicion quieres colocar la nueva letra: "))
resultado = ""
for i in range (len(cadena)):
    if i==posicion:
        resultado += letra
    else:
        resultado += cadena[i]
        print()
print(resultado)

