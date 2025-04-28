'''Este modulo seria la aplicacion con la que el usuario interactua.
En este modulo se define la clase MaquinaDeSnacks, que representa la máquina expendedora de snacks.'''
# Importamos la clase ServicioSnacks desde el módulo servicio_snacks
# y la clase Snacks desde el módulo snacks.
from servicio_snacks import ServicioSnacks
from snacks import Snacks
#Definimos la clase MaquinaDeSnacks que representa la máquina expendedora de snacks.
# Esta clase tiene métodos para mostrar el menú, ejecutar opciones, comprar snacks, mostrar el ticket y agregar nuevos snacks al inventario.
class MaquinaDeSnacks:
    def __init__(self):
        self.servicio_snacks = ServicioSnacks()
        self.productos = []
# Definimos el constructor de la clase, que inicializa el servicio de snacks y una lista vacía para los productos comprados.
# En el constructor, se crea una instancia de la clase ServicioSnacks y se inicializa la lista de productos como vacía.
    def maquina_snacks(self):
        salir = False
        print("***MAQUINA EXPENDEDORA DE SNACKS***")
        self.servicio_snacks.mostrar_snacks()
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f'Ocurrio un error: {e}')
#definimos el método mostrar_menu que imprime el menú de opciones disponibles para el usuario.
# Este método muestra las opciones de compra de snacks, mostrar ticket, agregar nuevo snack al inventario, inventario de snacks y salir.
    def mostrar_menu(self):
        print(f'''\t --- MENU ---
              1. Comprar Snack
              2. Mostrar ticket
              3. Agregar nuevo snack al inventario
              4. Inventario de Snacks
              5. Salir''')
        return int(input("Seleccione una opción: "))
    # Definimos el método ejecutar_opcion que ejecuta la opción seleccionada por el usuario.
    # Este método recibe la opción seleccionada y llama al método correspondiente según la opción elegida.
    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.comprar_snack()
        elif opcion == 2:
            self.mostrar_ticket()
        elif opcion == 3:
            self.agregar_snack()
        elif opcion == 4:
            self.servicio_snacks.mostrar_snacks()
        elif opcion ==5:
            print("Hasta pronto!")
            return True
        else:
            print(f"Opción no válida. Intente nuevamente {opcion}")
            return False
# Definimos el método comprar_snack que permite al usuario comprar un snack.
# Este método solicita al usuario que ingrese el ID del snack que desea comprar y verifica si existe en la lista de snacks.
    def comprar_snack(self):
        id_snack = int(input("Que snack desea comprar? (ID): "))
        snacks =self.servicio_snacks.get_snacks()
        snack = next((snack for snack in snacks if snack.id_snack == id_snack), None)
        if snack:
            self.productos.append(snack)
            print(f'Snack encontrado: {snack}')
        else:
            print(f'Id de snack no encontrado: {id_snack}')
    
# Definimos el método mostrar_ticket que imprime el ticket de compra con los productos comprados y el total a pagar.
# Este método calcula el total de la compra sumando los precios de los productos en la lista de productos.
    def mostrar_ticket(self):
        if not self.productos:
            print("No hay productos en el ticket.")
            return
        total = sum(snack.precio for snack in self.productos)
        print("--- ticket de compra--- ")
        for producto in self.productos:
            print(f'\t-- {producto.nombre} - ${producto.precio:.2f}')
        print(f'Total: ${total:.2f}')
# Definimos el método agregar_snack que permite al usuario agregar un nuevo snack al inventario de la máquina expendedora.
# Este método solicita al usuario que ingrese el nombre y precio del nuevo snack y lo agrega a la lista de snacks.
    def agregar_snack(self):
        nombre = input("ingrese el nombre del snack: ")
        precio = float(input("ingrese el precio del snack: "))
        nuveo_snack = Snacks(nombre, precio)
        self.servicio_snacks.agregar_snacks(nuveo_snack)
        print(f'Snack agregado: {nuveo_snack}')

#Programa principal
if __name__ == "__main__":
    maquina = MaquinaDeSnacks()
    maquina.maquina_snacks()