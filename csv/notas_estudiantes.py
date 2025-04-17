'''El script abre un archivo csv con las notas de los estudiantes de 4 periodos tomara la media y dependiendo si tiene
3 o mas mostrara por pantalla si aprobo no.'''
import csv

with open("notas_estudiantes.csv", "r") as file:
    reader = csv.DictReader(file)
    

