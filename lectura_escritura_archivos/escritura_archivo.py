'''En este script utilizare el modulo estandar de python "os", el cual sirve para manipular archivos,
directorios y variables de entorno y ejecutar comandos del sistema'''

#Creare una ruta dinamica para trabajar con el archivo sin importar donde se ubique el script.

import os

#Obtener la ruta obsoluta del scripit
ruta_absoluta = os.path.dirname(os.path.abspath(__file__))

#Crear la ruta del archivo dentro de la carpeta correcta
ruta_archivo = os.path.join(ruta_absoluta, "sentencia2.txt")
with open(ruta_archivo, "rt") as textfile:
    for line in textfile:
        print(line.strip().upper())

