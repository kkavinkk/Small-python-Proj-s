import random

def player():
    choice = input("rock, paper or scissors?: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice, rock, paper or scissors?: ").lower()
    return choice

def computer():
    computerchoice = ['rock', 'paper', 'scissors']
    return random.choice(computerchoice)

def winner(choice, computerchoice):
    if choice == computerchoice:
        return "Its a Tie" 
    elif(choice == 'rock' and computerchoice == "Scissors") or \
        (choice == 'rock' and computerchoice == "Scissors") or \
        (choice == 'rock' and computerchoice == "Scissors"):
        return "You beat the mighty computer"
    else:
        return "Computer Wins! We are all doomed"
    
def play():
    choice = player()
    computerchoice = computer()
    result = winner(choice, computerchoice)
    print(result)

play()