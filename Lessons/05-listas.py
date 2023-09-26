## - Sintaxis
# edades = [32, 20, 41, 35, 50]
# print(edades)

## - Heteregoneas
# datos = ["Mauricio", 32, True, ["Buenos Aires", "Barcelona", "Madrid"]]
# print(datos)


## - Indices
## - Anidamiento
# datos = ["Mauricio", 32, True, ["Buenos Aires", "Barcelona", "Madrid"]]
# print(datos[-1][0][-1])

## - Concatenación
# mi_lista1 = [10,20,30,40]
# mi_lista2 = ["Mauricio", "Pepe", "Juan"]

# mi_lista3 = mi_lista1 + mi_lista2

# print(mi_lista3)

## - Mutabilidad
# nombre = "mauricio"
# nombre[0] = "M"  # Error!

# nombres = ["mauricio", "Lionel", "Cristiano"]
# print(id(nombres))
# nombres[0] = "Mauricio"
# print(id(nombres))

# print(nombres)

# ## - Slicing, asignación por slicing
# nombres = ["Mauricio", "Lionel", "Cristiano", "Roman", "Pepe"]
# # print(nombres[0:3:2])
# # print(nombres[::-1])

# # nombres[1:3] = ["Mariano"]
# nombres[1:3] = []
# print(nombres)

## - Funciones integradas
nombres = ["Mauricio", "Lionel", "Cristiano", "Roman", "Pepe", "Lionel"]
# nombres.append("Jor" + "ge")
# print(nombres)

# print(len(nombres))
# print(nombres.pop(1))
# print(nombres)
# print(nombres.count("Lionel"))
# print(nombres.index("Cristiano"))
# print(nombres.index("Maria"))


## - Ejercicios #6 al #7
# 7 
# Dada la lista [5, 7, 3, 0, 4, 0, 4, 3, 4, 8, 6, 9, 8, 5, 1, 2, 3, 9, 7, 2, 1, 6] 
# pedir al usuario que ingrese un número entre 0 y 9 y devolver:
# - cuantas veces aparece el número en la lista
# - el indice de la segunda vez que aparece en la lista (suponer q aparece dos veces)

# mi_lista = [5, 7, 3, 0, 4, 0, 4, 3, 4, 8, 6, 9, 8, 5, 1, 2, 3, 9, 7, 2, 1, 6] 

# # print(mi_lista[17])
# # print(mi_lista.index(9))

# long_sublista = mi_lista.index(9)

# mi_lista = mi_lista[long_sublista+1:]

# print(mi_lista.index(9) + long_sublista+1)
