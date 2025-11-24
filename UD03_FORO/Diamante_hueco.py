#imprime un rombo sólido de altura 2n-1, centrado, usando asteriscos
altura =5

for i in range(1,altura):
    for j in range(i,altura,2):
            print("*",end=" ")
    print("")

#otra figura
for i in range(altura,0,-1):
    print(" "*(altura-i)+"*"*(2*i-1))

#otra figura
for i in range(1,altura+1):
     print(" "*(altura-i)+"*"*(2*i-1))


for i in range(1,altura+1):
    if i==1:
        print(" *")
    elif i==altura:
         print(" *"*i)
    else:
         print(" *"+"  "*(i-2)+" *")
#otra figura
for i in range(altura-1,0,-1):
    print(" "*(altura-i)+"*"*(2*i-1))
