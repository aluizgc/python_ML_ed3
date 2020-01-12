# Python Machine Learning, 3rd edition


<p align="center">
  <a href="https://www.amazon.com.br/dp/B07VBLX2W7/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1">
    <img src="https://images-na.ssl-images-amazon.com/images/I/41JKpkymExL._SX260_.jpg" width="400">
  </a>
</p>

Here I develop the projects contained in the book ****Python Machine Learning****. Each folder contains an individual project.


****I didn't create these algorithms, they were just implemented by me for the purpose of learning.****

## Requeriments

- [Anaconda Distribution (Python 3.x Version)](https://www.anaconda.com/distribution/)

### IDE (Optional)
- [Visual Stuido Code](https://code.visualstudio.com/)

## Projects and Results

### Perceptron learning

Using the [Iris Data Set](https://archive.ics.uci.edu/ml/datasets/iris), the perceptron learned the decision boundary and is able to classify all flower examples in the Iris training subset.

<p align="center">
    <img src="./Perceptron Learning/result.png" width="450">
</p>

### ADAptative LInear NEuron (ADALINE)
In the case of ADALINE we can define a objective function that is to be optimized during the learning process. This objective function is often a cost fuction that we want to minimize.

Using the Iris Data Set we can see that ADALINE converged after training on the standardized features using a learning rate of &eta; = 0.01. However, note that the objective function (Sum of Squared Errors) remains non-zero even though all flower examples were classified correctly.

<p align="center">
    <img src="./ADALINE - ADAptaive LInear NEuron\adaline01.png" width="400">
    <img src="./ADALINE - ADAptaive LInear NEuron\adaline02.png" width="400">
</p>
