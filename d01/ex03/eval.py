class Evaluator:
    def	zip_evaluate(coefs, words):
        if not all(isinstance(item, str) for item in words) or not all(isinstance(item, float) for item in coefs) or not len(words)==len(coefs):
            print("Error!!")
            print("Usage: exec.py [list_coefs] [list_words]")
        len_totale = 0
        for word, coef in zip(words, coefs):
            len_totale+=len(word)*coef
        print(len_totale)

    def	enumerate_evaluate(coefs,words):
        if not all(isinstance(item, str) for item in words) or not all(isinstance(item, float) for item in coefs) or not len(words)==len(coefs):
            print("Error!!")
            print("Usage: exec.py [list_coefs] [list_words]")
        len_totale = 0
        for i,word in enumerate(words):
            len_totale+=len(word)*coefs[i]
        print(len_totale)


