from tools import add_intercept
from prediction import predict_
import numpy as np
from tools import add_intercept

def	simple_gradient(x, y, theta):
    m = len(x)
    X = add_intercept(x)
    X_T = X.transpose()
    X = np.matmul(X, theta)
    return (1/m) * np.matmul(X_T, X - y)

if  __name__=="__main__":
    x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733]).reshape((-1, 1))
    y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554]).reshape((-1, 1))
    theta1 = np.array([2, 0.7]).reshape((-1, 1))
    # print(simple_gradient(x, y, theta1))
    print(simple_gradient(x, y, theta1))
