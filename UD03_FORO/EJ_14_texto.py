#Leer una cadena y contar cuántos caracteres numéricos ('0' a '9') contiene.

cadena = input("Dígame una palabra: ")
numeros = "0123456789"
contador = 0

for i in cadena:
    if i in numeros:
        contador += 1
    else:
        print()
print(f"Los números aparecen en un total de {contador} veces.")