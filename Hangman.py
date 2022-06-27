import random #importing the random module 
file = open('words.txt', 'r')
f = file.readlines()
word_list = []

for word in f:
    if word[-1] == "\n":
        word_list.append(word[:-1])
    else:
        word_list.append(word)

print(word_list)

file.close()
