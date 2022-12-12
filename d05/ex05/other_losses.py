import numpy as np
import math
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def	mse_(y, y_hat):
    diff = y_hat - y
    mse = sum((x)**2 for x in diff) / len(diff)
    return (mse)

def	rmse_(y, y_hat):
    return(math.sqrt(mse_(y, y_hat)))

def	mae_(y, y_hat):
    diff = y_hat - y
    mae = sum((abs(x)) for x in diff) / len(diff)
    return(mae)

def	r2score_(y, y_hat):
    diff = y_hat - y
    my_mean =np.mean(y)
    mse = sum((x)**2 for x in diff) / sum((x2 - my_mean)**2 for x2 in y)
    return (1 - mse)


if	__name__=="__main__":
    x = np.array([0, 15, -9, 7, 12, 3, -21])
    y = np.array([2, 14, -13, 5, 12, 4, -19])

    # print(mse_(x,y))
    # print(mean_squared_error(x,y))

    # print(rmse_(x,y))
    # print(math.sqrt(mean_squared_error(x,y)))

    # print(mae_(x,y))
    # print(mean_absolute_error(x,y))

    print(r2score_(x,y))
    print(r2_score(x,y))
