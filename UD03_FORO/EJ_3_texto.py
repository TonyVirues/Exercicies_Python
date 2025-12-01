#Contar cuántas veces aparece un carácter dado en una cadena usando for y un contador.

cadena=input("Digame una palabra: ")
contador=0
letra=input("Indícame que letra quieres comprobar si se repite: ")

for i in cadena:
    if letra==i:
        contador+=1
    else:
        print()
print(f"La letra selecionada aparecio un total de {contador}")