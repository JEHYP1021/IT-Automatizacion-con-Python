#Pequeño ejercicio de clases y herencia en Python, para practicar la creación de clases y la herencia.
class Personas:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def es_mayor_de_edad(self):
        return self.edad >= 18


class Alumnos(Personas):#La clase Alumno hereda de la clase padre Personas.
    #La clase Alumno tiene un atributo adicional llamado curso.
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)#El metodo super() llama al constructor de la clase padre Personas.
        self.curso = curso
       
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')
        print(f'Curso: {self.curso}')
        print(f'Es mayor de edad?: {self.es_mayor_de_edad()}')       
        

ramiro = Personas("Ramiro", 25)
Elena = Personas("Elena", 17)

print(ramiro.es_mayor_de_edad())  # True
print(Elena.es_mayor_de_edad())  # False
    
carlos = Alumnos("Carlos", 20 , "Bachiller")
carolina = Alumnos("Carolina", 16, "ESO")

print("***LISTA DE ALUMNOS***\n")
print(carlos.mostrar_informacion())
print(carolina.mostrar_informacion())


class GestorAlumnos:
    def __init__(self):
        self.alumnos = []

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def mostrar_alumnos(self):
        for alumno in self.alumnos:
            alumno.mostrar_informacion()
            print("---------------------")
gestor = GestorAlumnos()
while True:
    print("1. Agregar alumno")
    print("2. Mostrar alumnos")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        curso = input("Curso: ")
        nuevo_alumno = Alumnos(nombre, edad, curso)
        gestor.agregar_alumno(nuevo_alumno)
    elif opcion == "2":
        gestor.mostrar_alumnos()
    elif opcion == "3":
        break
    else:
        print("Opción no válida.")