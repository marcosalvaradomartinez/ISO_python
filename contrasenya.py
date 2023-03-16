# pedir=input("Introduce un número")
# print("Has introducido el número" +pedir)

import string
cont=input("Introduce la contraseña: ")
if(cont.lower() == "lala"):
    print("Has puesto bien la contraseña")
    num=input("Pon un numero jueputa: ")
    if num.isnumeric():
        num=int(num)
        if num>0 and num<10:
            print("El numero esta entre 1 y 10 ")
        else:
            print("Numero fuera de rango")
    else:
        print("No me has puesto un numero")
    print(type(num))
else :
    print("Contraseña incorrecta")
print("Fin del programa")