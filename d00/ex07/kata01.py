kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

if __name__ == "__main__":
    for i in range(len(kata)):
        print(f"{list(kata.keys())[i]} was created by {kata[list(kata.keys())[i]]}")
