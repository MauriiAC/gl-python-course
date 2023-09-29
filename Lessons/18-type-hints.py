## TypedDicts
from typing import List, Dict, Tuple, Optional, Union, Literal, TypeVar, TypedDict

# # # Especificar tipado para una función:
# def saludar(name: str, edad: int) -> str:
#     return f'Hola, me llamo {name}, y el año que viene tendré {edad+1} años'

# print(saludar("Mauricio", 32))

# ## - Especificar tipado para variables:
# datos1 = ["Mauricio", "General Pico", "31351351"]
# datos2: List[str | bool] = ["Mauricio", "General Pico", "31351351", True]

# ages1: Dict[str, int] = {"Mauricio": 32, "Lionel": 36, "Cristiano": 38}
# ages2: Dict[str, int | None] = {"Mauricio": 32, "Lionel": 36, "Cristiano": None}

# numbers: Tuple[int, ...] = (10,20,30,40,50)
# numbers2: Tuple[int, int, int] = (5,15,25)

# ## - Especificar tipado para clases:
# class Persona():

#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

# persona1 = Persona("Mauricio", 32)

# ## - Especificar argumentos opcionales con Optional:
# def full_name(first_name: str, last_name: str, middle_name: Optional[str] = None) -> str:
#     if middle_name:
#         return f'{first_name} {middle_name} {last_name}'
#     else:
#         return f'{first_name} {last_name}'


## - Permitir múltiples tipos con Union or |:  
# def suma(data: Union[List[int], Dict[str, int]]) -> int:
#     if isinstance(data, dict):
#         return sum(data.values())
#     else:
#         return sum(data)

# print(suma({
#     "value1": 10,
#     "value2": 20,
#     "value3": 30,
# }))

## - Restricciones de valor con Literal:

dato: Literal["hard"] = 'hard'
dificultad: Literal['easy', 'medium', 'hard'] = dato

# ## - Tipos genéricos con TypeVar
# T = TypeVar('T', int, str)

# def first_element(l: List[T]) -> T:
#     return l[0]

# a = first_element([10,20,30])
# b = first_element(["10","20","30"])
# c = first_element([5.5, 2.3, 4.8])
# d = first_element([1, "aaa", 5])

## - Tipado de decoradores


# ## - Campos de un diccionario con TypedDict
# class Movie(TypedDict):
#     name: str
#     year: int
#     ratings: list[float]

# movie = Movie(
#     name="Inception",
#     year=2007,
#     ratings=[8,7,9,9,10,8]
# )

# name = movie['name'] 
# year = movie['year'] 

# print(2023 - year)
