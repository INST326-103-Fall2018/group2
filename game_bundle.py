

import csv
import os.path
import installgames
from installgames import *




#create or load profile
def user_profile(game_list):
	points = []

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


	return user_save
	



def scores(user_save, game, score, plays):
	
	with open(user_save, 'r') as inhandle:
		reader = csv.DictReader(inhandle)

		for key, value in reader:
			if game in reader:


				reader[game] = [score, plays]

				

			else:

				#should write to file as new row if game not in savefile
				#I'm stuck here
				reader[game] = score, plays

			for row in reader:
				data.append(row)

	




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
		for game in initial_list:
			print("Game", g, ":", game) #include high score variable here
			g = g + 1

		selection = input("Select: ").lower() #need a custom exception

		if selection != 'exit':

			
			for game in game_list:

				if  game == selection: 
					print("Loading", game, "...")

					#this should be changed to the high score and total games from file
					print("High Score:", game_score, "/", "Total Games:", total_plays)

					#hangman should be replaced with game for each iteration and then executed but how?
					game_status, game_score, total_plays = installgames.hangmanexec()
					#print(game_status, game_score, total_plays) #for testing



					#total plays goes here, should always increment and add to total in file
					print("\nSaving...\n")

					#save to file here
					#scores(user_save, game, game_score, total_plays)

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