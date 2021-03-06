# -*- coding: utf-8 -*-
"""
Original file is located at
    https://colab.research.google.com/drive/10g6ZLSgLEWJzljkxkDr1RaD6SboW5MmL

# Pandas

## Importar información
"""

!pip3 install pandas
import pandas as pd
pd.set_option("display.precision", 2)
pd.set_option("display.max.columns", None)

"""Una vez importado Pandas hay que poder leer información y guardarlo en un DataFrame(), de este dataframe es lo que panda puede entender

* Se puede importar información desde un diccionario en donde se ponen los titulos de las caracteristicas y sus valores. Con esto se crea un dataframe
  * En caso de no poner un indice se le asigna un numero id automatico.
  * La función de Dataframe trae un parametro opcional que se llama index que recibe un arreglo de nombres para cada uno de las entradas.
"""

data = {
    'apples': [3, 2, 0, 1], 
    'oranges': [0, 3, 7, 2]
}

purchases = pd.DataFrame(data)
print(purchases)

purchases = pd.DataFrame(data,index=['June', 'Robert', 'Lily', 'David'])
print(purchases)

"""Una vez se tiene el dataframe se puede obtener incluso valores mas especifico por cada ejemplo. """

purchases.iloc[1]

infoNBA = pd.read_csv("nba_all_elo.csv")

print(infoNBA.head())
print(infoNBA.shape)

print(infoNBA.info())

"""Se pueden obtener informacion de cada una de las caracteristicas. Describe() por defecto lo hace con las caracteristicas que son numericas."""

print(infoNBA.describe())

print(infoNBA["team_id"].value_counts())

infoMovies = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")
print(infoMovies.head(2))
print(infoMovies.shape)

print(infoMovies.info())

"""Manejo de Duplicados

Con los parametros opcionales:

* inplace: reemplaza en vez de tener que recibirla
* keep: dice si quieres guardar por lo menos una de las dos copias, si esta en false elimina las dos
"""

print(infoMovies.shape)
duplicados = infoMovies.append(infoMovies) # Creamos los duplicados
print(duplicados.shape)

duplicados = duplicados.drop_duplicates()
print(duplicados.shape)

duplicados = infoMovies.append(infoMovies) # Creamos los duplicados
duplicados.drop_duplicates(inplace=True, keep=False) # Inplace, para que no retrne
print(duplicados.shape)

print(infoMovies.columns)
infoMovies.rename(columns={'Runtime (Minutes)':'Duration','Revenue (Millions)':'Revenue'},inplace=True)
print(infoMovies.columns)

"""## Valores vacios"""

print(infoMovies.isnull())

"""con la función dropna() se pueden eliminar aquellos ejemplos que tienen estos valores con nulos.

En caso de que mejor se quieran eliminar las columnas, se puede cambiar el eje por el cual se esta eliminando por medio del parametro opcional axis
"""

print(infoMovies.shape)
print(infoMovies.isnull().sum())

infoMovies.dropna(inplace=True) #axis=1

print(infoMovies.shape)
print(infoMovies.isnull().sum())

"""Asi mismo se puede, en vez de eliminar o los ejemplos o las caracteristicas, se puede reemplazar por algun valor. 

En este caso las vamos a reemplazar por su promedio
"""

infoMovies = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")
infoMovies.rename(columns={'Runtime (Minutes)':'Duration','Revenue (Millions)':'Revenue'},inplace=True)

revenue = infoMovies['Revenue']

promedio = revenue.mean()

revenue.fillna(promedio,inplace=True)

print(infoMovies.isnull().sum())

"""## Correlacion entre caracteristicas"""

print(infoMovies.corr())

"""## Extraer solo ciertas caracteristicas"""

sub = infoMovies[['Duration','Rating']]

print(sub.head())

sub = infoMovies.loc['Prometheus':'Suicide Squad']

print(sub)

sub = infoMovies.iloc[:2]

print(sub)

condicional = (infoMovies['Genre'] == 'Drama')

print(condicional)

condicional = infoMovies[infoMovies['Genre']=='Drama']

print(condicional.head())
