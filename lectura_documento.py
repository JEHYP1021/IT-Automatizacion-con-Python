#Usaremos la funcion open() para abrir un archivo
import os

ruta = r"C:\Users\Jehyner Puello\Desktop\WORKSPACE\laboratorio_coursera\lectura_escritura_archivos\doc.txt"

if os.path.exists(ruta):
    print("El archivo existe")
    with open(ruta, "r") as file:
        print(file.readline())
else:
    print("El archivo no existe.")

print("\n")

archivo = open("doc.txt")
print(archivo.readline())
print(archivo.readline())
print(archivo.read())

print("Directorio actual: ", os.getcwd())