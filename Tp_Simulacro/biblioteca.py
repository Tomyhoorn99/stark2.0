import json
from os import system

def imprimir_menu():
    print("A – Cargar archivo.\nB – Alta de datos.\nC – Modificar datos.\nD – Borrar datos.\nE – Listar todos los pasajeros\nF – Salir")

def menu_principal():
    retorno = False 
    imprimir_menu()
    opcion = input("Ingresa una opcion: ")
    if opcion.upper() >= "A" and opcion.upper() <= "F": 
        retorno = opcion.upper()
    return retorno

    # def menu_principal():
    # retorno = False
    # imprimir_menu()  # Suponiendo que imprimir_menu() imprime las opciones del menú

    # opcion = input("Ingresa una opción: ").strip().upper()

    # # Validar la opción ingresada está dentro del rango 'A' a 'F'                            #otra opcion
    # if opcion in ['A', 'B', 'C', 'D', 'E', 'F']:
    #     retorno = opcion
    # else:
    #     print("Opción no válida. reingrese una opción de A a F.")

    # return retorno



def pausa():
    var = input("Presione Enter para continuar...")
    system ("cls")

def aeropuerto_app(archivo_json):
    continuar = True
    carga = False
    while continuar:
        opcion = menu_principal()
        system('cls')
        if opcion == "A":
            """A – Cargar archivo."""
            archivo_cargado = cargar_archivo(archivo_json, 'pasajeros')
            carga = True
            pausa()    
        elif carga == False:
            print("No se cargo el archivo")
            pausa()
        elif carga == True:
            match(opcion):
                case "B":
                    """B – Alta de datos con sus respectivas validaciones. [Id, Aerolínea, DNI (número), Precio, Origen, Destino, Origen y Destino distintos, Clase, Fecha (numero)]."""
                    alta_datos(archivo_cargado)
                case "C":
                    """C – Modificar datos: Listar nuevo_id y nombre de todos pasajes, luego buscarlo por nuevo_id y realizar la modificación del DNI, apellido y nombre o la fecha"""
                    listar_registro_id_nombre(archivo_cargado)
                    modificar_registro(archivo_cargado)
                case "D":
                    """D – Borrar datos: Listar nuevo_id y nombre de todos los pasajes, luego buscarlo por nuevo_id y realizar la baja correspondiente."""
                    listar_registro_id_nombre(archivo_cargado)
                    baja_datos(archivo_cargado)
                case "E":
                    """E – Listar todos los pasajes cuyo encabezado deberá ser formateado de la siguiente manera: día | Aerolínea | Clase | Origen | Destino | Precio | DNI | Apellido y nombre"""
                    listar_registro_completo(archivo_cargado)
                case "F":
                    """F – Salir"""
                    alta(archivo_cargado, archivo_json)
                    print("Saliendo...")
                    continuar = False
                case _:
                    print("Opcion invalida")
            pausa()

'''A – Cargar el archivo data.json.'''
def cargar_archivo(archivo_json:json, key):
    with open(archivo_json, "r") as archivo:
        data = json.load(archivo)
        print("Archivo cargado exitosamente")
    return(data[key])

'''B – Alta de datos con sus respectivas validaciones. [Id, Aerolínea, Nombre y apellido, DNI (número), Precio, Origen, Destino, Origen y Destino distintos, Clase, Fecha (numero)].'''
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
    while nuevo_aerolinea != "AA" and nuevo_aerolinea != "LATAM" and nuevo_aerolinea != "IBERIA":
        nuevo_aerolinea = input("Aerolinea invalida,reingresa la aerolinea: ")
    nuevo_nombre_apellido = input("Ingresa el nombre y apellido: ")
    while validar_nombre_apellido(nuevo_nombre_apellido) == False:
        nuevo_nombre_apellido = input("Nombre o apellido invalido,reingresa el nombre y apellido: ")
    nuevo_dni = input("Ingresa el dni: ")
    while len(nuevo_dni) != 8 and nuevo_dni.isnumeric() == False:
        nuevo_dni = input("Dni invalido,reingresa el dni: ")
    nuevo_precio = input("Ingresa el precio: ")
    while validar_precio(nuevo_precio) == False or float(nuevo_precio) < 500000 or float(nuevo_precio) > 2000000:
        nuevo_precio = input("Precio invalido,reingresa el precio: ")
    nuevo_origen = input("Ingresa el origen: ")
    while nuevo_origen != "Buenos Aires" and nuevo_origen != "Madrid" and nuevo_origen != "París" and nuevo_origen != "Miami" and nuevo_origen != "Roma" and nuevo_origen != "Tokio":
        nuevo_origen = input("Origen invalido,reingresa el origen: ")
    nuevo_destino = input("Ingresa el destino: ")
    while nuevo_destino != "Buenos Aires" and nuevo_destino != "Madrid" and nuevo_destino != "París" and nuevo_destino != "Miami" and nuevo_destino != "Roma" and nuevo_destino != "Tokio" or nuevo_origen == nuevo_destino:
        nuevo_destino = input("Destino invalido,reingresa el destino: ")
    nuevo_clase = input("Ingresa la clase: ")
    while nuevo_clase != "Turista" and nuevo_clase != "Ejecutivo":
        nuevo_clase = input("Clase invalida,reingresa la clase: ")
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

def alta(archivo_cargado, archivo_json):
    data = {"pasajeros": archivo_cargado}
    with open (archivo_json, "w") as archivo:
        json.dump(data, archivo, indent=4, ensure_ascii=False )



'''C – Modificar datos: Listar nuevo_id y nombre de todos pasajes, luego buscarlo por nuevo_id y realizar la modificación del DNI, apellido y nombre o la fecha (Realizar un submenú => “ej: Ingrese nuevo_id, tipo y dato a modificar”).'''

def listar_registro_id_nombre(archivo_cargado):
    for pasajero in range(len(archivo_cargado)):
        for key in (archivo_cargado[pasajero]):
            if key == 'Id':
                print(f'"ID" : {archivo_cargado[pasajero]['Id']} | "NOMBRE" : {archivo_cargado[pasajero]['Apellido_Nombre_Pasajero']}')

def modificar_registro(archivo_cargado):
    opcion = input("Ingresa el ID del pasajero que quieres modificar: ")
    for pasajero in range(len(archivo_cargado)):
        for key in (archivo_cargado[pasajero]):
            if key == 'Id' and archivo_cargado[pasajero][key] == int(opcion):
                opcion = input("Ingrese el tipo de dato a modificar: ")
                while opcion != "DNI" and opcion != "Nombre y Apellido" and opcion != "Nombre" and opcion != "Apellido" and opcion != "Fecha":
                    opcion = input("Dato invalido,reingresa el tipo de dato a modificar: ")
                if opcion == "DNI":
                    nuevo_dni = input("Ingresa el nuevo dni: ")
                    while len(nuevo_dni) != 8 and nuevo_dni.isnumeric() == False:
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

def baja_datos(archivo_cargado):
    opcion = input("Ingresa el ID del pasajero que quieres dar la baja: ")
    for pasajero in range(len(archivo_cargado)):
        for key in (archivo_cargado[pasajero]):
            if key == 'Id' and archivo_cargado[pasajero][key] == int(opcion):
                del archivo_cargado[pasajero]
                print("Baja exitosa")
                return archivo_cargado
            
"""E – Listar todos los pasajes cuyo encabezado deberá ser formateado de la siguiente manera: Fecha | Aerolínea | Clase | Origen | Destino | Precio | DNI | Apellido y nombre."""

def listar_registro_completo(archivo_cargado):
    print("    Fecha   | Aerolinea  |   Clase    |   Origen   |  Destino   |   Precio   |    DNI     | Apellido y nombre")
    keys = ["Fecha", "Aerolinea", "Clase", "Origen", "Destino", "Precio", "DNI_Pasajero", "Apellido_Nombre_Pasajero"]
    lista_datos = []
    for pasajero in archivo_cargado:
        for key in keys:
            lista_datos.append(pasajero[key])
        mensaje = ""
        mensaje += f"  {lista_datos[0]}  |"
        for i in range(1, len(lista_datos)-1):
            if len(lista_datos[i]) == 2:
                mensaje += f"     {lista_datos[i]}     |"
            elif len(lista_datos[i]) == 4:
                mensaje += f"    {lista_datos[i]}    |"
            elif len(lista_datos[i]) == 5:
                mensaje += f"    {lista_datos[i]}   |"
            elif len(lista_datos[i]) == 6:
                mensaje += f"   {lista_datos[i]}   |"
            elif len(lista_datos[i]) == 7:
                mensaje += f"  {lista_datos[i]}   |"   
            elif len(lista_datos[i]) == 8:
                mensaje += f"  {lista_datos[i]}  |"
            elif len(lista_datos[i]) == 9:
                mensaje += f" {lista_datos[i]}  |"
            elif len(lista_datos[i]) == 10:
                mensaje += f" {lista_datos[i]} |"
            elif len(lista_datos[i]) == 12:
                mensaje += f"{lista_datos[i]}|"
        mensaje += f"{lista_datos[7]}"
        print(mensaje)
        lista_datos.clear()
