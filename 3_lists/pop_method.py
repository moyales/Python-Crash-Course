motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

cars = ["audi", "mercedes", "volkswagen"]
last_owned = cars.pop(0)
message = "The last car I owned was a " + last_owned.title() + "."
print(message)
