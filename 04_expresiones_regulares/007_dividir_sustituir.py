'''En este archivo usaremos dos funciones de la biblioteca re: re.split() y re.sub().
re.split() divide una cadena en una lista de cadenas utilizando una expresión regular como delimitador.'''

import re
re.split(r"[.?!]", "One sentence. Another one? And the last one!")#todo lo que se encuentra dentro de los corchetes se considera delimitador
# ['One sentence', ' Another one', ' And the last one', '']
#Si queremos tener en cuenta los delimitadores, podemos usar el modificador de captura (?:...) para no capturarlos en la lista resultante.
# re.split(r"([.?!])", "One sentence. Another one? And the last one!")#todo lo que se encuentra dentro de los corchetes se considera delimitador


#El metodo re.sub() sustituye todas las coincidencias de una expresión regular en una cadena por otra cadena.
# La función re.sub() toma tres argumentos: la expresión regular, la cadena de sustitución y la cadena de entrada.
re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")


'''Ejercicio 1
Está trabajando con un Archivo CSV que contiene información sobre los empleados. 
Cada registro tiene un campo de nombre, seguido de un campo de número de teléfono y un campo de función. El campo de número de teléfono
 contiene números de teléfono de EE.UU. y debe modificarse al formato internacional, con +1- delante del número de teléfono. 
 El resto del número de teléfono no debe cambiar. Rellene la expresión regular, utilizando grupos, para utilizar la 
 función transform_record() para hacerlo.'''

def transform_record(record):
  new_record = re.sub(r"(\d+-\d+-\d+)", r"+1-\1",record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer