def ft_filter(function_to_apply, iterable):
    try:
        for item in iterable:
            if function_to_apply(item):
                yield item
    except:
        return None

def	func_test(nb):
    return not nb % 2

if __name__=="__main__":
    lst = [1, 2, 3, 4]
    print(list(ft_filter(func_test,1)))
