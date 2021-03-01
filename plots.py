import matplotlib.pyplot as plt
import sys
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


def main():
    print("Hello World!")

if __name__ == "__main__":
    options = ["basic", "dashed", "hist"]
    if len(sys.argv) == 2:
        if sys.argv[1] == "basic":
            basic()
        elif sys.argv[1] == "dashed":
            dashed()
        elif sys.argv[1] == "hist":
            histogram()
            
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