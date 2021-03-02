"""

Original file is located at
    https://colab.research.google.com/drive/1tKbMOVm3a7nWFCi23zM0uQQCTB1aQPFf

# Numpy
## Importar y declaración.
"""

import numpy as np

"""Una vez importado la libreria ya se puede usar. Recordemos que la unidad básica para trabajar con numpy son los arreglos. Para crear arreglos sencillos nos da funciones también. 

* La función arange me crea un arreglo de 0 al numero que yo le diga
* Reshape le dice en que forma quiere que lo haga, en este caso 2 filas y 3 columnas.
  * Por obvias razones los numeros dentro de reshape multiplicados tienen que dar el tamaño.

"""

generado = np.arange(6).reshape(2,3)
print(generado)

"""También se pueden crear arreglos desde datos quemados dentro del programa."""

quemado = np.array([[6,7,8],[9,10,11]])
print(quemado)
matriz = np.matrix([[6,7,8],[9,10,11]])
print(matriz)

"""Por ultimo también podemos crearlo programaticamente"""

def arregloProgramatico():
  arreglo = []
  con = 12
  for i in range(3):
    interno =[]
    for j in range(2):
      interno.append(con)
      con+=1
    arreglo.append(interno)
  return np.array(arreglo)
  
programaticamente = arregloProgramatico()
print(programaticamente)

"""En el ejemplo anterior también podemos ver como se puede convertir de un arreglo o matriz convencional a uno en Numpy. 


## Indexación.

En general, la indexacion con python es como en los otros lenguajes, pero tiene una gran ventaja y es los indices negativos.
"""

arreglo = np.arange(6).reshape(2,3)
print(arreglo)
print(arreglo[0,1])
print(arreglo[-1,-1])

"""Los indices negativos me permiten acceder el arreglo en direccion contraria a la normal. Por lo tanto el indice '-1' es el ultimo del arreglo.

## Información que nos da Numpy
"""

arreglo = np.arange(15).reshape(5,3)

print(f'Forma del arreglo: {arreglo.shape}')

print(f'Dimension del arreglo: {arreglo.ndim}')

print(f'Tamaño: {arreglo.size}')

print(f'Tipo de datos que contiene: {arreglo.dtype}')

"""## Transformaciones que se pueden hacer


1. Extracciones
"""

arreglo = np.array([1, 2, 3, 4, 5, 6, 7])
print(f'Del primero al quinto: {arreglo[:5]}')
print(f'Despues del quinto al final: {arreglo[5:]}')
print(f'Despues del 3 al 6: {arreglo[3:6]}')
print(f'Con indices negativos {arreglo[-6:-4]}')
print(f'Para poner un arreglo al revez{arreglo[::-1]}')

"""2. Conversiones a algun tipo de dato en especifico.

"""

arreglo = np.array([1.1,2.5,3.8])
print(f'{arreglo}')

nuevoArreglo = arreglo.astype(int)
print(f'{nuevoArreglo}')

"""3. Cambiar la forma de la matriz

Se le puede dar alguna forma en especifico, pero si solo se quiere que tenga cierta cantidad de columnas o de filas se pone como -1 la otra dimension y solo calcula.
"""

arreglo = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(f'{arreglo}')

arreglo = arreglo.reshape(2,4)
print(f'Estatico: {arreglo}')

arreglo = arreglo.reshape(4,-1)
print(f'Calculado: {arreglo}')

"""4. Copiar el arreglo
  
  La diferencia entre view() y copy() es que copy crea un nuevo arreglo y en view es el mismo arreglo pero con una vista nueva. Si se modifica algo en el view asi mismo se va a ver en el arreglo original
"""

arreglo = np.array([1, 2, 3, 4, 5, 6, 7, 8])

copia = arreglo.copy()
vista = arreglo.view()