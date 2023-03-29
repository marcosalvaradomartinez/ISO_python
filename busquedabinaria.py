import msvcrt  #una libreria que nos permite esperar una tecla
from os import system
system("cls")
print("Piensa un número del 1 al 100 y presiona cualquier tecla")
msvcrt.getch()
min=1
max=100
intentos=0
encontrado=False
seguir=True

while seguir:
    intentos=intentos+1
    numero=int((min+max)/2)
    print(f"Es {numero}")
    respuesta=input("(s/n)")
    if respuesta =="s":
        print("Lo has acertado")
        seguir=False
        encontrado=True
    else:
        respuesta=input("Es mayor (s/n)")
        if respuesta=="s":  
            min=numero+1
        else:
            max=numero-1
    if min>max:
        print("Mentiroso")
        seguir=False
if encontrado:
    print(f"He necesitado {intentos} intentos")

