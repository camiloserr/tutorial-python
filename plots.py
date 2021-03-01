import matplotlib.pyplot as plt
import sys
import numpy as np
from random import seed
from random import randint
seed(1)



def getRandomArray():
    answer = []
    for _ in range(30):
        answer.append(randint(0,10))

    return answer

#basic plot
def basic():
    X = [1,2,3,4,5]
    Y = [10,20,30,40,50]
    plt.plot(X,Y)
    plt.savefig("graphs/basic.png")
    plt.show()


    #basic plot
def dashed():
    #valores
    X = [1,2,3,4,5]
    Y = [10,20,30,40,50]
    #opciones de presentacion
    plt.xlabel("valores del eje X")
    plt.ylabel("valores del eje y")
    # este arreglo contiene los limites de cada eje
    #[x inicial, x final, y inicial, y final]
    plt.axis([0,10,0,100])

    #plot
    plt.plot(X, Y, color='green', marker='p', linestyle='--')

    #mostrar grafica
    plt.savefig("graphs/dashed.png")
    plt.show()

def histogram():

    array = getRandomArray()
    plt.hist(array)
    plt.savefig("graphs/histogram.png")
    plt.show()


def cajas():

    # arreglo con los datos
    all_data = [np.random.normal(0, std, size=100) for std in range(1, 4)]
    labels = ['x1', 'x2', 'x3']

    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))

    # diagrama de cajas y bigotes rectangular
    bplot1 = ax1.boxplot(all_data,
                        vert=True,  # vertical box alignment
                        patch_artist=True,  # fill with color
                        labels=labels)  # will be used to label x-ticks
    ax1.set_title('Rectangular box plot')

    # con "cintura"
    bplot2 = ax2.boxplot(all_data,
                        notch=True,  # notch shape
                        vert=True,  # vertical box alignment
                        patch_artist=True,  # fill with color
                        labels=labels)  # will be used to label x-ticks
    ax2.set_title('Notched box plot')

    # ponerle color
    colors = ['pink', 'lightblue', 'lightgreen']
    for bplot in (bplot1, bplot2):
        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)

    # lineas horizontales
    for ax in [ax1, ax2]:
        ax.yaxis.grid(True)
        ax.set_xlabel('Three separate samples')
        ax.set_ylabel('Observed values')

    plt.savefig("graphs/box_plot.png")
    plt.show()

def pie():
    labels = 'Javeriana', 'Andes', 'Nacional', 'Rosario'
    sizes = [21, 49, 23, 7]

    # efecto 3D
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.savefig("graphs/pie.png")

    plt.show()

def multipleLines():
    t = np.arange(0., 15., 0.2)
    # grafica tres funciones
    # y = x en rojo
    # y = x^2 en azul 
    # y = 10x en verde
    plt.plot(t, t, 'r--', t, t**2, 'bs', t, t*10, 'g^')
    plt.savefig("graphs/multipleLines.png")

    plt.show()


def main():
    print("Hello World!")

if __name__ == "__main__":
    options = ["basic", "dashed", "hist", "boxplot", "pie", "multipleLines"]
    if len(sys.argv) == 2:
        if sys.argv[1] == "basic":
            basic()
        elif sys.argv[1] == "dashed":
            dashed()
        elif sys.argv[1] == "hist":
            histogram()
        elif sys.argv[1] == "boxplot":
            cajas()
        elif sys.argv[1] == "pie":
            pie()
        elif sys.argv[1] == "multipleLines":
            multipleLines()
            
        else:
            print("name not found")
            print("--------------------")
            print("plot types:")
            for i in options:
                print(i)
    else:
        print("ussage:")
        print("plots.py + plotType")

        print("--------------------")
        print("plot types:")
        for i in options:
            print(i)

