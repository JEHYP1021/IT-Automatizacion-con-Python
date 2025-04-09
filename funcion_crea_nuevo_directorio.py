'''La función nuevo_directorio crea un nuevo directorio dentro del directorio de trabajo actual, 
luego crea un nuevo archivo vacío dentro del nuevo directorio, y devuelve la lista de archivos en ese directorio.''' 

import os

def nuevo_directorio(directory, filename):
    if os.path.isdir(directory)==False:#Verifica si es un directorio
        os.mkdir(directory)#Si no lo es, lo crea
    os.chdir(directory)#Cambia de directorio de trabajo al que se ha creado.
    with open(filename, "w") as file:#Crea un nuevo archivo
        pass
    return os.listdir()#La funcion devuelve el listado de archivos que se encuentra en la carpeta de trabajo actual.

print(nuevo_directorio("PythonPrograms", "script.py"))
