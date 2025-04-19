cuadrados =[x**2 for x in range(100+1) if x%2==0]#creamos una lista de cuadrados de los numeros pares del 0 al 100
print(cuadrados)
lista = []
for x in range(1000000):
    lista.append(x)
sumatoria_total = sum(lista)#sumamos todos los elementos de la lista
print(sumatoria_total)
# La función sum() es más eficiente que un bucle for para sumar elementos de una lista, ya que está optimizada en Python.