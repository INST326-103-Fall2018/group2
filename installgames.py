#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Name: Chris Davis
#Assignment: Final Project

import os.path
import games
from games import *



#Provides list of games in package to populate main menu
def gamelist():

	#Add name of game as it should appear in the menu
	return(['Hangman', 'game2', 'Blackjack'])
gamelist.__doc__ = """List of available games"""



#Executes Hangman game
def hangmanexec():

	
	return hangman.main()
hangman.__doc__ = """Executes Hangman game"""



def game2():

	print("This is for game 2")


def blackjackexec():

	return Blackjack.main()
Blackjack.__doc__ = """Executes Blackjack game"""



if __name__ == '__main__':
    assert hangmanexec() == True
    assert blackjackexec() == True