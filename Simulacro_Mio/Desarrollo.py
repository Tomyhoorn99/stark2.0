import json
from os import system

"""De una sala de videojuegos se tienen los siguientes datos:
 Id (debe comenzar en 1 y ser autoincremental)
 Aerolínea (AA, LATAM o IBERIA)
 Apellido_Nombre_Pasajero (Hasta de 30 caracteres)
 DNI_Pasajero
 Precio (Entre 500.000 y 2.000.000)
 Origen (Buenos Aires, Madrid, París, Miami, Roma o Tokio)
 Destino (Buenos Aires, Madrid, París, Miami, Roma o Tokio)
 Clase (Turista o Ejecutivo)
 Fecha (formato AAAAMMDD)


A Cargar el archivo data.json
Luego de la carga del archivo, realizar un menú de opciones que realice lo siguiente en 
memoria:
Realizar un menú de opciones que realice lo siguiente:

B Alta de datos con sus respectivas validaciones. [Id, Aerolínea, DNI (número), Precio, 
Origen, Destino, Origen y Destino distintos, Clase, Fecha (numero)].

C Modificar datos: Listar id y nombre de todos pasajes, luego buscarlo por id y realizar la 
modificación del DNI, apellido y nombre o la fecha (Realizar un submenú => “ej: Ingrese id, 
tipo y dato a modificar”).

D Borrar datos: Listar id y nombre de todos los pasajes, luego buscarlo por id y realizar la 
baja correspondiente.

E Listar todos los pasajes cuyo encabezado deberá ser formateado de la siguiente manera:
Fecha | Aerolínea | Clase | Origen | Destino | Precio | DNI | Apellido y nombre

F Salir
    """

# Realizar un menú de opciones
def imprimir_menu():
    print("A: cargar archivo json\n B:Alta de datos\n C:Modificar datos\n D:Borrar datos\n E:Listar todos los pasajeros\n F:Salir")

def menu_de_opciones():
    retorno = False # se una para almacenar la opcion valida
    imprimir_menu() # imprime las opciones del menú
    opcion = input("ingresa una Opcion") # el usuruario ingresa una Opcion y se guarda en la variable "opcion"
    if opcion.upper() >= "A" and opcion.upper <= "F": # valida la Opcion. el "upper" lo convierte en mayúscula
        retorno = opcion.upper() # se retorna la Opcion 
    return retorno


# def menu_principal():
#     retorno = False
#     imprimir_menu()  # Suponiendo que imprimir_menu() imprime las opciones del menú
#     opcion = input("Ingresa una opción: ").strip().upper()
#     # Validar la opción ingresada está dentro del rango 'A' a 'F'                           
#     if opcion in ['A', 'B', 'C', 'D', 'E', 'F']:
#         retorno = opcion
#     else:
#         print("Opción no válida. reingrese una opción de A a F.")
#     return retorno

# print(menu_principal())


def sub_menu():
    retorno = False
    imprimir_menu()
    opcion = input("Ingresa una opcion: ")
    if opcion.upper() >= "A" and opcion.upper() <= "F":
        retorno = opcion.upper()
    return retorno

def pausa():
    var = input("Presione Enter para continuar...")
    system ("cls")




























# A Cargar el archivo data.json.
def cargar_archivo(archivo:json, key):
    with open(archivo, "r") as archivo:
        data = json.load(archivo)
        print("Archivo cargado exitosamente")
    return(data[key])



# B Alta de datos con sus respectivas validaciones. [Id, Aerolínea, DNI (número), Precio, Origen, Destino, Origen y Destino distintos, Clase, Fecha (numero)]

def validar_nombre_apellido(nombre):
    if len(nombre) > 30:
        retorno = False
    else:
        for letra in nombre:
            if letra == " " or letra.isalpha():
                retorno = True
            else:
                retorno = False
                break
    return retorno



def validar_precio(precio):
    for i in precio:
        if i == "." or i.isnumeric():
            retorno = True
        else:
            retorno = False
            break
    return retorno

# print(validar_precio("123.456"))



def generador_id(archivo_cargado):
    nuevo_id = 0
    for pasajero in range(len(archivo_cargado)):
        for key in (archivo_cargado[pasajero]):
            if key == 'Id':
                id = archivo_cargado[pasajero][key]
                nuevo_id += 1
            if nuevo_id != id:
                return nuevo_id


def alta_datos(archivo_cargado):
    nuevo_id = generador_id(archivo_cargado)

    nuevo_aerolinea = input("Ingresa la aerolinea: ")
    while nueva_aerolinea != "AA" and nueva_aerolinea != "LATAM" and nueva_aerolinea != "IBERIA":
        nueva_aerolinea = input("Aerolinea invalida,reingresa la aerolinea: ")

    nuevo_nombre_apellido = input("Ingresa el nombre y apellido: ")
    while validar_nombre_apellido(nuevo_nombre_apellido) == False:
        nuevo_nombre_apellido = input("Nombre o apellido invalido,reingresa el nombre y apellido: ")

    nuevo_dni = input("Ingresa el dni: ")
    while len(nuevo_dni) != 8 and nuevo_dni.isnumeric() == False:
        nuevo_dni = input("Dni invalido,reingresa el dni: ")

    nuevo_precio = input("Ingresa el precio: ")
    while validar_precio(nuevo_precio) == False:
        nuevo_precio = input("Precio invalido,reingresa el precio: ")

    nuevo_origen = input("Ingresa el origen: ")
    while nuevo_origen == nuevo_destino:
        nuevo_origen = input("Origen y destino no pueden ser iguales,reingresa el origen: ")

    nuevo_destino = input("Ingresa el destino: ")
    while nuevo_origen == nuevo_destino:
        nuevo_destino = input("Origen y destino no pueden ser iguales,reingresa el destino: ")

    nuevo_clase = input("Ingresa la clase: ")
    while nueva_clase != "E" and nueva_clase != "B" and nueva_clase != "T":
        nueva_clase = input("Clase invalida,reingresa la clase: ")

    nueva_fecha = input("Ingresa la fecha de vuelo: ")
    while not nueva_fecha.isdigit() or len(nueva_fecha) != 8:
        nueva_fecha = input("Fecha invalida,reingresa la fecha: ")


    nuevo_pasajero = {
        "Id": nuevo_id,
        "Aerolinea": nuevo_aerolinea,
        "Apellido_Nombre_Pasajero": nuevo_nombre_apellido,
        "DNI_Pasajero": nuevo_dni,
        "Precio": nuevo_precio,
        "Origen": nuevo_origen,
        "Destino": nuevo_destino,
        "Clase": nuevo_clase,
        "Fecha": nueva_fecha
    }
    print("Alta exitosa")
    archivo_cargado.append(nuevo_pasajero)
    return archivo_cargado


'''C Modificar datos: Listar nuevo_id y nombre de todos pasajes, luego buscarlo por nuevo_id y realizar la modificación del DNI, apellido y nombre o la fecha (Realizar un submenú => “ej: Ingrese nuevo_id, tipo y dato a modificar”).'''

# Listar nuevo_id y nombre de todos pasajes
def listar_registro_id_nombre(archivo_cargado):
    for pasajero in range(len(archivo_cargado)):
        for key in (archivo_cargado[pasajero]):
            if key == 'Id':
                print(f'"ID" : {archivo_cargado[pasajero]['Id']} | "NOMBRE" : {archivo_cargado[pasajero]['Apellido_Nombre_Pasajero']}')


# luego buscarlo por nuevo_id y realizar la modificación del DNI, apellido y nombre o la fecha

def modificar_registro(archivo_cargado):
    opcion = input("Ingresa el ID del pasajero que quieres modificar: ")
    for pasajero in range(len(archivo_cargado)):
        for key in (archivo_cargado[pasajero]):
            if key == 'Id' and archivo_cargado[pasajero][key] == int(opcion): #
                opcion = input("Ingrese el tipo de dato a modificar: ")
                while opcion != "DNI" and opcion != "Nombre y Apellido" and opcion != "Nombre" and opcion != "Apellido" and opcion != "Fecha":
                    opcion = input("Dato invalido,reingresa el tipo de dato a modificar: ")

                if opcion == "DNI": 
                    nuevo_dni = input("Ingresa el nuevo dni: ")
                    while len(nuevo_dni) != 8 and nuevo_dni .isnumeric() == False:
                        nuevo_dni = input("Dni invalido,reingresa el dni: ")
                        archivo_cargado[pasajero]['DNI_Pasajero'] = nuevo_dni
                        print("Modificación exitosa")

                elif opcion == "Nombre y Apellido" or opcion == "Nombre" or opcion == "Apellido":
                    nuevo_nombre_apellido = input("Ingresa el nuevo nombre y apellido: ")
                    while validar_nombre_apellido(nuevo_nombre_apellido) == False:
                        nuevo_nombre_apellido = input("Nombre o apellido invalido,reingresa el nombre y apellido: ")
                    archivo_cargado[pasajero]['Apellido_Nombre_Pasajero'] = nuevo_nombre_apellido
                    print("Modificación exitosa")

                elif opcion == "Fecha":
                    nueva_fecha = input("Ingresa la fecha de vuelo: ")
                    while not nueva_fecha.isdigit() or len(nueva_fecha) != 8:
                        nueva_fecha = input("Fecha invalida,reingresa la fecha: ")
                    archivo_cargado[pasajero]['Fecha'] = nueva_fecha
                    print("Modificación exitosa")
                
                return archivo_cargado
   

'''D – Borrar datos: Listar nuevo_id y nombre de todos los pasajes, luego buscarlo por nuevo_id y realizar la baja correspondiente.'''



                    
                    




























