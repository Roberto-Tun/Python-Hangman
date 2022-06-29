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
    for letters in wordlist: #for loop that appends '-' to the list of hidden letters for each by using the length of the word
        hidden_word.append("-") #appending the '-' in the hidden word list

    print("----------------------------------")
    print("--------Welcome To Hangman--------")#ui to welcome users
    print("----------------------------------")
    
    gameover = False
    while gameover == False: #user can guess until gameover = True

        hidden_string = " ".join(hidden_word) #converting the list to a string
        print("You Have", lives, "lives left") #printing the amount of lives they have
        print("The word to Guess is:", hidden_string) #printing the word to guess by placing '-'
        display_hangman(lives) #function called to draw the state of the hangman


        Guessed_letter = input("Enter your Guess: ").lower() #letter the user guessed
        if Guessed_letter in wordlist and Guessed_letter.isalpha: #if that checks if the letter entered by the user is in the word list (word) and is a letter and not a int
            Guessed_letters.append(Guessed_letter) #appending the letter entered into the list that keeps track of the letters that have been guessed
            for i in range(len(wordlist)): #for loop that run the length of the word
                character = word[i] #assigns the letter of the word at that index and assigns it to the variable labelled 'character'
                if character == Guessed_letter: #checks if the letter guessed is = to the 'character'
                    hidden_word[i] = word[i] #replaces the character in the hidden list where its index is = to the index of the word with the letter at that point
                    wordlist[i] = "-" #replaces the charcter at the index of the same letter with '-'
        elif Guessed_letter not in word and Guessed_letter not in Guessed_letters: #eluf that deacreases the lives of the user if they guessed wrong
            lives -= 1
            Guessed_letters.append(Guessed_letter) #appending the letter entered into the list that keeps track of the letters that have been guessed
        elif Guessed_letter in Guessed_letters: #checks if the word entered is in the list of guessed words
            print("You already Guessed this letter.")

        if (all("-" == char for char in wordlist)): #one line for to check if the characters in the wordlist(list) are all = "-" to check if the person has won
            gameover = True

        if lives == 0: #checks if the lives is 0 to stop the loop
            gameover = True

    else: #else that checks if the person won or lost
        if lives > 0:
            print("Congrats You won") 
        else:#else that prints the final score after you lost 
            display_hangman(lives)
            print("You Lost")
            print("The word was:",word)

#while loop to continue playing
play = input("Would you like to play hangman? Enter 'Y' or 'N' ")
while play.upper() == "Y":
    hangman()
    play = input("Would you like to play again? Enter 'Y' or 'N' ")
else:
    print("I guess your boring")
    exit()

#closing the file
file.close() #closing the file
