#Imprime una estrella de ocho puntas combinando lineas verticales, horizontales y diagonales con asteriscos en una matriz de tamaño impar n x n 
#Figura para n=9

altura = 4
for i in range(altura):
    if i==0:
        print("*"+(" "*(altura-i))+"*"+(" "*(altura-i))+"*")
    else:
        print((" "*i)+"*"+(" "*(altura-i))+"*"+(" "*(altura-i))+"*")
for i in range(altura,-1,-1):
    if i==altura:
       print("*"*(altura+i))
    else:
        print((" "*i)+"*"+(" "*(altura-i))+"*"+(" "*(altura-i))+"*")

#Probar con matriz. Usando for i y for j.