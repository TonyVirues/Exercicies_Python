altura =int(input("Escribe un número"))
#ejercicio 14
for i in range(1,altura+1):
    #vamos a construir los espacios
    for j in range(i,altura):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print("")