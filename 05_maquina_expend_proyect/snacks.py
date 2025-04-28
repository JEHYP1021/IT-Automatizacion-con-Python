class Snacks:
    """Clase que representa un snack en la máquina expendedora."""
    contador_snacks = 0# Contador de snacks
    def __init__(self, nombre='', precio=0.0):#Definimos el constructor de la clase
        Snacks.contador_snacks += 1# Incrementamos el contador de snacks
        # Asignamos el ID del snack y los atributos nombre y precio. Los id se crean de forma automatica
        # al crear un nuevo snack, por lo que no es necesario pasarlos como argumentos.
        self.id_snack = Snacks.contador_snacks
        self.nombre = nombre
        self.precio = precio
    # Definimos el método __str__ para representar el objeto como una cadena de texto.
    def __str__(self):
        return f'ID: {self.id_snack}, Nombre: {self.nombre}, Precio: {self.precio}'
    #Este metodo devuelve los argumentos en un formato de cadena de texto separados por comas.
    # Esto es útil para guardar los datos en un archivo CSV o similar.
    def escribir_snacks(self):
        return f'{self.id_snack},{self.nombre},{self.precio}\n'