#Exercise 4.11: My Pizzas, Your Pizzas
#Make a copy of the list from 4.1 and add different items to each seperate list.
pizzas = ["mushroom", "pepperoni", "meat-lovers"]
friends_pizzas = pizzas[:]

pizzas.append("white")
friends_pizzas.append("hawaiian")

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
	
print("\nMy friend's favorite pizzas are:")
for friend_pizza in friends_pizzas:
	print(friend_pizza)
