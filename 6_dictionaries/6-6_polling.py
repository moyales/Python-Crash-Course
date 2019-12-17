#6.6: Polling
favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'pyhton',
	}

poll_people = ['jen', 'matt', 'phil', 'james', 'paul']

for people in poll_people:
	if people in favorite_languages.keys():
		print("Thank you " + people.title() + 
		" for taking my poll!")
	else:
		print(people.title() + " please take our poll!")

