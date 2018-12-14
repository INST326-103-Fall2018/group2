#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Name: Chris Davis
#Assignment: Final Project


import pandas
import csv
import sys
import os.path
import installgames
from installgames import *




#create or load profile
def user_profile(game_list):
	

	if len(sys.argv) < 2:


		print("Welcome new user!")
		user = input("Enter username: ")
		user_save = user + '.csv'

		print('Creating profile...')


		with open(user_save, 'w') as file:
			headers = game_list
			writer = csv.DictWriter(file, fieldnames=headers)

			writer.writeheader()

	elif len(sys.argv) == 2:
		user = sys.argv[1]
		user_save = user + '.csv'
		if os.path.exists(user_save):

			print('Logging in...')

		else:

			while True:

				create = ''
				print("Profile not found!")
				create = input("Create new profile (Y/N)? ")
				create = create.lower()

				if create == 'y':

					print('Creating profile...')


					with open(user_save, 'w') as file:
						headers = game_list
						writer = csv.DictWriter(file, fieldnames=headers)

						writer.writeheader()

					break
					

				elif create == 'n':

					print("\nThanks for playing!\nGoodbye!")
					exit()

				else:

					print("Invalid entry")

					continue

	else:

		print("Error: Too many entries.")
		print("Only one profile can be loaded at a time.")
		print("Exiting...")
		exit()


	print("\nWelcome", user, "\n") 

	#read file and return as list


	return user_save













	'''
	user = input("Enter username: ")
	user_save = user + '.csv'
	if os.path.exists(user_save):

		print('Logging in...')
		#return dict of scores

	else:

		print('Creating profile...')
		#call scores?

		with open(user_save, 'w') as file:
			headers = game_list
			writer = csv.DictWriter(file, fieldnames=headers)

			writer.writeheader()



	print("\nWelcome", user, "\n") 

	#read file and return as list


	return user_save'''

	



def scores(user_save, game, score, plays):
	

	score_val = 0
	play_val = 0


	with open(user_save, 'r') as inhandle:
		df = pandas.read_csv(inhandle)
		print(type(df))
		game_dict = dict(df)
		print(type(game_dict))

		for key, val in game_dict():

			if game == key:

				if score > val:

					score_val = score


				else:
					pass

			else:
				pass #for now

	print(score_val)
	with open(user_save, 'w') as outhandle:
		game_dict.to_csv(outhandle)








	'''with open(user_save, 'r') as inhandle:
		reader = csv.DictReader(inhandle)
		game_dict = dict(reader)

		for key, val in game_dict.items():
			if game == key:

				if score > val:

					score_val = score

				else:

					pass

				#play_val = play_val + plays

	
	with open(user_save, 'w') as file:
			headers = game
			writer = csv.DictWriter(file, fieldnames=headers)
			writer.writeheader()
			for key,score_val in writer.items():
			
				writer.writerow([key, score_val])'''



def play_game(game):

	#hangman should be replaced with game for each iteration and then executed but how?
	
	game_exec = game + 'exec'


	launch_game	= getattr(installgames, game_exec)
	
	game_status, game_score, total_plays = launch_game()

	print(game_status, game_score, total_plays) #for testing

	return game_status, game_score, total_plays







def main():


	initial_list = installgames.gamelist()
	game_list = []

	for item in initial_list:
		item = item.lower()
		game_list.append(item)


	user_save = user_profile(initial_list)
	game_status = 'q'
	game_score = 0
	total_plays = 0

	
	


	while game_status == 'q':

		print("*** Main Menu ***")
		print("Type name of a game or 'exit' to quit the program.")
		

		g = 1
		for game_initial in initial_list:
			print("Game", g, ":", game_initial) #include high score variable here
			g = g + 1

		selection = input("Select: ").lower() #need a custom exception

		if selection != 'exit':

			
			for game in game_list:

				if  game == selection: 
					print("Loading", game, "...")

		
					print("High Score:", game_score, "/", "Total Games:", total_plays)

					
					game_status, game_score, total_plays = play_game(game)


					#total plays goes here, should always increment and add to total in file
					print("\nSaving...\n")

					#save to file here
					#scores(user_save, game_initial, game_score, total_plays)

				elif selection not in game_list:
					print("\nInvalid entry, please try again.\n")
					break
			

				else:

					pass
			

		else:

			

			print("\nThanks for playing!\nGoodbye!")
			exit()








if __name__ == '__main__':
	main()