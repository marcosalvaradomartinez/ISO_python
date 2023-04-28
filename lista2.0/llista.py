import msvcrt
from os import system

def pide():
    numero=""
    while not(numero.isnumeric()):
        numero=input ("Introduce un numero:")
    return int(numero)

def menu():
    system("cls")
    print("a) Introducir valor en la lista")
    print("b) Mostrar lista")
    print("c) Contar els elements que hi ha a la llista")
    print("d) Sumara els elements que hi ha a la llista")
    print("e) Calcula la media de la lista")
    print("f) Mostra el màxim de la llista")
    print("g) Mostra el mínim de la llista")
    print("h) Mostra la posició del màxim de la llista")
    print("i) Mostra la posició del mínim de la llista")
    print("j) Desa les dades")
    print("k) Carrega les dades")
    print("l) ordena les dades")
    print("m) mostra la mediana")
    print("q) Salir")
    print("")

def afegir_element():
    llista.append(pide())

def ordena():
     muestra_datos2()
     for i in range(len(llista)):
        for j in range(i+1,len(llista)):
             if llista[i]>llista[j]:
                  aux=llista[i]
                  llista[i]=llista[j]
                  llista[j]=aux
                  muestra_datos2()

def triar_opcio(opcio):
    if opcio=="a":
        afegir_element()
    if opcio=="b":
        muestra_datos()
    if opcio=="c":
        print(f"Els elements que hi ha a la llista son:{cuenta_elementos()}")
        msvcrt.getch()
    if opcio=="d":
          print(f"La suma dels elements de la llista és:{suma_elementos()}")  
          msvcrt.getch() 
    if opcio=="e":
          print(f"La mitjana dels elements de la llista és:{calcula_mitjana()}")
          msvcrt.getch()
    if opcio=="f":
          print(f"El màxim de la llista es:{maxim()}")
          msvcrt.getch()
    if opcio=="g":
          print(f"El mínim de la llista és:{minim()}")
          msvcrt.getch()
    if opcio=="h":
          print(f"La posició del màxim de la llista es:{pos_maxim()}")
          msvcrt.getch()
    if opcio=="i":
          print(f"El posició del mínim de la llista és:{pos_minim()}")
          msvcrt.getch()
    if opcio=="j":
          print(f"Dades desades, he registrar {desar_dades()}")
          msvcrt.getch()
    if opcio=="k":
          print(f"Dades carregades, he llegit {carregar_dades()}")
          msvcrt.getch()
    if opcio=="l":
          print("Dades ordenades")
          ordena()
          msvcrt.getch()
    if opcio=="m":
          print(f"La mediana és: {mediana()}")
          msvcrt.getch()

          
          

def mediana():
     ordena()
     puntoMedio=int(len(llista)/2)
     if len(llista)%2==1:
          return llista[puntoMedio]
     else:
          return (llista[puntoMedio]+llista[puntoMedio-1])/2

def muestra_datos2():
     cadena=""
     for elemento in llista:
          cadena+=str(elemento)+" "
     print(cadena)     
def muestra_datos():
    for elemento in llista:
        print(elemento)
    msvcrt.getch()

def cuenta_elementos():
    return len(llista)

def suma_elementos():
     suma=0
     for i in llista:
          suma+=i
     return suma

def calcula_mitjana():
     return suma_elementos()/cuenta_elementos()
def maxim():
     maxim=llista[0]
     for i in llista:
        if i > maxim:
            maxim=i
     return maxim

def minim():
    minim=llista[0]
    for i in llista:
        if i<minim:
            minim=i
    return minim
def pos_maxim():
    posicio=0
    for i in range(len(llista)):
        if llista[i] > llista[posicio]:
            posicio=i
    return posicio

def pos_minim():
    posicio=0
    for i in range(len(llista)):
        if llista[i]<llista[posicio]:
            posicio=i
    return posicio


def desar_dades():
    dades=0
    fitxer=open("fitxer.txt","w")
    for i in llista:
        fitxer.write(str(i)+"\n")
        dades+=1
    return dades

def carregar_dades():
    global llista
    llista=[]
    numero=0
    fitxer=open("fitxer.txt")
    for dada in fitxer:
        llista.append(int(dada))
        numero+=1
    return numero


#principal
#llista=[5,7,9,2,1]
llista=[]
entrada=""
while entrada!="q":
     menu()
     entrada=input("introduce una opción:")
     triar_opcio(entrada)