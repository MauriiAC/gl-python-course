## - Sintaxis
## - Heteregoneas
# datos1 = ["Mauricio", 32, True, ["Buenos Aires", "Barcelona", "Madrid"]]
# datos2 = ("Mauricio", 32, True, ["Buenos Aires", "Barcelona", "Madrid"])

# print(type(datos1))
# print(type(datos2))

# ## - Inmutabilidad
# dato = "mauricio"
# datos1 = ["Mauricio", 32, True, ["Buenos Aires", "Barcelona", "Madrid"]]
# datos2 = ("Mauricio", 32, True, ["Buenos Aires", "Barcelona", "Madrid"])

# print(id(datos1))
# datos1[0] = "Juan"
# print(datos1)
# print(id(datos1))

# print()
# # dato[0] = "M"
# # print(dato)

# # datos2[0] = "Juan"
# print(id(datos2))
# datos2 = ("Juan", 32, True, ["Buenos Aires", "Barcelona", "Madrid"])
# print(datos2)
# print(id(datos2))


## - Tupla de un solo elemento
## - Indices
# nombres = ("Mauricio", "Juan", "Pepe")
# print(type(nombres))
# print(nombres[-1])


# ## - Slicing
# nombres = ("Mauricio", "Juan", "Pepe")
# print(nombres[0:2])

# nombres[0:2] = ("Mario", "Ana")
# print(nombres)

## - Concatenación
# nombres = ("Mauricio", "Juan", "Pepe")
# edades = (30, 25, 32)
# print(nombres + edades)

## - Anidamiento


## - Funciones integradas
# datos2 = ("Juan", 32, True, ["Buenos Aires", "Barcelona", "Madrid"])

# print(datos2.index(True))


# ## - Parseo con listas
# nombres = ("Mauricio", "Juan", "Pepe")
# nombres = list(nombres)

# nombres.append("Ana")
# print(nombres)
