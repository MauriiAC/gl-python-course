## - integradas vs propias
## - sintaxis
## - definición vs invocación
# print(type(len("Mauricio")))

# def saluda(nombre):
#     print(f"Hola {nombre}!")

# saluda("Mauricio")


## - reutilización de código 
## - uso de parametros
## - generalización

# def calcula(op, a, b):
#     if op == 'sum':
#         print(f'El resultado de sumar {a} y {b} es {a+b}')
#         return a + b
#     elif op == 'res':
#         print(f'El resultado de restar {a} y {b} es {a-b}')
#     elif op == 'mul':
#         print(f'El resultado de multiplicar {a} y {b} es {a*b}')
#     elif op == 'div':
#         print(f'El resultado de dividir {a} y {b} es {a/b}')
#     else:
#         print('Operación invalida')

# print("Haciendo algunas cosas..")

# print(calcula("sum", 2,11))

# print("Haciendo otras cosas importantes en nuestra app..")

# calcula("sum", 5,8)

# print("Continua al app funcionando..")


## - return

# mi_lista = [10,20,30,40]

# print(mi_lista.append(50))

# print(mi_lista)

# ## - ambito de variable (scope a nivel de función)
# nombre = "Pepito"
# def saluda_con_nombre(nombre):
#     return f'Hola {nombre}'

# print(saluda_con_nombre("Mauricio"))
# print(nombre)

# ## - return tupla implicita
# def retorna_nombres():
#     return "Mauricio", "Juan", "Javier", "Maria"

# datos = retorna_nombres()

# print(datos)

## - Ejercicios #24 a #28
# 24
# Crear una función que reciba un número y una lista, e retorne {"Todos los valores son divisibles 
# por {numero}"} si son todos divisibles, y retorne {"Hay valores que no se pueden dividir por {numero}"} en caso contrario

# def todos_divisibles(lista, num):

#     for n in lista:
#         if n % num == 0:
#             continue
#         else:
#             return f"Hay valores que no se pueden dividir por {num}"
#     return f"Todos los valores son divisibles por {num}"

# print(todos_divisibles([2,7,12,20,30], 2))


# # 25
# # Crear una función que reciba una lista y un número y retorne una lista con todos 
# # los números aumentados en el valor del número pasado como parametro
# def suma_valor(lista, num):
#     valores_aumentados = []
#     for i in lista:
#         valores_aumentados.append(i+num)
#     return valores_aumentados
# print(suma_valor([10,20,30,40], 5))

# # 26
# # Crear una función que reciba una tupla de palabras y retorne una frase uniendo esas palabras separadas por un espacio

# def crea_frase(palabras):
#     frase = ""
#     for palabra in palabras:
#         frase += palabra + " "
#     return frase

# print(crea_frase(("adios", "mundo", "cruel")))

# ("adios", "mundo", "cruel") --> "adios mundo cruel"

# ## - Argumentos por nombre vs por posición
# def saluda(nombre, apellido):
#     return f'Hola, me llamo {nombre} {apellido}'

# print(saluda("Mauricio", "Cuello"))
# print(saluda("Cuello", "Mauricio"))

# print(saluda(nombre="Mauricio", apellido="Cuello"))
# print(saluda(apellido="Cuello", nombre="Mauricio"))

## - Parametros por defecto
# def saluda(nombre, apellido=""):
#     return f'Hola, me llamo {nombre} {apellido}'

# print(saluda(nombre="Mauricio"))
# print(saluda(nombre="Mauricio", apellido="Cuello"))

# def resta(a=None, b=None):
#     if a != None and b != None:
#         return a - b
#     else:
#         return("Debe ingresar ambos valores")

# print(resta(5, 0))

## - Pasaje de parametro por valor vs por referencia

# mi_nombre = "mauricio"
# mi_edad = 32
# mis_familiares = ["Juan", "Abril", "Jesica", "Mariela"]

# def cambia_familiar(nombres):

#     nombres.append("Hanna")
#     print(nombres)

# cambia_familiar(mis_familiares)
# print(mis_familiares)

# """
# int, float, bool, str --> Valor
# object, set, dict, tuple, list --> Referencia
# """

# mi_lista = [10,20,30,40]
# mi_numero = 5

# def cambia_valores(elem):

#     if type(elem) == list:
#         for i in range(len(elem)):
#             elem[i] *= 2
#             print('interno:',elem[i])
#     elif type(elem) == int:
#         elem *= 2
#         print('interno:',elem)

# cambia_valores(mi_lista)
# print('externo:',mi_lista)

# import copy

# mi_lista1 = [ [10,20,30,40] , [5,15,25,35]]
# mi_lista2 = mi_lista1
# mi_lista3 = copy.deepcopy(mi_lista1)

# def cambia_valores(matriz):
#     for fila in matriz:
#         fila.append(0)

# cambia_valores(mi_lista1)
# print(mi_lista1)
# print(mi_lista2)
# print(mi_lista3)

# ## - Argumentos indeterminados
# def suma(**kwargs):
    
#     return sum(kwargs.values())

# print(suma(a=10,b=20,c=30,d=40))

# def resultado(nombre, *args, **kwargs):

#     print(f'Hola {nombre}! estas son tus notas:')

#     for nota in args:
#         print(f'nota: {nota}')
    
#     print(f'Le enviaremos una copia a {list(kwargs.values())}')


# resultado("Mauricio", 7, 4, 6, 8, 9, padre="Roberto", madre="Mariela")


## - Ejercicio #29
# 29
# Crear una función llamada calcula_tiempo que puede recibir 1 o 3 parametros
# si recibe un valor, tomar como segundos y devolver la cantidad de hs, min y seg
# si se reciben 3 parametros tomar como hs, min y seg respectivamente
# y devolver la cantidad de segundos

# def calcula_tiempo(*args):

#     if len(args) == 1:

#         horas = args[0] // 3600
#         minutos = (args[0] % 3600) // 60
#         segundos = (args[0] % 3600) % 60

#         return f'{horas}hs, {minutos}min, {segundos}seg'

#     else:

#         segundos = args[0] * 3600 + args[1] * 60 + args[2]
#         return segundos

# print(calcula_tiempo(3680))
# print(calcula_tiempo(1,1,20))


## - Expresiones lambda
# def imc(peso, altura):

#     return peso / altura**2

# print(imc(70, 1.70))

# imc = lambda peso, altura: peso / altura**2
# print(imc(70, 1.70))

## - Funciones de alto orden
# mi_lista = [10, 11, 30, 33, 50, -4]

# def divisibles_por_cinco(numero):

#     return numero % 5 == 0

# # divisibles = filter(divisibles_por_cinco, mi_lista)
# divisibles = filter(lambda n: n%5 == 0, mi_lista)
# print(list(divisibles))

# def multiplica_por_diez(numero):
#     return numero * 10

# # multiplicados = map(multiplica_por_diez, mi_lista)
# multiplicados = map(lambda n: n*10, mi_lista)
# print(list(multiplicados))


## - Recursividad
# func recursiva --> es una función que se invoca a si misma

# Caso base --> no recursivo
# Caso recursivo

# def cuenta(numero):
#     numero -= 1

#     if numero > 0:
#         print(f'----> {numero}')
#         cuenta(numero)
#     else:
#         print('Booooom!')

# cuenta(7)

# factorial(n) = n * factorial(n-1)
#           n=1 --> 1

# def factorial(num):

#     if num > 1:
#         return num * factorial(num - 1)
#     else:
#         return num

# print(factorial(4))

"""
fact(4) = 4 * 6
fact(3) = 3 * 2
fact(2) = 2 * 1
"""

## - Ejercicios #30 a #35
# 30
# Crear una función que reciba dos string y devuelva la posición 
# donde se encuentra el segundo string dentro del primero
# en caso que no se encuentre, devolver -1
# NO ESTÁ PERMITIDO usar funciones de búsqueda como find o rfind
# Ej "Hello, welcome to my world.", "welcome" --> 7

# def pos_substr(main, sub):

#     for posM, charM in enumerate(main):

#         for posS, charS in enumerate(sub):

#             if main[posM + posS] != charS:
#                 break
#             if posS == len(sub) - 1:
#                 return posM
            
#     return -1


# def pos_substr(main, sub):

#     for posM, charM in enumerate(main):

#         if main[posM:posM+len(sub)] == sub:
#             return posM
        
#     return -1

# print(pos_substr("Hello, welcome to my world.", "well" ))

# 31
# Crear una función que reciba una lista ordenada de números enteros y un número objetivo
# la función debe devolver True si existe una combinación de dos números de la lista que 
# sumados arrojen como resultado el número objetivo
# Ej. [1,5,9,11,15], 10 --> True
# Ej. [1,5,9,11,15], 11 --> False

# def matchSuma(arr, target):

#     for i, num_i in enumerate(arr):
#         for j, num_j in enumerate(arr[i+1:]):
#             if num_i + num_j == target:
#                 return True
#     return False

# def matchSuma(arr, target):

#     start = 0
#     end = len(arr) - 1

#     while start < end:
#         suma = arr[start] + arr[end]

#         if suma == target:
#             return True
#         elif suma < target:
#             start += 1
#         else:
#             end -= 1
#     return False

# print(matchSuma([1,5,9,11,17], 11))

# Crear una función que reciba una lista que puede contener listas o números como elementos
# La función debe devolver la suma de todos los números de todas las sublistas
# Ej. [1,2,3,4] --> 10
# Ej. [ [2,4] , [1], [4,2,1] ] --> 14
# Ej. [ 2, [3,4], 5, [-3, [6 , [ 4,5 ] ] ] ] --> 26

# def sumList(my_list):

#     result = 0
#     for elem in my_list:
#         if type(elem) == list:
#             result += sumList(elem)
#         else:
#             result += elem

#     return result

# print(sumList([1,2,3,4]))
# print(sumList([ [2,4] , [1], [4,2,1] ]))
# print(sumList([ 2, [3,4], 5, [-3, [6 , [ 4,5 ] ] ] ]))

## - Generadores
# def multiplos(num, cantidad):

#     i = 1
#     lista_multiplos = []

#     while i < cantidad:
#         lista_multiplos.append(num*i)
#         i += 1
#     return lista_multiplos

# mis_multiplos = multiplos(5, 10)

# for i in mis_multiplos:
#     print(i)

# def multiplos2(num, cantidad):

#     i = 1
#     while i <= cantidad:
#         yield num*i
#         i += 1

# mis_multiplos = multiplos2(5, 3)

# # for i in mis_multiplos:
# #     print(i)

# print(next(mis_multiplos))
# print("otro código ejecutandose..")
# print(next(mis_multiplos))
# print("sigue corriendo otras cosas..")
# print(next(mis_multiplos))

## - Decoradores

def logs_funciones(f):

    def func_inter(*args, **kwargs):

        with open("/home/mauri/Documents/Temporary/gl-python-course/Lessons/mis_invocaciones.txt", "a") as file:
            file.write(f"Ejecutando la función {f.__name__} con los args {args} y los kwargs {kwargs}\n")
        
        print(f"Ejecutando la función {f.__name__} con los args {args} y los kwargs {kwargs}\n")
        return f(*args, **kwargs)
    
    return func_inter

@logs_funciones
def suma(a, b):

    return a + b

@logs_funciones
def resta(a, b):

    return a - b

def multiplica(a, b):

    return a * b

# print(suma(a=8, b=3))
# print(resta(5,9))



# import time

# def timeit(f):
    
#     def wrapper(*args,**kwargs):
#         t = time.time()
#         result = f(*args, **kwargs)
#         elapsed_time = time.time() - t
#         print(f'Execution time of function {f.__name__} is {elapsed_time}')
#         return result

#     return wrapper

# @timeit
# def sum(a,b):
#     return a + b

# @timeit
# def sub(a,b):
#     return a - b

# sum(10,15)
















# Creen un decorador que imprima por terminal el tiempo de ejecución de una función
import time

def calcular_tiempo(f):
    def func_int(*args, **kwargs):
        inicio = time.time()
        resultado = f(*args, **kwargs)
        fin = time.time()
        tiempo = fin - inicio
        print(f'Se demoró {tiempo} segundos!')
        return resultado
    return func_int

@calcular_tiempo
def suma(a, b):
    return a + b

# print(suma(10,50))