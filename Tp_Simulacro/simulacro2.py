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
 Fecha (formato AAAAMMDD)  A  Cargar el archivo data.json.  Luego de la carga del archivo, realizar un menú de opciones que realice lo siguiente en 
memoria:  Realizar un menú de opciones que realice lo siguiente: B  Alta de datos con sus respectivas validaciones. [Id, Aerolínea, DNI (número), Precio, 
Origen, Destino, Origen y Destino distintos, Clase, Fecha (numero)].  C Modificar datos: Listar id y nombre de todos pasajes, luego buscarlo por id y realizar la 
modificación del DNI, apellido y nombre o la fecha (Realizar un submenú => “ej: Ingrese id, 
tipo y dato a modificar”).  D  Borrar datos: Listar id y nombre de todos los pasajes, luego buscarlo por id y realizar la 
baja correspondiente.  E Listar todos los pasajes cuyo encabezado deberá ser formateado de la siguiente manera: Fecha | Aerolínea | Clase | Origen | Destino | Precio | DNI | Apellido y nombre  F – Salir """

aeropuerto_app("C:/Users/nacho/OneDrive/Escritorio/Facultad/1er Cuatrimestre/Programacion 1/TP_SIMULACRO/simulacro/test1234.json")
