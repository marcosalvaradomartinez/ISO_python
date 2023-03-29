import msvcrt
from os import system

# lista=[]
# lista.append("Hola") #para añadir elementos a la variable lista
# lista.append("Adeu adeu")
# print(lista)
# print("En la posicion 0 hay", lista[0]) #[] sirve para indicar la posición a la que se quiere acceder

# for i in range (len(lista)):
#     print("Elemento", lista[i])

# for elemento in lista:
#     print(elemento)

def pide(letra):
    numero=""
    while not(numero.isnumeric()):
        print("Vas a poner valor a", letra)
        numero=input("Introduce un número:")
    return int(numero)

def menu():
    print("MENÚ: ")
    print("a) Introduce un valor en la lista")
    print("b) Mostrar lista")
    print("i) Salir")

def mostrar():
    print("Los elemetos de la lista son=", lista)
    msvcrt.getch()

lista=[]
entrada=""
while entrada != "i":
    menu()
    entrada=input("Selecciona una opción:")
    if entrada == "a":
        lista.append(input("Introduce una opción:"))
    if entrada == "b":
        mostrar()
