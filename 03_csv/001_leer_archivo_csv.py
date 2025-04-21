'''Este pequeño script busca un archivo txt que tiene un formato csv, lo abre
y lo recorre para luego mostrarlo en pantalla con dicho formato.'''
#Importamos el modulo estandar de python para trabajar con el formato csv
import os
import csv
#Obtenemos la ruta relativa del documento
ruta_relativa ="csv/archivo_csv.txt"
#abrimos el documento
f = open(ruta_relativa)
f_csv = csv.reader(f)
#Recorremos el documento y desempaquetamos los campos para luego imprimirlos por pantalla.
for row in f_csv:
    nombre, telefono, funcion = row
    print("{}, {}, {}".format(nombre, telefono, funcion))
#Cerramos el documento
f.close()