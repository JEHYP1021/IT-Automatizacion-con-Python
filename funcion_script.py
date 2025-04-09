#Se define una funcion que crea un script de python en el directorio de trabajo actual.

import os

filname = "sentencia2.txt"

def crear_script(filname):
    comentarios = "#Aqui empieza un nuevo programa de python"
    with open(filname, "w") as file:
        file.write(comentarios)
    tamaño_archivo = os.path.getsize(filname)#Se obtine el tamaño del archivo
    return tamaño_archivo #Devuelve el tamaño en bytes.


print(crear_script(filname))
