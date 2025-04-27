class Snacks:
    contador_snacks = 0
    def __init__(self, nombre='', precio=0.0):
        Snacks.contador_snacks += 1
        self.id_snack = Snacks.contador_snacks
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f'ID: {self.id_snack}, Nombre: {self.nombre}, Precio: {self.precio}'
    def escribir_snacks(self):
        return f'{self.id_snack},{self.nombre},{self.precio}\n'