#7.2: Restaurant Seating
#Ask how many people are in the group; check if group is > 8.

group = input("How many people are in your dinner group? ")
group = int(group) #Input becomes an integer, not a string.

if group > 8:
	print("\nYou will have to wait for a table.")
else:
	print("\nWe can seat you right away.")


