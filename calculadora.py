import msvcrt
from os import system

def pide(letra):
    numero=""
    while not(numero.isnumeric()):
        print("Vas a poner valor a", letra)
        numero=input("Introduce un número:")
    return int(numero)

def menu():
    print("CALCULADORA: ")
    print("a) Introduce un numero")
    print("b) Introduce un numero")
    print("c) Sumar A + B")
    print("d) Restar A - B")
    print("e) Multiplicar A x B")
    print("f) Dividir A / B")
    print("g) Invertir A y B")
    print("h) Ver A y B")
    print("i) Salir")
    print("")

def mostrar():
    print("A=", A)
    print("B=", B)
    msvcrt.getch()

def sumarNumeros():
    return A + B

def restarNumeros():
      return A - B

def multiplicarNumeros():
    return A * B

def dividirNumeros():
    if B == 0:
        print("No se puede dividir por 0")
    else:
        return A/B

def invierteNumeros():
    global A, B
    c=A
    A=B
    B=c

A=B=0
entrada=""
while entrada != "i":
    menu()
    entrada=input("Selecciona una opción:")
    if entrada == "a":
        A= pide("a")
    if entrada == "b":
        B=pide("b")
    if entrada =="c":
        print("La suma de", A , "y", B , "es", sumarNumeros())
        msvcrt.getch()
    if entrada == "d":
        print("La resta de", A , "y", B , "es", restarNumeros())
    if entrada == "e":
        print("La multiplicación de", A , "y", B , "es", multiplicarNumeros())
    if entrada == "f":
        print("La división de", A , "y", B , "es", dividirNumeros())
    if entrada == "g":
        print("Antes de empezar A=", A, "B=", B)
        invierteNumeros()
        print("He invertido A y B")
        mostrar()
    if entrada == "h":
        mostrar()
