from sys import exit
from getpass import getpass #invisible input module

#Single round human playable prisoner's dilemma
print """You go to meet a partner of your drug ring. At the usual place. The 
weather man had predicted partly cloudy with a full moon, but you got another 
flash flood. They strike with unpredictable regularity. You show up, share a 
cig, and then it happens. They bust in. With the dogs. Throw you in the back of
car and start grilling you. 
""" 

#global variables
player1 = 0
player2 = 0  
turn_count = 0
def query():
	#Player one possible inputs c for cooperation d for defection 
	player1 = getpass("""Player One: c for not talking to the cops, d for 
	snitchin\' \n""") 

	#Player two possible inputs 1 for cooperation d for defection
	player2 = int(getpass("""Player Two: 1 for not talking to the cops, 2 for 
	snitchin\' \n"""))
	
	print player1
	print player2
	
	engine(player1, player2)

#game engine, compares player inputs and assigns score
def engine (play1, play2): 
	if play1 == 'c' and play2 == 1:
		print """Your drug ring lives by the rule of "don\'t be snitchin\'" and 
		without any witness testimonial the most either of you will get is one 
		year. \n"""
	elif play1 == 'c' and play2 == 2: 
		print """Player 2 is a dirty rat and snitches. He gets off scott-free 
		and	player 1 goes to jail for 5 years. \n"""
	elif play1 == 'd' and play2 == 1: 
		print """Player 1 is a dirty rat and snitches. He gets off scott-free 
		and	player 2 goes to jail for 5 years.\n"""
	elif play1 == 'd' and play2 == 2:
		print """Both players are selfish bastards and have no sense 
		camaraderie. Both go to jail for 3 years.\n""" 
	else:
		print """Incorrect input. Player 1 c for cooperating with other player d
		for defecting. Player two 1 is for cooperating 2 is for defecting.\n""" 
		
		
query()	

print player1
print player2
	
		
engine(player1, player2) 