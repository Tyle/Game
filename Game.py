#!r/local/bin/python
from sys import exit

def gold_room(): 
	print "This room is full of gold. How much do you take?"
	
	next = raw_input("> ")	
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type a number. This was your down fall. You died.")
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("Your DEAD! You greedy bastard!")
		
def	 lock_room():
	print "You have enterd a room with a lot of doors."
	print "There are several doors. Behind you, you can hear the tiger eating meat, then scratching the door."
	print "To your right you hear the kids. So that leaves the doors to you left or front."
	door_locked = True
	
	while True:
	
		next = raw_input("> ")
	
		if next == "right":
			kids_room()
		elif next == "behind":
			tiger_room()
		elif next == "front":
			snake_room()
		elif next == "left" and door_locked:
			print "DOOR LOCKED"
			door_locked = False
		elif next == "open door" and not door_locked:
				gold_room()
		elif next == "key" and not door_locked:
			print "door unlocked"
			door_locked = False
		else:
			print "Walls closing. Hurry up!!!!!"

def snake_room():
	print "you have entered the snake pit."
	print "They start winding their way around your body."
	print "What are you going to do? There is a lever across the room or you can freak out."
	snakes = True
	lever = False
	
	while True:
	
		next = raw_input("> ")
		
		if next == "freak out":
			dead("YOU DIE BECAUSE YOU FREAKED OUT IN SNAKE PEN!! THEY BIT YOU!") 
		elif next == "walk to lever":
			print "You are now infornt of the lever."
			lever = True
		elif next == "pull lever" and not lever:
			print "You are not by th lever."
		elif next == "pull lever" and lever:
			print "The snakes leave the room. Now choose a door. front, behind, left and right."
			snakes = False
		elif next == "right"and not snakes:
			lock_room()
		elif next == "behind" and not snakes:
			kids_room()
		elif next == "front" and not snakes:
			tiger_room()
		elif next == "left" and not snakes:
			wet_room()
		else:
			print "WHAT?? SNAKE."
			
			
def wet_room():
	print "You go in to a room and water starts flowiwng out of the corners."
	print "What do you want to do? Just then a voice says Tell me the color."
	print "whats the color he thinking of."
	sharks = False
	piranhas = False
	water = True
	
	while True:

		next = raw_input("> ")
		
		if next == "purple":
			print "water backs off. Choose the room you want to go in. right, left, front, behind."
			water = False
		elif next == "black":
			print "Now you have piranhas."
			piranhas = True
		elif next == "red":
			print "Now you have piranhas."
			piranhas = True
		elif next == "blue":
			sharks = True
			print "Now you have sharks."
		elif next == "green": 
			sharks = True
			print "Now you have sharks."
		elif next == "yellow": 
			print "Now you have piranhas"
			piranhas = True
		elif next == "pink":
			print "Now you have piranhas"
			piranhas = True
		elif next == "brown": 
			print "Now you have piranhas"
			piranhas = True 
		elif next == "white":
			sharks = True
			print "Now you have sharks."
			
		next = raw_input("> ")
		
		if next == "black" and piranhas:
			print "piranhas where sent a way. But the water still there"
			piranhas = False
		elif next == "red" and piranhas:
			dead("That got the piranhas all hungery. You where consumed.")
		elif next == "blue" and piranhas:
			dead("You drown.")
		elif next == "green" and piranhas: 
			dead("You where consumed.")
		elif next == "yellow" and piranhas: 
			dead("DEATH.")
		elif next == "pink" and piranhas:
			dead("THEY ATE INTO YOUR HEART") 
		elif next == "brown"and piranhas: 
			dead("NOM NOM NOM. YOU WERE EATEN.")
		elif next == "white" and piranhas:
			dead("EATEN ALIVE!!")
		elif next == "purple" and piranhas:
			dead("That got the piranhas all hungery. You where consumed.")

				
		if next == "right" and not water:
			gold_room()
		elif next == "behind" and not water:
			lock_room()
		elif next == "front" and not water:
			kids_room()
		elif next == "left" and not water:
			tiger_room()


		if next == "black" and sharks:
			dead("EATEN ALIVE!!!")
		elif next == "red" and sharks:
			dead("NOM NOM NOM. YOU WERE EATEN!")
		elif next == "blue" and sharks:
			dead("That got the Sharks all hungery. You where consumed.")
		elif next == "green" and sharks:
			kids_room()
		elif next == "yellow" and sharks: 
			dead("YOU PEE YOURSELF AND THE SHARKS ATE YOU!")
		elif next == "pink" and sharks:
			dead("DEATH IN A FEEDING FREEZY.")
		elif next == "brown" and sharks: 
			dead("NOM NOM NOM YOU TAST GOOD. SHARKS ARE NOW FULL.")
		elif next == "white" and sharks:
			dead("ONE SHARK TASTED YOUR BODY. THEN SPIT YOU OUT. BUT YOU BLED TO DEATH")
		elif next == "purple" and sharks:
			print "Sharks where sent a way. What the color?"
			sharks = False


		
def tiger_room():
	print "There is a Tiger here."
	print "The is very hungery."
	print "The tiger is stretched infornt of you exit."
	print "How are you going to move the Tiger poke?"
	tiger_moved = False
	
	while True:
		next = raw_input("> ")
		
		if next == "poke":
			dead("The tiger growls at you then racks his claws on you body. Then eats your corpse. Should have given him the fresh meat you had or just opened the door.")
		elif next == "give fresh meat" and not tiger_moved:
			print "The tiger has moved from the door. You can go through it now."
			tiger_moved = True
		elif next == "give fresh meat" and tiger_moved:
			dead("The tiger gets pissed off and attacks you.")
		elif next == "open door" and tiger_moved:
			lock_room()
		else:
			print "I got no idea what that means."
			
def kids_room():
	print "Here you see the great evil clinging, smelly, ball throwing, crying Childern."
	print "They stare at you and you start go insane, also getting a major headache."
	print "Then they turned you and they eyes are red. They lick their lips the charge you"
	print "What do you do? Eat your own head?"
	
	next = raw_input("> ")
	
	if "give candy" in next:
		tiger_room()
	elif "eat head" in next:
		dead("Well that was tasty! Could have given them candy.")
	else:
		dead("You were eaten by the kids.")
		
def dead(why):
	print why, "Good job!"
	exit(0)
	
def start():
	print "You are in a dark room."
	print "There is a door your right, left and in front and behind you."
	print "you have fresh meat, candy, key, and the power to open doors."
	print "Which door? do you take?"
	
	next = raw_input("> ")
	
	if next == "left":
		tiger_room()
	elif next == "front":
		snake_room()
	elif next == "right":
		kids_room()
	elif next == "behind":
		wet_room()
	else:
		dead("You stumble around the room until you starve.")
		
start()