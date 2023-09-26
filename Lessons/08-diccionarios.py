## - Sintaxis
# persona1 = {
#     "name": "Mauricio", 
#     "last_name": "Cuello", 
#     "age": 32
# }
# persona2 = {"name": "Lionel", "last_name": "Messi", "age": 36}

## - Recuperar un valor
# print(persona1["age"])
# print(persona1["name"])
# print(persona2["name"])

## - Mutabilidad

# persona1["age"] = 35
# persona1["age"] += 1
# print(persona1)

## - Funciones integradas
# persona1["name"] = "Pepe"
# print(persona1)
# persona1["email"] = "pepe@gmail.com"
# print(persona1)

# persona1.update({
#     "email": "mauricio@gmail.com",
#     "dni": "30123123",
#     "age": 40
# })

# persona1.update([
#     ("email", "mauricio@gmail.com"),
#     ("dni", "30123123"),
#     ("age", 40)
# ])

# persona1 = {
#     "name": "Mauricio", 
#     "last_name": "Cuello", 
#     "age": 32
# }

# print("last_name" in persona1)
# del persona1["last_name"]
# print("last_name" in persona1)

# persona1.pop("age")

# print(persona1)


