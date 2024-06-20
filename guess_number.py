import random

def guess(y):
    myrand = random.randint(1, y)
    guess = 0

    while guess != myrand:
        guess = int(input(f"Input a number between 1 and {y}: \n"))
        if guess < myrand:
            print("Too low! Guess again")
        elif guess > myrand:
            print("Too high! Guess again")
    print(f"Yay! You guessed the number {myrand} correctly!")


def computguess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            matguess = random.randint(low, high)
        else: 
            matguess = low # low = high
        
        feedback = input(f"Is {matguess} too high 'h', too low 'l' or correct 'c'? \n")
        if feedback == 'h':
            high = matguess -1
        elif feedback == 'l':
            low = matguess + 1
        
    print(f"Yay! The computer guessed {matguess} correctly!")


computguess(2500)
