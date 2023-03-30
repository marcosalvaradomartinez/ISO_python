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

def menu():
    print("MENÚ: ")
    print("a) Introduce un valor en la lista")
    print("b) Mostrar lista")
    print("c) Recuento de los elementos de la lista")
    print("d) Sumar los elementos de la lista")
    print("e) Hacer la media de los elementos de la lista")
    print("i) Salir")

def pide():
    numero=""
    while not(numero.isnumeric()):
        numero=input("Introduce un número:")
    return int(numero)

def mostrar():
    print("LISTA:", lista)

def contar():
    return len(lista)

def sumar():
    suma=0
    for i in lista:
        suma+=i
    return suma

def media():
    return sumar/contar()

lista=[]
entrada=""
while entrada != "i":
    menu()
    entrada=input("Selecciona una opción:")
    if entrada == "a":
        lista.append(pide())
    if entrada == "b":
        print(mostrar())
        msvcrt.getch()
    if entrada == "c":
        print("Los elementos que hay en la lista son:", contar())
        msvcrt.getch()
    if entrada=="d":
        print("El total es:", sumar())
        msvcrt.getch()
    if entrada == "e":
        print("La media es", media())
        msvcrt.getch()
