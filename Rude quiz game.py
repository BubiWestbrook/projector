

print("Welcome to Trash Talking Quiz")

playing = input("Do you want to play? Type 'YES' to start losing :) ")

if playing.lower() != "yes":
	quit()
	
print("I knew you'd want to play. But can you win? ")
score = 0

#1
answer = input("The North Pole receives 24 hours of sunlight when the sun is overhead on the ")
if answer.lower() == "antarctic circle":
	print("You try ")
	score += 1		
else:
	print("YOU SHAA o! ")

#2		
answer = input("The railway line from Dunkwa to Accra was built by the British mainly to transport what? ")
if answer.lower() == "bauxite":
	print("You try ")
	score += 1		
else:
	print("Who was Lexis in 'Faith'' anka you you go answer sharp ")
	
#3	
answer = input("Akans are said to have migrated from? ")
if answer.lower() == "old ghana empire":
	print("You try ")
	score += 1		
else:
	print("Hmm.. where ereach dierr, unless God")

#4		
answer = input("On which date is the sun vertically overhead on the Tropic of Cancer? ")
if answer.lower() == "21st june":
	print("You try ")
	score += 1		
else:
	print("You registered? Remedial no be sin..")

#5
answer = input("Entrepreneurs in need of larger capital capital can come together to form a")
if answer.lower() == "partnership":
	print("You try ")
	score += 1		
else:
	print("lol : | ")

#6		
answer = input("Which ocean lies between Africa and America? ")
if answer.lower() == "atlantic ocean":
	print("You try ")
	score += 1		
else:
	print("Eeyi Frank Ocean")

#7		
answer = input("The risk bearing of a business organization falls on the..")
if answer.lower() == "entrepreneurs":
	print("You try ")
	score += 1		
else:
	print("Ego come.")

#8		
answer = input("What is the full name of DOVVSU?")
if answer.lower() == "domestic violence and victim support unit":
	print("You try ")
	score += 1		
else:
	print("Hmm.. God.")

#9		
answer = input("Which regional capital can Lake Bososmtwi be found?")
if answer.lower() == "kumasi":
	print("You try ")
	score += 1		
else:
	print("Qwer! Kneel down.")

#10		
answer = input("Which regional capital can Volta Estuary be found?")
if answer.lower() == "accra":
	print("You try ")
	score += 1		
else:
	print("Make I open shop give you?")

#11		
answer = input("Which regional capital can Mole National Park be found?")
if answer.lower() == "tamale":
	print("You try ")
	score += 1		
else:
	print("No be your fault, I blame your Fada!")

#12		
answer = input("Which regional capital can Ussher Fort be found?")
if answer.lower() == "accra":
	print("You try ")
	score += 1		
else:
	print("But you know Justin Bieber ein house number, see your life? ")

#13		
answer = input("A bill passed by President becomes law when the president gives his? ")
if answer.lower() == "assent":
	print("You try ")
	score += 1		
else:
	print("Dancing in the rain, with you between my arms, barefoot on the grass, listening to your BOMBING!")

#14		
answer = input("The applications of checks and balances in Democratic governments helps to prevent what? ")
if answer.lower() == "dictatorship":
	print("You try ")
	score += 1		
else:
	print("Beans.")
	
					
print("You got " + str(score) + ("questions correct. "))
print("You got " + str((score  / 14) * 100) + "%")																															