#Ejercicio 15
#vamos a darle la vuelta
for i in range(1,altura+1):
    for j in range(0,i-1):
        print(" ",end="")
    #vamos a construir los asteriscos
    for k in range(1,(2*altura+1)-(i*2)):
        print("*",end="")
    print("")