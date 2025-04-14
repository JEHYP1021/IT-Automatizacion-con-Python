'''Estamos trabajando con una lista de flores y alguna información sobre cada una de ellas. 
La función crear_archivo escribe esta información en un Archivo CSV. 
La función contents_of_file lee este archivo en registros y devuelve la información en un bloque bien formateado.'''

import os
import csv

# Crea un archivo con los siguientes datos
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")


# Lee el contenido del archivo y formatea el contenido de cada fila
def contents_of_file(filename):
  return_string = ""

  # Llama la funcion crar un archivo
  create_file(filename)

  # abre el archivo
  with open(filename) as file:
    # Lee las filas del archivo en un diccionario
    reader = csv.DictReader(file)

    # Process each item of the dictionary
    for row in reader:
      
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

print(contents_of_file("flower.csv"))