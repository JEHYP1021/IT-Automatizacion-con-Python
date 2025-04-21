#Las expresiones regulares son una herramienta poderosa para buscar y manipular texto. 
# Se utilizan en una variedad de aplicaciones, desde la validación de formularios hasta la búsqueda y
#  reemplazo de texto en archivos. En este artículo, exploraremos cómo funcionan las expresiones regulares y cómo 
# se pueden utilizar en Python.
# Las expresiones regulares son patrones que se utilizan para buscar y manipular texto.
#  Se componen de caracteres literales y metacaracteres que tienen un significado especial. Por ejemplo, el metacaracter
#  "." coincide con cualquier carácter, mientras que el metacaracter "*" coincide con cero o más repeticiones del carácter anterior.
#  Las expresiones regulares se utilizan en una variedad de aplicaciones, desde la validación de formularios hasta la búsqueda y reemplazo de texto en archivos.
import re

patron = "hola"
texto = "hola mundo vente a la mutua"

resultado = re.search(patron, texto) #busca el patron en el texto y devuelve un objeto Match si lo encuentra, o None si no lo encuentra
if resultado:
    print("Se encontró el patrón en el texto")
else:
    print("No se encontró el patrón en el texto")
# La función re.search() busca el patrón en el texto y devuelve un objeto Match si lo encuentra, o None si no lo encuentra.
# El objeto Match contiene información sobre la coincidencia, como la posición de inicio y fin de la coincidencia en el texto.

#ejmplo 2:
#usaremos el metodo re.findall() para encontrar todas las coincidencias de un patrón en un texto.
# Este método devuelve una lista de todas las coincidencias encontradas.
patrron2 ="ia"
texto2 ="la ia es lo maximo, la ia es muy buena para facilitar tu trabajo pero la ia tiene muchos inconvenientes, se dice que la ia" \
"te puede quitar el trabajo, sera cierto"
resultado2 = re.findall(patrron2, texto2) #busca todas las coincidencias del patron en el texto y devuelve una lista con las coincidencias
print(resultado2) #imprimimos la lista de coincidencias
print(f"Se encontraron {len(resultado2)} coincidencias del patrón '{patrron2}' en el texto.") #imprimimos la cantidad de coincidencias encontradas


#ejmplo 3:
#objeto iterador

matches = re.finditer(patrron2, texto2)
#finditer devuelve un objeto iterador que contiene todas las coincidencias del patron en el texto
for match in matches:
    print(f"Se encontró el patrón '{match.group()}' en la posición {match.start()}-{match.end()}") 
    #imprimimos la posicion de inicio y fin de cada coincidencia


#ejmplo 4:
#usaremos el metodo re.sub() para reemplazar todas las coincidencias de un patrón en un texto.
patrron2 ="ia"
reemplazo ="python"
texto2 ="la ia es lo maximo, la ia es muy buena para facilitar tu trabajo pero la ia tiene muchos inconvenientes, se dice que la ia" \
"te puede quitar el trabajo, sera cierto"
nuevo_texto = re.sub(patrron2,reemplazo,texto2, flags=re.IGNORECASE)
#FLAGS: re.IGNORECASE hace que la busqueda no distinga entre mayusculas y minusculas
#reemplaza todas las coincidencias del patron en el texto por el texto de reemplazo
print(nuevo_texto) #imprimimos el nuevo texto con las coincidencias reemplazadas


#ejmplo 5:
#Ahora queremos buscar un patrón en un texto pero no sabemos exactamnete que hay dentro
#por ejemplo la palabra "casa" puede encontrarse cisa, cesa,cosa etc. usaremos el punto
texsto3 = "casa, cisa, cesa, cosa, causa"
patron3 = "c.sa" #el punto coincide con cualquier caracter
resultado3 = re.findall(patron3, texsto3) #busca todas las coincidencias del patron en el texto y devuelve una lista con las coincidencias
#en el caso de que queramos encontrar dos caracteres en vez de uno, por ejemplo causa usaremos dos puntos
#patron3 = "c..sa" #el punto coincide con cualquier caracter
patron4 = "c..sa" #el punto coincide con cualquier caracter
resultado4 = re.findall(patron4, texsto3) #busca todas las coincidencias del patron en el texto y devuelve una lista con las coincidencias

#y si ahora buscamos el caracter punto?
texto5 = "la casa es la casa. la casa es la casa. la casa es la casa."
patron5 = r"\." #el caracter \ indica que el siguiente caracter es un metacaracter, en este caso el punto
resultado5 = re.findall(patron5, texto5) #busca todas las coincidencias del patron en el texto y devuelve una lista con las coincidencias
print(resultado5) #imprimimos la lista de coincidencias

#ejmplo 6:
#Ahora queremos buscar un numero de telefono de españa y que tenga el formato correcto
tel = r'\+34 \d{9}' #el + indica que el siguiente caracter es un metacaracter, en este caso el 34
usuario = "Mi numero de telefono es +34 123456789"
resultado6 = re.findall(tel, usuario) #busca todas las coincidencias del patron en el texto y devuelve una lista con las coincidencias
print(resultado6) #imprimimos la lista de coincidencias

#ejmplo 7:
#Usaremos expresiones regulares para encontrar caracteres alfanumericos
alfa_num = r'\w'
usuario2 = "el_rubius_69"
resultado7 = re.findall(alfa_num, usuario2) 
#busca todas las coincidencias del patron en el texto y devuelve una lista con las coincidencias
print(resultado7) #imprimimos la lista de coincidencias


#ejmplo 8:
#Usaremos expresiones regulares para encontrar espacios en blanco
#\s coincide con cualquier espacio en blanco, tabulacion o salto de linea
espacio = r'\s'
usuario3 = "el rubius 69"
resultado8 = re.findall(espacio, usuario3)
#busca todas las coincidencias del patron en el texto y devuelve una lista con las coincidencias
print(resultado8) #imprimimos la lista de coincidencias


#ejmplo 9:
#Principios de cadena
#^ indica el inicio de una cadena, en python no se puede usar los nombres de variables que empiezan con un numero
user ="422_name%22"
patron9 = r'^\w' #busca todas las coincidencias del patron en el texto y devuelve una lista con las coincidencias
resultado9 = re.findall(patron9, user) #busca todas las coincidencias del patron en el texto y devuelve una lista con las coincidencias
print(resultado9) #imprimimos la lista de coincidencias


#ejmplo 10:
#Fin de cadena
# $ indica el final de una cadena, en python no se puede usar los nombres de variables que terminan con un numero
user ="name%22_422" 
patron10 = r'\w$' #busca todas las coincidencias del patron en el texto y devuelve una lista con las coincidencias
resultado10 = re.findall(patron10, user) #busca todas las coincidencias del patron en el texto y devuelve una lista con las coincidencias
print(resultado10) #imprimimos la lista de coincidencias


#ejmplo 11:
#\b: indica un limite de palabra, es decir, el inicio o el final de una palabra
texto11 = "la casa es la casa. la casa es la casa. la casa es la casa."
patron11 = r'\bc.sa\b' #busca todas las coincidencias del patron en el texto y devuelve una lista con las coincidencias
resultado11 = re.findall(patron11, texto11) #busca todas las coincidencias del patron en el texto y devuelve una lista con las coincidencias
print(resultado11) #imprimimos la lista de coincidencias


#ejmplo 12:
#|: indica una alternancia, es decir, busca uno u otro patron

frutas = "manzana, naranja, pera, uva, piña, aguacate, palpa, pera, piña"
patron12 = r'palpa|aguacate|p..a|\b\w{7}\b'
#busca todas las coincidencias del patron en el texto y devuelve una lista con las coincidencias
resultado12 = re.findall(patron12, frutas) #busca todas las coincidencias del patron en el texto y devuelve una lista con las coincidencias
print(resultado12) #imprimimos la lista de coincidencias



#ejemplo 13:
#Los cuantificadores se utilizan para especificar cuantas veces debe aparecer un caracter o grupo de caracteres en una cadena.
#+: indica que el caracter anterior se repite una o mas veces
palabras = " la a es aaaaa a que esta en la casa de b"
patron13 = 'a+'
#busca todas las coincidencias del patron en el texto y devuelve una lista con las coincidencias
resultado13 = re.findall(patron13, palabras) #busca todas las coincidencias del patron en el texto y devuelve una lista con las coincidencias  
print(resultado13) #imprimimos la lista de coincidencias
