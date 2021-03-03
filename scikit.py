import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier


np.random.seed(0)

# define dataset
iris_X, iris_y = datasets.load_iris(return_X_y=True)
np.unique(iris_y)


# returns accuracy as a number between 0 and 1
def accuracy(prediction, real):
    if len(prediction) != len(real):
        print("arrays dont match")
        return 0
    length = len(real)
    correct = 0
    for i in range(length):
        if prediction[i] == real[i]:
            correct += 1
    
    return correct / length

def plot():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')


    # For each set of style and range settings, plot n random points in the box
    # defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
    i = 0
    for i in range(len(iris_X)):
        element = iris_X[i]
        label = iris_y[i]

        m = 'o'
        if label == 0:
            c = 'r'

        elif label == 1:
            c = 'g'
        elif label == 2:
            c = 'b' 
        ax.scatter(element[0], element[1], element[2], marker=m, edgecolor='black', c=c)



    ax.set_xlabel('petal length')
    ax.set_ylabel('sepal length')
    ax.set_zlabel('width')

    # plt.savefig("graphs/iris_original.png")
    ax.view_init(30, 60)
    plt.savefig("graphs/iris_original.png")



    # plt.show()

def nearestNeighbour():
    indices = np.random.permutation(len(iris_X))
    iris_X_train = iris_X[indices[:-10]]
    iris_y_train = iris_y[indices[:-10]]
    iris_X_test = iris_X[indices[-10:]]
    iris_y_test = iris_y[indices[-10:]]
    # Create and fit a nearest-neighbor classifier
    knn = KNeighborsClassifier()
    knn.fit(iris_X_train, iris_y_train)
    prediction = knn.predict(iris_X_test)

    print('prediction: ', prediction)
    print('actual:     ', iris_y_test)
    print('accuracy:   ', accuracy(prediction, iris_y_test))


nearestNeighbour()