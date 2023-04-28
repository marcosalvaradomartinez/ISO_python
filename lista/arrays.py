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
    print("f) El número más pequeño es:")
    print("g) El número más grande es:")
    print("h) El número más pequeño se encuentra en la posición:")
    print("i) Ordenar los datos")
    print("j) Mediana de los números")
    print("x) Guardar los datos")
    print("y) Cargar los datos")
    print("z) Salir")

def pide():
    numero=""
    while not(numero.isnumeric()):
        numero=input("Introduce un número:")
    return int(numero)

def mostrar():
    for num in lista:
        print(num)

def contar():
    return len(lista)

def sumar():
    suma=0
    for i in lista:
        suma+=i
    return suma

def media():
    total = sumar()
    return total/contar()

def minimo():
    min=lista[0]
    for i in lista:
        if i<min:
            min=i
    return min

def maximo():
    max=lista[0]
    for i in lista:
        if i>max:
            max=i
    return max

def pos_minimo():
    posicion=0
    for i in range (len(lista)):
        if lista[posicion] > lista [i]:
            posicion=i
        return posicion

def guardarDatos():
    datos=0
    fichero=open("ficha.txt", "w")
    for x in lista:
        fichero.write(str(x)+"\n")
        datos+=1
    return datos

def cargarDatos():
    numero=0
    lista=[]
    fichero=open("ficha.txt", "r")
    for datos in fichero:
        lista.append(int(datos))
        numero=numero +1
    return numero

def ordenaDatos():
    for i in range (len(lista)):
        for j in range (i+1,len(lista)-1):
            print(lista)
            if lista [i] > lista [j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                print(lista)

def mediana():
    ordenaDatos()
    posicion = int(len(lista)/2)
    if len(lista)%2 == 1:
        return lista[posicion]
    else:
        return (lista[posicion]+lista[posicion-1])/2

lista=[]
entrada=""
while entrada != "z":
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
    if entrada == "f":
        print(minimo())
        msvcrt.getch()
    if entrada == "g":
        print(maximo())
        msvcrt.getch()
    if entrada == "h":
        print(pos_minimo())
        msvcrt.getch()
    if entrada == "i":
        print(ordenaDatos())
        msvcrt.getch()
    if entrada == "j":
        print(mediana(lista))
        msvcrt.getch()
    if entrada == "x":
        print(guardarDatos())
        msvcrt.getch()
    if entrada == "y":
        print(cargarDatos())
        msvcrt.getch()