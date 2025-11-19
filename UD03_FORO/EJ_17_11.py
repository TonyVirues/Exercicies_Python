

#Ejercicio del foro
altura=int(input("Escribe un número"))


for i in range(1,altura+1):
    for j in range(i,altura+1):
        print("4",end="")
    print("*")
    
print("7")
for i in range(1,altura-1):
    print("4",end="")
    print(" "*(i-1),end="")
    print("4")
print("4"*altura)
