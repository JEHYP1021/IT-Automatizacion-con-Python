'''Se debe tener especial cuidado cuando se trabaja con archivos en python.
Hay que verificar que python apunta hacia el espacio de trabajo correcto donde se encuentra el archivo con el que pretendemos trabajar.'''
#La primera opcion que nos permite hacer esto es mediante la "ruta relativa del archivo":
#con open se abre el archivo de texto en modo "lectura" por defecto
archivo = open("lectura_escritura_archivos/sentencia.txt")
print(archivo.readline())#imprime la linea del archivo donde se encuentre ubicado actualmente
print(archivo.readline())#imprime la siguiente linea
print(archivo.readline())
print(archivo.read())#imprime el resto de lineas del archivo
archivo.close()#cierra el archivo.
print("\n")

with open("lectura_escritura_archivos/sentencia.txt", "r") as archivo:
    print(archivo.readline(), "\n")
    print(archivo.read())