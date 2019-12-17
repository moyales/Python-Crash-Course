#Exercise 3.5: Use the list from the last program in order to make a statement that says the last person cannot make it.
guest_list = ["Lucas", "Celena", "Raquel"]
unavailable = guest_list.pop()
print(unavailable + " " + "cannot make it to the dinner party.")

guest_list.append('Shannon')
print(guest_list)
print("You are invited to a dinner party, ", guest_list[0], ".")
print("You are invited to a dinner party, ", guest_list[1], ".")
print("You are invited to a dinner party, ", guest_list[2], ".")
