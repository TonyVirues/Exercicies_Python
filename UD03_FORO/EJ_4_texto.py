#Construir manualmente una nueva cadena añadiendo un carácter a la vez(ejemplo:filtrar caracteres o construir cadenas invertidas).

tamaño = int(input("Cuantas letras tendra su palabra: "))
cadena= ""

for i in range(tamaño):
    letra = input("Comience a deletrear: ")
    cadena = cadena[:i] + letra
print(cadena)