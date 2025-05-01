#Pequeño ejercicio de clases y herencia en Python, para practicar la creación de clases y la herencia.
class Personas:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def es_mayor_de_edad(self):
        return self.edad >= 18


class Alumnos(Personas):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso
       
        
        

ramiro = Personas("Ramiro", 25)
Elena = Personas("Elena", 17)

print(ramiro.es_mayor_de_edad())  # True
print(Elena.es_mayor_de_edad())  # False
    
