import numpy as np


class Neuron:
    def __init__(self, bias, threshold):
        self.bias = bias
        self.weights = np.array([])
        self.threshold = np.array(threshold)

    def activationFunction(self, h):
        res = []
        for element in h:
            if element>=self.threshold:
                res.append(1)
            else:
                res.append(0)
        return res

    def initialFunction(self, inputs):
        h = np.sum(self.weights.transpose() *
                   np.array(inputs), axis=1) + self.bias
        #print(h[h.shape[0]-1]-[h.shape[0]-2])
        return h

    def predict(self, inputs):
        return self.activationFunction(self.initialFunction(inputs))

    def dldw(self, x, y, y_predicted):
        s = 0
        n = len(y)
        for i in range(n):
            s += -x[i]*(y[i]-y_predicted[i])
        return (2/n)*s

    def dldb(self, y, y_predicted):
        n = len(y)
        s = 0
        for i in range(len(y)):
            s += -(y[i]-y_predicted[i])
        return (2/n) * s

    def fit(self, X, Y, lr=0.05, epoch=10):
        x = np.array(X)
        y = np.array(Y)
        cols = x.shape[1]
        learning_rate = lr
        self.bias = 0
        self.weights = abs(np.random.randn(x.shape[1]))
        for i in range(epoch):
            y_predicted = self.activationFunction(self.initialFunction(x))
            self.weights = self.weights - learning_rate * \
                self.dldw(x, y, y_predicted)  # update weight
            self.bias = self.bias - learning_rate * self.dldb(y, y_predicted)
        return True


if __name__ == '__main__':
    bias = 0
    inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
    expOutput = [0, 0, 0, 1]
    threshold = 1
    n = Neuron(bias, threshold)
    n.fit(inputs, expOutput)
    h = n.initialFunction(inputs)
    n.threshold = h[len(h)-1]
    o = n.activationFunction(h)
    print("And gate:")
    print("x\ty\tO")
    a = 0
    for test in o:
        print(str(inputs[a][0])+"\t"+str(inputs[a][1]) +
              "\t"+str(test))
        a += 1
