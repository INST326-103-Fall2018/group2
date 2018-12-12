

import csv
import os.path
import hangman #need single file for all games "install.py"


#create or load profile
def user_profile():
	points = []

	user = input("Enter username: ")
	user_save = user + '.csv'
	if os.path.exists(user_save):

		print('Logging in...')
		#return dict of scores

	else:

		print('Creating savefile')
		#call scores?

		with open(user_save, 'w') as file:
			file.write('')


	print("\nWelcome", user, "\n") 

	#read file and return as list


	return user_save
	



def scores(user_save, game, score):
	
	with open(user_save, 'r') as inhandle:
		reader = csv.DictReader(inhandle)

		for key, value in reader:
			if game in reader:

				#if game exists in file, compare scores and write better score

				print("code goes here")

			else:

				#should write to file as new row if game not in savefile
				#I'm stuck here
				reader[game] = score

			for row in reader:
				data.append(row)

	




def main():


	high_scores = user_profile()
	game_status = 'q'

	game_list = ['hangman', 'game2', 'game3'] #hardcoded, should be populated from outside list


	while game_status == 'q':

		print("*** Main Menu ***")
		print("Type name of a game or 'exit' to quit the program.")
		#list of games goes here

		g = 1
		for game in game_list:
			print("Game", g, ":", game)
			g = g + 1

		selection = input("Select: ") #need a custom exception

		if selection != 'exit':

			
			for game in game_list:

				if  game == selection:
					print("Loading", game, "...")

					#hangman should be replaced with game for each iteration and then executed but how?
					game_status, game_score = hangman.main()
					
					print("\nSaving...\n")

					#save to file here
					scores(high_scores, game, game_score)

				elif selection not in game_list:
					print("\nInvalid entry, please try again.\n")
					break
			

				else:
					pass
			

		else:

			

			print("Thanks for playing!\nGoodbye!")
			exit()








if __name__ == '__main__':
	main()
