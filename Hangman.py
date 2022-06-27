import random #importing the random module 

file = open('words.txt', 'r') #opening a text file
f = file.readlines() #reading the lines on the text file
word_list = [] #creating a list to store different words in the text file

for word in f: #for loop to remove the '\n' after each word
    if word[-1] == "\n": #checks if the word has the '\n' at the end
        word_list.append(word[:-1]) #appends the word and removes the '\n' at the end of it
    else:
        word_list.append(word) #if the word doesn't have '\n' then it adds the complete word

def get_word(word_list):
    word = random.choice(word_list)
    return word

print(get_word(word_list))

file.close() #closing the file
