#Construir manualmente una nueva cadena añadiendo un carácter a la vez(ejemplo:filtrar caracteres o construir cadenas invertidas).

tamaño = int(input("Cuantas letras tendra su palabra: "))
cadena= ""
nuevaCadena=""
for i in range(tamaño):
    letra = input("Comience a deletrear: ")
    cadena = cadena[:i] + letra
print(cadena)

#filtración

n = int(input("Dime la posición para enseñarte la letra y filtrarla: "))
for i in range(len(cadena)):
    if i==n:
        print(cadena[i])
    else:
        print()

#Invertida

for i in range(len(cadena)):
    nuevaCadena=nuevaCadena+cadena[-i-1]
print(nuevaCadena)