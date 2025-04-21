#!/usr/bin/python3



def saluda(nombre=""):
    if(nombre != ""):
        print("Hola", nombre + "!")
    else:
        print("Hola!")


def suma(num1, num2):
    return num1 + num2

def despide(quien="Jacinto"):
    print("Estás despedido,", quien)

def retorna_multiple():
    uno = 1
    dos = 3
    return uno, dos



version = 0.5

app_title = "Playlist v" + str(version)

separacion = "-----------"

print(app_title)

print("-" * len(app_title))

if False:
    print("Cierto")
else:
    print("Falso")

primero = 5
segundo = 3

if primero > segundo:
    print("El primero es mayor que el segundo.")
elif segundo > primero:
    print("El segundo es mayor que el primero.")
else:
    print("Los dos numeros son iguales.")

contador = 10

while contador > 0:
    #print(contador)
    contador -= 1

print(separacion)

for num in range(1, 10): #range(INICIAL, FIN, PASOS) --> range(INICIAL) 
   # print(num)
   pass



personas = ["Jaimito", "Jacinto", 33, "Anselmito"]


for dato in personas:
    print(">", dato)


personaje = {# "clave":" valor"    Esto no es un array, clave no devuelve 0, 1, 2 sino que devuelve la clave.
    "nombre": "Paquito",
    "edad": 33,
    "pelo": "marrón"
 }

print(separacion)

print("Personaje:", personaje["nombre"])


for clave in personaje:
    print(">>", clave + ":", personaje[clave])


for clave, valor in personaje.items():
    print(">>>", clave +":", valor)



saluda()

print(suma(3, 5))

despide()
despide("Ramiro")

valor1, valor2 = retorna_multiple()

print(valor1, valor2)

nombre = input("¿Cómo te llamas?: ")

saluda(nombre)


