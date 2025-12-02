#Leer una cadena y crear una nueva donde sólo aparezcan los caracteres que se repiten más de una vez.

cadena = input("Dígame una palabra: ")
letraRepetida = ""
contador = 0
nuevaCadena = ""
#Pura tecnologia
for i in cadena:
    contador = 0
    for j in cadena:
        if i == j:
            contador += 1
            if contador>=2:
                nuevaCadena += i
                contador = 0
        else:
            print("")
print(nuevaCadena)

#Sencillo
for i in cadena:
    if cadena.count(i) > 1:
        nuevaCadena += i
print(nuevaCadena)