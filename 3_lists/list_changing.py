#Modifying elements in a list
motorcycles = ["honda", "yamaha", "ducati"]
print(motorcycles)

#Changes the specific element from the list and prints it out
motorcycles[0] = "suzuki"
print(motorcycles)

motorcycles[0] = "honda"

#Adding elements to a list
#Using the append function adds the item to the end of the list
motorcycles.append('suzuki')
print(motorcycles)

#You can start with a blank list and append the list to add items dynamically.
cars = []
cars.append("Audi")
cars.append("Mercedes-Benz")
cars.append("BMW")

print(cars)

#Use the "insert" method to place a new element at a designated position.
#Existing elements get pushed to the right.
fruits = ["apples", "bananas", "oranges"]
print(fruits)
fruits.insert(0, "grapes")
print(fruits)

#Remove items with the del statement
states = ["New Jersey", "Delaware", "New York"]
print(states)

#Removes item from list in that particular position.
del states[0]
print(states)

states.append("New Jersey")
#Remove using the pop method
popped_states = states.pop()
print(states)
print(popped_states)
