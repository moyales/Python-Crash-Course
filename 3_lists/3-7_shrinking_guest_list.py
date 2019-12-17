guest_list = ["Lucas", "Celena", "Raquel"]
print("Hey " + guest_list[0] + ", " + guest_list[1] + ", and " + guest_list[2] + ", I found a bigger dinner table.")

#Insert the names of three other people to add to the list.
guest_list.insert(0, "Ava")

guest_list.insert(2, "Evan")

guest_list.append("Shannon")

print("Hey everyone, the new dinner table won't arrive on time. Sorry.")

pop_1 = guest_list.pop()
print("I'm sorry " + pop_1 + ", I can't invite you to the dinner party.")

pop_2 = guest_list.pop()
print("I'm sorry " + pop_2 + ", I can't invite you to the dinner party.")

pop_3 = guest_list.pop()
print("I'm sorry " + pop_3 + ", I can't invite you to the dinner party.")

pop_4 = guest_list.pop()
print("I'm sorry " + pop_4 + ", I can't invite you to the dinner party.")

print("Hey " + guest_list[0] + ", you're still invited to the dinner party.")
print("Hey " + guest_list[1] + ", you're still invited to the dinner party.")

print(guest_list)

del guest_list[0]
del guest_list[0]

print(guest_list)
