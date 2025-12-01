#verificar si un carácter especifico esta en la cadena con un ciclo y comparaciones.
cadena = input("Digame la palabra: ")
letra = input("Que caracter quieres comprobar si se encuentra")
contador = 0
for i in cadena:
    if letra==i:
        contador+=1
    else:
        print()
print(f"La letra selecionada aparecio un total de {contador} veces ")