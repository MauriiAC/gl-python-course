import time

num_elementos = 1000000
lista = list(range(num_elementos))
conjunto = set(lista)

inicio = time.time()
elemento_buscar = num_elementos - 1
if elemento_buscar in lista:
    print(f"Elemento {elemento_buscar} encontrado en la lista.")
else:
    print(f"Elemento {elemento_buscar} no encontrado en la lista.")
fin = time.time()
tiempo_lista = fin - inicio
print(f"Búsqueda en lista tomó {tiempo_lista} segundos.")

inicio = time.time()
if elemento_buscar in conjunto:
    print(f"Elemento {elemento_buscar} encontrado en el conjunto.")
else:
    print(f"Elemento {elemento_buscar} no encontrado en el conjunto.")
fin = time.time()
tiempo_conjunto = fin - inicio
print(f"Búsqueda en conjunto tomó {tiempo_conjunto} segundos.")

print()
print(f'Búsqueda en lista tardó {round(tiempo_lista/tiempo_conjunto)} veces más')