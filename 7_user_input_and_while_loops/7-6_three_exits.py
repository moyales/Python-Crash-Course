#7.6: Three Exits
#Modify code from 7.4 or 7.5 to use a different kind of exit.

prompt = "\nEnter your desired toppings and we will add them to your pizza!"
prompt += "\n(Enter 'quit' when you are done adding toppings.)"
prompt += "\nInput topping: "

active = True
while active:
	topping = input(prompt)
	
	if topping == 'quit':
		active = False
	else:	
		print("We will add " + topping + " to your pizza!")
