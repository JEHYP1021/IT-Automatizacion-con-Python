from servicio_snacks import ServicioSnacks
from snacks import Snacks

class MaquinaDeSnacks:
    def __init__(self):
        self.servicio_snacks = ServicioSnacks()
        self.productos = []

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

    def mostrar_menu(self):
        print(f'''\t --- MENU ---
              1. Comprar Snack
              2. Mostrar ticket
              3. Agregar nuevo snack al inventario
              4. Inventario de Snacks
              5. Salir''')
        return int(input("Seleccione una opción: "))
    
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

    def comprar_snack(self):
        id_snack = int(input("Que snack desea comprar? (ID): "))
        snacks =self.servicio_snacks.get_snacks()
        snack = next((snack for snack in snacks if snack.id_snack == id_snack), None)
        if snack:
            self.productos.append(snack)
            print(f'Snack encontrado: {snack}')
        else:
            print(f'Id de snack no encontrado: {id_snack}')
    

    def mostrar_ticket(self):
        if not self.productos:
            print("No hay productos en el ticket.")
            return
        total = sum(snack.precio for snack in self.productos)
        print("--- ticket de compra--- ")
        for producto in self.productos:
            print(f'\t-- {producto.nombre} - ${producto.precio:.2f}')
        print(f'Total: ${total:.2f}')

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