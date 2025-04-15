'''Utilizando de nuevo el archivo CSV de flores, la función contents_of_file se utiliza para procesar los
 datos sin convertirlos en un diccionario.'''

import os
import csv

# Crea un archvio con los siguientes datos
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Lee el contenido del archivo y formatea el cada fila
def contents_of_file(filename):
  return_string = ""

  # Llamada a la funcion "crear archivo"
  create_file(filename)

  # Abrir el archivo en modo lectura
  with open(filename, "r") as file:
    # Lee las filas del archivo
    rows = csv.reader(file)
    next(rows) #Con esto saltamos el registro de las cabeceras con los nombres de los campos
    # Recorre cada fila del archivo mediante un for
    for row in rows:
      name, color, type = row #desempaquetamos cada fila
      # La funcion devuelve en formato cadena, solo el contenido de cada fila

      return_string += "a {} {} is {}\n".format(color,name, type)
  return return_string

#Llamamos a la funcion
print(contents_of_file("flowers.csv"))