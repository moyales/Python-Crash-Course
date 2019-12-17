#7.10: Dream Vacation
#Write an interactive poll about 
responses = {}

polling_active = True

while polling_active:
	name = input("\nInput your name: ")
	prompt = "If you were to visit one place in the world, where would you go?"
	prompt += "\nInput your answer here: "
	response = input(prompt)
	
	responses[name] = response
	
	repeat = input("Ask another person? (y/n): ")
	if repeat == 'n':
		polling_active = False

print("\n -- Poll Results --")
for name, response in responses.items():
	print("Name: " + name.title())
	print("Dream Vacation: " + response.title() + "\n")
