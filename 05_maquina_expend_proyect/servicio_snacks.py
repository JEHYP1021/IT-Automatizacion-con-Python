'''En este modulo se define la clase ServicioSnacks, que se encarga de gestionar los snacks disponibles en la máquina expendedora.
La clase tiene métodos para cargar snacks iniciales, guardar snacks en un archivo, obtener snacks desde un archivo, agregar nuevos snacks
 y mostrar la lista de snacks disponibles.'''
import os #Importamos el módulo os para trabajar con archivos y directorios
#Importamos la clase Snacks desde el módulo snacks
from snacks import Snacks                                         
#Esta clase representa el servicio de snacks en la máquina expendedora.
# Se encarga de cargar, guardar y gestionar los snacks disponibles.
class ServicioSnacks:
    NOMBRE_ARCHIVO = "listado_snacks.txt"
    def __init__(self):
        self.snacks = []
        #Revisar si ya existe el archivo listado de snacks
        #Si existe el archivo, leer los snacks existentes´
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self.snacks = self.obtener_snacks()
        # Si no existe el archivo, crear uno nuevo
        else:
            self.cargar_snacks_iniciales()
    # Definimos el método cargar_snacks_iniciales que carga una lista de snacks iniciales en la máquina expendedora.
    # Si el archivo no existe, se crean snacks predeterminados y se guardan en el archivo.
    def cargar_snacks_iniciales(self):
        snacks_iniciales =[Snacks("patatas fritas", 1.50),Snacks("galletas", 1.00), Snacks("chicles", 0.50)]
        self.snacks.extend(snacks_iniciales)
        self.guardar_snacks_archivo(snacks_iniciales)
    # Definimos el método guardar_snacks_archivo que guarda una lista de snacks en un archivo.
    #En este metodo, se trabaja con excepciones para manejar errores al abrir o escribir en el archivo.
    def guardar_snacks_archivo(self, snacks):
        try:#El archivo se abre en modo "a" (append) para agregar nuevos snacks al final del archivo sin borrar el contenido existente.
            #El bloque try se utiliza para manejar excepciones que puedan ocurrir al abrir o escribir en el archivo.
            with open(self.NOMBRE_ARCHIVO, "a") as archivo:
                for snack in snacks:
                    archivo.write(f'{snack.escribir_snacks()}\n')
        except Exception as e:#Si ocurre una excepción, se captura y se imprime un mensaje de error.
            #El bloque except se utiliza para manejar excepciones que puedan ocurrir durante la ejecución del bloque try.
            print(f"Error al guardar los snacks en el archivo: {e}")

# Definimos el método obtener_snacks que lee los snacks desde un archivo y los devuelve como una lista de objetos Snacks.
    #En este metodo, se trabaja con excepciones para manejar errores al abrir o leer el archivo.
    def obtener_snacks(self):
        snacks_lista =[]
        try:
            with open(self.NOMBRE_ARCHIVO, "r") as archivo:
                for linea in archivo:
                    id_snacks, nombre, precio = linea.strip().split(",")
                    snack = Snacks(nombre, float(precio))
                    snacks_lista.append(snack)
        except Exception as e:
            print(f"Error al leer el archivo de snacks:{e}")
        return snacks_lista
    # Definimos el método agregar_snacks que agrega un nuevo snack a la lista de snacks y lo guarda en el archivo.
    #En este metodo, se trabaja con excepciones para manejar errores al abrir o escribir en el archivo.
    def agregar_snacks(self, snacks):
        self.snacks.append(snacks)
        self.guardar_snacks_archivo([snacks])
     # Definimos el método mostrar_snacks que imprime la lista de snacks disponibles en la máquina expendedora.
    def mostrar_snacks(self):
        print("---Inventario de Snacks---")
        for snack in self.snacks:
            print(snack)
#definimos el método get_snacks que devuelve la lista de snacks disponibles en la máquina expendedora.
    #Este método es útil para acceder a la lista de snacks desde otras partes del código.
    def get_snacks(self):
        return self.snacks