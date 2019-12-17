#Making use of the 'input' function
#Using a while loop to let the user stay as long as they want

prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "
prompt += "\nEnter your word here: "

message = ""
while message != 'quit':
	message = input(prompt)
	
	if message != 'quit':
		print("\n" + message)
