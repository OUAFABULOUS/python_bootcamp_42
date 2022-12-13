import numpy as np
import matplotlib.pyplot as plt

def	add_intercept(x):
    ones = np.ones(len(x))
    return (np.c_[ones, x])

def	simple_gradient(x, y, theta):
    m = len(x)
    X = add_intercept(x)
    X_T = X.transpose()
    X = np.matmul(X, theta)
    return (1/m) * np.matmul(X_T, X - y)

class	MyLinearRegression():
    def	__init__(self, thetas, alpha=0.001, max_iter=100000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.thetas = thetas

    def	plot(self, x, y, theta):
        mlr = MyLinearRegression(theta)
        plt.figure()
        plt.plot(x,y,'o')
        # plt.scatter(x, mlr.predict_(x))
        # plt.plot(x, mlr.predict_(x))
        # plt.show()

    def fit_(self, x, y):
        # plt.figure()
        new_theta = self.thetas
        for i in range(self.max_iter):
            new_theta = new_theta - self.alpha * simple_gradient(x, y, new_theta)
        # self.plot(self.loss_elem_(y, self.predict_(x)) self.thetas)
        # plt.show()
        self.thetas = new_theta

    def	predict_with_thetas_(self, x, theta0, theta1):
        x_=add_intercept(x)
        return(np.matmul(x_, [theta0, theta1]))

    def	predict_(self, x):
        x_=add_intercept(x)
        return(np.matmul(x_, self.thetas))

    def	loss_elem_(self, y, y_hat):
        # return((y_hat - y)**2)
        return((y_hat - y))

    def	loss_(self, y, y_hat):
        diff = y_hat - y
        half_emq = sum((xi)**2 for xi in diff) / (2 * len(diff))
        return (half_emq)

if	__name__=="__main__":
    x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
    y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
    lr1 = MyLinearRegression(np.array([[2], [0.7]]))
    y_hat = lr1.predict_(x)
    # print(y_hat)
    # print(lr1.loss_elem_(y, y_hat))
    # print(lr1.loss_(y, y_hat))
    lr2 = MyLinearRegression(np.array([[1], [1]]), 5e-8, 1500000)
    lr2.fit_(x, y)
    print(lr2.thetas)
    y_hat = lr2.predict_(x)
    print(y_hat)
    print(lr2.loss_elem_(y, y_hat))
    print(lr2.loss_(y, y_hat))
