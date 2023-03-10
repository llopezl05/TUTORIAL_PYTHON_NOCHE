print("######################################")
print("#          DICCIONARIOS              #")
print("######################################")
print("Crear un diccionario")
persona = {"nombre": "Leidi", "edad": 28, "ciudad": "Popayan"}
print(persona)
print("######################################")
print("Acceder a un valor en un diccionario")
persona = {"nombre": "Leidi", "edad": 28, "ciudad": "Popayan"}
print(persona["nombre"])
print("######################################")
print("Añadir un elemento  un diccionario")
persona = {"nombre": "Leidi", "edad": 28, "ciudad": "Popayan"}
persona["telefono"] = "018000652"
print(persona)
print("######################################")
print("Recorrer un diccionario")
persona = {"nombre": "Leidi", "edad": 28, "ciudad": "Popayan"}
for clave, valor in persona.items():
    print(clave, "=", valor)
print("######################################")
print("Utilizar un diccionario en una función")
def calcular_precio(producto, cantidades):
    precios = {"Computador": 15000000, "TV": 1800000, "Labadora": 1700000}
    precio_unitario = precios[producto]
    precio_total = precio_unitario * cantidades
    return precio_total

producto = "TV"
cantidad = 20
precio = calcular_precio(producto, cantidad)
print("El precio de", cantidad, producto + "s es", precio, "$Pesos.")