#Using remove to take out all instances of a value
pets = ['dog', 'cat', 'dog', 'parrot', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')
	
print(pets)
