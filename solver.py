from cutdown import trim

trim()
letters = set()
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
        letters.add(pot)
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
letters.add(center)

wordcount = 0
with open('todays_answers.txt', 'w') as answers:
    with open('short_words.txt', 'r') as words:
        for line in words:
            yes = True
            temp = line.rstrip()
            chars = set()
            for char in temp:
                chars.add(char)
            # print(chars)
            if center not in chars:
                continue
            else:
                for char in chars:
                    if char not in letters:
                        yes = False
                        break
            if yes:
                if len(line.rstrip()) >= 4:
                    # print(line.rstrip())
                    wordcount += 1
                    answers.write(line)
print("There are {} possible solutions to today's spelling bee".format(wordcount))

print('\n\n\n\n\n If the following words work please enter yes and press enter, otherwise just press enter...\n\n')

with open('todays_answers.txt', 'r') as f:
    with open('blacklist.txt', 'a') as black:
        for line in f:
            yn = input(f'{line.rstrip()}?\t')
            if not yn:
                black.write(line)

print('Blacklist updated')

with open('whitelist.txt', 'a') as f:
    extra = input("\n\nDid we miss any words from yesterday? Type \'no\' if there were none. Press enter otherwise.\t\t")
    if extra.lower().lstrip().rstrip() != 'no':
        f.write('\n')
        word = input("\nType a word that we missed from yesterday. If none remain, just press enter.\t\t")
        while word:
            f.write(word+'\n')
            word = input("\nType a word that we missed from yesterday. If none remain, just press enter.\t\t")

print('Whitelist updated')
