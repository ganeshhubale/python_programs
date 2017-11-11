if __name__ == '__main__':
    print("welcome")
    word = "EVAPORATE"
    guessed = "_" * len(word)
    word = list(word)
    guessed = list(guessed)
    lsguessed = []
    letter = input("guess letter: ")
    while True:
        if letter.upper() in lsguessed:
            letter = ""
            print("Already guessed")
        elif letter.upper() in word:
            index = word.index(letter.upper())
            guessed[index] = letter.upper()
            word[index] = "_"
        else:
            print(''.join(guessed))
            if letter is not '':
                lsguessed.append(letter.upper())
            letter = input("guess :")
        if '_' not in guessed:
            print("you won")
            break
