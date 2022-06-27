import random #importing the random module 

lives = 6

file = open('words.txt', 'r') #opening a text file
f = file.readlines() #reading the lines on the text file
word_list = [] #creating a list to store different words in the text file

#note that each word is a line, therefore -1 index is for each line(word)
for word in f: #for loop to remove the '\n' after each word and append it to the empty list
    if word[-1] == "\n": #checks if the word has the '\n' at the end
        word_list.append(word[:-1]) #appends the word and removes the '\n' at the end of it
    else:
        word_list.append(word) #if the word doesn't have '\n' then it adds the complete word

def get_word(word_list): #function used to get a random word from the list
    word = random.choice(word_list) #random module used to get a random word form the list
    return word

def hangman():
    word = get_word(word_list)
    while len(word) > 0 and lives > 0:
        Guessed_letter = input("Enter your Guess: ").lower()


def display_hangman(lives):
    if lives == 6:
        print("|------|   ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|______    ")
    elif lives == 5:
        print("|------|   ")
        print("|      O   ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|______    ")
    elif lives == 4:
        print("|------|   ")
        print("|      O   ")
        print("|      |   ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|______    ")
    elif lives == 3:
        print("|------|   ")
        print("|      O   ")
        print("|     /|   ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|______    ")
    elif lives == 2:
        print("|------|   ")
        print("|      O   ")
        print("|     /|\  ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|______    ")
    elif lives == 1:
        print("|------|   ")
        print("|      O   ")
        print("|     /|\  ")
        print("|     /    ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|______    ")
    elif lives == 0:
        print("|------|   ")
        print("|      O   ")
        print("|     /|\  ")
        print("|     / \  ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|______    ")
file.close() #closing the file
