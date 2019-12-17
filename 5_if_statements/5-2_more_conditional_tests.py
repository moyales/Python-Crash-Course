#Exercise 5.2: More Conditional Tests

#Testing for equality and inequality with strings
city = "new york"
print("My campus is near New York:")
print(city == "new york")

print("\nMy campus is near Los Angeles:")
print(city == "los angeles")

#Using the lower function
phone = "Apple"
print("\n" + phone)
print("Using the lower function:")
print(phone.lower() == "apple")

print("\nNumerical Tests:")
#Numerical tests
score = 92
print("Your score was 8 points shy of perfect")
print(score < 100)

print("\nYour score was greater than or equal to an A-")
print(score <= 92)

print("\nYour score is an A+")
print(score > 98)

print("\nYour score is 98 or greater:")
print(score >= 98)

print("\nAnd & Or keywords")
#And & Or keywords
answer_0 = 31
answer_1 = 42
print((answer_0 >= 36) and (answer_1 >= 36))
print((answer_0 >= 36) or (answer_1 >= 36))

print("\nTesting items in a list")
#Testing if an item is or isn't in a list
guest_list = ["Evan", "Mohammed", "Lucas"]
other_person = "steven"
if "Evan" in guest_list:
	print(guest_list[0] + ", you are invited.")

if other_person not in guest_list:
	print(other_person.title() + ", you are not invited.")
