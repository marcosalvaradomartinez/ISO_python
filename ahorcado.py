import random

AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

palabras = "rotura futbol bate azul araña ciego dani marcos blanco mbappe".split()


def buscarPalabras(lista):
    aleatoria = random.randint(0, len(lista) -1)
    return lista[aleatoria]

def interfazGrafica(AHORCADO, buenaLetra, malaLetra, palabraAhorcado):
    print(AHORCADO[len(malaLetra)])
    print("")
    final=" "
    print("Las letras incorrectas son:", final)
    for letra in malaLetra:
        print(letra, final)
    print("")    
    lugarLetra = '_' * len(palabraAhorcado)
    for i in range(len(palabraAhorcado)):
        if palabraAhorcado[i] in buenaLetra:
            lugarLetra = lugarLetra[:i] + palabraAhorcado[i] + lugarLetra[i+1:]
    for letra in lugarLetra:
        print(letra, final)
    print("")

def elegirLetra(cualquiera):
    while True:
        print("Pon una letra: ")
        letra = input()
        letra = letra.lower()
        if len(letra) != 1:
            print("Solamente introduce una letra")
        elif letra in cualquiera:
            print("No repitas letras!!")
        elif letra not in 'abcdefghijklmnñopqrstuvwxyz':
            print("Solo introduce letras")
        else:
            return letra

print('AHORCADO')
malaLetra = ""
buenaLetra = ""
palabraAhorcado = buscarPalabras(palabras)
finJuego = False

while True:
    interfazGrafica(AHORCADO, buenaLetra, malaLetra, palabraAhorcado)
    letra = elegirLetra(malaLetra + buenaLetra)
    if letra in palabraAhorcado:
        buenaLetra = buenaLetra + letra
        letrasEncontradas = True
        for i in range(len(palabraAhorcado)):
            if palabraAhorcado[i] not in buenaLetra:
                letrasEncontradas = False
                break
        if letrasEncontradas:
            print("Has ganado, la palabra era" + palabraAhorcado + "Enhorabuena!!")
            finJuego = True
    else:
        malaLetra = malaLetra + letra
        if len(malaLetra) == len(AHORCADO) -1:
            interfazGrafica(AHORCADO, buenaLetra, malaLetra, palabraAhorcado)
            print("Te has quedado sin intentos")
            finJuego = True