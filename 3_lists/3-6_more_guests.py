#Exercise 3.6: More space has been added to the guest list.
guest_list = ["Lucas", "Celena", "Raquel"]
print("Hey " + guest_list[0] + ", " + guest_list[1] + ", and " + guest_list[2] + ", I found a bigger dinner table.")

#Insert the names of three other people to add to the list.
guest_list.insert(0, "Ava")
print("\n")
print(guest_list)

guest_list.insert(2, "Evan")
print(guest_list)

guest_list.append("Shannon")
print(guest_list)

print("\nYou are invited to a dinner party, ", guest_list[0], ".")
print("You are invited to a dinner party, ", guest_list[1], ".")
print("You are invited to a dinner party, ", guest_list[2], ".")
print("You are invited to a dinner party, ", guest_list[3], ".")
print("You are invited to a dinner party, ", guest_list[4], ".")
print("You are invited to a dinner party, ", guest_list[5], ".")
