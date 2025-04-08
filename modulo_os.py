'''Con este sencillo script vamos a obtener la ruta raiz, para que revise su contenido
y el programa me diga si es un directorio o un archivo.'''
#Importamos el modulo os
import os
#Obtenos la ruta actual donde se ejecuta el script
ruta_base = os.getcwd()
#Guardamos en una variable el listado de archivos que se encuentran en la ruta raiz
lista_de_archivos = os.listdir(ruta_base)
#Me muestra por pantalla lo que contiene dicha ruta
print(lista_de_archivos)

#iteramos la ruta 
for name in lista_de_archivos:
    #Juntamos la ruta con el nombre
    fullname = os.path.join(ruta_base, name)
    #Usamos este condicional para que nos muestre por pantalla si es un directorio
    if os.path.isdir(fullname):
        print(f'{fullname} es un directorio')
    else:
        print(f'{fullname} es un archivo')#En caso contrario, nos diga que es un archivo.





