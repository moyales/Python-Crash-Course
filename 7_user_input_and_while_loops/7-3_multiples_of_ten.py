#7.3: Multiples of 10
#Ask user for a number. Report if it's a multiple of 10 or not.

number = input("Give me a number, and I'll tell you if it's a multiple of 10 or not: ")
number = int(number)

if number % 10 == 0:
	print("\nThe number " + str(number) + " is a multiple of 10.")
else:
	print("\nThe number " + str(number) + " is not a multiple of 10.")
