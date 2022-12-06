import numpy as np

class Vector:
    def	__init__(self, *args):
        length = len(args[0])
        if (length > 1):
            self.values = []
            self.shape = (1, length)
            for i in range(length):
                self.values.append(args[0][i][0])
        else:
            self.shape = (length, 1)
            self.values = args[0]
    def	dot(self, a):
        if not isinstance(a, Vector) or a.shape!=self.shape:
            print("Dot product error: Vectors should have the same type")
            quit
        res = 0
        for vec1,vec2 in zip(a.values, self.values):
            res += vec1*vec2
        return (res)
    def	T(self):
        self.shape = self.shape[::-1]
