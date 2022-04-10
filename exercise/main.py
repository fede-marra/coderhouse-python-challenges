from curses.ascii import isdigit


base_de_datos = {}

opciones = {
    "ALTA": "Ingrese ALTA para crear un nuevo usuario",
    "BAJA": "Ingrese BAJA para eliminar datos de un usuario",
    "MODIFICAR": "Ingrese MODIFICAR para modificar datos de un usuario",
    "BUSCAR": "ingrese BUSCAR para encontrar un usuario ya creado",
    "SALIR": "Ingese SALIR para terminar la ejecucion del programa"
}

def display_menu():
    for key, value in opciones.items():
        print(f"{key} - {value}")

def user_is_valid(user):
    return len(user) > 5 and not isdigit(user[0])
        

def age_is_valid(age):
    return isinstance(age, int) and age > 0 

def password_is_valid(password):
    return len(password) == 3 and ("#" in password or "?" in password) 

def is_equal(a, b):
    return a == b


display_menu()
opcion = input("Ingrese la opcion deseada: ")

while opcion.upper() in opciones.keys():
    if opcion.upper() == "SALIR":
        break
    elif opcion.upper() == "ALTA":
        usuario = input("\n Ingrese su nombre de usuario, el usuario debe contener al menos 6 caracteres : ")
        if not user_is_valid(usuario):
            print("Usuario invalido, el usuario debe contener al menos 6 caracteres")

        nombre = input("\n Ingrese su nombre por favor: ")

        edad = int(input("\n Ingrese su edad por favor: "))
        if not age_is_valid(edad):
            print("Edad invalida, la edad debe ser un numero entero positivo")
        
        password = input("\n Ingrese su contraeña, la contraseña debe ser de 3 caracters y contener al menos un caracter '#' o '?': ")
        password_repite = input("\n Repita su contraseña: ")
        if not password_is_valid(password):
            print("Password invalido, el mismo debe ser de 3 caracters y contener al menos un caracter '#' o '?': ")
        if not is_equal(password, password_repite):
            print("Las contraseñas deben ser iguales")

        base_de_datos.update({usuario: {"nombre" : nombre, "edad":edad,"contrasena":password}})
        print(base_de_datos)
    display_menu()
    opcion = input("Ingrese la opcion deseada: ")



   
#    form_valido = True

#    if len(usuario) <= 6:
#     print ("\n Error Usuario tiene que tener mas de 6 caracteres\n")
#     form_valido = False

#    if usuario[0] in str(set(range(0,10))):
#     print ("\n Error no puede empezar con un numero \n")
#     form_valido = False
#    if usuario in base_de_datos:
#      print ("\n El usuario no se puede repetir \n")
#      form_valido = False
#    if len(nombre) < 3:
#      print ("\n El nombre no puede ser menor a 3 caracteres\n ")
#      form_valido = False

#    if edad_temp.count(".") > 0 or edad_temp.count(",") > 0:
#      print ("\n La edad debe ser un numero intero \n")
#      form_valido = False
#    else:
#      edad = int(edad_temp)

#    if not(len(password) == 3):
#     print ("\n Error la contraseña tiene que ser igual a 3 caracteres \n")
#     form_valido = False
#    b = []
#    valido = 0
#    for x in range(len(password)):
#     b.append(x)
#     c = int(b[x])
#     if password[c] in ["#","?"]:
#      valido += 1
#    if valido == 0:
#     print ("\n Contraseña no tiene caracter especial \n")
#     form_valido = False

#    if password != password_repite:
#     print ("\n La contraseña no se repite \n")
#     form_valido = False

#    if form_valido:
#      print ("\n El Formulario es valido \n")
#      base_de_datos.update({usuario: {"nombre" : nombre, "edad":edad,"contrasena":password}})
#      print (base_de_datos)
#      print("")
#    else:
#     print ("\n El Formulario no es valido \n")
  
#   elif opcion.upper() == "BAJA":
#     baja = input("Ingrese el nombre de usuario que desea eliminar: ")
#     if baja in base_de_datos:
#       del base_de_datos[baja]
#       print (f"\n El usuario {baja} ha sido eliminado con exito \n")
#     else:
#       print ("\n El usuario que desea eliminar no existe \n")
  
#   elif opcion.upper() == "MODIFICAR":
#     print (base_de_datos)
#     modifica = input("\n Ingrese el nombre de usuario que desea modificar: ")
#     datos = base_de_datos[modifica]
#     dato = input("\n Ingrese el dato que desae modificar: \n")
#     if dato.upper() == "EDAD":
#       info = input("Ingrese el valor deseado: ")
#       base_de_datos = {modifica: {"nombre":datos["nombre"],"edad":info,"contrasena":datos["contrasena"]}}
#     if dato.upper() == "NOMBRE":
#       info = input("Ingrese el valor deseado: ")
#       base_de_datos = {modifica: {"nombre":info,"edad":datos["edad"],"contrasena":datos["contrasena"]}}
#     if dato.upper() == "CONTRASEÑA":
#       info = input("Ingrese el valor deseado: ")
#       flag = 0
#       if not(len(info) == 3):
#         print ("\n Error la contraseña tiene que ser igual a 3 caracteres \n")
#         flag = 1
#       valido = 0
#       for x in range(len(password)):
#         b.append(x)
#         c = int(b[x])
#       if password[c] in ["#","?"]:
#         valido += 1
#       if valido == 0:
#         print ("\n Contraseña no tiene caracter especial \n")
#         flag = 1
#       if not (flag == 0):
#         base_de_datos = {modifica: {"nombre":datos["nombre"],"edad":datos["edad"],"contrasena":info}}
#       else:
#         print ("/n La contraseña no cumple los requerimientos de seguridad /n")
#     print (base_de_datos)
#   elif opcion.upper() == "BUSCAR":
#     busca = input("Ingrese el usuario que desea encontrar: ")
#     if busca in base_de_datos:
#       print (f"\n El usuario {busca} tiene los siguientes datos: \n")
#       print (base_de_datos[busca])
#     else:
#       print (f"\n El usuario {busca}, no existe \n")



def read_data(data, validator, mensaje, mensaje_error):
    while not validator(data):
        data = input(mensaje)
    return data


read_data(password, password_is_valid, mensaje)


if alta:
    new_user = {
        usuario: {
            nombre: read_data()
        }
    }
    db.update(new_user)