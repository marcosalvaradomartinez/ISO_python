import random

num=94
intentos=0
ordenador=0

while ordenador != num:
    ordenador=random.randrange(1,101)
    intentos=intentos+1
    if (num > ordenador):
        print("El numero es mas pequeño")
    else:
        print("El numero es mas grande")
print("Has ganado, has necesitado", intentos, "intentos")
