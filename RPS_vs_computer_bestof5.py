#This will be a code that will allow the user to play Rock, Paper, Scissors against the computer.

print ("Let's play Rock, Paper or Scissors!")  #initial statement

import random #imports random module for the computer plays

player_wins = 0
computer_wins = 0

while player_wins !=3 and computer_wins !=3:
	p1 = input("Player, select your move (R for rock, P for paper or S for scissors): ")  #input from Player (it accepts R, P or S)


	r1 = random.randint(1,3) # Generates a random number between 1 and 3 (inclusive)
	pc = 0
	if r1 == 1:
		pc = "R"
	elif r1 == 2:
		pc = "P"
	else:
		pc = "S"		 

	print (f"Computer plays {pc}")

	if p1 == pc: #the tie-case
		print (f"It's a tie! {player_wins} - {computer_wins}")
	elif p1 == "R" and pc == "P": #Paper beats Rock
		computer_wins +=1
		print (f"Computer wins! {player_wins} - {computer_wins}")
	elif p1 == "R" and pc == "S":  #Rock beats Scissors
		player_wins += 1
		print (f"Player wins! {player_wins} - {computer_wins}")	
	elif p1 == "P" and pc == "R":  
		player_wins += 1 
		print (f"Player wins! {player_wins} - {computer_wins}")
	elif p1 == "P" and pc == "S":
		computer_wins += 1
		print (f"Computer wins! {player_wins} - {computer_wins}")
	elif p1 == "S" and pc == "R":
		computer_wins += 1
		print (f"Computer wins! {player_wins} - {computer_wins}")
	elif p1 == "S" and pc == "P": #Scissors beat Paper
		player_wins += 1
		print (f"Player wins! {player_wins} - {computer_wins}")	
	else: 
		print ("Upps... Something is wrong.")	#Error message.

if player_wins > computer_wins:
	print ("Congratulations! You just beat my poor AI.")
else: 
	print ("PC Master Race!")			

