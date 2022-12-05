import sys

if __name__ == "__main__":
    ac = len(sys.argv)
    if ac != 2 or not sys.argv[1].isdigit():
        if not ac == 1:
            print("Error: The program accepts only one single integer arg")
        print("usage: exec.py arg")
        sys.exit(1)
    if int(sys.argv[1]) == 0:
        print("I'm Zero.")
    elif int(sys.argv[1]) % 2:
        print("I'm Odd.")
    else:
        print("I'm Even.")


