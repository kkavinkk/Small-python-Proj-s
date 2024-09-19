import random

def player():
    choice = input("Rock, Paper or Scissors?:").lower
    while choice not in ['Rock', 'Paper', 'Scissors']:
        choice = input("Invalid choice, Rock, Paper or Scissors?:").lower()
    return choice

def computer():
    computerchoice = ['Rock', 'Paper', 'Scissors']
    return random.choice(computerchoice)

def main(choice, computerchoice):
    if choice == computer:
        print("Its a Tie")
    elif(choice == 'rock' and computerchoice == "Scissors") or \
        (choice == 'rock' and computerchoice == "Scissors") or \
        (choice == 'rock' and computerchoice == "Scissors") or :
        print("You beat the mighty computer")
    else:
        return "Computer Wins! We are all doomed"
    
def play:
    choice = getuserchoice()
    computerchoice = getcomputerchoice()
    result = winner(choice, computerchoice)
    print(result)

play_game()