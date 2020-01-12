import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

class Perceptron(object):
    '''
    Parameters
    eta : float -- Learning rate (between 0.0 and 1.0)
    n_inter : int -- Passes over the training dataset
    random_state : int -- Random number generator seed for random weight initialization
    Attributes
    w_ : 1d-array -- Weights after fitting
    errors_ : list -- Number of misclassifications (updates) in each epoch
    '''
    def __init__(self, eta=0.01, n_inter = 50, random_state = 1):
        self.eta = eta
        self.n_inter= n_inter
        self.random_state = random_state
    
    def fit(self, X, y):
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale = 0.01, size = 1+X.shape[1])
        self.errors_ = []

        for _ in range(self.n_inter):
            errors = 0
            for xi, target in zip(X,y):
                update = self.eta*(target - self.predict(xi))
                self.w_[1:] += update*xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self
    
    def net_input(self,X):
        return np.dot(X,self.w_[1:]) + self.w_[0]

    def predict(self,X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)


s = 'Data/iris.data'
print(s)
#print('URL: ', s)

df = pd.read_csv(s,header=None,encoding='utf-8')
#print(df.tail())

# Select setosa and versicolor
y = df.iloc[0:100,4].values
y = np.where(y == 'Iris-setosa',-1,1)

# Extract sepal lenght and petal lenght
X = df.iloc[0:100, [0,2]].values

# Plot data
plt.scatter(X[:50,0], X[:50,1], color='red', marker='o', label='Setosa')
plt.scatter(X[50:100,0], X[50:100,1], color='blue', marker='x', label='Versicolor')
plt.xlabel('sepal lenght (cm)')
plt.ylabel('petal lenght (cm)')
plt.legend(loc='best')
plt.show()

ppn = Perceptron(eta=0.1, n_inter = 10)
ppn.fit(X,y)
plt.plot(range(1,len(ppn.errors_)+1), ppn.errors_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of updates')
plt.show()

def plot_decision_regions(X, y, classifier, resolution = 0.02):
    # Setup marker generator and color map
    markers = ('s','x','o','^','v')
    colors = ('red','blue','lightgreen','gray','cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # Plot the decision surface
    x1_min, x1_max = X[:,0].min() - 1, X[:,0].max() + 1
    x2_min, x2_max = X[:,1].min() - 1, X[:,1].max() + 1
    xx1,xx2 = np.meshgrid(np.arange(x1_min,x1_max, resolution), np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1,xx2,Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(),xx1.max())
    plt.ylim(xx2.min(),xx2.max())

    # Plot class examples
    for index, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl,0], y=X[y == cl, 1], alpha = 0.8, c = colors[index], marker = markers[index], label=cl, edgecolor = 'black')

plot_decision_regions(X, y, classifier=ppn)
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')
plt.show()