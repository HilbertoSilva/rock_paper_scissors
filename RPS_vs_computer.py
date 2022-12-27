#This will be a code that will allow the user to play Rock, Paper, Scissors against the computer.

print ("Let's play Rock, Paper or Scissors!")  #initial statement

import random #imports random module for the computer plays

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
	print ("It's a tie!")
elif p1 == "R" and pc == "P": #Paper beats Rock
	print ("Computer wins!")
elif p1 == "R" and pc == "S":  #Rock beats Scissors
	print ("Player wins!")	
elif p1 == "P" and pc == "R":   
	print ("Player wins!")
elif p1 == "P" and pc == "S":
	print ("Computer wins!")
elif p1 == "S" and pc == "R":
	print ("Computer wins!")
elif p1 == "S" and pc == "P": #Scissors beat Paper
	print ("Player wins!")	
else: 
	print ("Upps... Something is wrong.")	#Error message.

