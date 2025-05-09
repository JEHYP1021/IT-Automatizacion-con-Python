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


#BUSCAR UNA O MAS PALABRAS QUE CONTENGAN AL MENOS 3 VOCALES SEGUIDAS:
'''EJERCICIO 2
La función multi_vowel_words() devuelve todas las palabras con 3 o más vocales consecutivas (a, e, i, o, u).
 Rellene la expresión regular para hacerlo.'''

def multi_vowel_words(text):
  pattern = r"\b\w*[aeiou]{3,}\w*\b"#\b...\b Busca palbaras completas
  #\w* Permite cualquier cantidad de letras antes y despues de la palabra
  #[aeiou]{3,} Busca 3 o mas vocales consecutivas
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []


'''EJERCICIO 3
La función transform_comments() convierte los comentarios de un script Python en comentarios utilizables por un compilador C.
Esto significa buscar texto que empiece con una almohadilla (#) y sustituirla por barras dobles (//), que es el indicador de comentario 
de una sola línea de C. Para el propósito de este ejercicio, ignoraremos la posibilidad de una almohadilla incrustada dentro de un 
comando Python, y asumiremos que sólo se usa para indicar un comentario. También queremos tratar las marcas de almohadilla repetitivas 
(##), (###), etc., como un único indicador de comentario, que se sustituirá sólo por (//) y no por (#//) o (//#). Rellene los parámetros 
# del método de sustitución para completar esta función: '''


def transform_comments(line_of_code):
  result = re.sub(r"\s*#+", r"//", line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"



'''EJERCICIO 4
La función convert_phone_number() busca un formato de número de teléfono estadounidense: XXX-XXX-XXXX (3 dígitos seguidos de un guión, 
3 dígitos más seguidos de un guión, y 4 dígitos), y lo convierte a un formato más formal que tiene este aspecto: (XXX) XXX-XXXX. Rellene
 la expresión regular para completar esta función.'''


def convert_phone_number(phone):
  result = re.sub(r"\b(\d{3})-(\d{3})-(\d{4})\b", r"(\1) \2-\3", phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300