from __future__ import division
import numpy as np
class ClassName:
    """A class to read values from a text file and perform linear regression by gradient descent """
    def __init__(self, filename):
        print("About the class: " + ClassName.__doc__)
        self.filename = filename
    def getData(self):
        print "Getting data from the file: " + self.filename
        self.file = np.genfromtxt(self.filename, delimiter=",")
        #Getting the dimensions of the file matrix
        self.shape = self.file.shape
        self.m = self.shape[0]
        self.n = self.shape[1]
        #Initialising the arrays
        self.X = np.zeros((self.m, self.n))
        self.Y = np.zeros((self.m, 1))
        #Assigning values to the arrays
        for i in range(1, self.n):
            self.X[:, i] = self.file[:, i-1]
        self.Y[:, 0] = self.file[:, 1]
        self.X[:, 0] = np.ones_like(self.X[:, 0])
        #Initialising theta
        self.theta = np.zeros((self.n, 1))
    def costFunction(self):
        #Calculating cost function
        self.q = 1/(2*(self.m))
        self.e = self.X.dot(self.theta) - self.Y
        self.J = (self.q)*np.sum(np.power(self.e, 2))
        return self.J
    def gradientDescent(self):
        #Calculating gradient descent
        self.alpha = 0.01
        self.z = self.alpha/self.m
        for i in range(1500):
            self.e = self.X.dot(self.theta) - self.Y
            self.gd = self.X.transpose().dot(self.e)
            self.theta = self.theta - (self.z)*self.gd
        return self.theta
if __name__ == "__main__":
    className = ClassName("/home/rajiv/Downloads/ex1data1.txt")
    className.getData()
    j = className.costFunction()
    theta = className.gradientDescent()
    x = np.array([1, 4.5])*10000
    profit = x.dot(theta)
    print "The profit of the city with population 45000 is: " + str(profit[0])
