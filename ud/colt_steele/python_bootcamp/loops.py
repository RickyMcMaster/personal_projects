from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0 # store random number in here, each time through
i = 0  # i should be incremented by one each iteration

while number != 5:
    i += 1
    number = randint(0, 11)

# print(i)3
    
# Guessing game

guess_ans = randint(1, 10)
response = ""

while guess_ans != response:
    response = int(input("Guess a number between 1 and 10: "))
    if response < guess_ans:
        print("Too low, try again!")
    elif response > guess_ans:
        print("Too high, try again!")
    else:
        print(f"You guessed it!  The correct answer was {guess_ans}.")
        cont_response = ""
        while cont_response not in ("y", "n"):
            cont_response = input("Do you want to keep playing?  (y/n) ")
            if cont_response == "y":
                guess_ans = randint(1, 10)
                response = ""
            elif cont_response == "n":
                print("Goodbye!  See you next time!")
                break
            else:
                print("Not a valid response.")