import re
#El emparejamiento simple se utiliza para buscar patrones en un texto.
result = re.search(r"aza", "plaza")#Aqui buscamos la palabra "aza" en la palabra "plaza"
print(result)
result = re.search(r"aza", "bazaar")
print(result)

result = re.search(r"aza", "maze")
print(result)

print(re.search(r"^x", "xenon"))# Aqui buscamos la letra "x" al principio de la palabra "xenon"

print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge"))
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))# Aqui buscamos la palabra "p.ng" en la palabra "Pangaea" sin importar si es mayuscula o minuscula
