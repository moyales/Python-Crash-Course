#Filling a dictionary with user input

responses = {}

#Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
	#Prompt for person's name and response
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb one day? ")
	
	#Store the response in a dictionary
	responses[name] = response
	
	#Find out if anybody else will take the poll.
	repeat = input("Would you like to let another person respond? (y/n) ")
	if repeat == 'n':
		polling_active = False

#Polling is done, display the results
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(name.title() + " would like to climb " + response.title() + ".")
