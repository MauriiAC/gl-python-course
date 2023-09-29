## - clases abstractas, que son? simil interfaces
## - primer clase abstracta
## - implementación de la clase abstracta en clases concretas
## - clase ENUM

from abc import ABC, abstractmethod
from enum import Enum

dato = "Mauricio"

class TipoFigura(Enum):
    RECTANGULO = 1
    CIRCULO = 2

    def __str__(self):

        match self:
            case TipoFigura.RECTANGULO:
                return "Tipo Rectangulo"
            case TipoFigura.CIRCULO:
                return "Tipo Circulo"
            case _:
                return super().__str__()

class FiguraGeometrica(ABC):

    def __init__(self, tipo):
        self._tipo = tipo

    def pintar(self, color):
        return f'Coloreando la figura con el color {color}'

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def __repr__(self):
        return f'{self.__class__.__name__} de {self.area()}'

class Rectangulo(FiguraGeometrica):

    def __init__(self, base, altura):
        super().__init__(TipoFigura.RECTANGULO)
        self._base = base
        self._altura = altura

    def __str__(self):
        return f'Rectangulo de {self._base} por {self._altura}'
    
    def perimetro(self):
        return 2*self._base + 2*self._altura
    
    def area(self):
        return self._base * self._altura

class Circulo(FiguraGeometrica):

    def __init__(self, radio):
        super().__init__(TipoFigura.CIRCULO)
        self._radio = radio

    def perimetro(self):
        return 2 * 3.14 * self._radio
    
    def area(self):
        return 3.14 * self._radio**2
    

rectangulo1 = Rectangulo(5,4)
rectangulo2 = Rectangulo(2,3)
circulo1 = Circulo(5)
circulo2 = Circulo(10)
# print(rectangulo1.perimetro())
# print(circulo1.perimetro())
# print(circulo1.pintar("verde"))

# print(rectangulo1._tipo)
# print(circulo1._tipo)


## - clase abstracta para asegurar caracteristicas - ej callable

class Ordenador():

    ordenables = [int, str, FiguraGeometrica]

    def __call__(self, x):
        if not any( isinstance(x, cls) for cls in Ordenador.ordenables):
            raise TypeError(f'{x.__class__} no se puede ordenar')
        match x:
            case FiguraGeometrica():
                return x.area()
            case int(x):
                return x
            case str(x):
                return len(x)

from collections.abc import Callable

ordenador1: Callable = Ordenador()

# words = ["hola", "hi", "dinosaurio", "elefante"]
# numbers = [5, -4, 11, 3, 21, 0, 10]
# figuras = [circulo1, rectangulo1, circulo2, rectangulo2]
datos: list[int] = ["hola", 20, circulo1, 2.5]

try:
    datos.sort(key=ordenador1)
except Exception as e:
    print(e)

# print(datos)


## - blackjack project
"""
Juego
- Se le entregan dos cartas al jugador y una a la casa
- Mientras el jugador tenga menos de 21 puntos se le pregunta si desea recibir otra carta
- Cuando el jugador deja de pedir cartas y se pasa de 21 se empieza a dar cartas a la casa
- La casa recibirá cartas hasta que alcance al menos los 17 puntos, si el jugador se pasó
  de 21 puntos, la casa gana con llegar a 17, sino puede haber un empata si la casa iguala
  los puntos del jugador, si los supera sin pasarse de 21 gana la casa, y si se pasa de 21
  gana el jugador

  _suit_to_unicode = {
    'spades': '♠', 
    'diamonds': '♦',
    'clubs': '♣',
    'hearts': '♥'
  }

"""


## - @dataclass