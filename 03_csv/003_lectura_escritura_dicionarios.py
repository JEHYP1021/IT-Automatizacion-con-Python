'''Para este script vamos a simular que queremos guardar los datos sobre los usuarios de nuestra empresa y los 
departamentos en los que trabajan'''
#importamos el modulo csv para trabajar con archivos de este tipo
import csv
#Creamos una variable users que contiene una lista de diccionarios con la informacion de nuestros usuarios
users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
 {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
  {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
#Abrimos un documento csv en modo escritura y definimos la lista de claves que tendra el archivo
with open("por_departamento.csv", "w") as por_departamento:
    escritor = csv.DictWriter(por_departamento, fieldnames=keys)
  #Usamos el DictWriter pasando las claves que habiamos identificado antes, y con esto se creara nuestra primera linea del csv
    escritor.writeheader()
    #El metodo writerows convertira las listas del diccionario en lineas de ese fichero.
    escritor.writerows(users)
