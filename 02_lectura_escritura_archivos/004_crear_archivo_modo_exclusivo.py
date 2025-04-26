#Verificar si un archivo existe antes de crearlo
#Si existe, saltara un error FileExistsError
#Si no existe, lo creara

nombre_archivo = "archivo_exclusivo.txt"

try:
    with open(nombre_archivo, "x") as archivo:# Modo exclusivo (x) para crear un archivo
        # Escribir contenido en el archivo
        archivo.write("Este es un archivo creado en modo exclusivo.\n")
        print(f"Archivo '{nombre_archivo}' creado exitosamente.")
except FileExistsError as e:# Si el archivo ya existe, se lanzará una excepción FileExistsError
    # Manejar la excepción si el archivo ya existe
    print(f"El archivo '{nombre_archivo}' ya existe. No se puede crear en modo exclusivo.")
except Exception as e:
    # Manejar cualquier otra excepción que pueda ocurrir
    print(f"Ocurrió un error: {e}")