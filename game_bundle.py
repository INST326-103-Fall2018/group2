#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Name: Chris Davis
#Assignment: Final Project



import sys
import os.path
import installgames
from installgames import *



#create or load profile
def user_profile(game_list):

	profile = ['', '0', '0']
	

	if len(sys.argv) < 2:


		print("Welcome new user!")
		user = input("Enter username: ")
		user_save = user + '.txt'

		print('Creating profile...')


		with open(user_save, 'w') as file:

			for game in game_list:

				profile = [game, '0', '0']
				profile = ['{0} '.format(i) for i in profile]
				

				for item in profile:

					file.write(item)

				file.write('\n')



	elif len(sys.argv) == 2:
		user = sys.argv[1]
		user_save = user + '.txt'
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

						for game in game_list:

							profile = [game, '0', '0']
							profile = ['{0} '.format(i) for i in profile]


							for item in profile:

								file.write(item)

							file.write('\n')

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

	#read file and return current scores


	return user_save
user_profile.__doc__ == """Loads or creates a profile for current user"""	




def scores(user_save, game_list, game_name, score, plays):
	
	profile = []

	high_score = 0
	total_plays = 0


	with open(user_save, 'r') as inhandle:
		

		profile = [row.strip('\n').split(' ') for row in inhandle] #maybe commas


	for row in profile:


		if row[0] == game_name:

			high_score = int(row[1])
			total_plays = int(row[2])



	if score > high_score:

		high_score = score

	total_plays = total_plays + plays



	#convert back and forth bw string and int


	for row in profile:
		if row[0] == game_name:
			high_score == str(high_score)
			total_plays == str(total_plays) #string(int(plays))


			with open(user_save, 'w') as outhandle:

				for game in game_list:

					if game == game_name:

						profile = [game_name, high_score, total_plays, '\n']
						profile = ['{0} '.format(i) for i in profile]

						for item in profile:

							outhandle.write(item)

						outhandle.write('\n')

					else:

						pass





		
scores.__doc__ == """Updates user scores in profile .csv file"""



def play_game(game):
	
	game_exec = game + 'exec'


	launch_game	= getattr(installgames, game_exec)
	game_status, game_score, total_plays = launch_game()



	return game_status, game_score, total_plays
play_game.__doc__ == """Dynamically loads game module based on user input"""




def main():



	initial_list = installgames.gamelist()
	game_list = []

	for item in initial_list:
		item = item.lower()
		game_list.append(item)



	user_save = user_profile(game_list)
	game_status = 'q'
	game_score = 0
	total_plays = 0



	while game_status == 'q':

		print("*** Main Menu ***")
		print("Type name of a game or 'exit' to quit the program.")
		


		g = 1
		for game_initial in initial_list:
			print("Game", g, ":", game_initial) #include high score variable
			g = g + 1



		selection = input("Select: ").lower() 

		if selection != 'exit':

			for game in game_list:

				if  game == selection: 
					print("Loading", game, "...")


					print("High Score:", game_score, "/", "Total Games:", 
						total_plays)

					
					game_status, game_score, total_plays = play_game(game)


					
					print("\nSaving...\n")

					#save to file here
					scores(user_save, game_list, game, game_score, total_plays)



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

	#figure out some tests