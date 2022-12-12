import numpy as np

def loss(y, y_hat):
    diff = y_hat - y
    half_emq = sum((xi)**2 for xi in diff) / (2 * len(diff))
    return (half_emq)

if	__name__=="__main__":
    X = np.array([[0], [15], [-9], [7], [12], [3], [-21]])
    Y = np.array([[2], [14], [-13], [5], [12], [4], [-19]])
    print(loss(X, Y))
