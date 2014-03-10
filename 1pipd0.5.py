from sys import exit
from getpass import getpass #invisible input module
from random import randint


print """How many turns do you want to play? Or [R]andom""" 

turns = raw_input("> ") 
print turns

#generate random number between 2-10, otherwise make input an int so 
#it fits in range module and add 1 due to zero indexing 
#Bugs out, for some reason always does if portion even if inputs are not 'r'
if turns == 'r' or 'R':
	turns = randint(2, 10) 
	print turns
else:
	turns = int(turns) +1	
	print turns
print turns

print """You go to meet a partner of your drug ring. At the usual place. The 
weather man had predicted partly cloudy with a full moon, but you got another 
flash flood. They strike with unpredictable regularity. You show up, share a 
cig, and then it happens. They bust in. With the dogs. Throw you in the back of
car and start grilling you. 
""" 
#global var
player1 = 0 
player2 = 0

player1_score = 0
player2_score = 0  
#to do: incorrect input function

class CompStrat(object):
	
	
	#Paramaters are the move strategy takes if previous move the player 
	#cooperates or defects
	def __init__(self, cooperation, defection):
		self.iplayerscore = 0
	
	def npcengine(iplayerscore):
		if iplayerscore == 1 or 0: 
			return cooperation
		if iplayerscore == 3 or 5:
			return defection	
		

 
	
		
 
def query (previous_score):
	
	#Player one possible inputs c for cooperation d for defection 
	global player1
	global player2
	

	
	player1 = getpass("""Player One: c for not talking to the cops, d for 
	snitchin\' \n""") 
 	
	tit_for_tat = CompStrat(1, 2)
	
	tit_for_tat.iplayerscore = previous_score 
	
	player2 = tit_for_tat.npcengine


#game engine, compares player inputs and assigns score
def engine (play1, play2): 
	if play1 == 'c' and play2 == 1:
		print """Your drug ring lives by the rule of "don\'t be snitchin\'" and 
without any witness testimonial the most either of you will get is one 
year."""
		return 1, 1
	elif play1 == 'c' and play2 == 2: 
		print """Player 2 is a dirty rat and snitches. He gets off scott-free 
		and	player 1 goes to jail for 5 years.""" 
		return 5, 0
	elif play1 == 'd' and play2 == 1: 
		print """Player 1 is a dirty rat and snitches. He gets off scott-free 
		and	1 player 2 goes to jail for 5 years."""
		return 0, 5
	elif play1 == 'd' and play2 == 2:
		print """Both players are selfish bastards and have no sense 
		camaraderie. Both go to jail for 3 years"""
		return 3, 3 
	else:
		print """Incorrect input. Player 1 c for cooperating with other player d
		for defecting. Player two 1 is for cooperating 2 is for defecting.""" 
		#query()
		#engine(player1, player2) 


#iterated prisoners dilemma loop. Add some plot so it makes sense in 
#iterated story line

for turn_count in range(1, turns):
	
	#set up turn 0 so tit_for_tat can make first turn decision
	if turn_count == 1:
		iplayer2_score = 1 
	
	print "Player1 Jailtime:", player1_score, "years\n"
	print "Player2 Jailtime:", player2_score, "years\n"
	print "Round:", turn_count, "\n" 
	query(iplayer2_score)
		
	iplayer1_score, iplayer2_score = engine(player1, player2)
	
	player1_score += iplayer1_score
	player2_score += iplayer2_score
	
	print "\n" 
