# FUNCIONES

def miFuncion():
    print("Hola Mundo")


miFuncion()

def mostrarNomber(nombre , apellido):
    print("su nombre es: "+ nombre+ "  " + apellido)


mostrarNomber("Leidi" , "Lopez") #invocar la función

#datos de entrada

base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))

#proceso

def calcularAreaTriangulo (a, b):
    area = (b*a)/2
    return area

#salida
resultado = calcularAreaTriangulo(base, altura)
print("el area del triangula es: ", resultado)

def mostrarMensaje(pais="Colombia"):
    print( "Yo soy de :" +pais)

mostrarMensaje("Suiza")
mostrarMensaje("Ecuador")
mostrarMensaje()
mostrarMensaje("Bolivia")