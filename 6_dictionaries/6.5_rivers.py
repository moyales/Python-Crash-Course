#6.5: Rivers
#Make a dictionary of three major rivers and their countries.

rivers = {
	"nile" : "egypt",
	"mississippi" : "the united states",
	"rhine" : "germany"
	}

for river, country in rivers.items():
	print("The " + river.title() + " runs through " + country.title())

print("\nThe list of rivers:")
for river in rivers:
	print(river.title())

print("\nThe list of countries:")
for country in rivers.values():
	print(country.title())
