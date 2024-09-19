from random import randint

#list of choices
choice = ["Rock", "Paper", "Scissors"]

#computer choses
computer = choice[randint(0, 2)]
player = False
while player == False:
    player = input("Rock, Paper or Scissors?:")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "Suffocates", player)
        else:
            print("You Win!", player, "Smashes computer like a luddite", player)
    elif player == "Paper":
        if computer == "Scissor":
            print("You lose!", computer, "Shanks", player)
        else:
            print("You Win!", player, "Suffocates", player)
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "Suffocates", player)
        else:
            print("You Win!", player, "Smashes computer like a luddite", player)