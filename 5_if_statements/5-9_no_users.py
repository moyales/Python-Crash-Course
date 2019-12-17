#Exercise 5.9: No User
#Add an if test to 5.8 to make sure list is not empty.
usernames = []
if usernames:
	for user in usernames:
		print("Thanks for logging in " + user)
else:
	print("We need more users here!")
