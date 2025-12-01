# Programa que lee una secuncia de notas (con valores que van de 0 a 10) que termina con el valor -1 y nos dice si hubo o no algunanota con valor 10.
nota=int(input("Dime su nota :"))
valor=False
while (nota!=-1):
    if nota==10:
        valor=True
        nota=int(input("Dime una nota :"))
    else:
        nota=int(input("Dime una nota :"))
if valor==True:
    print("Existe alguna nota con 10 ")
else:
    print("no existe nota con 10")
