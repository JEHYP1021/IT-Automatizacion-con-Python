import os 
from snacks import Snacks                                         

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
    
    def cargar_snacks_iniciales(self):
        snacks_iniciales =[Snacks("patatas fritas", 1.50),Snacks("galletas", 1.00), Snacks("chicles", 0.50)]
        self.snacks.extend(snacks_iniciales)
        self.guardar_snacks_archivo(snacks_iniciales)
    
    def guardar_snacks_archivo(self, snacks):
        try:
            with open(self.NOMBRE_ARCHIVO, "a") as archivo:
                for snack in snacks:
                    archivo.write(f'{snack.escribir_snacks()}\n')
        except Exception as e:
            print(f"Error al guardar los snacks en el archivo: {e}")


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
    
    def agregar_snacks(self, snacks):
        self.snacks.append(snacks)
        self.guardar_snacks_archivo([snacks])

    def mostrar_snacks(self):
        print("---Inventario de Snacks---")
        for snack in self.snacks:
            print(snack)

    def get_snacks(self):
        return self.snacks