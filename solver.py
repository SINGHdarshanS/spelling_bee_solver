import numpy as np

letters = []
i = 0
cont = False
# gathering outer letters
while i < 6:
    cont = False
    pot = input("Input one of the external letters... \t").lower().lstrip().rstrip()
    cont = True
    if not pot.isalpha():
        print("Please input a letter, not a number or character")
        cont = False

    if len(pot) > 1:
        print("Please enter only one character")
        cont = False

    if pot in letters:
        print("You have already inputted \'{}.\' Please enter a different letter".format(pot))
        cont = False

    if cont:
        letters.extend(pot)
        i += 1

cont = False
center = ""
# gathering central letter
while not cont:
    cont = False
    center = input("Please input the letter in the center\t").lower().lstrip().rstrip()
    cont = True

    if not center.isalpha():
        print("Please input a letter, not a number or character")
        cont = False

    if len(center) > 1:
        print("Please enter only one character")
        cont = False

    if center in letters:
        print("You have already inputted \'{}.\' Please enter a different letter".format(center))
        cont = False


