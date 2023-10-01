# assignment: programming assignment 1
# author: (write your full name here)
# date: (write the date you finished working on the program)
# file: hangman.py is a program that (put the description of the program)
# input: (write input description)
# output: (write output description)

from random import choice, random

dictionary_file = "dictionary.txt"   # make a dictionary.txt in the same folder where hangman.py is located

# write all your functions here
# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12

def import_dictionary (filename) :
    dictionary = {}

    with open(filename,"r") as file:
        word_list = file.readlines()
        word_list = [word.strip() for word in word_list]
        dictionary = {len(word): [] for word in word_list}
        for word in word_list:
            max_size = len(word)
            if max_size > 12:
                max_size = 12
            dictionary[max_size].append(word)
    return dictionary

# print the dictionary (use only for debugging)
# get options size and lives from the user, use try-except statements for wrong input

def get_game_options () :
    valid_sizes = list(range(3, 13))  # valid sizes are 3 to 12
    try:
        size = input("Please choose a size of a word to be guessed [3 – 12, default any size]:")
        if int(size) > 12:
            size = choice(valid_sizes)
        else:
            size = int(size)
    except ValueError:
        size = choice(valid_sizes)
    print(f"The word size is set to {size}.")
    try:
        lives = int(input("Please choose a number of lives [1 – 10, default 5]:"))
        if lives > 10:
            lives = 5
    except ValueError:
        lives = 5
    print(f'You have {lives} lives.')
    return (size, lives)

# MAIN

if __name__ == '__main__' :

    # make a dictionary from a dictionary file
    dictionary = import_dictionary("dictionary.txt")
    # print the dictionary (use only for debugging)
    # remove after debugging the dictionary function import_dictionary
print("Welcome to the Hangman Game!")
end = False
while end == False:
    size, lives = get_game_options()
    word_list = dictionary[size]
    word = choice(word_list)
    word_list = word.split
    word = word.upper()
    complete_word = "__ " * size
    complete_word = complete_word.split()
    start_lives = lives
    letter_string = []
    old_guess = []
    guess = ""
    if "-" in word:
            for k in range(len(word)):
                if word[k] == "-":
                    complete_word[k] = "-"
    already = False
    enter_guess = True
    while lives > 0: 
        complete_word_str = ' '.join(complete_word)
        length_guess = True
        enter_guess = True
        letter_string = ''.join(letter_string).upper()
        circles = "O" * lives
        cross = 'X' * (start_lives - lives)
        result = cross + circles
        old_guess.append(guess)
        while already==False:
            print("Letters chosen:",letter_string)
            print(f'{complete_word_str} lives: {lives} {result}')
            break
        already = False
        if letter_string != '':
            letter_string +=  ","
        guess = input("Please choose a new letter >").upper()
        while enter_guess == True:
            if not guess.isalpha():
                guess = input("Please choose a new letter >").upper()
            elif guess == "" :
                guess = input("Please choose a new letter >").upper()
                continue
            else:
                break
        while length_guess == True:
            if len(guess) >1:
                guess = input("Please choose a new letter >").upper()
            else:
                break
        if guess in word:
            if guess in old_guess:
                print("You have already chosen this letter.")
                already = True
            else:
                print("You guessed right!")
                letter_string += guess
            letter_string = letter_string.rstrip(",")
            new_complete_word = []
            for i in range(len(word)):
                if guess == word[i]:
                    new_complete_word += [guess]
                else:
                    new_complete_word += [complete_word[i]]
            complete_word = new_complete_word
        else:
            if guess in old_guess:
                letter_string = letter_string.rstrip(",")
                print("You have already chosen this letter.")
                already = True
            else:
                letter_string +=guess
                letter_string = letter_string.rstrip(",")
                print("You guessed wrong, you lost one life.")
                lives -=1
        if lives > 0 and "__" not in complete_word:
            complete_word_str = ' '.join(complete_word)
            letter_string = letter_string.rstrip(",")
            print(f'Letters chosen: {letter_string}')
            print(f'{complete_word_str}, "lives:", {lives}, {result}')
            print(f'Congratulations!!! You won! The word is {word}!')
            last = input("Would you like to play again [Y/N]?").upper()
            if last == "Y":
                break
            else:
                print("GoodBye!")
                end = True
                break
        elif lives == 0 and "__" in complete_word :
            complete_word_str = ' '.join(complete_word)
            cross = 'X' * (start_lives - lives)
            result = cross
            letter_string = letter_string.rstrip(",")
            print(f'Letters chosen: {letter_string}')
            print(f'{complete_word_str} "lives:" {lives} {result}')
            print(f'You lost! The word is {word.upper()} !')
            last = input("Would you like to play again [Y/N]?").upper()
            if last == "Y":
                lives = start_lives
                break
            else:
                print("GoodBye!")
                end = True
                break
    # print a game introduction

    # START MAIN LOOP (OUTER PROGRAM LOOP)

    # set up game options (the word size and number of lives)

    # select a word from a dictionary (according to the game options)
    # use choice() function that selects an item from a list randomly, for example:
    # mylist = ['apple', 'banana', 'orange', 'strawberry']
    # word = choice(mylist)
    
        # START GAME LOOP   (INNER PROGRAM LOOP)

        # format and print the game interface:
        # Letters chosen: E, S, P                list of chosen letters
        # __ P P __ E    lives: 4   XOOOO        hidden word and lives

        # ask the user to guess a letter

        # update the list of chosen letters

        # if the letter is correct update the hidden word,
        # else update the number of lives
        # and print interactive messages      

        # END GAME LOOP   (INNER PROGRAM LOOP)

        # check if the user guesses the word correctly or lost all lives,
        # if yes finish the game

    # END MAIN LOOP (OUTER PROGRAM LOOP)

    # ask if the user wants to continue playing, 
    # if yes start a new game, otherwise terminate the program
