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
    max_attempts = len(word+5)
    attemps = 0
    

hangman()