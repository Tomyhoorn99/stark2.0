import json
from os import system

'''
Apellido y nombre: Hoorn Tomas Gonzalo
Division: 313-1
'''

def imprimir_menu():
    print("A – Cargar archivo.\nB – Alta de datos.\nC – Modificar datos.\nD – Borrar datos.\nE – Listar todos los pasajeros\nF – Otro\nG – Salir")

def menu_principal():
    retorno = False
    imprimir_menu()
    opcion = input("Ingresa una opcion: ")
    if opcion.upper() >= "A" and opcion.upper() <= "F":
        retorno = opcion.upper()
    return retorno

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
                    """F – Hacer un submenú que realice lo siguiente:"""
                    continuar_submenu = True
                    copia_flag = False
                    dato_flag = False
                    while continuar_submenu:
                        print("1 - Listar pasajes de mayor y menor precio\n2 - Cantidad de pasajeros por destino\n3 - Listar pasajes por fecha \n4 - Exportar a JSON\n5 - Exportar a CSV\n6 - Volver al menu principal")
                        sub_menu = input("Ingresa una opcion: ")
                        match(sub_menu):
                            case "1":
                                """1 - Listar por pantalla los pasajes de menor y mayor precio."""

                                dato = max_min(archivo_cargado)
                                listar_max_min(archivo_cargado, dato[0], dato[1])
                                dato_flag = True
                                
                            case "2":
                                """2 - Calcular y mostrar la cantidad de pasajes de un destino determinado, el mismo será ingresado por el usuario por consola."""
                                cantidad_pasajeros_destino(archivo_cargado)
                            case "3":
                                """3 - Listar los pasajes ordenados por Fecha. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’). Este ítem debe ser realizado por el algoritmo de ordenamiento bubble sort (burbujeo)."""
                                copia = listar_por_fecha(archivo_cargado)
                                (listar_registro_completo(copia))
                                copia_flag = True
                            case "4":
                                """4 - Exportar a JSON la lista de pasajes, de acuerdo a la información F 3."""
                                if copia_flag == True:
                                    imput = input("Ingresa el nombre del archivo: ")
                                    nuevo_json = imput
                                    guardar_json(nuevo_json ,copia)
                                else:
                                    print("No se genero el archivo")
                                
                            case "5":
                                """5 - Exportar a CSV la lista de pasajes, de acuerdo a la información F 1."""
                                if dato_flag == True:
                                    nombre = input("Ingresa el nombre del archivo: ")
                                    generar_csv(nombre,dato)
                                else:
                                    print("No se genero el archivo")
                            case "6":
                                continuar_submenu = False
                            case _ :
                                print("Opcion invalida")
                        pausa()
                case "G":
                    continuar = False
                case _ :
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
    for pasajero in precio:
        if pasajero == "." or pasajero.isnumeric():
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

'''C Modificar datos: Listar nuevo_id y nombre de todos pasajes, luego buscarlo por nuevo_id y realizar la modificación del DNI, apellido y nombre o la fecha (Realizar un submenú => “ej: Ingrese nuevo_id, tipo y dato a modificar”).'''

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
        for pasajero in range(1, len(lista_datos)-1):
            if len(lista_datos[pasajero]) == 2:
                mensaje += f"     {lista_datos[pasajero]}     |"
            elif len(lista_datos[pasajero]) == 4:
                mensaje += f"    {lista_datos[pasajero]}    |"
            elif len(lista_datos[pasajero]) == 5:
                mensaje += f"    {lista_datos[pasajero]}   |"
            elif len(lista_datos[pasajero]) == 6:
                mensaje += f"   {lista_datos[pasajero]}   |"
            elif len(lista_datos[pasajero]) == 7:
                mensaje += f"  {lista_datos[pasajero]}   |"   
            elif len(lista_datos[pasajero]) == 8:
                mensaje += f"  {lista_datos[pasajero]}  |"
            elif len(lista_datos[pasajero]) == 9:
                mensaje += f" {lista_datos[pasajero]}  |"
            elif len(lista_datos[pasajero]) == 10:
                mensaje += f" {lista_datos[pasajero]} |"
            elif len(lista_datos[pasajero]) == 12:
                mensaje += f"{lista_datos[pasajero]}|"
        mensaje += f"{lista_datos[7]}"
        print(mensaje)
        lista_datos.clear()

"""
F – Hacer un submenú que realice lo siguiente:
1 - Listar por pantalla los pasajes de menor y mayor precio.
2 - Calcular y mostrar la cantidad de pasajes de un destino determinado, el mismo será ingresado por el usuario por consola.
3 - Listar los pasajes ordenados por Fecha. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’). Este ítem debe ser realizado por el algoritmo de ordenamiento bubble sort (burbujeo).
4 - Exportar a JSON la lista de pasajes, de acuerdo a la opción F 3.
5 - Exportar a CSV la lista de pasajes, de acuerdo a la opción F 1. 
"""
"F - 1"

def max_min(archivo_cargado)-> list:
    i_max = True
    i_min = True
    for pasajero in range(len(archivo_cargado)):
        for key in archivo_cargado[pasajero].keys():
            if key == 'Precio':
                archivo_cargado[pasajero][key] = float(archivo_cargado[pasajero][key])
                if i_max or (archivo_cargado[pasajero][key] > max):
                    max = archivo_cargado[pasajero][key]
                    i_max = False
                if i_min or (archivo_cargado[pasajero][key] < min):
                    min = archivo_cargado[pasajero][key]
                    i_min = False
    return max, min

def listar_max_min(archivo_cargado, max, min):
    print("Mayor Precio\n    Fecha   | Aerolinea  |   Clase    |   Origen   |  Destino   |   Precio   |    DNI     | Apellido y nombre")
    keys = ["Fecha", "Aerolinea", "Clase", "Origen", "Destino", "Precio", "DNI_Pasajero", "Apellido_Nombre_Pasajero"]
    lista_datos = []
    for pasajero in range(len(archivo_cargado)):
        for key in archivo_cargado[pasajero].keys():
            if key == 'Precio':
                comparacion = float(archivo_cargado[pasajero][key])
                if comparacion == max:
                        for key in keys:
                            lista_datos.append(str(archivo_cargado[pasajero][key]))
                        mensaje = ""
                        mensaje += f"  {lista_datos[0]}  |"
                        for pasajero in range(1, len(lista_datos)-1):
                            if len(lista_datos[pasajero]) == 2:
                                mensaje += f"     {lista_datos[pasajero]}     |"
                            elif len(lista_datos[pasajero]) == 4:
                                mensaje += f"    {lista_datos[pasajero]}    |"
                            elif len(lista_datos[pasajero]) == 5:
                                mensaje += f"    {lista_datos[pasajero]}   |"
                            elif len(lista_datos[pasajero]) == 6:
                                mensaje += f"   {lista_datos[pasajero]}   |"
                            elif len(lista_datos[pasajero]) == 7:
                                mensaje += f"  {lista_datos[pasajero]}   |"   
                            elif len(lista_datos[pasajero]) == 8:
                                mensaje += f"  {lista_datos[pasajero]}  |"
                            elif len(lista_datos[pasajero]) == 9:
                                mensaje += f" {lista_datos[pasajero]}  |"
                            elif len(lista_datos[pasajero]) == 10:
                                mensaje += f" {lista_datos[pasajero]} |"
                            elif len(lista_datos[pasajero]) == 12:
                                mensaje += f"{lista_datos[pasajero]}|"
                        mensaje += f"{lista_datos[7]}"
                        print(mensaje)
                        lista_datos.clear()
    print("Mayor Precio\n    Fecha   | Aerolinea  |   Clase    |   Origen   |  Destino   |   Precio   |    DNI     | Apellido y nombre")
    keys = ["Fecha", "Aerolinea", "Clase", "Origen", "Destino", "Precio", "DNI_Pasajero", "Apellido_Nombre_Pasajero"]
    lista_datos = []
    for pasajero in range(len(archivo_cargado)):
        for key in archivo_cargado[pasajero].keys():
            if key == 'Precio':
                comparacion = float(archivo_cargado[pasajero][key])
                if comparacion == min:
                        for key in keys:
                            lista_datos.append(str(archivo_cargado[pasajero][key]))
                        mensaje = ""
                        mensaje += f"  {lista_datos[0]}  |"
                        for pasajero in range(1, len(lista_datos)-1):
                            if len(lista_datos[pasajero]) == 2:
                                mensaje += f"     {lista_datos[pasajero]}     |"
                            elif len(lista_datos[pasajero]) == 4:
                                mensaje += f"    {lista_datos[pasajero]}    |"
                            elif len(lista_datos[pasajero]) == 5:
                                mensaje += f"    {lista_datos[pasajero]}   |"
                            elif len(lista_datos[pasajero]) == 6:
                                mensaje += f"   {lista_datos[pasajero]}   |"
                            elif len(lista_datos[pasajero]) == 7:
                                mensaje += f"  {lista_datos[pasajero]}   |"   
                            elif len(lista_datos[pasajero]) == 8:
                                mensaje += f"  {lista_datos[pasajero]}  |"
                            elif len(lista_datos[pasajero]) == 9:
                                mensaje += f" {lista_datos[pasajero]}  |"
                            elif len(lista_datos[pasajero]) == 10:
                                mensaje += f" {lista_datos[pasajero]} |"
                            elif len(lista_datos[pasajero]) == 12:
                                mensaje += f"{lista_datos[pasajero]}|"
                        mensaje += f"{lista_datos[7]}"
                        print(mensaje)
                        lista_datos.clear()

"""2 - Calcular y mostrar la cantidad de pasajes de un destino determinado, el mismo será ingresado por el usuario por consola."""

def cantidad_pasajeros_destino(archivo_cargado):
    destino = input("Ingresa el destino: ")
    contador = 0
    for pasajero in range(len(archivo_cargado)):
        for key in archivo_cargado[pasajero].keys():
            if key == 'Destino' and archivo_cargado[pasajero][key] == destino:
                contador += 1
    print(f"La cantidad de pasajeros con destino a {destino} es de {contador}")


"""3 - Listar los pasajes ordenados por Fecha. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’). Este ítem debe ser realizado por el algoritmo de ordenamiento bubble sort (burbujeo)."""

def listar_por_fecha (archivo_cargado):
    criterio = input("Ingresa 1 para ASC o 2 para DESC: ")
    match(criterio):
        case "1" | "2":
            for pasajero_1 in range(len(archivo_cargado) - 1):
                for pasajero_2 in range(pasajero_1 + 1, len(archivo_cargado)):
                            if (criterio == '1' and archivo_cargado[pasajero_1]['Fecha'] > archivo_cargado[pasajero_2]['Fecha']) or (criterio == '2' and archivo_cargado[pasajero_1]['Fecha'] < archivo_cargado[pasajero_2]['Fecha']):
                                aux = archivo_cargado[pasajero_1]
                                archivo_cargado[pasajero_1] = archivo_cargado[pasajero_2]
                                archivo_cargado[pasajero_2] = aux
                            elif archivo_cargado[pasajero_1]['Fecha'] == archivo_cargado[pasajero_2]['Fecha']:
                                if (criterio == '1' and archivo_cargado[pasajero_1]['Apellido_Nombre_Pasajero'] > archivo_cargado[pasajero_2]['Apellido_Nombre_Pasajero']) or (criterio == '2' and archivo_cargado[pasajero_1]['Apellido_Nombre_Pasajero'] < archivo_cargado[pasajero_2]['Apellido_Nombre_Pasajero']):
                                    aux = archivo_cargado[pasajero_1]
                                    archivo_cargado[pasajero_1] = archivo_cargado[pasajero_2]
                                    archivo_cargado[pasajero_2] = aux
            return archivo_cargado
        case _:
            print("Opcion no valida")

"""F- 4"""
def guardar_json(archivo_json:str, lista:list):
    lista = {"nombre_lista": lista}
    with open(archivo_json, 'w') as archivo:
        json.dump(lista, archivo, indent=4)

"""F- 5"""
def guardar_archivo(archivo_nombre:str, contenido_archivo:str):
    if len(contenido_archivo) == 0:
        retorno = False
    else:
        with open(archivo_nombre, 'w+') as archivo:
            archivo.write(contenido_archivo)
        retorno = f"Se creó el archivo: {archivo_nombre}"
    return retorno

def generar_csv(nombre_csv:str, lista:list):
    if len(lista) == 0:
        retorno = False
        return retorno
    else:
        claves = ""
        datos = ""
        for key in lista[0].keys():
            claves += key + ","
        claves += '\n'
        for personaje in lista:#
            for dato in personaje.values():
                datos += dato + ","
            datos += '\n'
        guardar_archivo(nombre_csv, claves + datos)