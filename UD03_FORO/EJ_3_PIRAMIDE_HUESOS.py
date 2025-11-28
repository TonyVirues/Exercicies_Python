n = int(input("Escribeme un número :"))
altura = n

for i in range(1,altura):
     if i==1:
        print(" "*(altura-i)+" *"*(2*i-1))
     elif i==altura-1:
        print(" *"*altura)
     elif i==altura/2:
        print(" "*(altura-i)+" *"+"  "*(i-2)+" *")
     else:
        print(" "*(altura-i)+" *"+"  "*(i-2)+" *")