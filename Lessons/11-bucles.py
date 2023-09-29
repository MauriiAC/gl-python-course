## - Necesidad de su uso
# n = int(input("Ingrese el limite:"))

# if 1 < n:
#     print(1)
# if 2 < n:
#     print(2)
# if 3 < n:
#     print(3)
# DRY --> don't repeat yourself

## - while, sintaxis
# limite = int(input("Ingrese el limite:"))
# i = 1

# while i < limite:
#     print("imprimimos el valor de i")
#     print(i)
#     i += 1

# print("Finalizando ejecución")

# ## - uso, caso indeterminado
# contrasena = 'Homero123'

# valor_ingresado = input("Ingrese la contraseña: ")

# while contrasena != valor_ingresado:

#     valor_ingresado = input("Contraseña incorrecta, vuelva a intentarlo: ")

# print("Bienvenido!")

## - break, else, continue
# numero = int(input("Ingrese un numero: "))
# i = 0

# while i<numero:
#     if i > 10:
#         break
#     i += 1
#     if i == 5:
#         continue
#     print(i)
# else:
#     print("Se imprimieron todos los números")

# print("Finalizando ejecucón..")


## - for, sintaxis
# lista = [10,20,30,40]
# lista_dobles = []

# for elem in lista:
#     lista_dobles.append(elem*2)

# print(lista_dobles)

## - desempaquetado en variable iteradora, r4
# lista_personas = [("Mauricio", "Cuello", 30), ("Lionel", "Messi", 34), ("Cristiano", "Ronaldo", 34), ("Pepe", "Mujica", 40)]

# for nombre, apellido, edad in lista_personas:
#     print(nombre)

## - enumerate, Ejer #23
# paises = ['Canada', 'USA', 'Mexico', 'Australia', 'Argentina', 'China', 'India', 'Singapur', 'Croacia', 'Corea del Sur']

# for pos, pais in enumerate(paises):
#     print(pos, pais)


## Ejercicios Ejercicios #8, #10 y #16 a #20
# 8
# Dada la lista 'personas' (mockups.py) devolver la cantidad de generos diferentes que hay
# personas = [
#     {"id":1,"first_name":"Catha","last_name":"Carlton","city":"Qingshandi","email":"ccarlton0@twitter.com","gender":"Polygender"},
#     {"id":2,"first_name":"Toddie","last_name":"Ibeson","city":"San Juan","email":"tibeson1@freewebs.com","gender":"Bigender"},
#     {"id":3,"first_name":"Ashlee","last_name":"McAuslan","city":"São Jerônimo","email":"amcauslan2@pcworld.com","gender":"Polygender"},
#     {"id":4,"first_name":"Julie","last_name":"Fischer","city":"Lasusua","email":"jfischer3@ucoz.com","gender":"Agender"},
#     {"id":5,"first_name":"Manda","last_name":"Mapis","city":"Sindang","email":"mmapis4@foxnews.com","gender":"Non-binary"},
#     {"id":6,"first_name":"Noami","last_name":"Rubanenko","city":"Siemianowice Śląskie","email":"nrubanenko5@geocities.com","gender":"Genderfluid"},
#     {"id":7,"first_name":"Daffi","last_name":"Wherton","city":"Kamirenjaku","email":"dwherton6@privacy.gov.au","gender":"Bigender"},
#     {"id":8,"first_name":"Tamma","last_name":"Worsham","city":"Batang","email":"tworsham7@globo.com","gender":"Male"},
#     {"id":9,"first_name":"Gibby","last_name":"Blacktin","city":"Makarov","email":"gblacktin8@mac.com","gender":"Agender"},
#     {"id":10,"first_name":"Locke","last_name":"Pirdy","city":"Ketanggungan","email":"lpirdy9@wix.com","gender":"Polygender"},
#     {"id":11,"first_name":"Dorree","last_name":"Claypool","city":"Laborie","email":"dclaypoola@un.org","gender":"Female"},
#     {"id":12,"first_name":"Jermaine","last_name":"Duplan","city":"Chemin Grenier","email":"jduplanb@skype.com","gender":"Polygender"},
#     {"id":13,"first_name":"Kliment","last_name":"Divill","city":"Baochang","email":"kdivillc@tamu.edu","gender":"Agender"},
#     {"id":14,"first_name":"Bernice","last_name":"O'Hartnett","city":"Askainen","email":"bohartnettd@tripod.com","gender":"Genderqueer"},
#     {"id":15,"first_name":"Teirtza","last_name":"Summerlee","city":"Babakanbungur","email":"tsummerleee@scientificamerican.com","gender":"Agender"}
#     ]

# genders = set()

# for persona in personas:
#     genders.add( persona["gender"] )

# print(len(genders))

# 10  
# Dado el diccionario "respuestas", escribir un programa que saque por pantalla 
# el mensaje "chat activo: " y según lo que el usuario ingrese devolver el valor correspondiente 
# a esa clave, si la clave no existe imprimir 'lo siento, no te entendí, me lo dices de otra forma?'
# Finalizar el chat si el segundo valor de la tupla de respuesta es True

# respuestas = {
#     'hola chatbot': ('hola, como estás?', False),
#     'buen dia': ('muy buenos días, espero te encuentres muy bien', False),
#     'adios': ('hasta la próxima compañero', True),
#     'cuanto es 2 + 2?': (4, False)
# }

# texto = input("Chat activo: ")

# while True:

#     if texto in respuestas:
#         respuesta = respuestas[texto]
#         if respuesta[1]:
#             print(respuesta[0])
#             break
#         else:
#             print(respuesta[0])
#             texto = input('>>> ')
#     else:
#         texto = input('lo siento, no te entendí, me lo dices de otra forma? ')

# persona = {
#     "name": "Martin",
#     "last_name": "Martinez",
#     "age": 32
# }

# for key in persona:
#     if persona[key] == "Martinez":
#         print(key)

# print("Mauricio" in persona.values())

# 16
# Escribir un programa donde el usuario tiene que adivinar un número, si adivina, 
# imprimir el mensaje "Advinaste", si no lo logra darle otra
# oportunidad hasta llegar a 3 oportunidades, en caso que no adivine imprimir "Se te acabaron las oportunidades" - Usar while-else

# numero = int(input("Ingrese un número: "))
# intentos = 1
# numero_secreto = 5

# while numero != numero_secreto:
#     if intentos == 3:
#         print("Se te acabaron los intentos!")
#         break
#     else:
#         numero = int(input("Ingrese otro número: "))
#         intentos += 1
# else:
#     print("Adivinaste!")

# 17  
# Escribir un programa que pregunte al usuario números hasta que ingrese el 0, 
# en ese momento devolver la suma de todos los números ingresados
# 18  
# Escribir un progama que pida al usuario valores hasta que ingrese el 0, devolver 
# la suma de los números ingresados pero sin tener en cuenta los números que sean divisibles por 3

# numero = int(input("Ingrese un numero: "))
# acumulador = 0

# while numero != 0:
#     if numero % 3 == 0:
#         numero = int(input("Ingrese otro numero: "))
#         continue
#     acumulador += numero
#     numero = int(input("Ingrese otro numero: "))

# print(acumulador)


## - recorrer distintas coleciones, str, set, dict, list
# saludo = "Hola Mundo!"

# for i in saludo:
#     print(i)

# mi_conjunto = {"hola", 20, True, (10,20,30)}

# for elem in mi_conjunto:
#     print(elem)

# for i in range(10, 20, 3):
#     print(i)

## - else, break, continue
# mi_lista = [10,20,30,40,25,50,100]

# for n in mi_lista:
#     if n == 30:
#         continue
#     if n == 25:
#         break
#     print(n)
# else:
#     print("No había un 25 en la lista")

## - Ejercicio #9
# 9
# Dada la lista personas en mockups.py, pedir al usuario que ingrese una letra y devolver 
# una lista con los nombres de las personas que su nombre empieza con esa letra
# En el caso que no haya ninguno, devolver que no existe ningún nombre con esa letra 
# personas = [
#     {"id":1,"first_name":"Catha","last_name":"Carlton","city":"Qingshandi","email":"ccarlton0@twitter.com","gender":"Polygender"},
#     {"id":2,"first_name":"Toddie","last_name":"Ibeson","city":"San Juan","email":"tibeson1@freewebs.com","gender":"Bigender"},
#     {"id":3,"first_name":"Ashlee","last_name":"McAuslan","city":"São Jerônimo","email":"amcauslan2@pcworld.com","gender":"Polygender"},
#     {"id":4,"first_name":"Julie","last_name":"Fischer","city":"Lasusua","email":"jfischer3@ucoz.com","gender":"Agender"},
#     {"id":5,"first_name":"Manda","last_name":"Mapis","city":"Sindang","email":"mmapis4@foxnews.com","gender":"Non-binary"},
#     {"id":6,"first_name":"Noami","last_name":"Rubanenko","city":"Siemianowice Śląskie","email":"nrubanenko5@geocities.com","gender":"Genderfluid"},
#     {"id":7,"first_name":"Daffi","last_name":"Wherton","city":"Kamirenjaku","email":"dwherton6@privacy.gov.au","gender":"Bigender"},
#     {"id":8,"first_name":"Tamma","last_name":"Worsham","city":"Batang","email":"tworsham7@globo.com","gender":"Male"},
#     {"id":9,"first_name":"Gibby","last_name":"Blacktin","city":"Makarov","email":"gblacktin8@mac.com","gender":"Agender"},
#     {"id":10,"first_name":"Locke","last_name":"Pirdy","city":"Ketanggungan","email":"lpirdy9@wix.com","gender":"Polygender"},
#     {"id":11,"first_name":"Dorree","last_name":"Claypool","city":"Laborie","email":"dclaypoola@un.org","gender":"Female"},
#     {"id":12,"first_name":"Jermaine","last_name":"Duplan","city":"Chemin Grenier","email":"jduplanb@skype.com","gender":"Polygender"},
#     {"id":13,"first_name":"Kliment","last_name":"Divill","city":"Baochang","email":"kdivillc@tamu.edu","gender":"Agender"},
#     {"id":14,"first_name":"Bernice","last_name":"O'Hartnett","city":"Askainen","email":"bohartnettd@tripod.com","gender":"Genderqueer"},
#     {"id":15,"first_name":"Teirtza","last_name":"Summerlee","city":"Babakanbungur","email":"tsummerleee@scientificamerican.com","gender":"Agender"}
#     ]

# letra = input("Ingrese una letra: ")
# nombres = set()

# while len(letra) != 1:
#     letra = input("Ingrese UNA SOLA letra: ")

# letra = letra.upper()
# for persona in personas:
#     if persona["first_name"][0] == letra:
#         nombres.add(persona["first_name"])

# if nombres:
#     print(list(nombres))
# else:
#     print(f"No existe ningún nombre que empiece con {letra}")

## - Comprehensions
# mi_lista = []
# for i in range(1,50,3):
#     mi_lista.append(i)

# print(mi_lista)
# mi_lista = [ i for i in range(1,50,3) ]
# print(mi_lista)

# mi_lista = [ i*2 for i in range(1,50,3) ]
# print(mi_lista)

# mi_lista = [ i for i in range(1,50,3) if i % 2 == 0]
# print(mi_lista)

# mi_lista = [ (lambda x: x%8 == 0)(i) for i in range(1,50,3) if i % 2 == 0]
# print(mi_lista)

# palabra = "Anana"
# n_veces = { letra: palabra.count(letra) for letra in palabra }

# print(n_veces)

# palabra = "Anana"
# letras = { letra for letra in palabra }

# print(letras)

## Tuple comprehension NO existe! esto es un generador!
# mis_datos = ( i for i in range(1,50,3) )
# print(mis_datos)

# print(next(mis_datos))
# print(next(mis_datos))