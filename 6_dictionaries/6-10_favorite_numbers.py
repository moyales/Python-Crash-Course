#6.10: Favorite Numbers
#Modify 6.2 program so each person has more than one fav. number

favorite_numbers = {
	"josh" : [31, 12, 49],
	"lucas" : [38, 2, 69, 193],
	"avogadro" : [6.022],
	"matt" : [7, 26]
	}

for name, numbers in favorite_numbers.items():
	if len(numbers) > 1:
		print(name.title() + "'s favorite numbers are:")
		for number in numbers:
			print(str(number))
	else:
		print(name.title() + "'s favorite number is:")
		for number in numbers:
			print(str(number))
	print("\n")
