## - @property 
## - @attr.setter
## - @attr.deleter
# class Persona():

#     cant_cerebros = 1

#     def __init__(self, nombre, apellido, edad):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.__edad = edad

#     @property
#     def edad(self):
#         return self.__edad
    
#     @edad.setter
#     def edad(self, nueva_edad):
#         if isinstance(nueva_edad, int) and nueva_edad > 0:
#             self.__edad = nueva_edad
#         else:
#             print("La edad debe ser un entero positivo")
    
#     @edad.deleter
#     def edad(self):
#         del self.__edad

# persona1 = Persona("Mauricio", "Cuello", 32)

# print(persona1.edad)
# persona1.edad = "holisss"
# print(persona1.edad)
# persona1.edad = 33
# print(persona1.edad)
# del persona1.edad
# print(persona1.edad)

## - métodos de clase

# class Persona():

#     __siguiente_id = 1

#     def __init__(self, nombre, apellido, edad):
#         self.__nombre = nombre
#         self.__apellido = apellido
#         self.__edad = edad
#         self.__id = Persona.__siguiente_id
#         Persona.__siguiente_id += 1

#     def __str__(self):
#         return(
#             f"Id: {self.__id}\n"
#             f"Nombre: {self.__nombre}\n"
#             f"Apellido: {self.__apellido}\n"
#         )
    
#     # def get_siguiente_id(self):
#     #     print(self.__nombre)
#     #     return Persona.__siguiente_id    
    
#     @classmethod
#     def get_siguiente_id(cls):
#         return cls.__siguiente_id

# persona1 = Persona("Mauricio", "Cuello", 32)
# persona2 = Persona("Lionel", "Messi", 36)
# persona3 = Persona("Cristiano", "Ronaldo", 39)

# print(persona1)
# print(persona2)
# print(persona3)

# # print(persona1.get_siguiente_id())
# print(Persona.get_siguiente_id())

## - métodos especiales, dunder methods

class Vector():

    def __init__(self, data):
        self._data = data

    def __str__(self):
        return f'Los valores son: {self._data}'

    def __len__(self):
        return len(self._data)
    
    def __getitem__(self, pos):
        return self._data[pos]
    
    def __setitem__(self, pos, value):
        self._data[pos] = value

    def __iter__(self):
        for pos in range(0, len(self._data)):
            yield f'Value: {self._data[pos]}'
    
v = Vector( [10,20,30] )
# print(v)
# print(len(v))
# v[0] = 5
# print(v)
# print(v[0])

# for num in v:
#     print(num)


## - herencia

# class Persona():

#     def __init__(self, nombre, apellido, edad, dni):
#         self.__nombre = nombre
#         self.__apellido = apellido
#         self.__edad = edad
#         self.__dni = dni

#     def saluda(self):
#         return f'Hola, me llamo {self.__nombre} {self.__apellido}'
    
#     def get_nombre(self):
#         return self.__nombre

#     def get_apellido(self):
#         return self.__apellido

# class Empleado(Persona):

#     def __init__(self, nombre, apellido, edad, dni, sueldo, horario):
#         super().__init__(nombre, apellido, edad, dni)
#         self.__sueldo = sueldo
#         self.horario = horario

#     def saluda(self):
#         return(
#             f'Buen día, soy {self.get_nombre()} {self.get_apellido()}'
#             f'y gano {self.__sueldo} euros'
#         )

#     def fichar(self, horario_ingreso):
#         if horario_ingreso < self.horario:
#             return f'Llegué {self.horario - horario_ingreso} minutos temprano'
#         else:
#             return f'Llegué {horario_ingreso - self.horario} minutos tarde'


# class Seguridad(Empleado):

#     def __init__(self, nombre, apellido, edad, dni, sueldo, horario, vehiculo, arma):
#         super().__init__(nombre, apellido, edad, dni, sueldo, horario)
#         self.vehiculo = vehiculo
#         self.arma = arma


#     def llamar_policia(self, mensaje):
#         return f'Llamo a la policía y le digo que {mensaje}'

# persona1 = Persona("Mauricio", "Cuello", 32, "123123")
# empleado1 = Empleado("Cristiano", "Ronaldo", 38, "303030", 2200, 420)
# seguridad1 = Seguridad("Lionel", "Messi", 36, "545454", 2700, 360, "Fiat 600", "AK-47")

# print(persona1.saluda())
# print(empleado1.saluda())
# print(seguridad1.saluda())

# print(empleado1.fichar(430))
# print(seguridad1.fichar(345))

## - polimorfismo
## - duck typing

# class CosaQueSaluda():

#     def __init__(self, nombre):
#         self.nombre = nombre

#     def saluda(self):
#         return 'Soy una cosa saludando!'

# cosa1 = CosaQueSaluda("Cosa")

# saludadores = [persona1, empleado1, seguridad1, cosa1]

# for saludador in saludadores:
#     print(saludador.saluda())

## - monkey patching
# class Persona():

#     def __init__(self, nombre, apellido, edad, dni):
#         self._nombre = nombre
#         self._apellido = apellido
#         self.__edad = edad
#         self._dni = dni

#     def saluda(self):
#         return f'Hola, me llamo {self._nombre} {self._apellido}'
    
# persona1 = Persona("Mauricio", "Cuello", 32, "123123")

# # print(dir(persona1))

# def saluda2(self):
#     return f'Hola, soy {self._nombre} {self._apellido} y tengo {self._Persona__edad} años'

# print(persona1.saluda())

# Persona.saluda = saluda2

# print(persona1.saluda())

## - herencia multiple

class Mamifero():

    def __init__(self, cant_mamas, esp_vida):
        self.cant_mamas = cant_mamas
        self.esp_vida = esp_vida
        self.peso = 0.5
        self.vivo = False

    def nacer(self):
        self.vivo = True

    def alimentarse(self, tiempo):
        self.peso += tiempo * 2

class AnimalMarino():

    def __init__(self, tiene_branqueas, especie):
        self.tiene_branqueas = tiene_branqueas
        self.especie = especie

    def nadar(self):
        return "Estoy nadando..."
    
class Cetaceo(Mamifero, AnimalMarino):

    def __init__(self, cant_mamas, esp_vida, especie, habitat):
        Mamifero.__init__(self, cant_mamas, esp_vida)
        AnimalMarino.__init__(self, False, especie)
        self.habitat = habitat

    # def nadar(self):
    #     return "Nadando como un cetaceo.."
    
cetaceo1 = Cetaceo(6, 120, False, "Ballenato", "Aguas calidas")

# print(Cetaceo.__mro__)

# print(cetaceo1.vivo)
# cetaceo1.nacer()
# print(cetaceo1.vivo)
# print(cetaceo1.peso)
# cetaceo1.alimentarse(4)
# print(cetaceo1.peso)
# print(cetaceo1.nadar())


