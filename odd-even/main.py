def odd_even(numero):
    if numero % 2 == 0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")

numero = int(input("Ingrese un numero entero por favor: "))
odd_even(numero)