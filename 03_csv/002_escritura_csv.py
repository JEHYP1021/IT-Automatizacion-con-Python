'''Este pequeño script agrega un par de lineas a un archivo csv, de nombre ejemplo1'''
#Importamos el modolo para trabajar con archivos csv
import csv
#En una variable guardamos una lista
host = [["servidor.local","192.56.234.001"],["servidor.web","192.255.255.152"]]

#Abrimos el archivo ejemplo1.csv en modo escritura
with open("csv/ejemplo1.csv", "w") as host_csv:
    #Agregamos la lista al arhcivo que abrimos
    writer = csv.writer(host_csv)
    writer.writerows(host)

