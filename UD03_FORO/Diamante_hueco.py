#Imprime un diamante hueco de altura total 2n-1, centrado con asteriscos, donde solo se imprimen los bordes y el centro. 
#Figura para n=5
n = int(input("Escribe un número :"))
altura = 2*n-1

for i in range(1,altura):
     if i==1:
          print(" "*(altura-i)+" *"*(2*i-1))
     else:
           print(" "*(altura-i)+" *"+"  "*(i-2)+" *")
for i in range(altura,0,-1):
     if i==1:
           print(" "*(altura-i)+" *"*(2*i-1))
     else:
          print(" "*(altura-i)+" *"+"  "*(i-2)+" *")
