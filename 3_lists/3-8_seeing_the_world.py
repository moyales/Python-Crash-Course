#Exercise 3.8: Seeing the World
locations = ['New York' , 'London', 'Vancouver', 'Amsterdam', 'Tokyo']
print("Here is the original list:")
print(locations)

print("\nHere is the list sorted by alphabetical order:")
print(sorted(locations))

print("\nThe original list is still in the same order:")
print(locations)

print("\nHere is the list in reverse alphabetical order:")
print(sorted(locations, reverse=True))

print("\nAgain, the list is still in the same order as it was before:")
print(locations)

print("\nNow, we are going to reverse the order of the list using the reverse method:")
locations.reverse()
print(locations)

print("\nUsing the reverse method again will restore the list back to its original form:")
locations.reverse()
print(locations)

print("\nThe sort method will permanently sort this list in alphabetical order:")
locations.sort()
print(locations)

print("\nPut the list in reverse alphabetical order:")
locations.sort(reverse=True)
print(locations)
