#Ejercicio 13
num=1
altura=int(input("Escriba un número :"))
for i in range(altura+1):
    num=1
    for j in range(i):
        print(num, end="")
        num=num+1
    print("")