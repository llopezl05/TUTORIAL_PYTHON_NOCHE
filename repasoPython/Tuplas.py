print("######################################")
print("#              TUPLAS                #")
print("######################################")
print("Crear una tupla")
numeros = (1, 2, 3, 4, 5)
print(numeros)
print("######################################")
print("Acceder a elementos de una tupla")
numeros = (1, 2, 3, 4, 5)
print(numeros[0])
print(numeros[-1])
print("######################################")
print("Convertir una lista en una tupla")
utiles = ["lapicero", "borrador", "cuaderno", "sacapuntas", "marcador", "colores"]
tupla_utiles = tuple(utiles)
print(tupla_utiles)
print("######################################")
print("Desempaquetar una tupla")
coordenadas = (20, 90)
x, y = coordenadas
print("x =", x)
print("y =", y)
print("######################################")
print("Utilizar tuplas en una función")
def dividir(numero1, numero2):
    cociente = numero1 // numero2
    resto = numero1 % numero2
    return (cociente, resto)

resultado = dividir(1596, 8)
print(resultado)

print("######################################")