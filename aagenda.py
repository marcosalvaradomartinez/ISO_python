import msvcrt

def menu():
    print("a)Introduce un nombre en la agenda")
    print("b)Buscar un nombre")
    print("c)Mostrar la agenda")
    print("z)Salir")

def pedirNombre():
    nombre=input("Introduce un nombre:")
    numero=int(input("Introduce un número:"))
    diccionario[nombre] = numero

def buscaNombre():
    busca=input("Introduce el nombre que quieres buscar:")
    print(diccionario[busca])

def mostrarAgenda():
    print(diccionario)

diccionario = {}
entrada=""
while entrada != "z":
    menu()
    entrada=input("Selecciona una opción:")
    if entrada == "a":
        print(pedirNombre())
    if entrada == "b":
        buscaNombre()
        msvcrt.getch()
    if entrada == "c":
        mostrarAgenda()
        msvcrt.getch()