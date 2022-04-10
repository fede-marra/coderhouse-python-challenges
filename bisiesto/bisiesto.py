def bisiesto(year):
    if int(year) % 4 == 0 and int(year) % 100 != 0:
        return True
    elif int(year) % 4 == 0 and int(year) % 400 == 0:
        return True
    else:
        return False

year = input("\n Ingrese un año para saber si es bisiesto o 0 para salir: ")
while not year == "0":
    if not year.isnumeric():
        print("\n Ingrese el año en numeros \n")
    else:
        if bisiesto(year) is True:
            print(F"\n El año {year} es un año bisiesto \n")
        else:
            print(f"\n El año {year} no es un año bisiesto \n")
    year = input("Ingrese un año para saber si es bisiesto o 0 para salir: ")