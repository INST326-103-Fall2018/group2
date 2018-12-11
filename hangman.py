#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Name: Chris Davis
# Directory ID: cdav1601
# Date: 2018-11-12
# Assignment: Midterm 2, Question 4



import sys
import string
import random



#Opens a file given in command line and creates list
def words_in_file(file):

    #Open file given in command line
    fhand = open(file)


    #Create dictionary
    word_list = list()

 
    for line in fhand:
        
        #Removes punctuation
        line = line.translate(str.maketrans('', '', string.punctuation))

        #Make all words uppercase so each word is counted
        line = line.upper()
        
        #Seperate each word to be counted
        words = line.split()

        #Removes 'hyphen', or 'em dash'
        words = [word.replace('—', '') for word in words]
    

        #Either adds word to dictionary or adds 1 to existing entry
        for word in words:

            if word not in word_list:

                word_list.append(word)

            else:

                pass

    return word_list




def main():

    #Will allow user to keep playing until they choose to quit
    keep_playing = True

    wins = 0
    total_games = 0


    while keep_playing:



        #Variables, dictionaries, and lists
        #----------------------------------------------------------

        #Reads file into function for list of words
        #hangman_words = (words_in_file(sys.argv[1]))
        hangman_words = (words_in_file('m2_hangman_words.txt')) 

        #Chooses a random word from the list for user to guess
        rand_word = random.choice(hangman_words)
        
        #Dictionary used to track correct guesses
        num_guessed = dict.fromkeys(rand_word, 0)

        #Tracks correct guesses
        correct = 0

        #Tracks incorrect guesses
        strikes = 5

        #----------------------------------------------------------
        


        print("\nWelcome to Hangman!\n")
        #Displays underscores representing hidden letters in word
        print("_ " * len(rand_word))


        #User can continue guessing until 5 incorrect guesses
        while strikes != 0:


            #Asks and stores user guess as uppercase letter
            while True:

                guess = input("Please guess a letter: ")
                guess = guess.upper()


                if guess.isalpha(): #Makes sure user only enters letter
                    break


            #Loop if guess is correct
            if guess in rand_word and guess is not "":

                print ("Correct!", '\n')

                num_guessed[guess] = 1


                #Loop for instances of char, with each counting towards winning
                for L in rand_word:

                    if guess in L:

                        correct = correct + 1 #increment


                #If the correct number of guesses are made, user wins
                if correct == len(rand_word):

                    #Replace underscores with correct guess
                    game_line = (" ".join([letter if num_guessed[letter]\
                        else "_" for letter in rand_word]))
                         
                    print(game_line)

                    wins = wins + 1
                    print("Winner! The word was ", rand_word, "!", sep = '')

                    break


            #If guess is incorrect
            else:

                strikes = strikes - 1 #increment

                print("Incorrect:", (strikes), "guess(es) remaining!",'\n')


            #Replace underscores with correct guess in appropriate position
            game_line = (" ".join([letter if num_guessed[letter]\
                        else "_" for letter in rand_word]))


            print(game_line)


        #If maximum number of guesses are used, user loses the game
        else:

            print("Sorry, you lose! The word was ", rand_word, "!", sep = '')

        total_games = total_games + 1

        #Loop for quitting conditions
        while True:

            #User chooses to keep playing or quit
            print(wins, "wins", "/", total_games, "total games")
            keep_playing = input("Play again? (Y/N): ")
            keep_playing = keep_playing.upper()


            if keep_playing == 'Y':

                break
                

            elif keep_playing == 'N':

                print('\nThanks for playing!\n')

                keep_playing = False

                #exit()
                return 'q', wins


            else:

                print('Invalid entry')

                continue



if __name__ == '__main__':
    main()
