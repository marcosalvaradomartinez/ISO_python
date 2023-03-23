import random

def pintarnum(a):
    if a==1:
        print("Piedra")
    elif a==2:
        print("Papel")
    elif a==3:
        print("Tijeras")

ganadas=perdidas=rondas=empates=0

while ganadas <3 and perdidas <3:
    rondas+=1
    maquina=random.randrange(1,4)
    persona=int(input("Piedra (1), Papel (2), Tijeras(3)"))
    print("Has elegido"), pintarnum(persona)
    print("El ordenador ha elegido"), pintarnum(maquina)

    if persona == maquina:
        print("Empate")
        empates+=1
    elif (maquina == 1 and persona == 2) or (maquina == 2 and persona == 3) or (maquina == 3 and persona == 1):
        print("Ganas")
        ganadas+=1
    else:
        print("Pierdes")
        perdidas+=1

print (f"Has ganado {ganadas} rondas, has perdido {perdidas} y has empatado {empates} en {rondas} que hemos jugado")
