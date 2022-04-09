def is_even(numero):
    return numero % 2 == 0

numero = int(input("Ingrese un numero entero por favor o 0 para terminar la ejecucion: "))
while numero != 0:
    if is_even(numero):
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")
    numero = int(input("Ingrese un numero entero por favor o 0 para terminar la ejecucion: "))