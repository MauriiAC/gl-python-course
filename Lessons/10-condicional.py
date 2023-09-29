## - Flujo de control
# https://juegosrobotica.es/wp-content/uploads/diagrama-de-flujo-cafe.jpg


## - Sintaxis del condicional
## - Anidamiento
# nombre = input("Ingrese su nombre: ")

# if nombre:
#     print(f'Hola {nombre}')
#     print("otro print dentro del bloque")

# print("chau")

# if len(nombre)>5:
#     print("Su nombre es largo")
#     if nombre[0] == 'A':
#         print("Tu nombre empieza con A")
# if nombre == nombre.capitalize():
#     print("Tu nombre está bien escrito")

# print("Finalizando programa..")



## - elif, else
# edad = int(input("Ingrese su edad: "))

# if edad < 18:
#     print("Tienes toda una vida por delante!")
# elif edad < 30:
#     print("Trabaja duro por tu futuro!")
# elif edad < 60:
#     print("Disfruta lo que has logrado!")
# else:
#     print("Que bueno seguir compartiendo contigo!")


# ## - autocasting
# nombre = input("Ingrese nombre: ")
# if nombre:
#     print(f'Hola {nombre}')
#     print("otro print dentro del bloque")

# if []:
#     print("Hola")

# print(bool([]))

## - condiciones con operadores lógicos

# nombre = input("Ingrese nombre: ")

# if len(nombre)>5:
#     if nombre[0] == 'A':
#         print("Tu nombre empieza con A y es largo")

# if len(nombre)>5 and nombre[0] == 'A':
#     print("Tu nombre empieza con A y es largo")


## - pass
# nombre = input("Ingrese nombre: ")
# if len(nombre) > 5:
#     pass

# print("Continuo con la ejecución del programa")

## - Ejercicios #11 al #15
# Pedir al usuario que ingrese una palabra y devolver un msj diciendo si la misma es capicua o no

# palabra = input("Ingrese una palabra: ")

# palabra = palabra.upper()

# if palabra == palabra[::-1]:
#     print("Su palabra es capicua!")
# else:
#     print("La palabra NO es capicua")

# 14  
# Pedir al usuario que ingrese un número
# Si el número es divisible por 3 imprimir {"El número es divisible por 3"} 
# Si el número es divisible por 7 imprimir {"El número es divisible por 7"} 
# Si el número es divisible por 3 y por 7 a la vez imprimir {"El número es divisible por 3 y por 7"}
# Si el número no es divisible ni por 3 ni por 7 imprimr {"El número no es divisible ni por ni por 7"} 

# numero = int(input("Ingrese un numero: "))

# if numero % 3 == 0 and numero % 7 == 0:
#     print("El número es divisible por 3 y por 7")
# elif numero % 3 == 0:
#     print("El número es divisible por 3")
# elif numero % 7 == 0:
#     print("El número es divisible por 7")
# else:
#     print("El número NO es divisible por ni 3 ni por 7")


# 15  
# Dada la tupla #1 de resources.py, pedir al usuario que ingrese un nombre de una ciudad, 
# devolver si se encuentra en la primer o segunda mitad de la tupla, según el indice que define su posición.
# Si se encuentra exactamente en el medio, imprimir {"Se encuentra en el medio de la tupla"}
# Si la ciudad no se encuentra en el listado, imprimir {"No se encuentra {nombre ciudad} en la lista"}

ciudades = (
    "San Jorge", "Quitilipi", "Granadero Baigorria", "Alderetes", "Gualeguay", "Chimbas", "Rada Tilly", "Cote-Lai", "Elena", "Yerba Buena", "Laboulaye", "La Rioja", "Castelli", "Aminga", "Isla Verde", "Pirane", "General Enrique Godoy", "Alumine", "Rio Pico", "Sampacho", "Villa de Soto", "Embarcacion", "Caseros", "Jesus Maria", "Salta", 
    "Esquina", "Barcelona",
    "Puerto Iguazu", "Mercedes", "Castelli", "Cinco Saltos", "El Bolson", "Tamberias", "Guernica", "Doblas", "Villa Santa Rita", "Mercedes", "Carlos Casares", "Vera", "Zapala", "Santa Ana", "Libertador General San Martin", "Villa Maria", "Basail", "Gualeguay", "Villa La Angostura", "Basail", "San Lorenzo", "Tostado", "Libertad", "General Conesa", "General Pico"
    )

"""
1   2   3   4   5   6

3 --> 2
4 --> 2.5
5 --> 3
6 --> 3.5
"""

ciudad = input("Ingrese la ciudad a buscar: ")
posicion = -1

if ciudad in ciudades:
    posicion = ciudades.index(ciudad)+1

if posicion == -1:
    print(f"No se encuentra {ciudad} en la lista")
elif posicion > (len(ciudades)+1)/2:
    print("La ciudad se encuentra en la segunda mitad")
elif posicion < (len(ciudades)+1)/2:
    print("La ciudad se encuentra en la primer mitad")
else:
    print("La ciudad se encuentra en el centro")