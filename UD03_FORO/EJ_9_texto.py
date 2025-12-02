#Leer una cadena y contar cuántos caracteres son letras mayúsculas.

cadena = input("Dígame una palabra: ")
contador = 0
for i in cadena:
    if i.isupper():
        contador +=1
    else:
        print()
print(f"Hay {contador} palabras en mayúsculas")
print()