#Leer una cadena y eliminar todos los espacios, construyendo una cadena continua.

cadena = input("Dígame una palabra con espacios: ")
papelera = ""
eliminarEspacios = ""

for i in cadena:
    if i==" ":
        papelera += i
    else:
        eliminarEspacios += i
print(eliminarEspacios)