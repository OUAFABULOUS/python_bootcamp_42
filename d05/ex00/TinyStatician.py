import numpy as np
import math

class	TinyStatician:
    def __init__(self):
        pass

    def	mean(self, x):
        return sum(x) / len(x)

    def	median(self, non_sorted_x):
        x = sorted(non_sorted_x)
        n = len(x)
        if n % 2:
            return x[int((n + 1) / 2) - 1]
        else:
            n_bef = int((n / 2) - 1)
            n_aft = int(n / 2)
            return((x[n_bef] + x[n_aft]) / 2)

    def get_quartile(self, x,q_index):
        if round(q_index - int(q_index), 2)==0.25:
            q = (3 * x[int(q_index) - 1] + x[int(q_index)]) / 4
        elif round(q_index - int(q_index), 1)==0.5:
            q = (x[int(q_index) - 1] + x[int(q_index)]) / 2
        elif round(q_index - int(q_index), 2)==0.75:
            q = (x[int(q_index) - 1] + 3 * x[int(q_index)]) / 4
        else:
            q = x[int(q_index - 1)]
        return float(q)

    def	quartile(self, non_sorted_x):
        try:
            quartiles = []
            x = sorted(non_sorted_x)
            n = len(x)
            q1_index = (n + 3) / 4
            quartiles.append(self.get_quartile(x, q1_index))
            quartiles.append(float(self.median(x)))
            q2_index = (3 * n + 1) / 4
            quartiles.append(self.get_quartile(x, q2_index))
            return(quartiles)
        except:
            return None

    def percentile(self, x_not_sorted, p):
        x = sorted(x_not_sorted)
        n = len(x)
        r = (p / 100) * (n - 1) + 1
        ri = int(r)
        rf = r - ri
        p = x[ri - 1] + rf*(x[ri] - x[ri - 1])
        return (p)

    def var(self, x):
        mean = self.mean(x)
        var = sum((xi - mean)**2 for xi in x) / (len(x) - 1)
        return (var)

    def std(self, x):
        return (math.sqrt(self.var(x)))



if __name__=="__main__":
    ts = TinyStatician()
    # a_pair = np.array([1, 3, 4,3, 5,6, 6, 7, 8, 8])
    # a_pair = [ 1, 11, 15, 19, 20, 24, 28, 34, 37, 47, 50, 61]
    # a_impair = np.array([2, 4, 4, 5, 6, 7, 8])
    # a = [ 1, 11, 15, 19, 20, 24, 28, 34, 37, 47, 50, 61, 68]
    # a = [1, 11, 15, 19, 20, 24, 28, 34, 37, 47, 50, 61]
    a = [1, 42, 300, 10, 59]
    # print(ts.quartile(a))
    # print([np.quantile(a, 0.25), np.median(a), np.quantile(a, 0.75)]) #to compare with np builtiln quartle function
    # print(ts.percentile(a, 10))
    # print(np.percentile(a, 10))
    print(ts.var(a))
    print(np.var(a))
    print(ts.std(a))


