import numpy as np

class	TinyStatician:
    def __init__(self):
        pass
    def	mean(self, x):
        return sum(x) / len(x)
    def	median(self, x):
        x.sort()
        n = len(x)
        if n % 2:
            return x[int((n + 1) / 2) - 1]
        else:
            n_bef = int((n / 2) - 1)
            n_aft = int(n / 2)
            return((x[n_bef] + x[n_aft]) / 2)
    def	quartile(self, x):
        try:
            quartiles = []
            x.sort()
            n = len(x)
            if not n % 2:
                quartiles.append(self.median(x[:n//2]))
                quartiles.append(self.median(x))
                quartiles.append(self.median(x[n//2:]))
            else:
                quartiles.append(self.median(x[:(n+1)//2 - 1]))
                quartiles.append(self.median(x))
                quartiles.append(self.median(x[(n + 1) // 2:]))
            return quartiles
        except:
            pass

if __name__=="__main__":
    ts = TinyStatician()
    # a_pair = np.array([1, 3, 4,3, 5,6, 6, 7, 8, 8])
    a_pair = [ 1, 11, 15, 19, 20, 24, 28, 34, 37, 47, 50, 61]
    a_impair = np.array([2, 4, 4, 5, 6, 7, 8])
    print(ts.quartile(a_pair))
    print(np.quantile(a_pair, 0.75))
    # print(ts.quartile(a_impair))

