import functools

def ft_reduce(function_to_apply, iterable):
    try:
        a = iterable[0]
        for i in range(len(iterable) - 1):
            res = function_to_apply(a, iterable[i + 1])
            a = res
        return a
    except:
        return None

if __name__=="__main__":
    lst = [1, 2, 3]
    print(ft_reduce(lambda a, b: a * b, lst))
