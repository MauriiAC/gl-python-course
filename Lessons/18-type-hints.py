## TypedDicts [TO DO]

from typing import List, Dict, Tuple, Optional, Union, TypedDict, Literal, TypeVar, Generic, Callable, NoReturn


# # Especificar tipado para una función:
# def saludar(name: str, edad: int) -> str:
#   return f'Hola me llamo {name}, y el año que viene tendré {edad+1} años'

# print(saludar("Mauricio", 32))

# # Especificar tipado para variables:
# # Variable de tipo lista de strings
# names: List[str] = ['Mauricio', 'Lionel', 'Cristiano']
# names: List[str | int] = ['Mauricio', 'Lionel', 'Cristiano', 10]

# # Variable de tipo diccionario con key str y value int
# ages: Dict[str, int] = {'Mauricio': 32, 'Lionel': 36, "Cristiano": 39}
# ages: Dict[str, int | None] = {'Mauricio': 32, 'Lionel': 36, "Cristiano": None}

# #Variable con un número indeterminado de int
# numbers: Tuple[int, ...] = (10, 20, 30, 40)

# #Variable con un exactamente dos int
# point: Tuple[int, int] = (10, 20)

# Especificar tipado para clases:
# class Person:
#   def __init__(self, name: str, age: int):
#     self.name = name
#     self.age = age

# # Especificar argumentos opcionales con Optional:
# def fullname(first_name: str, last_name: str, middle_name: Optional[str] = None) -> str:
#   if middle_name:
#     return f'{first_name} {middle_name} {last_name}'
#   else:
#     return f'{first_name} {last_name}'

# # Permitir múltiples tipos con Union or |:  
# def suma(data: Union[List[int], Dict[str, int]]) -> int:
#   if isinstance(data, dict):
#     return sum(data.values())
#   else:
#     return sum(data)

# agesDict = {
#   "Mauricio": 32,
#   "Lionel": 36,
#   "Cristiano": 39
# }
# agesList = [32,36,39]
# print(suma(agesDict))
# print(suma(agesList))


# # Restricciones de valor con Literal:
# dato = "hard"
# diffculty: Literal['easy', 'medium', 'hard'] = dato

# dato: Literal['hard'] = "hard"
# diffculty: Literal['easy', 'medium', 'hard'] = dato


"""
Otros tips:

Usar Tuple para valores de retorno múltiples
Alias de tipos con typing.TypeAlias
Clases abstractas con typing.Protocol
Tipos de datos NumPy con typing.Array
El módulo typing es muy potente para documentar código y mejorar la calidad. ¡Recomiendo explorar la documentación oficial!
"""


# # Tipos genéricos con TypeVar
T = TypeVar('T', int, str)

# def first_element(l: List[T]) -> T:
#   return l[0]

# a = first_element([1, 2, 3]) # ok, lista de enteros
# b = first_element(["a", "b", "c"]) # ok, lista de cadenas 
# c = first_element([20.5, 5.41, 2.32]) # error, lista de float
# d = first_element([1, "a", 2]) # error, lista mixta


# # Clases genéricas 
# class Stack(Generic[T]):
#   def __init__(self) -> None:
#     self._container: List[T] = []
  
#   def push(self, item: T) -> None:
#     self._container.append(item)

#   def pop(self) -> T:
#     return self._container.pop()

#   def __repr__(self) -> str:
#     return repr(self._container)

# # Retornar self para encadenar 
# class MyClass:
#   def method(self) -> 'MyClass': 
#     print('Called method')
#     return self

# Tipado de decoradores
def log_call(func: Callable[..., T]) -> Callable[..., T]:
  def wrapper(*args, **kwargs):
    print(f'Calling {func.__name__}')
    return func(*args, **kwargs)
  return wrapper

@log_call
def process_data(data):
  print('Processing', data)

process_data([10,20,30])


# """
# Otros tips avanzados:

# Uso de typing.overload para sobrecarga de métodos
# Metaclases genéricas con typing.GenericMeta
# Tipado de callbacks asíncronos con asyncio.coroutine
# ¡Espero estos ejemplos te sirvan para explotar typing al máximo! Házme saber si necesitas más info.
# """


# Especifico campos de un diccionario con TypedDict
class Movie(TypedDict):
    name: str
    year: int
    ratings: list[float]

movie = Movie(
    name="Inception", 
    year=2008,
    ratings=[8, 9, 7]  
)

print(movie["name"])
print(movie["year"])
print(movie["ratings"])