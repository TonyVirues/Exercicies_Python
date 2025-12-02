#Extraer subcadenas usando slicing (rebanado de cadenas sin usar listas).
cadena = input("Digame una palabra: ")
for i in cadena:
    print([i])

print(cadena[0])
print()
for i in range(len(cadena)):
    print(cadena[i:])