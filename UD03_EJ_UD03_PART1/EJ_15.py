n_1=float(input("Escriba el primer número :"))
n_2=float(input("Escriba el segundo número :"))
n_3=float(input("Escriba el tercer número :"))
if n_1>n_2:
    if n_1==n_2:
        if n_2>n_3:
            print(f"{n_1} y {n_2} Son iguales")
            print(f"{n_3}Es mas pequeño")
        else:
            print(f"{n_3}Es el mayor")
            print(f"{n_1} y {n_2} Son iguales")
    elif n_2>n_3:
        print(f"{n_1}Es el mayor")
        print(f"{n_2}Es el mediano")
        print(f"{n_3}Es el pequeño")
    else:
        print(f"{n_1}Es el mayor")
        print(f"{n_3}Es el mediano")
        print(f"{n_2}Es el pequeño")
elif n_2>n_3:
    if n_3>n_1:
        print(f"{n_2}Es el mayor")
        print(f"{n_3}Es el mediano")
        print(f"{n_1}Es el pequeño")
    else:
        print(f"{n_2}Es el mayor")
        print(f"{n_1}Es el mediano")
        print(f"{n_3}Es el pequeño")
elif n_3>n_1:
    if n_1>n_2:
        print(f"{n_3}Es el mayor")
        print(f"{n_1}Es el mediano")
        print(f"{n_2}Es el pequeño")
    else:
        print(f"{n_3}Es el mayor")
        print(f"{n_2}Es el mediano")
        print(f"{n_1}Es el pequeño")
elif n_1==n_2:
    if n_2==n_3:
        print("Todos los números son iguales")
    else:
        print("Uno y dos son iguales pero 3 no")
else:
    print("sigue probando")