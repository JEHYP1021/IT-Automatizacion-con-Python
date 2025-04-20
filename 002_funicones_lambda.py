#Las funciones landa son funciones que no tienen nombre y se pueden definir en una sola línea.
# Se utilizan para crear funciones pequeñas y rápidas que se pueden usar una sola vez.
cudaros = lambda x: x**2 #definimos una funcion lambda que eleva al cuadrado el numero que le pasemos como argumento
print(cudaros(5))#imprimimos el resultado de la funcion lambda
# La función lambda toma un argumento x y devuelve su cuadrado.

#ejmplo 2:
numeros =[1, 2, 3, 4, 5, 6]
cuadra_listas = list(map(lambda x: x**2, numeros))
#map aplica la funcion lambda a cada elemento de la lista numeros y devuelve una nueva lista con los resultados
print(cuadra_listas)#imprimimos la lista de cuadrados

#ejemplo 3:
# Filtrar una lista de números para obtener solo los números pares
pares =list(filter(lambda x: x%2==0, numeros))
print(pares)#imprimimos la lista de numeros pares
#filter aplica la funcion lambda a cada elemento de la lista numeros y devuelve una nueva lista con los resultados que cumplen la condicion

#ejemplo 4:
personas = [{'nombre': 'Juan', 'edad': 25},
           {'nombre': 'Ana', 'edad': 30},
           {'nombre': 'Pedro', 'edad': 20}]
# Ordenar la lista de diccionarios por edad utilizando una función lambda
personas_ordenadas = sorted(personas, key=lambda x: x['edad'])
print(personas_ordenadas)#imprimimos la lista de personas ordenadas por edad