altura=5
#triangulos vacios. 

for i in range(1,altura+1):
    if i==1:
        print(" *")
    elif i==altura:
         print(" *"*i)
    else:
         print(" *"+"  "*(i-2)+" *")

print("<----->")

for i in range(altura,0,-1):
    if i==altura:
        print(" *"*i)
    elif i==1:
        print(" *")
    else:
        print(" *"+"  "*(i-2)+" *")
print("<------>")
for i in range (1,altura+1):
    if i==1:
        print(" "*(altura+3)+" *")
    elif i==altura:
        print(" *"*i)
    else:
        print("  "*(altura-i)+" *"+" "*(i)+" *")

print("<--Dibujo del profe-->")
for i in range(1,altura+1):
        for j in range(i, altura):
            print(" ", end="")
        for k in range(1, 2):
            print("*",end="")
        for j in range(1,i):
            print(" ", end="")
        print("*")