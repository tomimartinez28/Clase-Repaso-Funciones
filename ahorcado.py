"""
Juego de ahorcado: 
Crea un juego de ahorcado en el que la computadora seleccione una palabra al azar y el jugador tenga que adivinarla letra por letra. El jugador tiene un número limitado de intentos y la computadora debe mostrar el progreso del jugador, indicando qué letras ha adivinado correctamente y cuáles aún están ocultas. Utiliza funciones, condicionales y bucles para implementar este juego.

"""

import random


palabras = ['python', 'auto', 'programacion', 'cajero', 'desaprobado', 'variable', 'celular', 'paralelepipedo']

# Funcion para elegir palabra
def seleccionar_palabra():``
    return random.choice(palabras)


# Funcion que muestro el progreso actual
def mostrar_progreso(palabra, letras_adivinadas):
    progreso = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            progreso += letra
        else:
            progreso += '_'
    return progreso






def jugar_ahorcado():
    # Inicializado variables
    palabra_secreta = seleccionar_palabra()
    intentos_maximos = 6
    letras_adivinadas = []
    intentos_realizados = 0

    # Inicia el juego
    print('Bienvenidos al ahorcado.')
    print(f'La palabra tiene {len(palabra_secreta)} letras')

    while True:
        print(f'Progreso actual: {mostrar_progreso(palabra_secreta, letras_adivinadas)}')

        letra = input('Ingrese una letra: ').lower()

        if letra in letras_adivinadas:
            print('Ya has ingresado esa letra. Proba otra')
            continue
            
        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            if set(letras_adivinadas) == set(palabra_secreta):
                mostrar_progreso()
                print('Felicidades ganaste.')
                break
        else:
            intentos_realizados += 1
            print(f'Letra incorrecta. Llevas {intentos_realizados} intentos.')
            if intentos_realizados == intentos_maximos:
                print(f'Perdiste. La palabra era: {palabra_secreta}')
                break




# ARRANCA EL PROGRAMA
jugar_ahorcado()