print("######################################")
print("#     ESTRUCTURAS SELECTIVAS         #")
print("######################################")
print( "Estructura IF")

x = 15
if x > 10:
    print("x es mayor que 10")
print("######################################")
print( "Estructura ELSE")

x = 150
if x > 180:
    print("x es mayor que 150")
else:
    print("x es menor o igual que 150")

print("######################################")
print( "Estructura ELIF")
mes = input("Ingrese un mes (en minúsculas): ")

if mes == "enero" or mes == "marzo" or mes == "mayo" or mes == "julio" or mes == "agosto" or mes == "octubre" or mes == "diciembre":
    print("El mes tiene 31 días")
elif mes == "febrero":
    print("El mes tiene 28 o 29 días, dependiendo del año")
else:
    print("El mes tiene 30 días")
############################################################################################################
print("######################################")
print( "ESTRUCTURAS REPETITIVAS")
print("######################################")

print( "Estructura FOR")

for i in range(1, 11):
    print(i)

print("######################################")

print( "Estructura WHILE")

i = 1
while i <= 10:
    print(i)
    i += 1

print("######################################")