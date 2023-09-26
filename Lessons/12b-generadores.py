"""65
Generadores: función especial que permite generar una secuencia de valores sobre la marcha, en lugar de generarlos todos a la vez y devolverlos en una lista.
    
    Se define como una función normal, pero usando la palabra clave yield en lugar de return para devolver valores.
    Cuando se llama al generador, este devuelve un objeto iterable pero no ejecuta ningún código en ese momento.
    Cada vez que se solicita el siguiente valor al generador (llamando a next()), este se ejecuta hasta el próximo yield, generando un nuevo valor.
    Un generador puede contener tantos yield como sean necesarios para producir todos los valores que queremos generar.
    Cuando el generador termina, se levanta automáticamente una excepción StopIteration para indicar que se terminó la secuencia.

"""

## - lista vs generadores