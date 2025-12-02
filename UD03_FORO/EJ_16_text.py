#Leer dos cadenas y concatenarlas manualmente sin usar el operador + en una sola operación (concatenar carácter a carácter con un ciclo).

cadena = input("Dígame una palabra: ")
cadena2 = input("Dígame una segunda palabra: ")
nuevaCadena = ""

for i in cadena," ",cadena2:
    nuevaCadena += i
print(nuevaCadena)