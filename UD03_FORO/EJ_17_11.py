#Ejercicio del foro
#Primera figura
altura=int(input("Escribe un número"))
print("4")
for i in range(1,altura-1):
    print("4",end="")
    print(" "*(i-1),end="")
    print("4")
print("4"*altura)
#Figura dos
#----------------no me sale--------------------->
for i in range(1,altura):
    if i!=altura:
        print(" ",end="")
    else:
        print("*")