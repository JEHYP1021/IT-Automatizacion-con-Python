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