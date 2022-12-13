from my_linear_regression import MyLinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def	plot(x, y, theta):
    mlr = MyLinearRegression(theta)
    plt.figure()
    plt.plot(x,y,'o')
    # plt.scatter(x, mlr.predict_(x))
    # plt.plot(x, mlr.predict_(x))
    plt.show()


if	__name__=="__main__":
    data = pd.read_csv("are_blue_pills_magics.csv")
    Xpill = np.array(data["Micrograms"]).reshape(-1,1)
    Yscore = np.array(data["Score"]).reshape(-1,1)
    # plot(data["Micrograms"], data["Score"], np.array([[89.0], [-8]]))
    mlr = MyLinearRegression(np.array([[89.0], [-8]]))
    # plt.figure()
    mlr.fit_(Xpill, Yscore)
    new_theta = mlr.thetas
    # theta0 = np.full(100, new_theta[0])
    theta0_range = new_theta[0]
    theta1_var = np.arange(-14, -4, 0.1)
    for theta0 in np.arange(theta0_range - 2, theta0_range + 3, 1):
        loss = []
        for theta in theta1_var:
            tmp = mlr.predict_with_thetas_(Xpill, theta0, theta)
            loss_i = mlr.loss_(Yscore, mlr.predict_with_thetas_(Xpill, theta0, theta).reshape(-1,1))
            #print(">>", loss_i.shape)
            #break
            loss.append(loss_i)
        plt.plot(theta1_var, loss)
    plt.show()

    # for x, y in zip(data["Micrograms"],data["Score"]):
    # loss = mlr.loss_elem_(Yscore, mlr.predict_(Xpill))

    # plt.plot(np.full(7, 89), loss)
    # print(loss)
    # print(Yscore)
    # print(mlr.predict_(Xpill))
    # print(mlr.predict_(Xpill) - Yscore)
    # plt.plot(mlr.loss_(Yscore, mlr.predict_(Xpill)))
    # print(Yscore)
    # print(Xpill)
    # plt.show()

