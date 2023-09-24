#   --------------------------
#   r1
mi_lista = [2, 8, -5, 24]

mi_numero = 5

def cambia_valores(elem):
    if(type(elem) == list):
        for i in elem:
            i *= 2
    elif(type(elem) == int):
        elem *= 2

cambia_valores(mi_lista)
cambia_valores(mi_numero)

print(mi_lista)
print(mi_numero)

#   --------------------------
#   r2
mi_lista = [2, 8, -5, 24]

mi_numero = 5

def cambia_valores(elem):
    if(type(elem) == type([])):
        for i in range(len(elem)):
            elem[i] *= 2
    elif(type(elem) == type(2)):
        elem *= 2

cambia_valores(mi_lista)
cambia_valores(mi_numero)

print(mi_lista)
print(mi_numero)


#   ---------------
#   r3
mi_numero = 5
mi_lista = [[2, 8, -5, 24],[1, 3, 5, 7]]

mi_lista2 = mi_lista.copy()
mi_lista3 = mi_lista

mi_lista3.append([0,0,0,0])

print(mi_lista)
print(mi_lista2)
print(mi_lista3)


#   ---------------
#   r4
mi_lista = [[2, 8, -5, 24],[1, 3, 5, 7]]

mi_numero = 5

mi_lista2 = mi_lista.copy()
mi_lista3 = mi_lista

def cambia_valores(matriz):
    for fila in matriz:
        fila.append(0)

cambia_valores(mi_lista3)

print(mi_lista)
print(mi_lista2)
print(mi_lista3)



#   ---------------
#   r5
import copy

mi_lista = [[2, 8, -5, 24],[1, 3, 5, 7]]

mi_numero = 5

mi_lista2 = copy.deepcopy(mi_lista)
mi_lista3 = mi_lista

def cambia_valores(matriz):
    for fila in matriz:
        fila.append(0)

cambia_valores(mi_lista2)

print(mi_lista)
print(mi_lista2)
print(mi_lista3)



# r6 - recursividad
def cuenta(numero):
    numero -= 1

    if numero > 0:
        print(f'----> {numero}')
        cuenta(numero)
    else:
        print('Booooom!!')


# r7 - recursividad
def factorial(num):
    
    if(num > 1):
        return num * factorial(num - 1)
    else:
        return num


# r8 - cambio valores
def cambia_valor(dato):

    # print(id(dato))
    if type(dato) == type(list()):
        dato.append(6)
        # print(id(dato))
    if type(dato) == type(tuple()):
        dato = (1,2,3,4,5,6)
        # print(id(dato))
    if type(dato) == type(set()):
        dato.add(6)
        # print(id(dato))
    if type(dato) == int:
        dato = 0
        # print(id(dato))
    else:
        dato = "Chau"
        # print(id(dato))