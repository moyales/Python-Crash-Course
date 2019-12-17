#7.4: Pizza Toppings
#Loop that propmpts user to enter a series of pizza toppings
#Until they say 'quit'

prompt = "\nEnter your desired toppings and we will add them to your pizza!"
prompt += "\n(Enter 'quit' when you are done adding toppings.)"
prompt += "\nInput topping: "

topping = ""
while topping != 'quit':
	topping = input(prompt)
	
	if topping != 'quit':
		print("We will add " + topping + " to your pizza!")
