## - clases abstractas

def suma(a, b):
    if type(a) == str:
        raise 'no puede ser un str'
    return a + b

print(suma("hola", 2))