import random

def hangman():
    total=int (input("How many words would you like to possibly have"))
    i=0
    words = []
    while (i<total):
        wordforlist = input("Enter a word ")
        words.append(wordforlist)
        i=i+1
    word = random.choice(words)
    guessed = []
    max_attempts = len(word)+5
    attempts = 0

    while True:
        print("\nWord: ", end=" ")
        for letter in word:
            if letter in guessed:
                print(letter, end=" ")
            else:
                print("_", end=" ")

        guess = input ("\nGuess a letter: ").lower()

        if guess in guessed:
            print(guess, " has already been guessed")
            continue
        elif guess in word:
            guessed.append(guess)
            print(guess, " is correct")
        else:
            attempts +=1
            print(guess, " is not correct ", max_attempts-attempts, " guesses left")
            if attempts == max_attempts:
                print("You ran out of guesses, cope")
                return
        if all(letter in guessed for letter in word):
            print("You guessed the word, noice")
            return
hangman()