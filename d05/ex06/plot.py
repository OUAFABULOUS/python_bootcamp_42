from prediction import predict_
import matplotlib.pyplot as plt
import numpy as np

def	plot_with_loss(x, y, theta):
    plt.figure()
    plt.plot(x,y,'o')
    plt.plot(x, predict_(x, theta))
    plt.show()

if __name__=="__main__":
    x = np.arange(1,6)
    y = np.array([11.52434424, 10.62589482, 13.14755699, 18.60682298, 14.14329568])
    theta1= np.array([18,-1])
    plot_with_loss(x, y, theta1)

