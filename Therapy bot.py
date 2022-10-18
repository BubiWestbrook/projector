#Therapybot v4.0

answer = input("I dont like that most conversations seem to start with 'How'. How are you? How is school? How is work? We almost always give the same very old answers - 'Its okay' 'fine' 'We're managing' These are lies we tell ourselves, and others, cause though they ask, lets face it - they dont care enough to actually listen. In this quite underdeveloped environment, we'll talk. Scratch that - You'll talk. To your past self, your ideal self, and most importantly, to your true self. This is not real therapy. They're just open ended questions you could and should ask yourself. The code is not the real work, and finding these questions wasn't the hard part either. The hard part is yet to come. Are you willing to go on this journey into your You? (y/n)" ).lower()

if answer == "y":
	answer = input("You already know your name, but it'll help to type it out in full and just stare at it for now. Your full name: ")
	answer = input(answer + " - Ever wanted to change your name and start life at fresh? (y/n) ").lower()
	if answer == "y":
		reason = input("Why? ")
		reason = input("What's another reason why? ")
		reason = input("What's one other reason why? ")
		answer = input("What name would you have chosen instead? ")
		answer = input("What does it mean? ")
		answer = input("Why does it mean so much to you? ")
		answer = input("How old are you?")
		answer = input("Any siblings? (y/n)").lower()
		if answer == "y":
			number = input("How many are you? Remind yourself. ")
			answer = input("Ever wished you were an only child? (y/n) ")
			
			if answer == "y":
				answer = input("Why?")
				answer = input("Again  though, why?")
				print("Just two more questions and you're done. I promise.")
				answer = input("What if the concept of the multiverse is fact and not fiction. What if you could write a detailed description of the best version of yourself, burn it up, mix the 		ashes with 300ml of water, take the 'whoever you want to be' pill with the water solution and wake up the next day as you, but 'perfect'. What will you write down? Don't type it. Actually write it down.")
				answer = input("The creator of this program would like to say something --------- 'I believe in you. I've likely never met you and definitely don't know you well. But i believe in you, in your efforts, your endurance and your mental fortitude. I believe in you. But do you.... do you believe in you as much as I do?")
			elif answer == "n":	
				answer = print("Is it as fun having no siblings as some people say? (y/n) ")
				if answer == "y":
					answer = input("Why?")
					print("Just two more questions and you're done. I promise.")
					answer = input("What if the concept of the multiverse is fact and not fiction. What if you could write a detailed description of the best version of yourself, burn it up, mix the 		ashes with 300ml of water, take the 'whoever you want to be' pill with the water solution and wake up the next day as you, but 'perfect'. What will you write down? Don't type it. Actually write it down.")
					answer = input("The creator of this program would like to say something --------- 'I believe in you. I've likely never met you and definitely don't know you well. But i believe in you, in your efforts, your endurance and your mental fortitude. I believe in you. But do you.... do you believe in you as much as I do?")
			
				elif answer == "n":
					answer = input("Why not?")
					print("Just two more questions and you're done. I promise.")
					answer = input("What if the concept of the multiverse is fact and not fiction. What if you could write a detailed description of the best version of yourself, burn it up, mix the 		ashes with 300ml of water, take the 'whoever you want to be' pill with the water solution and wake up the next day as you, but 'perfect'. What will you write down? Don't type it. Actually write it down.")
					answer = input("The creator of this program would like to say something --------- 'I believe in you. I've likely never met you and definitely don't know you well. But i believe in you, in your efforts, your endurance and your mental fortitude. I believe in you. But do you.... do you believe in you as much as I do?")
				
				else:
					print("Answer is not valid. ")	
				
			
				
			else:
				print("Answer is not valid. ")	
		
		
	
	elif answer == "n":	
		reason = input("Why not? ")
		reason = input("What's another reason why not? ")
		reason = input("What's one other reason why not? ")
		answer = input("What does your name mean? ")
		answer = input("Why does it mean so much to you? ")
		answer = input("How old are you?")
		answer = input("Any siblings? (y/n)").lower()
		
		if answer == "y":
			number = input("How many are you? Remind yourself. ")
			answer = input("Ever wished you were an only child? (y/n) ")
			
			if answer == "y":
				answer = input("Why?")
				answer = input("Again  though, why?")
				print("Just two more questions and you're done. I promise.")
				answer = input("What if the concept of the multiverse is fact and not fiction. What if you could write a detailed description of the best version of yourself, burn it up, mix the 		ashes with 300ml of water, take the 'whoever you want to be' pill with the water solution and wake up the next day as you, but 'perfect'. What will you write down? Don't type it. Actually write it down.")
				answer = input("The creator of this program would like to say something --------- 'I believe in you. I've likely never met you and definitely don't know you well. But i believe in you, in your efforts, your endurance and your mental fortitude. I believe in you. But do you.... do you believe in you as much as I do?")
			elif answer == "n":	
				answer = print("Is it as fun having no siblings as some people say? (y/n) ")
				if answer == "y":
					answer = input("Why?")
					print("Just two more questions and you're done. I promise.")
					answer = input("What if the concept of the multiverse is fact and not fiction. What if you could write a detailed description of the best version of yourself, burn it up, mix the 		ashes with 300ml of water, take the 'whoever you want to be' pill with the water solution and wake up the next day as you, but 'perfect'. What will you write down? Don't type it. Actually write it down.")
					answer = input("The creator of this program would like to say something --------- 'I believe in you. I've likely never met you and definitely don't know you well. But i believe in you, in your efforts, your endurance and your mental fortitude. I believe in you. But do you.... do you believe in you as much as I do?")
			
				elif answer == "n":
					answer = input("Why not?")
					print("Just two more questions and you're done. I promise.")
					answer = input("What if the concept of the multiverse is fact and not fiction. What if you could write a detailed description of the best version of yourself, burn it up, mix the 		ashes with 300ml of water, take the 'whoever you want to be' pill with the water solution and wake up the next day as you, but 'perfect'. What will you write down? Don't type it. Actually write it down.")
					answer = input("The creator of this program would like to say something --------- 'I believe in you. I've likely never met you and definitely don't know you well. But i believe in you, in your efforts, your endurance and your mental fortitude. I believe in you. But do you.... do you believe in you as much as I do?")
				
				else:
					print("Answer is not valid. ")	
				
			
				
			else:
				print("Answer is not valid. ")	
		
		
		
		
	else:
		print("Answer is not valid. ")	
		
		
elif answer == "n":
		print("Not a good time to start? No worries, you could rerun this anytime you're ready : ) ")		
	
else:
		print("Answer is not valid. ")	
		
		
	
	





