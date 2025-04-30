import re
print(re.search(r"[Pp]ython", "Python"))# Aqui buscamos la palabra "Python" en la palabra "Python" sin importar si es mayuscula o minuscula


import re
print(re.search(r"[a-z]way", "The end of the highway"))# Aqui buscamos la palabra "way" en la palabra "highway" sin importar si es mayuscula o minuscula
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))


import re
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))# Aqui buscamos la palabra "This is a sentence with spaces." en la palabra "This is a sentence with spaces." sin importar si es mayuscula o minuscula
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

print(re.search(r"cat|dog", "I like cats."))# Aqui buscamos la palabra "cat" o "dog" en la palabra "I like cats." sin importar si es mayuscula o minuscula
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))
print(re.findall(r"cat|dog", "I like both dogs and cats."))

#encontrar puntos comas y signos de interrogacion dentro de una cadena

texto = "Hola, ¿cómo estás? Espero que estés bien. ¡Hasta luego!"
resultado = re.findall(r"[.,;¿?]", texto)
print(resultado)  # ['¿', '?', '.', '¡']