'''El script abre un archivo csv con las notas de los estudiantes que contiene 3 notas, agregara dos columnas nuevas con nombres
"nota_final" y "estado", la nota final sera el promedio de las 3 notas y dependiendo si es mayor o igual 3 se completara la siguiente 
columna con aprobado o reprobado.'''
import csv

with open("notas_estudiantes2.csv", "r", newline="") as archivo:
    lector = csv.DictReader(archivo, delimiter='\t')#Argramos el delimitador para que lea el archivo correctamente
    filas = list(lector)#convertimos el objeto en una lista para poder recorrerlo

columnas_notas = [col for col in lector.fieldnames if col not in ("ALUMNO", "ID")]#obtenemos las columnas que contienen las notas


for fila in filas:
    notas =[float(fila[col]) for col in columnas_notas if fila[col]]#convertimos las notas a float y las guardamos en una lista
    # Si la lista de notas no está vacía, calculamos el promedio
    if notas:
        promedio = sum(notas) / len(notas)
    else:# Si no hay notas, el promedio es 0.0
        promedio = 0.0
    fila['nota_final'] = round(promedio, 2)# redondeamos el promedio a 2 decimales
    fila['estado'] = "Aprobado" if promedio >= 3 else "Reprobado"# asignamos el estado dependiendo del promedio

nuevos_campos = lector.fieldnames + ['nota_final', 'estado']# obtenemos los nombres de las columnas originales y agregamos las nuevas columnas
# Escribimos el nuevo archivo CSV con las notas finales y el estado de los estudiantes
with open("notas_actualizadas.csv", "w", newline="") as archivo_salida:
    escritor = csv.DictWriter(archivo_salida, fieldnames=nuevos_campos)
    escritor.writeheader()# escribimos la cabecera con los nombres de las columnas
    escritor.writerows(filas)## escribimos las filas con los datos de los estudiantes y sus notas finales y estado

print("Archivo actualizado con las notas finales y estado de los estudiantes guardado como 'notas_actualizadas.csv'")

