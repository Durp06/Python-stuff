def ifpractice():
    state = int(input("Pick a number: "))

    if(state>10):
        print(state, " is greater than 10")
    elif(state<10):
        print(state, " is less than 10")
    else:
        print("Your number is ", state)

ifpractice()