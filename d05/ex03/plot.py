import matplotlib.pyplot as plt
import numpy as np
from prediction import predict_

def	plot(x, y, theta):
    plt.figure()
    plt.plot(x,y,'o')
    plt.plot(x, predict_(x, theta))
    plt.show()

if __name__=="__main__":
    x = np.arange(1,6)
    y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])
    theta1 = np.array([[4.5],[-0.2]])
    # plot(x, y, theta1)
    theta2 = np.array([[-1.5],[2]])
    # plot(x, y, theta2)
    theta3 = np.array([[3],[0.3]])
    plot(x, y, theta3)
