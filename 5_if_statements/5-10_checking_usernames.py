#5.10: Checking Usernames
#Create a program that simulates checking for unique usernames.

current_users = ["snivysaurus", "seiko", "badstrider", "bob", "renard"]
new_users = ["RENARD", "billy", "snivysaUrus", "drako", "42069"]

print(current_users)
print(new_users)
print("\n")

for users in new_users:
	print(users)
	if users.lower() in current_users:
		print("Sorry, that username is already taken.\n")
	else:
		print("That username is available!\n")
