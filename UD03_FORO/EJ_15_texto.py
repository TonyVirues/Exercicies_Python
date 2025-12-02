#Dada una cadena, construir una nueva cadena donde cada vocal se reemplaza por un asterisco '*'.

cadena = input("Dígame una palabra: ")
asterisco = "*"
vocales = "aeiouAEIOU"
nuevaCadena = ""
for i in cadena:
    if i in vocales:
        nuevaCadena += asterisco
    else:
        nuevaCadena += i
print(nuevaCadena)