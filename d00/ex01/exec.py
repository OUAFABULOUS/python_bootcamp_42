import sys

if __name__ == "__main__":
    ac = len(sys.argv)
    if ac == 1:
        print("usage: .exe arg1 arg2 ...")
        sys.exit(1)
    for i,arg in enumerate(sys.argv):
       if i > 0:
           new_arg = arg[::-1].swapcase()
           print(new_arg, end="")
           if (i < ac - 1):
               print(" ", end="")
