print ("Let's play Rock, Paper or Scissors!")  #initial statement

player_one = input("Player 1, select your move (R for rock, P for paper or S for scissors): ")  #input from player 1 (it accepts R, P or S)

print("No cheating!\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNo cheating!")  #adds several lines to prevent player 2 from seeing the input from player 1

player_two = input("Player 2, select your move (R for rock, P for paper or S for scissors): ")   #input from player 2

if player_one == player_two: #the tie-case
	print ("It's a tie!")
elif player_one == "R" and player_two == "P": #Paper beats Rock
	print ("Player 2 wins!")
elif player_one == "R" and player_two == "S":  #Rock beats Scissors
	print ("Player 1 wins!")	
elif player_one == "P" and player_two == "R":   
	print ("Player 1 wins!")
elif player_one == "P" and player_two == "S":
	print ("Player 2 wins!")
elif player_one == "S" and player_two == "R":
	print ("Player 2 wins!")
elif player_one == "S" and player_two == "P": #Scissors beat Paper
	print ("Player 1 wins!")	
else: 
	print ("Upps... Something is wrong.")	#Error message.
