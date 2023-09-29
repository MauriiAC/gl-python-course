## - Fundamento de la POO
  # Bloques de código excesivamente grandes
  # Modularización
  # Código difícil de interpretar (cod spaguetti)
  # Difícil de depurar y escalar
  # Difícil la reutilización
  # Los errores posiblemente provocaban el crush de la aplicación
  # Complejo el control de la interacción con usuarios
  # Encapsulamiento

## - Como se piensa con POO? identindad, caract, funcionalidades --> instancia, atributos, métodos


## - Diagrama de clase
# http://diagramaweb.com/wp-content/uploads/2020/08/diagrama-de-clases-tipos-1024x606.png


## - partes importantes: clase, objetos, metodo constructor, self, atributos de instancia


## - primer ejemplo
# class Persona():

#     def __init__(self, nom, ape, ed, amigos):
#         self.nombre = nom
#         self.apellido = ape
#         self.edad = ed
#         self.amigos = amigos

#     def saluda(self):
#         return f'Hola, mi nombre es {self.nombre} {self.apellido}'
    
#     def listar_amigos(self):
#         mis_amigos = []
#         for p in self.amigos:
#             mis_amigos.append(p.nombre)
#         lista_nombres = ' '.join(mis_amigos)
#         return f'Soy amigo de {lista_nombres}'


# messi = Persona("Lionel", "Messi", 36, None)
# cristiano = Persona("Cristiano", "Ronaldo", 39, None)
# riquelme = Persona("Roman", "Riquelme", 43, None)
# mauricio = Persona("Mauricio", "Cuello", 32, [messi, cristiano, riquelme])

# print(mauricio.listar_amigos())


# class Perro():

#     patas = 4
#     def __init__(self, nombre, raza, edad):
#         self.nombre = nombre
#         self.raza = raza
#         self.edad = edad

#     def ladrar(self, cant):
#         return 'guau'*cant
    
# perro1 = Perro("Aura", "caniche", 5)
# perro2 = Perro("Cachito", "dalmata", 2)
# print(Perro.patas)
# print(perro2.patas)
# perro2.patas = 3
# print(Perro.patas)
# print(perro1.patas)
# print(perro2.patas)


## - métodos de instancia
## - atributo de clase vs atributo de instancia, metodos con 
## - encapsulamiento, modificación controlada

class Persona():

    cant_cerebros = 1

    def __init__(self, nom, ape, ed, perro=None):
        self.nombre = nom
        self.apellido = ape
        self.__edad = ed
        self.__perro = perro

    def saluda(self):
        return f'Hola, mi nombre es {self.nombre} {self.apellido}'
    
    def get_edad(self):
        return self.__edad
    
    def get_perro(self):
        return self.__perro

    def cumple_agno(self):
        self.__edad += 1
    
    def set_meta(self, meta):
        self.meta = meta

    def camina(self, pasos):
        if pasos > self.meta:
            return f'Felicidades {self.nombre}, cumpliste tu meta!'
        else:
            return 'No lograste tu meta, ponete las pilas!'
        
class Perro():

    patas = 4
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def ladrar(self, cant):
        return 'guau'*cant

# name mangling

# messi.set_meta(5000)
# cristiano.set_meta(4000)
# print(messi.camina(4500))
# print(cristiano.camina(4500))
# messi = Persona("Lionel", "Messi", 36)
# cristiano = Persona("Cristiano", "Ronaldo", 39)
# print(messi.get_edad())
# messi.cumple_agno()
# print(messi.get_edad())

# ## - relación entre clases
# perro1 = Perro("Aura", "caniche", 5)
# perro2 = Perro("Cachito", "dalmata", 2)
# persona1 = Persona("Mauricio", "Cuello", 32, perro1)

# print(persona1.get_perro().nombre)

## - ejercicio de tickets
# 15-tickets.py