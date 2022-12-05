import sys
import string

def text_analyzer(*ag):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if not len(ag) or ag == None:
        ag = input("What is the text to analyze?")
        # if not ag[0]:
            # sys.exit(1)
    if not ag:
        ag = ""
    else:
        ag = ag[0]
    print(f"this is thr TYYYYYYYYYPE: {type(ag)}")
    if (type(ag) is not str):
        print("AssertionError: argument is not a aging")
        sys.exit(1)
    uppercase_count = 0
    lowercase_count = 0
    punctuation_mark = 0
    space = 0
    for char in ag:
         uppercase_count += char.isupper()
         lowercase_count += char.islower()
         punctuation_mark += char in string.punctuation
         space += char.isspace()
    print(f"The text contains {len(ag)} character(s):")
    print(f"- {uppercase_count} upper letter(s)")
    print(f"- {lowercase_count} lower letter(s)")
    print(f"- {punctuation_mark} punctuation mark(s)")
    print(f"- {space} space(s)")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error")
        exit(1)
    text_analyzer(sys.argv[1])

