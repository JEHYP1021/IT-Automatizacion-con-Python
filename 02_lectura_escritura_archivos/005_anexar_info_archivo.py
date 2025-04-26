#En este script se va anexar informacion a un archivo ya existente mediante el modo 'a' (append)
nombre_archivo = "archivo_exclusivo.txt"

with open (nombre_archivo, "a") as archivo:
    # Se anexa la informacion al final del archivo

    archivo.write("Esta nueva linea se agregara al arhcivo\n")
    archivo.write("Seguimos argrando mas lineas\n")
    archivo.write("Ultima linea\n")

print(f"Se ha anexado la informacion al archivo: {nombre_archivo}")
