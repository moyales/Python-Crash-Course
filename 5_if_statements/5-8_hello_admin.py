#Exercise 5.8: Hello Admin
#Make a list of usernames and admin, making a custom greeting for admin
usernames = ["snivysaurus", "lol_69", "seiko", "renard", "admin"]
for user in usernames:
	if user == "admin":
		print("Hello admin, would you like to see a status report?")
	else:
		print("Hello " + user + ", thanks for logging in.")

