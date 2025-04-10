'''La función fecha_archivo crea un nuevo archivo en el directorio de trabajo actual, 
comprueba la fecha en que se modificó el archivo y devuelve sólo la parte de fecha de la marca de tiempo en el formato aaaa-mm-dd.'''

import os
import datetime


def file_date(filename):
    #crea un archivo en el directorio actual
    with open(filename, "w") as file:
        timestamp = os.path.getmtime(filename) #Convertimos "timestamp", en un formato de fecha legible
    dt =datetime.datetime.fromtimestamp(timestamp)

    return ("{}".format(dt))

print(file_date("sentencia.txt"))