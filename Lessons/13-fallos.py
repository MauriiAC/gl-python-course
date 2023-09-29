## - Tipos de fallos: errores, excepciones
## - Sintacticos
## - Excepciones, runtime
## - Comprobaciones para evitar errores

# print("Iniciando")

# n = int(input("Ingrese un numero: "))
# mi_lista = [10,20,30,40]

# for i in range(n):
#     if mi_lista:
#         print(mi_lista.pop())
#     else: 
#         break

# print("Continuo con la ejecución")

## - Capturar errores
## - else, finally, varias excepciones, aserciones custom

print("Iniciando")

def imc(peso, altura):

    assert peso > 0, "El peso debe ser mayor a 0"
    assert altura > 0, "La altura debe ser mayor a 0"
    return peso / altura**2

while True:
    try:
        peso = float(input("Ingrese su peso: "))
        altura = float(input("Ingrese su altura: "))
        res_imc = imc(peso, altura)
        print(res_imc)
    except ValueError as e:
        print("La altura y peso deben ser datos numéricos")
    except ZeroDivisionError as e:
        print("La altura debe ser mayor a 0")
    except AssertionError as e:
        print(e)
    except Exception as e:
        print(type(e).__name__)
        print("Ingresó valores incorrectos, intentelo de nuevo")
    else:
        print("Todo anduvo bien!")
        break
    finally:
        print("Se finalizó un intento")

print("Continuo con la ejecución")


