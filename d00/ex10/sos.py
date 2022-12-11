import sys
import argparse
import string

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'}

def	word_to_morse(word):
    morse_word = ''
    try:
        for c in word:
            if c!=' ':
                morse_word += MORSE_CODE_DICT[c.upper()] + ' '
            else:
                morse_word += '/'
        return (morse_word)
    except:
        print("ERROR")
        return None


if	__name__=="__main__":
    ac = len(sys.argv)
    if ac == 1:
        print("usage: sos.py S_to_trtanslate(string)")
        sys.exit(1)
    parser = argparse.ArgumentParser()
    for i,arg in enumerate((sys.argv)[1:]):
        parser.add_argument("var"+str(i), type=str)
    args = parser.parse_args()
    morse_code = ""
    try:
        for i, arg in enumerate(vars(args).values()):
            morse_code += word_to_morse(arg)
            if i != len(vars(args)) - 1:
                    morse_code += '/'
        print(morse_code)
    except:
        pass

