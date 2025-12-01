n = int(input("Escribeme un número :"))
altura = n
mitad=(altura//2)+1
for i in range(1,altura):
     if i==1:
        print(" "*(altura-i)+" *"*(2*i-1))
     elif i==altura-1:
        print(" *"*altura)
     elif i==mitad:
        print(" "*(altura-i)+" *"*i)
     else:
        print(" "*(altura-i)+" *"+"  "*(i-2)+" *")