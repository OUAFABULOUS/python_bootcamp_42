import numpy as np

def	add_intercept(x):
    ones = np.ones(len(x))
    return (np.c_[ones, x])

if __name__=="__main__":
    x = np.arange(1,6)
    ret = add_intercept(x)
    print(ret)

    y = np.arange(1,10).reshape((3,3))
    print(add_intercept(y))
