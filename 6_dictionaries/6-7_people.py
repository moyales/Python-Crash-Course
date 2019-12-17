#6.7: People
#Use program from 6.1 and make two new dictionaries.
#Store the three dictionaries in a list called people.

#Creating three separate dictionaries with identical keys
matthew = {
	"first_name" : "matthew", 
	"last_name" : "oyales",
	"age" : "18",
	"city" : "hackettstown"
	}
mike = {
	"first_name" : "mike",
	"last_name" : "fiktenbaum",
	"age" : "16",
	"city" : "montville"
	}
alexis = {
	"first_name" : "alexis",
	"last_name" : "oyales",
	"age" : "29",
	"city" : "san jose"
	}
	
#List of dictionaries
people = [matthew, mike, alexis]

#Info has all the dictionaries and their keys
for info in people:
	print("Full name: " + info["first_name"].title() + " " + 
		 info["last_name"].title())
	print("Age: " + info["age"])
	print("City: " + info["city"].title() + "\n")
