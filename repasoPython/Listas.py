print("######################################")
print("#             LISTAS                 #")
print("######################################")
print("Crear una lista")
print("######################################")
frutas = ["manzana", "banana", "naranja", "kiwi", "pera", "mango", "papaya", "fresa"]
print(frutas)
print("######################################")
print("Acceder a elementos de una lista")
print("######################################")
frutas = ["manzana", "banana", "naranja", "kiwi", "pera", "mango", "papaya", "fresa"]
print(frutas[0])
print(frutas[-1])
print("######################################")
print("Agregar elementos a una lista")
print("######################################")
frutas = ["manzana", "banana", "naranja", "kiwi", "pera", "mango", "papaya", "fresa"]
frutas.append("piña")
print(frutas)
print("######################################")
print("Recorrer una lista con un bucle")
print("######################################")
frutas = ["manzana", "banana", "naranja", "kiwi", "pera", "mango", "papaya", "fresa"]
for fruta in frutas:
    print(fruta)
print("######################################")
print("Eliminar elementos de una lista")
print("######################################")
frutas = ["manzana", "banana", "naranja", "kiwi", "pera", "mango", "papaya", "fresa"]
frutas.remove("fresa")
print(frutas)