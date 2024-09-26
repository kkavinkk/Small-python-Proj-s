"""
WELCOME



"""



text = input("Text: ")

letter = 0
space = 0
sentence = 0

for characters in text:
    if characters.isalpha():
        letter += 1
    elif characters == " ":
        space += 1
    elif characters == "." or characters == "?" or characters == "!":
        sentence += 1

words = space + 1

L = (letter / words) * 100
S = (sentence / words) * 100

index = 0.0588 * L - 0.296 * S - 15.8

if index > 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {round(index)}")
