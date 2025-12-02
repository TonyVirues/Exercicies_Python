#triangulo
altura = int(input("Digame un número: "))
for i in  range (altura):
    print(" *"*altura)



for i in range(altura+1):
    print(" "*(altura-i) + " *"*i)
for i in range(altura,0,-1):
    print(" "*(altura-i) + " *"*i)

print("espacio espacio")
for i in range(1,altura+1):
     print(" "*(altura-i)+"*"*(2*i-1))
print("espacio espacio espacio")


for i in range (altura,0,-1):
    print("  "*(altura-i) + " *"*i) #por un espacio mas haces un triangulo en vez de la piramide
mitad = altura//2
print("que bien me sale no?")
for i in range(altura,0,-1):
    if (i==altura-1):
        print(" ."*altura)
    elif (i==mitad):
        print(" *"*altura)
    else:
        print(" ."*(altura-i) + (" *"*i) + "."+" *"*i+(" .") )
        
