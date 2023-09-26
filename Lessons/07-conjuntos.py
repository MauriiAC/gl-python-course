## - Definicion: una colección NO ordenada de elementos únicos

# , ["Buenos Aires", "Barcelona", "Madrid"]
## - Heterogeneos, tipos inmutables
## - Sintaxis
# datos1 = ["Juan", 32, True, ("Buenos Aires", "Barcelona", "Madrid")]
# datos2 = ("Juan", 32, True, ("Buenos Aires", "Barcelona", "Madrid"))
# datos3 = {"Juan", 32, True, ("Buenos Aires", "Barcelona", "Madrid")}

# print(datos1)
# print(datos2)
# print(datos3)

## - Set vacío
# mi_lista = []
# mi_tupla = ()
# mi_conjunto = set()

# print(type(mi_lista))
# print(type(mi_tupla))
# print(type(mi_conjunto))

## - Parseo con otras colecciones
# datos1 = ["Juan", 32, True, ("Buenos Aires", "Barcelona", "Madrid")]
# datos2 = set(datos1)
# print(datos2)

# datos = [10,20,10,30,10,40]
# print(set(datos))

# name = "pepe"
# print(set(name))

datos3 = {"Juan", 32, True, ("Buenos Aires", "Barcelona", "Madrid")}
# print(datos3[0:2])
# datos3.add({"Maria", "Ernesto"}) # ERROR! el conjunto es mutable!
# datos3.add("Maria")
# datos3.update({30, "Juan", False})
# datos3.discard("Juan")
# datos3.discard("Sebastian")
# print(datos3)
# print(len(datos3))
# datos3.clear()
# datos3.pop()


# print(datos3)

# print("asdas" in datos3)



## - Funciones integradas


## - Eficiencia: set vs list --> set_vs_list.py