import random

num=random.randrange(1,101)
intentos=0
persona=0

while num != persona:
    persona=int(input("Pon un número del 1 al 100:"))
    intentos=intentos+1
    if (persona > num):
        print("El numero es mas pequeño")
    else:
        print("El numero es mas grande")
print("Has ganado, has necesitado", intentos, "intentos")