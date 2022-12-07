def	ft_map(function_to_apply, iterable):
    try:
        for item in iterable:
            yield function_to_apply(item)
    except:
        return None

def	fun_test(nb):
    return(nb * nb)

if __name__=="__main__":
    lst = [4,5,6,7]
    print(list(ft_map(fun_test, lst)))

