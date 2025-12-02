#verificar si un carácter especifico esta en la cadena con un ciclo y comparaciones.

cadena = input("Digame la palabra: ")
letra = input("Que caracter quieres comprobar si se encuentra: ")
contador = 0
bandera = False
for i in cadena:
    if letra==i:
        bandera = True
        contador+=1
    else:
        print("")
if bandera==True:
    print(f"La letra selecionada aparecio. Un total de {contador} veces.")
else:
    print("La letra introducida nose encuentra en la cadena.")