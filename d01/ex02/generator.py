import random
import sys
import argparse

def generator(text, sep=" ", option=None):
    for c in text:
        if not c.isprintable():
            print("The text should only contain printable chars!")
            quit
    res = text.split(sep)
    if option == "shuffle":
        for i in range(len(res)):
            other = random.randint(0, len(res) - 1)
            if i == other:
                continue
            else:
                res[i], res[other] = res[other], res[i]
    elif option == "unique":
        unique_list = []
        for i in range(len(res)):
            if res[i] not in unique_list:
                unique_list.append(res[i])
        res = unique_list
    elif option=="sort":
        res.sort()
    elif option!="":
        print("The only options possible are: shuffle, sort, unique")
        quit
    for elem in res:
        yield elem




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Introduce the txt + the Sep")
    parser.add_argument('text', type=str)
    parser.add_argument('sep', type=str)
    args =parser.parse_args()
    # for word in generator(args.text, args.sep):
        # print(word)
    # for word in generator(args.text, args.sep, option="shuffle"):
        # print(word)
    # for word in generator(args.text, args.sep, option="unique"):
        # print(word)
    for word in generator(args.text, args.sep, option="sort"):
        print(word)
