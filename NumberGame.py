import random
import math

#take inputs for a lower and upper bound
lower_bound = int(input("input lower bound: "))
higher_bound = int(input("input higher bound: "))

#generate random integer withing the bounds
random_ans = random.randint(lower_bound, higher_bound)
guesses = 5
print("you have 5 guesses to get the right answer")

count = 0
flag = False
#use a while loop to repeat guessing
while count < 5:
    count += 1

    guess = int(input("Guess a number: "))

    if guess == random_ans:
        print("Correct")
        flag = True
        break
    # if the user guessed higher print a message and repeat the question
    if guess > random_ans:
        print("Too high")
    # else the user guessed lower print message and repeast
    elif guess < random_ans:
        print("Too low")
    # if the user guessed right print a message
    #else if the user didnt guess correctly print a message for losing
if not flag:
    print("Bad luck")
