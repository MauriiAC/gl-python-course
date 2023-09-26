## - Sintaxis


## - Equivalencia numerica
# lista = [10, 2, 5, True, "Hola", [True, 1]]
# print(lista.count(True))

# print(True > False)

# resultado = 10 == 5+5
# print(resultado+3)

## - Operadores relacionales
# print("hola".capitalize() != "Hola")
# print(50 == 25 * 2)
# print(50 <= 20 * 2)

## - Operadores lógicos, not, and, or
## - Precedencia
# print(False or False and not False or True)

# ## - Ejemplo
# tengo_dinero = False
# esta_lloviendo = False
# tengo_paraguas = True

# "Voy a ir si: tengo dinero y no está lloviendo ó tengo paraguas"

# print( tengo_dinero and (not esta_lloviendo or tengo_paraguas) )


## - Cortocircuito lógico, autocasting, weird cases
# print("True" and "False")
# print(True and False)

# print( ("True" and "False") == (True and False) )

# True and print("hola")
# False and print("chau")

# print(type(("True" and "False")))
# print(type((True and False)))

# print(True and True and "Pepe" and "Jorge")

# False or "hola" and False or print("chau")