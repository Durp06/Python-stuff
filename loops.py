def looper():
    loops = int(input("Enter the number of words: "))
    int i=0
    words = []
    
    while (i<=loops):
        toAdd = input("Enter word ", i, ": ")
        words.append(toAdd)
        i+=1

    for word in words:
        print(words[word])
looper()
