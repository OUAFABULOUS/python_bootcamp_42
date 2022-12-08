import numpy as np
import random

class	NumPyCreator:
    def	from_list(self, lst, ar_type):
        return(np.array(lst, dtype=object))
    def	from_tuple(self, tpl):
        return(self.from_list(tpl))
    def	from_iterable(self, itr):
        return(self.from_list(itr))
    def	from_shape(self, shape, value=0):
        return(np.full(shape, value))
    def	random(self, shape):
        return(self.from_shape(shape, random.random()))
    def	identity(self, n):
        return(np.identity(n))


if 	__name__=="__main__":
    np_creator=NumPyCreator()
    lst = [1, 2, [3, 4, [1, 2, [3]]]]
    tpl = ("a", "b", ("c", "d"))
    str = "abc123"
    dict = {"a" : 1, "b" : {"d" : 3, "c" : 1}}
    # ar_lst = np_creator.from_list(lst)
    # print(ar_lst)
    # print(type(ar_lst))
    # ar_tpl = np_creator.from_tuple(tpl)
    # print(ar_tpl)
    # print(type(ar_tpl))
    # ar_str = np_creator.from_iterable(str)
    # print(ar_str)
    # print(type(ar_str))
    # ar_dict = np_creator.from_iterable(dict)
    # print(ar_dict)
    # print(type(ar_dict))
    print(np_creator.from_shape((2, 5), 1))
    print(np_creator.random((1, 5)))
