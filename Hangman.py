import random #importing the random module 

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

def display_hangman(lives): #function that creates the state of the hangman
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

def hangman():

    lives = 6 #assingning the amount of lives
    word = get_word(word_list) #assigning the word returned from the function
    Guessed_letters = [] #Empty list to stores words that have been guessed
    wordlist = list(word) #turning the word into a list
    hidden_word = [] #Empty list that will have '-' for the amount of letters in the word that need to be guessed
    for letters in word: #for loop that appends '-' to the list of hidden letters for each by using the length of the word
        hidden_word.append("-") #appending the '-' in the hidden word list

    print("----------------------------------")
    print("--------Welcome To Hangman--------")#ui to welcome users
    print("----------------------------------")

    while lives > 0: #user can guess until lives = 0

        hidden_string = " ".join(hidden_word) #converting the list to a string

        print("You Have", lives, "lives left") #printing the amount of lives they have
        print("The word to Guess is:", hidden_string) #printing the word to guess by placing '-'
        display_hangman(lives) #function called to draw the state of the hangman
        Guessed_letter = input("Enter your Guess: ").lower() #letter the user guessed
        if Guessed_letter in wordlist and Guessed_letter.isalpha: #if that checks if the letter entered by the user is in the word list (word) and is a letter and not a int
            Guessed_letters.append(Guessed_letter) #appending the letter entered into the list that keeps track of the letters that have been guessed
            for i in range(len(word)): #for loop that run the length of the word
                character = word[i] #assigns the letter of the word at that index and assigns it to the variable labelled 'character'
                if character == Guessed_letter: #checks if the letter guessed is = to the 'character'
                    hidden_word[i] = word[i] #replaces the character in the hidden list where its index is = to the index of the word with the letter at that point
                    wordlist[i] = "-" #replaces the charcter at the index of the same letter with '-'
        if Guessed_letter in Guessed_letters:
            print("You already Guessed this letter.")
        elif Guessed_letter not in word and Guessed_letter not in Guessed_letters:
            lives -= 1
        else:
            print("Invalid Input:")

    else:
        display_hangman(lives)
        print("You Lost")
        print("The word was:",word)


hangman()

file.close() #closing the file
