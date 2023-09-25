from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Rectangulo(FiguraGeometrica):

    def __init__(self, base, altura):
        self._base = base
        self._altura = altura

    def area(self):
        return self._base * self._altura
    
    def perimetro(self):
        return 2*self._base + 2*self._altura

class Circulo(FiguraGeometrica):

    def __init__(self, radio):
        self._radio = radio

    def area(self):
        return 3.14 * (self._radio ** 2)

    def perimetro(self):
        return 2 * 3.14 * self._radio

# Esto lanzará error porque FiguraGeometrica es abstracta
figura = FiguraGeometrica()

rectangulo = Rectangulo(3, 4)
print(rectangulo.perimetro())
print(rectangulo.area())

circulo = Circulo(5)
print(circulo.perimetro())
print(circulo.area())
