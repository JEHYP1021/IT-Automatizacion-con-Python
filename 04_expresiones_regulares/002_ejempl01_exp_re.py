#Aqui el codigo es un poco diferente, ya que no se trata de un archivo csv, sino de un log de un sistema operativo.
#El log tiene un formato diferente, pero la idea es la misma, leer el archivo y mostrarlo por pantalla.
import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1]) # 12345

#ejemplo 2
#El comando grep se utiliza para buscar patrones en un archivo de texto.
#usaremnos el comando grep para buscar la palabra "ERROR" en el archivo log.txt
#El archivo log.txt tiene el siguiente contenido:
