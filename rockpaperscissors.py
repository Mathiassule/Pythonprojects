import random

""" def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"
    
    # r > s, s > p, p > r
    if is_win(user, computer):
        return "You won!"
    
    return "You lost!"

def is_win(player, opponent):
    # return true if player wins

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True """
    
def gamestart():
    user = input("Choose between rock 'r', paper 'p' or scissors 's'\n")
    computer = random.choice(['r', 'p', 's'])
    # r > s, s > p, p > r
    if user == computer:
        return "It's a tie!!"
    
    if userwins(user, computer):
        return "You win!!!"
    
    return "You lost!"

def userwins(player, opponent):
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
            return True

print(gamestart())