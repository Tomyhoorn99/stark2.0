'''
A.Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
fuerza (MÁXIMO)
C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
(MÍNIMO)
D. Recorrer la lista y determinar el peso promedio de los superhéroes
masculinos (PROMEDIO)
E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
género) los cuales su fuerza supere a la fuerza promedio de todas las
superhéroes de género femenino
NOTA: Se debe construir un menú en el que se sea posible acceder a cada una de
las opciones (A-E)'''

from os import system
from data_Stark_3 import lista_personajes
from Stark_Bibliotecas import *


continuar = True


while continuar:

#     case 'B'  | 'b':
#             """"B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
# fuerza (MÁXIMO)"""


#             primera_fuerza = True
#             for datos in lista_personajes:
#                 for key in datos.keys():
#                     if key == 'fuerza':
#                         if primera_fuerza == True or  int(datos[key]) > fuerza_maxima:
#                             fuerza_maxima = int(datos[key])
#                             identidad_maxima = datos['identidad']
#                             peso_mayor_fuerza = datos['peso']
#                             primera_fuerza = False
#                         elif fuerza_maxima == int(datos[key]):
#                             identidad_maxima += '  y ' + datos['identidad']
#                             peso_mayor_fuerza += ' y ' + datos['peso']


#             bandera_altura = True
#             for datos in lista_personajes:
#                 for key in datos.keys():
#                     if key == 'altura':
#                         if bandera_altura == True or float(datos[key]) < altura_minima:
#                             altura_minima = float(datos[key])
#                             identidad_altura_minima = datos['identidad']
#                             nombre_altura_minima = datos['nombre']
#                             bandera_altura = False
#                         elif altura_minima == float(datos[key]):
#                             identidad_altura_minima += '  y ' + datos['identidad']
#                             nombre_altura_minima += ' y ' + datos['nombre']        



            acumlador_peso = 0
            contador = 0
            for datos in lista_personajes:
                for key in datos.keys():
                    if key == "peso" and datos["genero"] == "M":
                        acumlador_peso = acumlador_peso + float(datos[key])
                        contador += 1
            promedio = acumlador_peso / contador
            print(f"El promedio de peso de Genero Masculino es {promedio}")