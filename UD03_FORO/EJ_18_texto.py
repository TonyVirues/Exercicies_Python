#Leer una cadena y construir una nueva cadena dejando sólo los caracteres que son consonantes (sin listas, usando condiciones y concatenación).

cadena = input("Dígame una palabra: ")
vocales = "aeiouAEIOU"
nuevaCadena = ""
papelera = ""

for i in cadena:
    if i in vocales:
        papelera += i
    else:
        nuevaCadena += i
print(nuevaCadena)