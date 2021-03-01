# asi se escriben los comentarios
# en las primeras lineas van los imports
import plots
import numpy as np


# aca se definen las variables globales
x = 9
y = 'mineria de datos'
z = False


# asi se definen las funciones
def saludar(nombre):
    print("Hola", nombre, "!")

    # si nombre tiene mas de 7 letras:
    if len(nombre) > 7:
        print('tienes un nombre largo')
    else:
        print('tu nombre no es tan largo...')

    print('tu nombre tiene estas letras:')
    for i in range(len (nombre)):
        print(i, nombre[i])


if __name__ == "__main__":
    print('hola mundo!')
    nombre = input('como es tu nombre? ')
    saludar(nombre)
    plots.basic()


    