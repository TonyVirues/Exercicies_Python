#Ejercicio 8: Rombo sólido
#Imprime un rombo sólido de altura 2n-1,centrado usando asteriscos. figura para n=4
n = int(input("Escribe un número :"))
altura = 2*n-1
for i in range(1,altura):
     print(" "*(altura-i)+"*"*(2*i-1))
for i in range(altura,0,-1):
    print(" "*(altura-i)+"*"*(2*i-1))