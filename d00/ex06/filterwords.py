import sys
import argparse
import string

def	find_punc_numb(str):
    nb_punc = 0
    for i in range(len(str)):
        nb_punc += str[i] in string.punctuation
    return(nb_punc)

def	good_string(str, n):
    return (len(str) - find_punc_numb(str)) > n

if __name__ == "__main__":
    ac = len(sys.argv)
    if ac == 1:
        print("usage: exec.py S(string) N(int)")
        sys.exit(1)
    parser = argparse.ArgumentParser()
    parser.add_argument('S', type=str)
    parser.add_argument('N', type=int)
    args = parser.parse_args()
    s_split = args.S.split()
    res = [x for x in s_split if good_string(x, args.N)]
    res_bis = [s.translate(s.maketrans("", "", string.punctuation)) for s in res]
    print(res_bis)
