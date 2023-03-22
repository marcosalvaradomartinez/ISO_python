import random

rondas=0
ganadas=0
perdidas=0

while rondas < 5:
    rondas=rondas+1
    num=random.randrange(1,7)
    persona=int(input("Introduce un número del 1 al 6:"))
    if(persona == num):
        print("Has muerto")
        perdidas = perdidas +1
# si ponemos la instrucción break, ejecutará el programa hasta llegar a la instrucción BREAK
    else:
        print("Has ganado, el rival había elegido el número", num)
        ganadas=ganadas +1
        
print("De 3 rondas has ganado", ganadas, "y has perdido",perdidas)

# for rondas in range (1,4):
#     num=random.randrange(1,7)
#     persona=int(input("Introduce un número del 1 al 6:"))
#     if(persona == num):
#         print("Has muerto")
#         perdidas = perdidas +1
#     else:
#         print("Has ganado, el rival había elegido el número", num)
#         ganadas=ganadas +1
# print("De 3 rondas has ganado", ganadas, "y has perdido",perdidas)
