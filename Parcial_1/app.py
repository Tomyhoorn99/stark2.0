import json 
from biblioteca import *
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
A – Cargar el archivo data.json.  Luego de la carga del archivo, realizar un menú de opciones que realice lo siguiente en 
memoria:  Realizar un menú de opciones que realice lo siguiente: 
B – Alta de datos con sus respectivas validaciones. [Id, Aerolínea, DNI (número), Precio, 
Origen, Destino, Origen y Destino distintos, Clase, Fecha (numero)].  
C – Modificar datos: Listar id y nombre de todos pasajes, luego buscarlo por id y realizar la 
modificación del DNI, apellido y nombre o la fecha (Realizar un submenú => “ej: Ingrese id, 
tipo y dato a modificar”).  
D – Borrar datos: Listar id y nombre de todos los pasajes, luego buscarlo por id y realizar la 
baja correspondiente.  
E – Listar todos los pasajes cuyo encabezado deberá ser formateado de la siguiente manera: Fecha | Aerolínea | Clase | Origen | Destino | Precio | DNI | Apellido y nombre 
F – Hacer un submenú que realice lo siguiente:
1 - Listar por pantalla los pasajes de menor y mayor precio.
2 - Calcular y mostrar la cantidad de pasajes de un destino determinado, el mismo será ingresado por el usuario por consola.
3 - Listar los pasajes ordenados por Fecha. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’). Este ítem debe ser realizado por el algoritmo de ordenamiento bubble sort (burbujeo).
4 - Exportar a JSON la lista de pasajes, de acuerdo a la opción F 3.
5 - Exportar a CSV la lista de pasajes, de acuerdo a la opción F 1. 
G – Salir """
'''
Apellido y nombre: Hoorn Tomas Gonzalo
Division: 313-1
'''
aeropuerto_app('C:/Users/Usuario/OneDrive/Escritorio/python/Desafio_Stark.py/Parcial_1/data.json')