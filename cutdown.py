# file to trim down words_alpha.txt into short_words.txt, which will contain words consisting of only 7 letters or less
from nltk.corpus import words
import nltk

nltk.download('words')

def letter_count(word):
    word = word.rstrip()
    pool = set()
    for char in word:
        if char.isalpha():
            pool.add(char)
    return len(pool)


nf = open('short_words.txt', 'w')
# with open('words_alpha.txt', 'r') as f:
#     for line in f:
#         count = letter_count(line.rstrip())
#         if count <= 7:
#             nf.write(line)
#             print(line.rstrip())

word_list = words.words()
with open('blacklist.txt', 'r') as f:
    blacklist = f.read()
    for word in words.words():
        word = word.lower()
        count = letter_count(word)
        if count <= 7:
            if word not in blacklist:
                nf.write(word+'\n')
                print(word)


nf.close()
