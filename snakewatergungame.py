# importing random module for game 
import random
# initialize the value
computer = 0
user = 0

# giving simple information for user
print("This is a snake, water and gun game \n")
print ("PRESS 1 FOR STONE, 2 FOR PAPER AND 3 FOR SCISSOR \n")

# using a simple while loop for giving 10 chances to the user

i = 1
while (i<=10):
	# taking user input 1,2,3 for S, W, G respectively 
	user_input_for_game = int(input("Enter 1,2,3............ 	"))

	# using the random function
	random_choice = random. randint(1,3)
	print(f"\nMy choice was {random_choice} \n")

	''' giving conditions to equate @random_choice and 	@
	user_input_for_game'''

	if (user_input_for_game == 1 and random_choice == 	3):
		user = user + 1
		print("		You won this chance")

	elif (user_input_for_game == 1 and random_choice 	== 2):
		computer = computer + 1
		print("		Computer won this chance!! ")

	elif (user_input_for_game ==  2 and random_choice 	== 1):
		user = user + 1
		print("		You won this  chances")

	elif (user_input_for_game ==  2 and random_choice 	== 3):
		computer = computer + 1
		print("		Computer won this chance!! ")

	elif (user_input_for_game ==  3 and random_choice 	== 2):
		user = user + 1
		print("		you won this chance!!")

	elif (user_input_for_game ==  3 and random_choice 	== 1):
		computer = computer + 1
		print("		Computer won this chance!!")
	
	elif (user_input_for_game == random_choice):
		print("		This chance is drawn")

	else:
		print ("		 give the correct input ")
	i +=1

if (computer < user):
	print(f"\n\n\n You won the game with {user} points")
elif(computer > user):
	print(f"\n\n\n Computer won the game with {computer} points")
elif(computer == user):
	print("The game is drawn")
else:
	print ('error')