from abc import ABC, abstractmethod
from enum import Enum

class TipoFigura(Enum):
    RECTANGULO = 1
    CIRCULO = 2

    def __str__(self):
        match self:
            case TipoFigura.RECTANGULO:
                return "Rectangulo"
            case TipoFigura.CIRCULO:
                return "Circulo"
            case _:
                return super().__str__()


class FiguraGeometrica(ABC):

    def __init__(self, tipo: TipoFigura):
        self._tipo = tipo

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def __str__(self) -> str:
        return f'{self._tipo} de {self.area()}'
    
    def __repr__(self) -> str:
        return f'{self._tipo} de {self.area()}'

class Rectangulo(FiguraGeometrica):

    def __init__(self, base, altura):
        super().__init__(TipoFigura.RECTANGULO)
        self._base = base
        self._altura = altura

    def area(self):
        return self._base * self._altura
    
    def perimetro(self):
        return 2*self._base + 2*self._altura

class Circulo(FiguraGeometrica):

    def __init__(self, radio):
        super().__init__(TipoFigura.CIRCULO)
        self._radio = radio

    def area(self):
        return 3.14 * (self._radio ** 2)

    def perimetro(self):
        return 2 * 3.14 * self._radio

# Esto lanzará error porque FiguraGeometrica es abstracta
# figura = FiguraGeometrica()

rectangulo = Rectangulo(30, 4)
print(rectangulo.perimetro())
print(rectangulo.area())
print(rectangulo._tipo)

circulo = Circulo(5)
print(circulo.perimetro())
print(circulo.area())
print(circulo._tipo)

from collections.abc import Callable

class Ordenador():

    ordenables = [FiguraGeometrica, int, str]

    def __call__(self, x: object):
        if not any(isinstance(x, cls) for cls in Ordenador.ordenables):
            raise TypeError(f'{x.__class__} no se puede ordenar')
        match x:
            case FiguraGeometrica():
                return x.area()
            case int(x):
                return x
            case str(x):
                return len(x)

ordenador = Ordenador()

ordenador: Callable = Ordenador()

words = ["hola", "hi", "dinosaurio", "elefante"]  
words.sort(key=ordenador)
print(words)

figuras = [rectangulo, circulo]
figuras.sort(key=ordenador)
print(figuras)

# --> Arroja un error ya que no ordena flotantes
flotantes = [20.32, 10.5, 8.54, 9.42]
flotantes.sort(key=ordenador)
print(flotantes)

# --> Ordena mezclando criterios
datos = ["hola", 20, circulo]
datos.sort(key=ordenador)
print(datos)

datos: list[int] = ["hola", 20, circulo]
datos.sort(key=ordenador)
print(datos)