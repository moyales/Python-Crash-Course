#7.5: Movie Tickets
#Write a loop that asks for age and tell them the cost of their ticket.

prompt = "\nEnter your age to determine the price of your movie ticket."
prompt += "\n(Input 'quit' when you are done.)"
prompt += "\nAge: "

age = ""
while True:
	age = input(prompt)
	
	if age == 'quit':
		break
	else:
		age = int(age)
	
		if age < 3:
			print("Your ticket is free.")
		if age > 3 and age <= 12:
			print("Your ticket is $10.")
		if age > 12 and age <= 100:
			print("Your ticket is $15.")
		if age > 100:
			print("You're probably lying.")
	

	
	
